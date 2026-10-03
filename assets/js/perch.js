import { height } from './perch-birds.js';
import { createFlock } from './perch-flock.js';

const header = document.querySelector('.site-header');
const perch = header?.querySelector('.header-perch');

if (perch) {
  const cover = createFlock();
  const namespace = 'http://www.w3.org/2000/svg';
  let lastWidth = 0;

  function render() {
    // Match the CSS pixel size without stretching the SVG to fit the viewport.
    const scale = perch.getBoundingClientRect().height / height;
    const width = Math.ceil(perch.getBoundingClientRect().width / scale);
    if (!Number.isFinite(width) || width <= 0 || width === lastWidth) return;
    const svg = document.createElementNS(namespace, 'svg');
    svg.setAttribute('width', width * scale);
    svg.setAttribute('height', height * scale);
    svg.setAttribute('viewBox', `0 0 ${width} ${height}`);
    svg.setAttribute('shape-rendering', 'crispEdges');
    svg.setAttribute('focusable', 'false');

    for (const { bird, x, flipped } of cover(width)) {
      const group = document.createElementNS(namespace, 'g');
      group.setAttribute('transform', flipped
        ? `translate(${x + bird.width} 0) scale(-1 1)`
        : `translate(${x} 0)`);
      group.dataset.species = bird.name;
      for (const [colour, d] of Object.entries(bird.paths)) {
        const path = document.createElementNS(namespace, 'path');
        path.setAttribute('fill', colour);
        path.setAttribute('d', d);
        group.append(path);
      }
      svg.append(group);
    }
    perch.replaceChildren(svg);
    header.classList.add('has-random-perch');
    lastWidth = width;
  }

  render();
  if (typeof ResizeObserver !== 'undefined') {
    new ResizeObserver(render).observe(perch);
  } else {
    window.addEventListener('resize', render);
  }
}
