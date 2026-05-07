(function () {
  'use strict';

  var WIDE_QUERY = '(min-width: 1200px)';
  var SIDENOTE_GAP = 12;

  function init() {
    var footnotesBlock = document.querySelector('.footnotes');
    if (!footnotesBlock) return;

    var article = document.querySelector('article.article') || document.querySelector('article');
    if (!article) return;

    var refs = Array.from(article.querySelectorAll('sup[id^="fnref:"]'));
    if (refs.length === 0) return;

    document.body.classList.add('has-sidenotes');

    var contentMap = {};
    footnotesBlock.querySelectorAll('ol > li').forEach(function (li) {
      var clone = li.cloneNode(true);
      clone.querySelectorAll('.reversefootnote').forEach(function (a) { a.remove(); });
      contentMap[li.id] = clone.innerHTML.trim();
    });

    var sidenotesEl = document.createElement('aside');
    sidenotesEl.className = 'sidenotes';
    var sidenoteByRef = new Map();

    refs.forEach(function (sup, idx) {
      var num = idx + 1;
      var fnId = sup.id.replace('fnref:', 'fn:');
      var content = contentMap[fnId] || '';

      // Force the visible label to the running index, so the badge/sidenote
      // numbering matches even if kramdown id ordering differs.
      var link = sup.querySelector('a');
      if (link) link.textContent = String(num);

      var sn = document.createElement('div');
      sn.className = 'sidenote';
      sn.dataset.ref = sup.id;
      sn.innerHTML = '<span class="sidenote-num">' + num + '.</span> ' + content;
      sidenotesEl.appendChild(sn);
      sidenoteByRef.set(sup, sn);

      if (link) {
        link.addEventListener('click', function (e) {
          if (window.matchMedia(WIDE_QUERY).matches) {
            e.preventDefault();
            return;
          }
          e.preventDefault();
          openPopup(num, content);
        });
      }
    });

    article.appendChild(sidenotesEl);

    var popup = createPopup();
    document.body.appendChild(popup.root);

    function openPopup(num, html) {
      popup.num.textContent = num + '.';
      popup.content.innerHTML = html;
      popup.root.classList.add('is-open');
      document.body.style.overflow = 'hidden';
    }

    function closePopup() {
      popup.root.classList.remove('is-open');
      document.body.style.overflow = '';
    }

    popup.root.addEventListener('click', function (e) {
      if (e.target === popup.root) closePopup();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && popup.root.classList.contains('is-open')) closePopup();
    });

    function layoutSidenotes() {
      if (!window.matchMedia(WIDE_QUERY).matches) return;
      var articleTop = article.getBoundingClientRect().top + window.scrollY;
      var lastBottom = 0;
      refs.forEach(function (sup) {
        var sn = sidenoteByRef.get(sup);
        if (!sn) return;
        var supTop = sup.getBoundingClientRect().top + window.scrollY - articleTop;
        var top = Math.max(supTop, lastBottom + SIDENOTE_GAP);
        sn.style.top = top + 'px';
        lastBottom = top + sn.offsetHeight;
      });
    }

    var resizeTimer;
    function scheduleLayout() {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(layoutSidenotes, 80);
    }

    window.addEventListener('resize', scheduleLayout);
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(layoutSidenotes);
    }
    if (document.readyState === 'complete') {
      layoutSidenotes();
    } else {
      window.addEventListener('load', layoutSidenotes);
    }
    setTimeout(layoutSidenotes, 300);
  }

  function createPopup() {
    var root = document.createElement('div');
    root.className = 'fn-popup';
    root.setAttribute('role', 'dialog');
    root.setAttribute('aria-modal', 'true');
    root.innerHTML =
      '<div class="fn-popup-card">' +
      '  <span class="fn-popup-num"></span>' +
      '  <div class="fn-popup-content"></div>' +
      '</div>';
    return {
      root: root,
      num: root.querySelector('.fn-popup-num'),
      content: root.querySelector('.fn-popup-content')
    };
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
