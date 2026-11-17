#!/usr/bin/env python3
"""Verifica possíveis credenciais em arquivos versionados, sem imprimir seus valores.
Não substitui auditoria humana nem varredura de todo o histórico Git.
"""
from pathlib import Path
import re
import subprocess
import sys

RULES = {
    "chave privada": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "token GitHub": re.compile(r"\b(?:ghp_|gho_|ghu_|ghs_|ghr_)[A-Za-z0-9]{20,}\b|\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    "chave AWS": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "chave Google API": re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"),
    "token Slack": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{15,}\b"),
    "token OpenAI": re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    "credencial em URL": re.compile(r"(?i)\b(?:https?|postgres(?:ql)?|mysql|redis)://[^\s/@:]+:[^\s/@]+@"),
    "atribuição suspeita": re.compile(
        r"""(?im)\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret|password|passwd|senha|secret[_-]?key)\b\s*[:=]\s*["']?(?!\s*(?:\$\{|\$|os\.getenv|process\.env|None|null|undefined|example|exemplo|change[_-]?me|seu[_-]|<))[^\s"'#]{8,}"""
    ),
}
BAD_NAMES = re.compile(r"(?i)(^|/)(?:\.env(?:\..+)?|id_rsa|id_ed25519|credentials\.json|service[_-]?account\.json)$")
BAD_SUFFIXES = {".pem", ".p12", ".pfx", ".key", ".db", ".sqlite", ".sqlite3"}

def main() -> int:
    paths = subprocess.check_output(["git", "ls-files", "-z"]).decode("utf-8", "replace").split("\0")
    problems = []
    for path in filter(None, paths):
        suffix = Path(path).suffix.lower()
        if BAD_NAMES.search(path) or suffix in BAD_SUFFIXES:
            problems.append((path, "nome de arquivo potencialmente sensível"))
        file = Path(path)
        if not file.is_file():
            continue
        try:
            data = file.read_bytes()
            if b"\0" in data[:4096] or len(data) > 1_000_000:
                continue
            content = data.decode("utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for label, pattern in RULES.items():
            for match in pattern.finditer(content):
                line = content.count("\n", 0, match.start()) + 1
                problems.append((f"{path}:{line}", label))
    if problems:
        print("ALERTA: possíveis informações sensíveis (valores omitidos):")
        for filename, label in problems:
            print(f" - {filename}: {label}")
        return 1
    print("Nenhum padrão conhecido de segredo foi identificado nos arquivos versionados.")
    print("ATENÇÃO: inspeção automatizada limitada; confirme histórico, permissões e dados internos.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
