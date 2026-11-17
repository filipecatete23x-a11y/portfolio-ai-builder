"use strict";

/**
 * Motor didático de cronômetro, sem vínculo com softwares de terceiros.
 * O relógio é injetável para permitir testes determinísticos.
 */
class TimerEngine {
  constructor(durationSeconds = 90, now = () => performance.now()) {
    if (!Number.isSafeInteger(durationSeconds) || durationSeconds < 1 || durationSeconds > 3600) {
      throw new RangeError("Duração inválida (1 a 3600 segundos).");
    }
    this.durationSeconds = durationSeconds;
    this.now = now;
    this.remainingMs = durationSeconds * 1000;
    this.endsAtMs = null;
  }

  snapshot() {
    if (this.endsAtMs !== null) {
      this.remainingMs = Math.max(0, this.endsAtMs - this.now());
      if (this.remainingMs <= 0) this.endsAtMs = null;
    }
    return {
      durationSeconds: this.durationSeconds,
      remainingSeconds: Math.ceil(this.remainingMs / 1000),
      running: this.endsAtMs !== null
    };
  }

  start() {
    const state = this.snapshot();
    if (!state.running && this.remainingMs > 0) {
      this.endsAtMs = this.now() + this.remainingMs;
    }
    return this.snapshot();
  }

  pause() {
    const state = this.snapshot();
    this.endsAtMs = null;
    return { ...state, running: false };
  }

  reset() {
    this.endsAtMs = null;
    this.remainingMs = this.durationSeconds * 1000;
    return this.snapshot();
  }
}

module.exports = { TimerEngine };
