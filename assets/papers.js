(function () {
  const DATA = JSON.parse(document.getElementById('data').textContent);
  const ALL = DATA.papers;
  const TAB = Object.fromEntries(DATA.tabs.map((t) => [t.key, t]));
  const LEAF = Object.fromEntries(DATA.leaves.map((l) => [l.key, l]));
  const BY_ID = Object.fromEntries(ALL.filter((p) => p.id).map((p) => [p.id, p]));
  const $ = (s) => document.querySelector(s);
  const $$ = (s) => document.querySelectorAll(s);
  const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const store = {
    get(k, d) { try { const v = localStorage.getItem(k); return v == null ? d : JSON.parse(v); } catch { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} },
  };
  const SORTS = ['sections', 'newest', 'stars', 'upvotes'];

  function colKey() { return 'jevp-cols-' + (window.innerWidth < 640 ? 'm' : window.innerWidth < 1100 ? 't' : 'd'); }
  const state = {
    q: '', tab: '', sort: store.get('jevp-sort', 'sections'),
    cols: store.get(colKey(), Math.max(1, Math.min(4, Math.round(window.innerWidth / 470)))),
  };
  const hay = new Map(ALL.map((p) => [p, [p.name, p.title, (p.authors || []).join(', '), p.abstract, p.id, p.cat,
    TAB[p.tab].name, LEAF[p.sec].name, ...(p.code || []).map((c) => c.repo)].join('\n').toLowerCase()]));

  function pxIcon(rows) {
    const w = rows[0].length, h = rows.length;
    let d = '';
    rows.forEach((r, y) => { for (let x = 0; x < w; x++) if (r[x] === '#') d += `M${x} ${y}h1v1h-1z`; });
    return `<svg class="px" width="${w * 2}" height="${h * 2}" viewBox="0 0 ${w} ${h}" fill="currentColor" aria-hidden="true"><path d="${d}"/></svg>`;
  }
  const I_STAR = pxIcon(['...#...', '...#...', '#######', '.#####.', '..###..', '.##.##.', '.#...#.']);
  const I_UP = pxIcon(['...#...', '..###..', '.#####.', '#######']);
  const I_GLOBE = pxIcon(['..####..', '.#.##.#.', '#..##..#', '########', '#..##..#', '.#.##.#.', '..####..']);
  const I_DOC = pxIcon(['#####..', '#...##.', '#....##', '#.....#', '#.###.#', '#.....#', '#.###.#', '#######']);
  const I_HF = pxIcon(['..####..', '.#....#.', '#.#..#.#', '#......#', '#.#..#.#', '#..##..#', '.#....#.', '..####..']);
  const I_GH = '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>';
  const EAR = (() => {
    let c = '', e = '', f = '';
    for (let y = 0; y < 9; y++) for (let x = 0; x < 9; x++) {
      const r = `M${x} ${y}h1v1h-1z`;
      if (x > y) c += r; else if (x === y || x === 0 || y === 8) e += r; else f += r;
    }
    return `<svg class="px ear" viewBox="0 0 9 9" aria-hidden="true"><path class="c" d="${c}"/><path class="f" d="${f}"/><path class="e" d="${e}"/></svg>`;
  })();

  const num = (n) => n >= 1000 ? (n / 1000).toFixed(1).replace(/\.0$/, '') + 'k' : String(n);
  const absUrl = (p) => p.id ? `https://arxiv.org/abs/${p.id}` : p.url;
  const topStars = (p) => Math.max(-1, ...(p.code || []).map((c) => c.stars ?? 0));
  const ups = (p) => (p.daily && p.daily.up != null) ? p.daily.up : -1;
  function authors(p, all) {
    const a = p.authors || [];
    if (!a.length) return '';
    return all || a.length <= 3 ? a.join(', ') : a.slice(0, 3).join(', ') + ' et al.';
  }
  function chips(p, withAbs) {
    const out = [];
    if (withAbs && p.abstract) out.push(`<button class="chip go" type="button" data-abs="${esc(p.id)}">abstract</button>`);
    if (!withAbs && p.id) out.push(`<a class="chip" href="${esc(absUrl(p))}" target="_blank" rel="noopener">${I_DOC}arXiv</a>`);
    if (p.id) out.push(`<a class="chip" href="https://arxiv.org/pdf/${esc(p.id)}" target="_blank" rel="noopener">pdf</a>`);
    for (const c of p.code || []) {
      out.push(`<a class="chip" href="${esc(c.url)}" target="_blank" rel="noopener" title="${esc(c.repo)}">${I_GH}code${c.stars != null ? ` ${I_STAR}${num(c.stars)}` : ''}</a>`);
    }
    if (p.model) out.push(`<a class="chip" href="${esc(p.model)}" target="_blank" rel="noopener">${I_HF}model</a>`);
    if (p.site) out.push(`<a class="chip" href="${esc(p.site)}" target="_blank" rel="noopener">${I_GLOBE}site</a>`);
    if (p.daily) out.push(`<a class="chip" href="${esc(p.daily.url)}" target="_blank" rel="noopener" title="Hugging Face Daily Papers upvotes">daily${p.daily.up ? ` ${I_UP}${num(p.daily.up)}` : ''}</a>`);
    return out.join('');
  }
  function cardHTML(p, i) {
    const k = state.cols === 1 ? i % 4 : (i % state.cols + 2 * Math.floor(i / state.cols)) % 4;
    const au = authors(p, false);
    return `<article class="card b${k}" style="--sc:var(--s-${p.tab})">
      <a class="win-t" href="${esc(absUrl(p))}" target="_blank" rel="noopener" tabindex="-1"><span class="t">${esc(p.name)}</span><span class="n">${esc(p.date)}</span></a>
      <a class="pg" href="${esc(absUrl(p))}" target="_blank" rel="noopener">${EAR}<span class="ti">${esc(p.title)}</span>${au ? `<span class="au">${esc(au)}</span>` : ''}</a>
      <div class="chips">${chips(p, true)}</div>
    </article>`;
  }
  function headHTML(l, n) {
    const tag = l.parent ? `<small>${esc(l.parent)}</small>` : '';
    return `<div class="sh" style="--sc:var(--s-${l.tab})"><i></i><h2>${tag}<span>${esc(l.name)}</span><em>${n}</em></h2>${l.desc ? `<p>${esc(l.desc)}</p>` : ''}</div>`;
  }

  function compute() {
    const terms = state.q.toLowerCase().split(/\s+/).filter(Boolean);
    let list = ALL.filter((p) => (!state.tab || p.tab === state.tab) && (!terms.length || terms.every((w) => hay.get(p).includes(w))));
    if (state.sort === 'newest') list = list.slice().sort((a, b) => (b.date || '').localeCompare(a.date || '') || a.order - b.order);
    else if (state.sort === 'stars') list = list.slice().sort((a, b) => topStars(b) - topStars(a) || a.order - b.order);
    else if (state.sort === 'upvotes') list = list.slice().sort((a, b) => ups(b) - ups(a) || a.order - b.order);
    return list;
  }
  function render() {
    const list = compute();
    const grid = $('#grid');
    grid.style.setProperty('--cols', state.cols);
    let html = '';
    if (state.sort === 'sections') {
      const groups = new Map();
      for (const p of list) { if (!groups.has(p.sec)) groups.set(p.sec, []); groups.get(p.sec).push(p); }
      for (const [sec, ps] of groups) html += headHTML(LEAF[sec], ps.length) + ps.map((p, i) => cardHTML(p, i)).join('');
    } else {
      html = list.map((p, i) => cardHTML(p, i)).join('');
    }
    grid.innerHTML = html;
    $('#empty').hidden = list.length > 0;
    $('#count').textContent = list.length === ALL.length ? `${ALL.length} papers` : `${list.length} of ${ALL.length}`;
    $$('#sort button').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.sort === state.sort)));
  }
  function applyCols() { $('#colN').textContent = state.cols; store.set(colKey(), state.cols); render(); }
  function pressTab() { $$('#pills button').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.tab === state.tab))); }
  function setParam(k, v) {
    const u = new URL(location.href);
    if (v) u.searchParams.set(k, v); else u.searchParams.delete(k);
    history.replaceState(null, '', u.pathname + (u.search ? u.search : '') + u.hash);
  }

  const dlg = $('#abs');
  function openAbs(id) {
    const p = BY_ID[id];
    if (!p || !dlg.showModal) return;
    const facts = [p.date, p.id && 'arXiv ' + p.id, p.cat, LEAF[p.sec].name].filter(Boolean);
    dlg.innerHTML = `<div class="win-t" style="--sc:var(--s-${p.tab})"><span class="t" id="absName">${esc(p.name)}</span><button class="x" type="button" aria-label="Close">close</button></div>
      <div class="bd">
        <h2>${esc(p.title)}</h2>
        ${p.authors && p.authors.length ? `<p class="au">${esc(authors(p, true))}</p>` : ''}
        <div class="dt">${facts.map((f) => `<span>${esc(f)}</span>`).join('')}</div>
        <p class="ab">${esc(p.abstract)}</p>
        <div class="chips">${chips(p, false)}</div>
      </div>`;
    if (!dlg.open) dlg.showModal();
    dlg.scrollTop = 0;
    setParam('p', p.id);
  }
  dlg.addEventListener('click', (e) => { if (e.target === dlg || e.target.closest('.x')) dlg.close(); });
  dlg.addEventListener('close', () => setParam('p', ''));
  $('#grid').addEventListener('click', (e) => { const b = e.target.closest('[data-abs]'); if (b) openAbs(b.dataset.abs); });

  $('#pills').addEventListener('click', (e) => {
    const b = e.target.closest('button'); if (!b) return;
    state.tab = b.dataset.tab === state.tab ? '' : b.dataset.tab;
    pressTab(); setParam('tab', state.tab); render();
  });
  let qT; $('#q').addEventListener('input', (e) => { clearTimeout(qT); qT = setTimeout(() => { state.q = e.target.value.trim(); render(); }, 150); });
  $('#sort').addEventListener('click', (e) => {
    const b = e.target.closest('button'); if (!b) return;
    state.sort = b.dataset.sort; store.set('jevp-sort', state.sort); render();
  });
  $('#colDec').addEventListener('click', () => { state.cols = Math.max(1, state.cols - 1); applyCols(); });
  $('#colInc').addEventListener('click', () => { state.cols = Math.min(5, state.cols + 1); applyCols(); });
  const root = document.documentElement, tb = $('#theme');
  const theme = () => root.getAttribute('data-theme') || 'light';
  const label = () => { tb.textContent = theme() === 'dark' ? 'Light' : 'Dark'; };
  if (store.get('jevp-theme', null)) root.setAttribute('data-theme', store.get('jevp-theme'));
  label();
  tb.addEventListener('click', () => { const t = theme() === 'dark' ? 'light' : 'dark'; root.setAttribute('data-theme', t); store.set('jevp-theme', t); label(); });
  document.addEventListener('keydown', (e) => {
    const typing = /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName);
    if (e.key === 'Escape' && typing) { document.activeElement.blur(); return; }
    if (e.key === '/' && !typing && !dlg.open) { e.preventDefault(); $('#q').focus({ preventScroll: true }); $('#q').scrollIntoView({ block: 'center' }); $('#q').select(); }
  });

  const sub = $('#sub');
  if (sub && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const full = sub.textContent, cur = document.createElement('span');
    cur.className = 'cursor';
    let i = 0;
    sub.textContent = ''; sub.append(cur);
    const tick = () => { i++; sub.textContent = full.slice(0, i); sub.append(cur); if (i < full.length) setTimeout(tick, 30); };
    setTimeout(tick, 600);
  }

  const qs = new URLSearchParams(location.search);
  if (qs.get('q')) { $('#q').value = qs.get('q'); state.q = qs.get('q').trim(); }
  if (qs.get('tab') && TAB[qs.get('tab')]) state.tab = qs.get('tab');
  if (!SORTS.includes(state.sort)) state.sort = 'sections';
  pressTab();
  applyCols();
  if (qs.get('p')) openAbs(qs.get('p'));
})();
