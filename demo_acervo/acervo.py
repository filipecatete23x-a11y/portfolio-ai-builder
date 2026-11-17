#!/usr/bin/env python3
"""Demo local de acervo de texto: CLI + SQLite, sem dependências externas."""
import argparse
from pathlib import Path
import sqlite3

DB = Path(__file__).with_name("acervo_demo.db")


def connect():
    connection = sqlite3.connect(DB)
    connection.execute("""CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        source TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )""")
    return connection


def main():
    parser = argparse.ArgumentParser(description="Acervo local de textos — demonstração")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init", help="Cria banco/tabela")
    p_add = sub.add_parser("add", help="Cadastra texto .txt")
    p_add.add_argument("--title", required=True)
    p_add.add_argument("--source", required=True)
    p_add.add_argument("--file", type=Path, required=True)
    p_search = sub.add_parser("search", help="Busca texto por termo")
    p_search.add_argument("--term", required=True)
    sub.add_parser("list", help="Lista textos cadastrados")
    args = parser.parse_args()

    with connect() as conn:
        if args.cmd == "init":
            print(f"Banco iniciado: {DB.name}")
        elif args.cmd == "add":
            if args.file.suffix.lower() != ".txt":
                parser.error("O arquivo deve ter extensão .txt")
            try:
                content = args.file.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                parser.error(f"Erro ao ler o arquivo: {exc}")
            if not content.strip():
                parser.error("O arquivo está vazio")
            conn.execute("INSERT INTO documents (title, source, content) VALUES (?, ?, ?)",
                         (args.title, args.source, content))
            print(f"Cadastrado: {args.title}")
        elif args.cmd == "list":
            rows = conn.execute("SELECT id, title, source FROM documents ORDER BY id DESC").fetchall()
            for doc_id, title, source in rows:
                print(f"#{doc_id} | {title} | {source}")
            print(f"Total: {len(rows)}")
        elif args.cmd == "search":
            term = args.term.strip()
            if not term:
                parser.error("Informe um termo não vazio")
            rows = conn.execute("""SELECT id, title, source FROM documents
                WHERE instr(lower(title), lower(?)) > 0 OR instr(lower(content), lower(?)) > 0
                ORDER BY id DESC""", (term, term)).fetchall()
            for doc_id, title, source in rows:
                print(f"#{doc_id} | {title} | {source}")
            print(f"Encontrados: {len(rows)}")


if __name__ == "__main__":
    main()
