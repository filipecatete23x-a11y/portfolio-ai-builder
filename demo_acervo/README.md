# Demo pública — Mini Acervo de Estudos

Esta é uma **demonstração independente** criada para o portfólio. Ela se inspira no problema geral de organizar textos e metadados, mas **não é o código original do projeto Transcritor Oráculo nem de sistemas privados ou corporativos**.

### Requisitos

- Python 3.9+.
- Nenhuma biblioteca externa.

### Executar (Linux, macOS ou Windows com Python instalado)

Dentro da pasta `demo_acervo`, execute:

```bash
python3 acervo.py init
python3 acervo.py add --title "Introdução a redes" --source "Material de estudo" --file exemplo.txt
python3 acervo.py search --term "roteador"
python3 acervo.py list
```

No Windows, substitua `python3` por `python`, se necessário.

O banco `acervo_demo.db` será criado localmente. Use somente textos próprios ou que tenha direito de utilizar.

### Funcionalidades

- Criar a tabela `documents` em SQLite.
- Inserir conteúdo de arquivos `.txt` UTF-8 com título e fonte.
- Listar documentos cadastrados.
- Pesquisar termos no título ou no conteúdo.

### Segurança e limitações

Não envia dados para serviços externos, não realiza scraping e não utiliza modelos de IA em tempo de execução. O projeto demonstra **Python + SQLite + automação de tarefas**, e o processo de desenvolvimento pode ser assistido por IA. É uma demo didática, não uma aplicação empresarial pronta.
