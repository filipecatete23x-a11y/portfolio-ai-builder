# Mini Cronômetro Web — demonstração independente

Este é um **exemplo novo, escrito para o portfólio**, inspirado no problema genérico de sincronizar uma contagem entre abas do navegador. **Não contém e não representa o código original do Cronômetro Eleitoral do IFPA ou da TV Norte/SBT**.

## Tecnologias

Node.js 20+, Express (HTTP), biblioteca `ws` (WebSocket) e JavaScript no navegador.

## Execução local

```bash
cd demo_cronometro_web
npm install
npm audit --audit-level=high
npm test
npm start
```

Abra **http://127.0.0.1:3000** e, em outra aba, **http://127.0.0.1:3000/?mode=display**. Os comandos Iniciar, Pausar e Reiniciar são refletidos nas duas telas, sem atualizar a página. O tempo inicial é de 90 segundos.

## Limitações e segurança

- É uma demonstração educacional, **não um sistema para uso em debates reais**.
- Escuta apenas em `127.0.0.1` e verifica a origem de comandos e conexões WebSocket.
- **Não tem autenticação nem persistência:** não exponha a aplicação à rede, à internet ou à produção.
- Não utiliza credenciais, dados de terceiros, imagens de emissoras ou infraestrutura interna.
- Não possui IA embutida: o interesse para AI Builder é mostrar desenvolvimento e verificação de código com auxílio de IA.
- Dependências são resolvidas no momento da instalação: verifique `npm audit` e revise o lockfile antes de qualquer distribuição.
