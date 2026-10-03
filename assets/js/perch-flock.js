import { birds, gap, height } from './perch-birds.js';

// A shuffled bag shows every species before starting the next round.
// Keep the flock for this page so resizing only reveals more birds.
export function createFlock(random = Math.random) {
  let bag = [];
  let previous;
  let nextX = 0;
  const rightEdges = Array(height).fill(-Infinity);
  const placed = [];

  function nextBird() {
    if (bag.length === 0) {
      bag = [...birds];
      for (let i = bag.length - 1; i > 0; i--) {
        const j = Math.floor(random() * (i + 1));
        [bag[i], bag[j]] = [bag[j], bag[i]];
      }
      // The next item is popped from the end; avoid a repeat at the seam.
      if (bag.length > 1 && bag[bag.length - 1] === previous) {
        const j = Math.floor(random() * (bag.length - 1));
        [bag[j], bag[bag.length - 1]] = [bag[bag.length - 1], bag[j]];
      }
    }
    previous = bag.pop();
    return previous;
  }

  return function cover(width) {
    // A later bird can tuck under an earlier tail. Continue until no later
    // origin can be visible, rather than stopping at the rightmost pixel.
    while (nextX < width) {
      const bird = nextBird();
      const flipped = random() < 0.5;
      const edges = flipped
        ? bird.edges.map(edge => edge && [bird.width - 1 - edge[1], bird.width - 1 - edge[0]])
        : bird.edges;
      let x = nextX;
      edges.forEach((edge, y) => {
        if (edge) x = Math.max(x, rightEdges[y] + gap + 1 - edge[0]);
      });
      edges.forEach((edge, y) => {
        if (edge) rightEdges[y] = x + edge[1];
      });
      placed.push({ bird, x, flipped });
      nextX = x + 1;
    }
    return placed.filter(({ x }) => x < width);
  };
}
