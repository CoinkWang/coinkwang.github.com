import test from 'node:test';
import assert from 'node:assert/strict';
import { createFlock } from '../assets/js/perch-flock.js';
import { birds, gap, height } from '../assets/js/perch-birds.js';

function seeded(seed) {
  return () => {
    seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0;
    return seed / 2 ** 32;
  };
}

test('every round contains all species, with no repeated neighbours across rounds', () => {
  for (let seed = 0; seed < 100; seed++) {
    const flock = createFlock(seeded(seed))(5000);
    const names = flock.map(({ bird }) => bird.name);
    for (let i = 1; i < names.length; i++) assert.notEqual(names[i], names[i - 1]);
    for (let i = 0; i + birds.length <= names.length; i += birds.length) {
      assert.equal(new Set(names.slice(i, i + birds.length)).size, birds.length);
    }
  }
});

test('different page seeds produce different arrangements', () => {
  const orders = new Set(Array.from({ length: 20 }, (_, seed) =>
    createFlock(seeded(seed))(600).map(({ bird }) => bird.name).join(',')));
  assert.equal(orders.size, 20);
});

test('each species can face either way across random pages', () => {
  const orientations = new Map(birds.map(bird => [bird.name, new Set()]));
  for (let seed = 0; seed < 20; seed++) {
    for (const { bird, flipped } of createFlock(seeded(seed))(600)) {
      orientations.get(bird.name).add(flipped);
    }
  }
  for (const [name, choices] of orientations) assert.equal(choices.size, 2, name);
});

test('resizing preserves the visible birds and extends the existing flock', () => {
  const cover = createFlock(seeded(42));
  const mobile = cover(195);
  const desktop = cover(640);
  assert.deepEqual(desktop.slice(0, mobile.length), mobile);
  assert.deepEqual(cover(195), mobile);
  assert.deepEqual(cover(640), desktop);
});

test('all random orders keep tails and feet apart on an integer grid', () => {
  for (let seed = 0; seed < 100; seed++) {
    const rightEdges = Array(height).fill(-Infinity);
    for (const { bird, x, flipped } of createFlock(seeded(seed))(2000)) {
      assert.ok(Number.isInteger(x));
      bird.edges.forEach((edge, y) => {
        if (!edge) return;
        const left = flipped ? bird.width - 1 - edge[1] : edge[0];
        const right = flipped ? bird.width - 1 - edge[0] : edge[1];
        assert.ok(x + left - rightEdges[y] > gap, `${bird.name}, row ${y}`);
        rightEdges[y] = x + right;
      });
    }
    // The viewport may end in the clear gap before the next clipped bird.
    assert.ok(Math.max(...rightEdges) >= 1999 - gap);
  }
});
