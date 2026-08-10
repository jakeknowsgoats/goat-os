#!/usr/bin/env python3
"""Generate a self-contained, filterable web explorer (Artifact content-only HTML)
from data.json. Output: shiny_explorer.html  (no <html>/<head>/<body> — the Artifact
host wraps it; also renders fine standalone since <style>/<script> are body-legal)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
db = json.load(open(os.path.join(HERE, "data.json"), encoding="utf-8"))
DATA_JSON = json.dumps(db, ensure_ascii=False, separators=(",", ":"))

HTML = r"""<style>
:root{
  --ground:#f4f3f8; --surface:#ffffff; --surface-2:#eeecf4; --raise:#faf9fd;
  --ink:#1b1a24; --muted:#5d5b6c; --faint:#8a8798; --line:#e3e0ec;
  --accent:#9c7414; --accent-2:#c79a3b; --accent-soft:#f4ead0;
  --a:#1f8a5b; --e:#a9741a; --b:#2f6fbf; --c:#6f57c7; --d:#7c7a88;
  --home:#2f6fbf; --gogo:#d1472e;
  --shadow:0 1px 2px rgba(20,18,30,.06),0 8px 24px rgba(20,18,30,.06);
  --radius:14px;
}
:root:not([data-theme="light"]){}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#121119; --surface:#1c1a26; --surface-2:#252332; --raise:#221f2e;
    --ink:#ecebf4; --muted:#9c99ac; --faint:#726f81; --line:#2e2b3b;
    --accent:#e6c368; --accent-2:#c9a34e; --accent-soft:#3a331f;
    --a:#4fd39f; --e:#e0b25a; --b:#5aa2e6; --c:#a892f0; --d:#9a97a8;
    --home:#3f83d6; --gogo:#e3563b;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 30px rgba(0,0,0,.35);
  }
}
:root[data-theme="dark"]{
  --ground:#121119; --surface:#1c1a26; --surface-2:#252332; --raise:#221f2e;
  --ink:#ecebf4; --muted:#9c99ac; --faint:#726f81; --line:#2e2b3b;
  --accent:#e6c368; --accent-2:#c9a34e; --accent-soft:#3a331f;
  --a:#4fd39f; --e:#e0b25a; --b:#5aa2e6; --c:#a892f0; --d:#9a97a8;
  --home:#3f83d6; --gogo:#e3563b;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 30px rgba(0,0,0,.35);
}
*{box-sizing:border-box}
body{background:var(--ground);color:var(--ink);margin:0;
  font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  font-size:15px;line-height:1.5;-webkit-text-size-adjust:100%;}
.mono{font-family:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,monospace;
  font-variant-numeric:tabular-nums;}
.wrap{max-width:1140px;margin:0 auto;padding:26px 18px 80px;}
a{color:var(--accent);}
h1,h2,h3{text-wrap:balance;margin:0;}

/* header */
.masthead{display:flex;justify-content:space-between;align-items:flex-start;gap:16px;flex-wrap:wrap;}
.eyebrow{font-family:ui-monospace,"SF Mono",Menlo,monospace;font-size:11px;letter-spacing:.18em;
  text-transform:uppercase;color:var(--faint);}
h1{font-size:clamp(26px,4.5vw,40px);font-weight:800;letter-spacing:-.02em;line-height:1.05;margin:.18em 0 .1em;}
h1 .spark{position:relative;background:linear-gradient(100deg,var(--accent),var(--accent-2),var(--accent));
  -webkit-background-clip:text;background-clip:text;color:transparent;background-size:200% 100%;}
@media (prefers-reduced-motion:no-preference){h1 .spark{animation:shimmer 6s linear infinite;}}
@keyframes shimmer{to{background-position:200% 0;}}
.sub{color:var(--muted);max-width:60ch;margin-top:4px;}
.sub b{color:var(--ink);font-weight:600;}
.themebtn{flex:0 0 auto;border:1px solid var(--line);background:var(--surface);color:var(--muted);
  border-radius:10px;padding:8px 12px;font-size:13px;cursor:pointer;display:flex;gap:7px;align-items:center;}
.themebtn:hover{color:var(--ink);border-color:var(--accent);}

/* KPI tiles */
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:22px 0 6px;}
.kpi{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:14px 15px;
  box-shadow:var(--shadow);cursor:pointer;text-align:left;color:inherit;font:inherit;
  transition:transform .12s ease,border-color .12s ease;position:relative;overflow:hidden;}
.kpi:hover{transform:translateY(-2px);border-color:var(--accent);}
.kpi[aria-pressed="true"]{border-color:var(--accent);box-shadow:0 0 0 2px var(--accent-soft),var(--shadow);}
.kpi .n{font-size:30px;font-weight:800;letter-spacing:-.02em;line-height:1;}
.kpi .l{font-size:12px;color:var(--muted);margin-top:6px;}
.kpi .sub2{font-size:11px;color:var(--faint);margin-top:2px;}
.kpi .stripe{position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--k,transparent);}

/* controls */
.controls{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);
  padding:14px;margin:18px 0 14px;box-shadow:var(--shadow);}
.searchrow{display:flex;gap:10px;align-items:center;flex-wrap:wrap;}
.search{flex:1 1 260px;display:flex;align-items:center;gap:8px;background:var(--surface-2);
  border:1px solid var(--line);border-radius:10px;padding:9px 12px;}
.search input{border:0;background:transparent;color:var(--ink);font:inherit;width:100%;outline:none;}
.search svg{flex:0 0 auto;color:var(--faint);}
.sortsel{background:var(--surface-2);border:1px solid var(--line);color:var(--ink);border-radius:10px;
  padding:9px 10px;font:inherit;font-size:13px;}
.chipset{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px;align-items:center;}
.chipset .glab{font-family:ui-monospace,Menlo,monospace;font-size:10.5px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--faint);margin-right:2px;}
.chip{border:1px solid var(--line);background:var(--surface-2);color:var(--muted);border-radius:999px;
  padding:5px 11px;font-size:12.5px;cursor:pointer;white-space:nowrap;transition:all .12s ease;}
.chip:hover{color:var(--ink);border-color:var(--accent);}
.chip[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);
  color:#fff;font-weight:600;}
:root[data-theme="dark"] .chip[aria-pressed="true"],
.chip[aria-pressed="true"]{color:var(--btn-on,#20180a);}
.chip.b[aria-pressed="true"]{--btn-on:#fff;}
.divider{width:1px;height:20px;background:var(--line);margin:0 4px;}
.count{margin-left:auto;font-size:12.5px;color:var(--muted);}
.reset{border:0;background:none;color:var(--accent);font:inherit;font-size:12.5px;cursor:pointer;text-decoration:underline;}

/* table */
.tablewrap{overflow-x:auto;border:1px solid var(--line);border-radius:var(--radius);background:var(--surface);
  box-shadow:var(--shadow);}
table{border-collapse:collapse;width:100%;min-width:680px;}
thead th{position:sticky;top:0;background:var(--raise);z-index:1;text-align:left;
  font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--faint);
  font-weight:600;padding:11px 12px;border-bottom:1px solid var(--line);white-space:nowrap;}
tbody td{padding:11px 12px;border-bottom:1px solid var(--line);vertical-align:middle;}
tbody tr.row{cursor:pointer;}
tbody tr.row:hover{background:var(--surface-2);}
.name{font-weight:650;}
.name .gx{font-family:ui-monospace,Menlo,monospace;font-size:11px;color:var(--faint);margin-left:7px;}
.formflag{font-family:ui-monospace,Menlo,monospace;font-size:9.5px;letter-spacing:.04em;text-transform:uppercase;
  color:var(--c);border:1px solid color-mix(in srgb,var(--c) 35%,transparent);border-radius:5px;
  padding:1px 5px;margin-left:8px;vertical-align:1px;}
.cattag{font-size:11px;color:var(--muted);}
.dot{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:6px;vertical-align:1px;}
.pill{display:inline-flex;align-items:center;gap:6px;font-size:11.5px;font-weight:650;
  padding:3px 9px;border-radius:999px;line-height:1.35;white-space:nowrap;
  background:var(--surface-2);color:var(--pc,var(--muted));
  background:color-mix(in srgb,var(--pc) 15%,var(--surface));border:1px solid color-mix(in srgb,var(--pc) 30%,transparent);}
.pill.A{--pc:var(--a);} .pill.E{--pc:var(--e);} .pill.B{--pc:var(--b);}
.pill.C{--pc:var(--c);} .pill.D{--pc:var(--d);}
.mchips{display:flex;flex-wrap:wrap;gap:4px;}
.mchip{font-family:ui-monospace,Menlo,monospace;font-size:10.5px;color:var(--muted);
  background:var(--surface-2);border:1px solid var(--line);border-radius:6px;padding:2px 6px;}
.go-y{color:var(--a);font-weight:600;} .go-g{color:var(--b);} .go-n{color:var(--faint);}
.exp{font-size:11px;color:var(--faint);}
td.center,th.center{text-align:center;}

/* detail panel */
tr.detail td{padding:0;border-bottom:1px solid var(--line);background:var(--raise);}
.panel{padding:16px 18px;display:grid;gap:14px;}
.panel .meta{display:flex;flex-wrap:wrap;gap:8px;}
.badge{font-size:11.5px;padding:3px 9px;border-radius:8px;background:var(--surface-2);border:1px solid var(--line);color:var(--muted);}
.badge b{color:var(--ink);}
.methods{display:grid;gap:9px;}
.method{border:1px solid var(--line);border-radius:11px;padding:11px 13px;background:var(--surface);}
.method .top{display:flex;justify-content:space-between;gap:10px;align-items:baseline;flex-wrap:wrap;}
.method .g{font-weight:650;}
.method .enc{color:var(--muted);font-size:13px;}
.method .facts{display:flex;flex-wrap:wrap;gap:8px 16px;margin-top:8px;font-size:12.5px;}
.method .facts span{color:var(--muted);}
.method .facts b{color:var(--ink);}
.locked{color:var(--d);font-weight:650;}
.open{color:var(--a);font-weight:650;}
.acc-no{color:var(--e);}
.tag{font-family:ui-monospace,Menlo,monospace;font-size:10px;padding:1px 6px;border-radius:5px;
  border:1px solid color-mix(in srgb,var(--tc) 40%,transparent);color:var(--tc);
  background:color-mix(in srgb,var(--tc) 12%,transparent);}
.tag.A{--tc:var(--a);} .tag.B{--tc:var(--b);} .tag.C{--tc:var(--c);} .tag.D{--tc:var(--d);}
.mnote{font-size:12px;color:var(--faint);margin-top:6px;}
.gorow{font-size:13px;color:var(--muted);} .gorow b{color:var(--ink);font-weight:600;}
.pnote{font-size:13px;color:var(--muted);}
.empty{padding:40px;text-align:center;color:var(--muted);}

/* legend / footer */
.legend{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:8px;margin:22px 0 6px;}
.leg{display:flex;gap:9px;align-items:flex-start;font-size:12.5px;color:var(--muted);
  background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:10px 12px;}
.leg .k{flex:0 0 auto;width:10px;height:10px;border-radius:3px;margin-top:4px;background:var(--lc);}
.leg b{color:var(--ink);}
footer{margin-top:26px;font-size:12px;color:var(--faint);border-top:1px solid var(--line);padding-top:16px;}
footer a{color:var(--accent);}
/* collection progress */
.progress{display:flex;align-items:center;gap:14px;background:var(--surface);border:1px solid var(--line);
  border-radius:var(--radius);padding:13px 16px;margin:14px 0 2px;box-shadow:var(--shadow);flex-wrap:wrap;}
.progress .phead{font-size:13px;color:var(--muted);}
.progress .phead b{color:var(--ink);font-weight:700;font-size:15px;}
.progress .bar{flex:1 1 200px;height:9px;border-radius:999px;background:var(--surface-2);overflow:hidden;min-width:130px;}
.progress .fill{height:100%;width:0;border-radius:999px;
  background:linear-gradient(90deg,var(--accent),var(--accent-2));transition:width .35s ease;}
.progress .pct{font-family:ui-monospace,Menlo,monospace;font-size:13px;color:var(--accent);font-weight:700;}
.progress .exportbtns{display:flex;gap:8px;}
.mini{border:1px solid var(--line);background:var(--surface-2);color:var(--muted);border-radius:9px;
  padding:7px 11px;font:inherit;font-size:12.5px;cursor:pointer;display:inline-flex;gap:6px;align-items:center;}
.mini:hover{color:var(--ink);border-color:var(--accent);}
.lswarn{font-size:11.5px;color:var(--e);flex-basis:100%;}
/* ownership toggles (HOME / GO) */
th.gotcol,td.gotcol{width:122px;}
.apps{display:flex;gap:5px;justify-content:center;}
.app{font-family:ui-monospace,Menlo,monospace;font-size:10px;font-weight:700;letter-spacing:.03em;
  border:1px solid var(--line);background:var(--surface-2);color:var(--faint);border-radius:7px;
  padding:5px 7px;cursor:pointer;line-height:1;transition:all .12s ease;}
.app:hover{color:var(--ink);border-color:var(--accent);}
.app.home[aria-pressed="true"]{background:var(--home);border-color:var(--home);color:#fff;}
.app.go[aria-pressed="true"]{background:var(--gogo);border-color:var(--gogo);color:#fff;}
.app:disabled{opacity:.25;cursor:not-allowed;}
tr.row.owned{background:color-mix(in srgb,var(--accent) 8%,transparent);}
tr.row.owned:hover{background:color-mix(in srgb,var(--accent) 13%,transparent);}
tr.row.owned .name{color:var(--accent);}
tr.row.both .name::after{content:"✦";color:var(--accent-2);margin-left:6px;font-size:11px;}
.legdot{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--accent-2);
  margin-left:7px;vertical-align:1px;}
.progress .brk{font-family:ui-monospace,Menlo,monospace;font-size:12px;color:var(--muted);
  display:flex;gap:14px;flex-wrap:wrap;align-items:center;}
.progress .brk b{color:var(--ink);}
.progress .brk .h{color:var(--home);} .progress .brk .g{color:var(--gogo);}
.progress .brk .swatch{display:inline-block;width:9px;height:9px;border-radius:3px;margin-right:5px;vertical-align:0;}
@media (max-width:560px){
  .kpi .n{font-size:24px;} .wrap{padding:18px 12px 60px;}
  .name .gx{display:none;}
}
</style>

<div class="wrap">
  <header class="masthead">
    <div>
      <div class="eyebrow">Shiny hunt intelligence · as of <span id="asof" class="mono"></span></div>
      <h1>Legendary &amp; Mythical <span class="spark">Shiny&nbsp;Hunt</span> Database</h1>
      <p class="sub">Every Legendary and Mythical Pokémon (Gens I–IX) and where its shiny can be
        <b>legitimately hunted</b> — main-series methods and <b>Pokémon GO</b> as a first-class platform.
        A true RNG hunt is kept strictly separate from a guaranteed reward or a fixed event shiny.</p>
    </div>
    <button class="themebtn" id="theme" aria-label="Toggle color theme">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
      <span id="themelbl">Theme</span>
    </button>
  </header>

  <section class="kpis" id="kpis"></section>

  <section class="progress">
    <div class="phead">Your shiny collection&nbsp; <b><span id="pcount">0</span> / <span id="ptotal">0</span></b> owned</div>
    <div class="bar"><div class="fill" id="pfill"></div></div>
    <div class="pct" id="ppct">0%</div>
    <div class="brk">
      <span class="h"><span class="swatch" style="background:var(--home)"></span>HOME <b id="nhome">0</b></span>
      <span class="g"><span class="swatch" style="background:var(--gogo)"></span>GO <b id="ngo">0</b></span>
      <span><span class="swatch" style="background:var(--accent-2)"></span>Both <b id="nboth">0</b></span>
    </div>
    <div class="exportbtns">
      <button class="mini" id="exportbtn" title="Download a backup of your caught list">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v12M8 11l4 4 4-4M4 21h16"/></svg>Export</button>
      <label class="mini" title="Restore a caught list from a backup file">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21V9M8 13l4-4 4 4M4 3h16"/></svg>Import
        <input id="importfile" type="file" accept="application/json,.json" hidden></label>
    </div>
    <div class="lswarn" id="lswarn" hidden>Heads-up: this browser is blocking local storage (Private Browsing?), so your picks won't be saved between visits. Use Export to keep a backup.</div>
  </section>

  <section class="controls">
    <div class="searchrow">
      <label class="search">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
        <input id="q" type="search" placeholder="Search a Pokémon or a note…" autocomplete="off" />
      </label>
      <select class="sortsel" id="sort" aria-label="Sort">
        <option value="dex">Sort: National order</option>
        <option value="name">Sort: Name A–Z</option>
        <option value="bucket">Sort: Bucket A→D</option>
        <option value="cat">Sort: Category</option>
      </select>
    </div>
    <div class="chipset" id="chips"></div>
  </section>

  <div class="tablewrap">
    <table>
      <thead><tr>
        <th class="center gotcol" title="Mark where you have this shiny stored">In HOME / GO</th>
        <th>Pokémon</th><th>Category</th><th>Shiny</th><th>Status</th>
        <th>Bucket</th><th>Pokémon GO</th><th>Methods</th><th class="center"></th>
      </tr></thead>
      <tbody id="tb"></tbody>
    </table>
    <div class="empty" id="empty" hidden>No Pokémon match these filters. <button class="reset" onclick="resetAll()">Reset</button></div>
  </div>

  <section class="legend" id="legend"></section>

  <footer>
    <b>Buckets:</b> A = true hunt now · E = hunt historical only · B = guaranteed reward (HOME dex / GO Masterwork) ·
    C = event distribution · D = shiny unavailable. &nbsp;•&nbsp;
    Counts are computed from the dataset. Ultra Beasts are shown as a separate class and excluded from the
    Legendary/Mythical totals. Sources &amp; verification caveats live in <span class="mono">sources.md</span>.
    Post-Jan-2026 Pokémon GO specifics verified by web search where possible; a few exact dates are approximate.
    <br><br><b>Your collection</b> — tap <b>HOME</b> and/or <b>GO</b> on any row to record where you have that shiny
    (light up both for a "both" ✦). It's saved locally in this browser on this device, so reopening in Safari keeps it;
    it doesn't sync across devices — use <b>Export</b> to save a backup file and <b>Import</b> to restore it here or on
    another device. The GO toggle is disabled for shinies not available in Pokémon GO.
  </footer>
</div>

<script id="DB" type="application/json">__DATA__</script>
<script>
const DB = JSON.parse(document.getElementById('DB').textContent);
const S = DB.summary, MONS = DB.mons;
document.getElementById('asof').textContent = DB.access_date;
const GEN_ORDER = ["I","II","III","IV","V","VI","VII","VIII","IX"];
const romanIdx = g => GEN_ORDER.indexOf(g);

/* ---- theme toggle ---- */
const root = document.documentElement;
const tbtn = document.getElementById('theme');
function curTheme(){ return root.getAttribute('data-theme') ||
  (matchMedia('(prefers-color-scheme:dark)').matches ? 'dark':'light'); }
function setTheme(t){ root.setAttribute('data-theme', t);
  document.getElementById('themelbl').textContent = t==='dark'?'Light':'Dark'; }
setTheme(curTheme());
tbtn.onclick = () => setTheme(curTheme()==='dark'?'light':'dark');

/* ---- state ---- */
const state = { q:'', sort:'dex', cat:new Set(), bucket:new Set(), method:new Set(), gen:new Set(), flag:new Set() };

/* ---- ownership tracker: where you have each shiny (HOME / GO), per-device ---- */
const SHINY_TOTAL = MONS.filter(m=>m.shiny_exists).length;
const LS_KEY='shinydex.store.v2';
const LS_OLD='shinydex.caught.v1';
let store={}, lsOK=true;   // store[name] = {home:bool, go:bool, legacy:bool}
try{ store = JSON.parse(localStorage.getItem(LS_KEY)||'{}') || {}; }catch(e){ store={}; }
// one-time migration from the old single-"caught" model -> legacy-owned (app unspecified)
try{
  const old = JSON.parse(localStorage.getItem(LS_OLD)||'null');
  if(old && typeof old==='object'){
    Object.keys(old).forEach(n=>{ if(!store[n]) store[n]={home:false,go:false,legacy:true}; });
    localStorage.removeItem(LS_OLD);
  }
}catch(e){}
try{ localStorage.setItem('__t','1'); localStorage.removeItem('__t'); }catch(e){ lsOK=false; }
function saveStore(){ try{ localStorage.setItem(LS_KEY, JSON.stringify(store)); }catch(e){} }
const rec = n => store[n] || null;
const hasApp = (n,app) => !!(store[n] && store[n][app]);
const isOwned = n => { const r=store[n]; return !!(r && (r.home||r.go||r.legacy)); };
const isBoth = n => { const r=store[n]; return !!(r && r.home && r.go); };
function toggleApp(n,app){
  const r = store[n] || (store[n]={home:false,go:false});
  r[app] = !r[app];
  if(r.legacy) r.legacy=false;               // once a real app is set, drop the legacy marker
  if(!r.home && !r.go && !r.legacy) delete store[n];
  saveStore(); updateProgress();
}
const ownedCount = () => MONS.filter(m=>m.shiny_exists && isOwned(m.name)).length;
const appCount = app => MONS.filter(m=>m.shiny_exists && hasApp(m.name,app)).length;
const bothCount = () => MONS.filter(m=>m.shiny_exists && isBoth(m.name)).length;
function updateProgress(){
  const c=ownedCount(), pct= SHINY_TOTAL ? Math.round(c/SHINY_TOTAL*100):0;
  document.getElementById('pcount').textContent=c;
  document.getElementById('ptotal').textContent=SHINY_TOTAL;
  document.getElementById('pfill').style.width=pct+'%';
  document.getElementById('ppct').textContent=pct+'%';
  document.getElementById('nhome').textContent=appCount('home');
  document.getElementById('ngo').textContent=appCount('go');
  document.getElementById('nboth').textContent=bothCount();
}

/* ---- KPI tiles (clickable) ---- */
const KPIS = [
  {n:S.total_combined, l:'Legendary + Mythical', sub:`${S.total_legendary} Legendary · ${S.total_mythical} Mythical`, k:'--accent'},
  {n:S.huntable_now, l:'Huntable now', sub:'true RNG hunt available', k:'var(--a)', act:['flag','huntable']},
  {n:S.rng_hunt_ever, l:'Ever RNG-huntable', sub:`${S.historical_only} historical-only`, k:'var(--e)', act:['flag','rng']},
  {n:S.shiny_exists, l:'Shiny form exists', sub:`of ${S.total_combined} species`, k:'var(--accent-2)', act:['flag','shiny']},
  {n:S.event_or_reward_only, l:'Guaranteed / event only', sub:'shiny exists, never a hunt', k:'var(--b)', act:['flag','eventonly']},
  {n:S.shiny_never, l:'No shiny ever', sub:'shiny unavailable', k:'var(--d)', act:['bucket','D']},
];
const kEl = document.getElementById('kpis');
KPIS.forEach(k=>{
  const b=document.createElement('button'); b.className='kpi'; b.setAttribute('aria-pressed','false');
  b.innerHTML=`<span class="stripe" style="--k:${k.k}"></span><div class="n">${k.n}</div><div class="l">${k.l}</div><div class="sub2">${k.sub}</div>`;
  if(k.act){ b.onclick=()=>{ toggle(state[k.act[0]], k.act[1]); syncChips(); render(); };
    b.dataset.grp=k.act[0]; b.dataset.val=k.act[1]; }
  else b.style.cursor='default';
  kEl.appendChild(b);
});

/* ---- filter chips ---- */
const CHIPS = [
  {g:'Category', items:[['cat','Legendary'],['cat','Mythical'],['cat','Ultra Beast']]},
  {sep:1},
  {g:'Bucket', items:[['bucket','A'],['bucket','E'],['bucket','B'],['bucket','C'],['bucket','D']]},
  {sep:1},
  {g:'Quick', items:[['flag','huntable','Huntable now'],['flag','go','GO shiny'],['flag','gorng','RNG in GO'],
    ['flag','home','HOME guaranteed'],['flag','eventonly','Event-only'],
    ['flag','inhome','In HOME'],['flag','ingo','In GO'],['flag','both','In both'],
    ['flag','owned','Owned (any)'],['flag','need','Not in either app'],['flag','form','Alt forms']]},
  {sep:1},
  {g:'Method', items:[['method','da','Dynamax Adv.'],['method','uw','Ultra Wormhole'],['method','bdsp','Ramanas Park'],
    ['method','swsh','SwSh static'],['method','za','Z-A Hyperspace'],['method','gorng','GO raid/box']]},
  {sep:1},
  {g:'Gen', items:GEN_ORDER.map(g=>['gen',g,g])},
];
const chipEl = document.getElementById('chips');
function buildChips(){
  CHIPS.forEach(block=>{
    if(block.sep){ const d=document.createElement('span'); d.className='divider'; chipEl.appendChild(d); return; }
    const lab=document.createElement('span'); lab.className='glab'; lab.textContent=block.g; chipEl.appendChild(lab);
    block.items.forEach(([grp,val,label])=>{
      const c=document.createElement('button'); c.className='chip'+(grp==='bucket'&&val==='B'?' b':'');
      c.textContent=label||val; c.setAttribute('aria-pressed','false');
      c.dataset.grp=grp; c.dataset.val=val;
      c.onclick=()=>{ toggle(state[grp], val); syncChips(); render(); };
      chipEl.appendChild(c);
    });
  });
  const cnt=document.createElement('span'); cnt.className='count'; cnt.id='count'; chipEl.appendChild(cnt);
  const rs=document.createElement('button'); rs.className='reset'; rs.textContent='Reset all'; rs.onclick=resetAll; chipEl.appendChild(rs);
}
function toggle(set,v){ set.has(v)?set.delete(v):set.add(v); }
function syncChips(){
  document.querySelectorAll('.chip').forEach(c=>{
    const s=state[c.dataset.grp]; c.setAttribute('aria-pressed', s&&s.has(c.dataset.val)?'true':'false'); });
  document.querySelectorAll('.kpi[data-grp]').forEach(b=>{
    const s=state[b.dataset.grp]; b.setAttribute('aria-pressed', s&&s.has(b.dataset.val)?'true':'false'); });
}
function resetAll(){ state.q=''; document.getElementById('q').value='';
  ['cat','bucket','method','gen','flag'].forEach(k=>state[k].clear()); syncChips(); render(); }

document.getElementById('q').addEventListener('input', e=>{ state.q=e.target.value.toLowerCase().trim(); render(); });
document.getElementById('sort').addEventListener('change', e=>{ state.sort=e.target.value; render(); });

/* ---- filtering ---- */
function flagOK(m){
  for(const f of state.flag){
    if(f==='huntable' && !m.huntable_now) return false;
    if(f==='rng' && !m.rng_hunt) return false;
    if(f==='shiny' && !m.shiny_exists) return false;
    if(f==='go' && !m.go_shiny) return false;
    if(f==='gorng' && !m.go_rng_hunt) return false;
    if(f==='home' && !m.home_guaranteed) return false;
    if(f==='eventonly' && !m.event_only) return false;
    if(f==='inhome' && !hasApp(m.name,'home')) return false;
    if(f==='ingo' && !hasApp(m.name,'go')) return false;
    if(f==='both' && !isBoth(m.name)) return false;
    if(f==='owned' && !isOwned(m.name)) return false;
    if(f==='need' && (isOwned(m.name) || !m.shiny_exists)) return false;
    if(f==='form' && !m.is_form) return false;
  }
  return true;
}
function methodOK(m){
  for(const md of state.method){
    if(md==='da' && !m.in_da) return false;
    if(md==='uw' && !m.in_uw) return false;
    if(md==='bdsp' && !m.in_bdsp) return false;
    if(md==='swsh' && !m.in_swsh) return false;
    if(md==='za' && !m.in_za) return false;
    if(md==='gorng' && !m.go_rng_hunt) return false;
  }
  return true;
}
function match(m){
  if(state.cat.size && !state.cat.has(m.category)) return false;
  if(state.bucket.size && !state.bucket.has(m.bucket)) return false;
  if(state.gen.size && !state.gen.has(m.gen)) return false;
  if(!flagOK(m) || !methodOK(m)) return false;
  if(state.q){ if(!(m.name.toLowerCase().includes(state.q) || (m.notes||'').toLowerCase().includes(state.q) ||
     (m.go||'').toLowerCase().includes(state.q))) return false; }
  return true;
}
const BORD={A:0,E:1,B:2,C:3,D:4};
function sortRows(rows){
  const s=state.sort;
  return rows.sort((a,b)=>{
    if(s==='name') return a.name.localeCompare(b.name);
    if(s==='bucket') return (BORD[a.bucket]-BORD[b.bucket])|| (romanIdx(a.gen)-romanIdx(b.gen));
    if(s==='cat') return a.category.localeCompare(b.category)||(romanIdx(a.gen)-romanIdx(b.gen))||a.name.localeCompare(b.name);
    return (romanIdx(a.gen)-romanIdx(b.gen))|| MONS.indexOf(a)-MONS.indexOf(b); // dex-ish
  });
}

/* ---- render ---- */
const methodBadges = m => {
  const out=[];
  if(m.in_da) out.push('DA'); if(m.in_uw) out.push('USUM'); if(m.in_bdsp) out.push('BDSP');
  if(m.in_swsh) out.push('SwSh'); if(m.in_za) out.push('Z-A'); if(m.go_rng_hunt) out.push('GO');
  if(!out.length){ for(const x of m.methods){ if(x.cat==='A'&&!x.accessible&&!x.locked){out.push('legacy');break;} } }
  return out;
};
function goCell(m){
  if(!m.go_shiny) return '<span class="go-n">—</span>';
  return m.go_rng_hunt ? '<span class="go-y">RNG hunt</span>' : '<span class="go-g">guaranteed</span>';
}
const esc = s => (s||'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
const tb = document.getElementById('tb');

function detailHTML(m){
  const meth = m.methods.map(x=>{
    const lock = x.locked?'<span class="locked">Shiny-locked</span>':'<span class="open">Not locked</span>';
    const odds = x.base && x.base!=='n/a' ? `<span>Odds <b class="mono">${esc(x.base)}</b>${x.charm&&x.charm!=='n/a'?` → <b class="mono">${esc(x.charm)}</b> charm`:''}</span>`:'';
    const acc = x.accessible?'<span>Accessible <b>Yes</b></span>':'<span class="acc-no">Accessible <b>No — historical</b></span>';
    return `<div class="method"><div class="top"><span class="g">${esc(x.game)} <span class="tag ${x.cat}">${x.cat}</span></span></div>
      <div class="enc">${esc(x.encounter)}</div>
      <div class="facts">${lock}${odds}${acc}<span>Charm: <b>${esc(x.charm_eff)}</b></span></div>
      ${x.note?`<div class="mnote">${esc(x.note)}</div>`:''}</div>`;
  }).join('');
  return `<div class="panel">
    <div class="meta">
      <span class="badge">Gen <b>${m.gen}</b></span>
      <span class="badge">${m.category}</span>
      <span class="badge">Shiny exists: <b>${m.shiny_exists?'Yes':'No'}</b></span>
      <span class="badge">RNG hunt ever: <b>${m.rng_hunt?'Yes':'No'}</b></span>
      <span class="badge">Huntable now: <b>${m.huntable_now?'Yes':'No'}</b></span>
      <span class="badge">HOME guaranteed: <b>${m.home_guaranteed?'Yes':'No'}</b></span>
      <span class="badge">Event-only: <b>${m.event_only?'Yes':'No'}</b></span>
      ${m.is_form?`<span class="badge">Form of <b>${esc(m.base)}</b></span>`:''}
    </div>
    ${m.forms&&m.forms.length?`<div class="pnote"><b>Alternate forms:</b> ${m.forms.map(esc).join(' &nbsp;·&nbsp; ')}</div>`:''}
    <div class="methods">${meth}</div>
    <div class="gorow"><b>Pokémon GO:</b> ${esc(m.go)||'Not in Pokémon GO.'}</div>
    <div class="pnote">${esc(m.notes)}</div>
  </div>`;
}

function render(){
  const rows = sortRows(MONS.filter(match));
  document.getElementById('count').textContent = `${rows.length} shown`;
  tb.innerHTML='';
  document.getElementById('empty').hidden = rows.length>0;
  const frag=document.createDocumentFragment();
  rows.forEach(m=>{
    const tr=document.createElement('tr'); tr.className='row'+(isOwned(m.name)?' owned':'')+(isBoth(m.name)?' both':''); tr.tabIndex=0;
    const legacy = rec(m.name) && rec(m.name).legacy;
    tr.innerHTML = `
      <td class="center gotcol">${m.shiny_exists ? `<div class="apps">
        <button class="app home" data-name="${esc(m.name)}" data-app="home" aria-pressed="${hasApp(m.name,'home')}" aria-label="${esc(m.name)} in Pokémon HOME">HOME</button>
        <button class="app go" data-name="${esc(m.name)}" data-app="go" aria-pressed="${hasApp(m.name,'go')}" ${m.go_shiny?'':'disabled title="Shiny not available in Pokémon GO"'} aria-label="${esc(m.name)} in Pokémon GO">GO</button>
      </div>` : '<span class="go-n" title="No shiny exists to store">—</span>'}</td>
      <td><span class="name">${esc(m.name)}<span class="gx">${m.gen}</span></span>${legacy?'<span class="legdot" title="Marked owned earlier — set HOME or GO"></span>':''}${m.forms&&m.forms.length&&!m.is_form?'<span class="formflag" title="Has alternate forms">forms</span>':''}</td>
      <td><span class="cattag">${m.category}${m.is_form?` · form of ${esc(m.base)}`:''}</span></td>
      <td>${m.shiny_exists?'Yes':'<span class="go-n">No</span>'}</td>
      <td>${m.huntable_now?'<span class="pill A"><span class="dot" style="background:var(--a)"></span>Now</span>':
            (m.rng_hunt?'<span class="pill E">Historical</span>':'<span class="go-n">—</span>')}</td>
      <td><span class="pill ${m.bucket}">${m.bucket}</span></td>
      <td>${goCell(m)}</td>
      <td><div class="mchips">${methodBadges(m).map(x=>`<span class="mchip">${x}</span>`).join('')||'<span class="go-n">—</span>'}</div></td>
      <td class="center exp">▸</td>`;
    const dtr=document.createElement('tr'); dtr.className='detail'; dtr.hidden=true;
    const dtd=document.createElement('td'); dtd.colSpan=9; dtr.appendChild(dtd);
    const openIt=()=>{ const now=dtr.hidden; if(now){ dtd.innerHTML=detailHTML(m); }
      dtr.hidden=!now; tr.querySelector('.exp').textContent = now?'▾':'▸'; };
    tr.onclick=openIt; tr.onkeydown=e=>{ if(e.key==='Enter'||e.key===' '){e.preventDefault();openIt();} };
    tr.querySelectorAll('.app').forEach(btn=>{
      btn.onclick=(e)=>{ e.stopPropagation(); if(btn.disabled) return;
        const n=btn.dataset.name, app=btn.dataset.app;
        toggleApp(n,app); btn.setAttribute('aria-pressed', hasApp(n,app));
        tr.classList.toggle('owned', isOwned(n)); tr.classList.toggle('both', isBoth(n));
        const ld=tr.querySelector('.legdot'); if(ld) ld.remove();
        if(['inhome','ingo','both','owned','need'].some(k=>state.flag.has(k))) render();
      };
      btn.onkeydown=e=>{ if(e.key==='Enter'||e.key===' ') e.stopPropagation(); };
    });
    frag.appendChild(tr); frag.appendChild(dtr);
  });
  tb.appendChild(frag);
}

/* ---- legend ---- */
const LEG=[['var(--a)','A — true hunt now','roll / reset / raid / breed'],
  ['var(--e)','E — historical only','discontinued service or expired event'],
  ['var(--b)','B — guaranteed reward','HOME dex reward, GO Masterwork'],
  ['var(--c)','C — event distribution','fixed shiny code/gift'],
  ['var(--d)','D — shiny unavailable','no legitimate shiny exists']];
document.getElementById('legend').innerHTML = LEG.map(([c,t,d])=>
  `<div class="leg"><span class="k" style="--lc:${c}"></span><span><b>${t}</b><br>${d}</span></div>`).join('');

/* ---- export / import backup ---- */
document.getElementById('exportbtn').onclick = async () => {
  const items={};
  MONS.forEach(m=>{ const r=store[m.name]; if(r && (r.home||r.go||r.legacy))
    items[m.name]={home:!!r.home, go:!!r.go}; });
  const payload = {app:'legendary-mythical-shiny-hunt', version:2,
    exported:new Date().toISOString(), total:SHINY_TOTAL, owned:ownedCount(), items};
  const data = JSON.stringify(payload, null, 2);
  if(window.claude && window.claude.downloads){
    try{ await window.claude.downloads.save({filename:'shiny-collection.json', data}); }
    catch(err){ if(err && err.code!=='declined')
      alert('Could not export here — but your picks are still saved in this browser.'); }
  } else {
    try{ const url=URL.createObjectURL(new Blob([data],{type:'application/json'}));
      const a=document.createElement('a'); a.href=url; a.download='shiny-collection.json'; a.click();
      URL.revokeObjectURL(url);
    }catch(e){ alert('Export is not supported in this view.'); }
  }
};
document.getElementById('importfile').onchange = (e) => {
  const f=e.target.files[0]; if(!f) return;
  const r=new FileReader();
  r.onload=()=>{ try{ const o=JSON.parse(r.result); const known=new Set(MONS.map(m=>m.name)); let n=0;
      if(o && o.items && typeof o.items==='object'){                 // v2 format
        Object.entries(o.items).forEach(([name,v])=>{ if(!known.has(name)) return;
          store[name]={home:!!v.home, go:!!v.go}; if(!v.home&&!v.go) store[name].legacy=true; n++; });
      } else {                                                        // v1 (list or {caught:[]})
        const list=Array.isArray(o)?o:(o.caught||[]);
        list.forEach(name=>{ if(known.has(name)){ store[name]=store[name]||{home:false,go:false,legacy:true}; n++; } });
      }
      saveStore(); updateProgress(); render();
      alert('Imported '+n+' Pokémon from the backup.');
    }catch(err){ alert('That file could not be read as a collection backup.'); } };
  r.readAsText(f); e.target.value='';
};

if(!lsOK) document.getElementById('lswarn').hidden=false;
buildChips(); syncChips(); updateProgress(); render();
</script>
"""

out = HTML.replace("__DATA__", DATA_JSON)
open(os.path.join(HERE, "shiny_explorer.html"), "w", encoding="utf-8").write(out)
print("wrote shiny_explorer.html", len(out), "bytes")
