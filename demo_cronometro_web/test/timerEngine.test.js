"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const { TimerEngine } = require("../timerEngine");

test("iniciar, pausar, retomar e finalizar de modo determinístico", () => {
  let now = 0;
  const engine = new TimerEngine(10, () => now);
  assert.deepEqual(engine.snapshot(), { durationSeconds: 10, remainingSeconds: 10, running: false });
  engine.start();
  now = 1500;
  assert.equal(engine.snapshot().remainingSeconds, 9);
  engine.pause();
  now = 5000;
  assert.equal(engine.snapshot().remainingSeconds, 9);
  engine.start();
  now = 13500;
  assert.deepEqual(engine.snapshot(), { durationSeconds: 10, remainingSeconds: 0, running: false });
  engine.reset();
  assert.equal(engine.snapshot().remainingSeconds, 10);
});

test("não reinicia o tempo ao receber iniciar repetido", () => {
  let now = 0;
  const engine = new TimerEngine(5, () => now);
  engine.start();
  now = 1000;
  engine.start();
  now = 5000;
  assert.equal(engine.snapshot().remainingSeconds, 0);
});

test("valida limites de duração", () => {
  assert.throws(() => new TimerEngine(0), RangeError);
  assert.throws(() => new TimerEngine(3601), RangeError);
});
