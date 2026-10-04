import { birds } from './perch-birds.js';

// Comment avatars for people without one of their own. The comment server
// asks Cravatar with d=404 (GRAVATAR_STR in the waline-comments project), so
// such an avatar fails to load; one of the header's birds is drawn in its
// place, picked by name so a commenter keeps the same bird on every page.

const AVATARS = '.wl-user-avatar, .wl-avatar img';

// The rows and columns each bird actually covers on its 38-row canvas
const frames = new Map(birds.map(bird => {
  let left = Infinity, top = Infinity, right = 0, bottom = 0;
  for (const d of Object.values(bird.paths)) {
    for (const [, x, y, w] of d.matchAll(/M(\d+) (\d+)h(\d+)/g)) {
      left = Math.min(left, +x);
      top = Math.min(top, +y);
      right = Math.max(right, +x + +w);
      bottom = Math.max(bottom, +y + 1);
    }
  }
  return [bird, { left, top, width: right - left, height: bottom - top }];
}));

// FNV-1a: cheap, and the same name lands on the same bird everywhere
export function birdFor(name) {
  let hash = 0x811c9dc5;
  for (let i = 0; i < name.length; i++) {
    hash = Math.imul(hash ^ name.charCodeAt(i), 0x01000193);
  }
  return birds[(hash >>> 0) % birds.length];
}

// The bird centred in a square of `size` CSS pixels, as large as fits with a
// bird pixel to spare all round, each bird pixel a whole number of device
// pixels so the edges stay crisp
export function birdSvg(bird, size, ratio = 1) {
  const { left, top, width, height } = frames.get(bird);
  const dots = Math.max(1, Math.floor(size * ratio / (Math.max(width, height) + 2)));
  const side = size * ratio / dots;
  const snap = v => Math.round(v * dots) / dots;
  const dx = snap((side - width) / 2) - left;
  const dy = snap((side - height) / 2) - top;
  const paths = Object.entries(bird.paths)
    .map(([colour, d]) => `<path fill="${colour}" d="${d}"/>`)
    .join('');
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${side} ${side}" shape-rendering="crispEdges">`
    + `<g transform="translate(${dx} ${dy})">${paths}</g></svg>`;
}

function nameFor(img) {
  const card = img.closest('.wl-card-item');
  if (card) return card.querySelector(':scope > .wl-card > .wl-head .wl-nick')?.textContent ?? '';
  // the signed-in reader beside the form
  return img.closest('.wl-login-info')?.textContent ?? '';
}

export function perchAvatars(root) {
  // error events don't bubble, so listen on the way down; this also covers
  // avatars Waline adds later (new comments, the next page of them)
  root.addEventListener('error', ({ target }) => {
    if (!(target instanceof HTMLImageElement) || !target.matches(AVATARS)) return;
    if (target.src.startsWith('data:')) return;
    const size = target.getBoundingClientRect().width || 40;
    const svg = birdSvg(birdFor(nameFor(target).trim()), size, window.devicePixelRatio || 1);
    target.src = `data:image/svg+xml,${encodeURIComponent(svg)}`;
  }, true);
}
