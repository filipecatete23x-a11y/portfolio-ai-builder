# Práticas de uso de IA no desenvolvimento

Uso assistentes de IA como apoio para compreender problemas, elaborar alternativas e revisar soluções. **Os prompts abaixo são modelos de trabalho para fins de portfólio, não cópias literais de conversas anteriores.**

## Exemplo 1 — tarefa de desenvolvimento guiada por requisitos

> Estou criando em Python um utilitário para cadastrar transcrições em SQLite. O projeto deve armazenar apenas texto e metadados, não vídeos nem áudios. Sugira uma estrutura mínima de tabelas e funções, explique os riscos de duplicidade e proponha testes. Não execute comandos destrutivos e explicite qualquer hipótese.

**Validação humana:** conferir a estrutura gerada, executar testes locais, revisar caminhos de arquivo e evitar perda de dados.

## Exemplo 2 — investigação de falha

> Analise este traceback de Python. Identifique a provável causa raiz e proponha uma alteração pequena. Explique como reproduzir a falha e como verificar a correção. Se faltarem informações, indique quais testes devo executar em vez de inventar resultados.

**Validação humana:** comparar a sugestão com o código real e testar novamente.

## Limites importantes

- Assistentes de IA podem errar; saídas devem ser verificadas.
- Não enviar dados sigilosos, credenciais nem conteúdo interno sem autorização.
- Não atribuir à IA ganhos de produtividade que não tenham sido medidos.
