import test from 'node:test';
import assert from 'node:assert/strict';
import { birdFor, birdSvg } from '../assets/js/perch-avatar.js';
import { birds } from '../assets/js/perch-birds.js';

test('a name always gets the same bird', () => {
  for (const name of ['沉风', 'Tilnel', '25时01分', '']) {
    assert.equal(birdFor(name), birdFor(name));
  }
});

test('names spread over every species', () => {
  const seen = new Set(Array.from({ length: 500 }, (_, i) => birdFor(`reader ${i}`).name));
  assert.equal(seen.size, birds.length);
});

test('every bird fits its square with a pixel to spare, on whole device pixels', () => {
  for (const [size, ratio] of [[40, 1], [40, 2], [32, 2], [40, 3]]) {
    for (const bird of birds) {
      const svg = birdSvg(bird, size, ratio);
      const side = +svg.match(/viewBox="0 0 ([\d.]+)/)[1];
      const [dx, dy] = svg.match(/translate\(([-\d.]+) ([-\d.]+)\)/).slice(1).map(Number);
      const dots = size * ratio / side;
      assert.ok(Number.isInteger(Math.round(dots * 1e9) / 1e9), `${bird.name} ${dots}`);
      for (const d of Object.values(bird.paths)) {
        for (const [, x, y, w] of d.matchAll(/M(\d+) (\d+)h(\d+)/g)) {
          assert.ok(+x + dx >= 1 - 1e-9 && +x + +w + dx <= side - 1 + 1e-9, `${bird.name} x`);
          assert.ok(+y + dy >= 1 - 1e-9 && +y + 1 + dy <= side - 1 + 1e-9, `${bird.name} y`);
          // edges on the device grid
          assert.ok(Math.abs((+x + dx) * dots - Math.round((+x + dx) * dots)) < 1e-6, `${bird.name} grid`);
        }
      }
    }
  }
});
