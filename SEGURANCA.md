# Política de publicação segura

Este repositório é **público**. Não utilize códigos ou dados internos sem autorização expressa.

## Antes de enviar código

1. Verifique se é trabalho pessoal, acadêmico autorizado pelo grupo ou material livre para publicação.
2. Procure dados internos: endereços IP privados, nomes de servidores, domínios internos, caminhos de rede, nomes de funcionários, logs, capturas de tela e dados de operação.
3. Nunca inclua senhas, tokens, chaves, arquivos de configuração reais ou arquivos `.env`. Use `.env.example` apenas com valores fictícios.
4. Rode `python3 scripts/verificar_segredos.py` e revise o `git diff --cached`. O scanner é limitado e **não garante** que não existam segredos.
5. Antes de abrir um PR, examine também o histórico Git com uma ferramenta especializada como Gitleaks; o script local verifica somente arquivos atualmente versionados.
6. Se um segredo já foi enviado, **revogue/rotacione imediatamente**. Excluir o arquivo de um commit novo **não remove o segredo do histórico**.
7. Não publique código original do Cronômetro Eleitoral acadêmico sem alinhar os direitos do grupo; não publique material de terceiros ou da TV Norte/SBT sem autorização.

## Demonstrações e atribuições

- As pastas `demo_acervo/` e `demo_cronometro_web/` contêm **exemplos independentes**, não sistemas originais.
- A documentação dos projetos distingue protótipos, estudos e soluções profissionais.
- Não afirme que uma demonstração foi implantada em produção sem evidências.

## Limites da auditoria

Uma busca de padrões não identifica todas as credenciais ou informações confidenciais. Verifique também dependências, imagens, histórico, direitos autorais e autorização de publicação.
