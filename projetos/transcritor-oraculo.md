# Transcritor Oráculo — acervo pessoal de conhecimento técnico

**Estado:** protótipo local funcional / evolução contínua.  
**Stack:** Python 3, SQLite, arquivos de texto, metadados públicos do YouTube.

## Problema

Durante o estudo de vídeos técnicos, é difícil reencontrar uma explicação específica. Guardar vídeos completos também ocupa espaço desnecessário.

## Abordagem

Organizar **texto e metadados** (título, canal, URL, identificador e localização de arquivos de texto) em um acervo pesquisável, sem arquivar vídeos ou áudios. Uma aplicação em Python cadastra registros; outra permite pesquisar termos de estudo.

## Recursos já explorados no protótipo

- Cadastro de vídeos e metadados em SQLite.
- Associação a transcrições em arquivos de texto quando disponíveis.
- Pesquisa textual no acervo e tratamento de algumas variações de termos técnicos.

## Aprendizados

Organização de dados, modelagem simples com SQLite, processamento de texto, desenvolvimento incremental e verificação de respostas geradas por IA.

## Próximos passos

Melhorar os mecanismos de busca e a conferência de informações extraídas de transcrições.

**Código demonstrativo:** [demo independente de acervo](../demo_acervo/README.md), criada especificamente para apresentação pública. Não é uma cópia do código original do projeto.
