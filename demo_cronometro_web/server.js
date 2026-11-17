"use strict";

const express = require("express");
const { createServer } = require("node:http");
const path = require("node:path");
const { WebSocket, WebSocketServer } = require("ws");
const { TimerEngine } = require("./timerEngine");

const HOST = "127.0.0.1"; // Não expor em rede ou internet: demo sem autenticação.
const PORT = 3000;
const ORIGIN = `http://${HOST}:${PORT}`;
const app = express();
const engine = new TimerEngine(90);
const server = createServer(app);
const wss = new WebSocketServer({ noServer: true });

app.disable("x-powered-by");
app.use(express.json({ limit: "1kb" }));
app.get("/api/state", (_req, res) => res.json(engine.snapshot()));

function broadcast() {
  const payload = JSON.stringify(engine.snapshot());
  for (const client of wss.clients) {
    if (client.readyState === WebSocket.OPEN) client.send(payload);
  }
}

app.post("/api/command", (req, res) => {
  // Uma página externa não deve conseguir acionar o cronômetro local pelo navegador.
  if (req.get("origin") !== ORIGIN) return res.status(403).json({ error: "Origem negada." });
  const action = req.body?.action;
  if (!["start", "pause", "reset"].includes(action)) {
    return res.status(400).json({ error: "Comando inválido." });
  }
  const state = engine[action]();
  broadcast();
  return res.json(state);
});

app.use(express.static(path.join(__dirname, "public"), { dotfiles: "deny" }));

server.on("upgrade", (req, socket, head) => {
  if (req.headers.origin !== ORIGIN || req.url !== "/ws") {
    socket.end("HTTP/1.1 403 Forbidden\r\nConnection: close\r\n\r\n");
    return;
  }
  wss.handleUpgrade(req, socket, head, ws => {
    wss.emit("connection", ws, req);
  });
});

wss.on("connection", ws => {
  ws.send(JSON.stringify(engine.snapshot()));
  // Somente o servidor envia estados. Comandos chegam por HTTP.
});

setInterval(broadcast, 250).unref();
server.listen(PORT, HOST, () => {
  console.log(`Demo local em ${ORIGIN}`);
});
