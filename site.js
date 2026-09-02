const META={
  en:{
    title:'New Zealand Property Intelligence API | PropData New Zealand',
    description:'New Zealand property intelligence from authoritative Toitū Te Whenua LINZ data. Resolve addresses, parcels, titles, coordinates and available building outlines through one production PropData API.',
    ogTitle:'New Zealand Property Intelligence. One API. National Coverage.',
    ogDescription:'3.04M primary parcels, 2.42M authoritative addresses, 2.45M property titles and a national building-outline layer—connected through one source-aware property API.',
    locale:'en_NZ'
  },
  mi:{
    title:'Mōhiotanga Rawa o Aotearoa | PropData New Zealand',
    description:'He API mōhiotanga rawa mō Aotearoa i hangaia ki runga i ngā raraunga whai mana o Toitū Te Whenua LINZ—wāhitau, pānga whenua, taitara, taunga wāhi me ngā tapuwae whare.',
    ogTitle:'Mōhiotanga Rawa o Aotearoa. Kotahi te API. Kapi ā-motu.',
    ogDescription:'Ka hono a PropData i ngā wāhitau whai mana, ngā pānga whenua, ngā taitara me ngā tapuwae whare o Aotearoa ki tētahi whatunga rawa whai puna.',
    locale:'mi_NZ'
  }
};

function setMeta(selector,attribute,value){const el=document.querySelector(selector);if(el)el.setAttribute(attribute,value)}
function setLanguage(lang,{updateUrl=true}={}){
  if(!META[lang])lang='en';
  document.documentElement.lang=lang==='mi'?'mi-NZ':'en-NZ';
  try{localStorage.setItem('propdata_nz_lang',lang)}catch{}
  document.querySelectorAll('[data-en][data-mi]').forEach(el=>{const value=el.dataset[lang];if(value!=null)el.textContent=value});
  document.querySelectorAll('.lang-btn').forEach(btn=>{const active=btn.dataset.lang===lang;btn.classList.toggle('active',active);btn.setAttribute('aria-pressed',String(active))});
  const meta=META[lang];
  document.title=meta.title;
  setMeta('meta[name="description"]','content',meta.description);
  setMeta('meta[property="og:title"]','content',meta.ogTitle);
  setMeta('meta[property="og:description"]','content',meta.ogDescription);
  setMeta('meta[property="og:locale"]','content',meta.locale);
  setMeta('meta[name="twitter:title"]','content',meta.ogTitle);
  setMeta('meta[name="twitter:description"]','content',meta.ogDescription);
  if(updateUrl){const u=new URL(location.href);if(lang==='en')u.searchParams.delete('lang');else u.searchParams.set('lang',lang);history.replaceState({},'',u)}
}

document.querySelectorAll('.lang-btn').forEach(btn=>btn.addEventListener('click',()=>setLanguage(btn.dataset.lang)));
const params=new URLSearchParams(location.search);
let stored='';try{stored=localStorage.getItem('propdata_nz_lang')||''}catch{}
const requested=params.get('lang');
const preferred=requested&&META[requested]?requested:(stored&&META[stored]?stored:((navigator.language||'').toLowerCase().startsWith('mi')?'mi':'en'));
setLanguage(preferred,{updateUrl:false});

const header=document.getElementById('site-header')||document.querySelector('.site-header');
const nav=document.getElementById('primary-nav')||document.querySelector('.nav-links');
const toggle=document.getElementById('menu-toggle')||document.querySelector('.menu-toggle');
const onScroll=()=>header?.classList.toggle('scrolled',scrollY>12);
addEventListener('scroll',onScroll,{passive:true});onScroll();

toggle?.addEventListener('click',()=>{const open=nav?.classList.toggle('open');toggle.setAttribute('aria-expanded',String(Boolean(open)))});
nav?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');toggle?.setAttribute('aria-expanded','false');nav.querySelectorAll('details[open]').forEach(d=>d.removeAttribute('open'))}));

document.addEventListener('click',event=>{
  document.querySelectorAll('.nav-menu[open]').forEach(details=>{if(!details.contains(event.target))details.removeAttribute('open')});
  if(nav?.classList.contains('open')&&!nav.contains(event.target)&&!toggle?.contains(event.target)){nav.classList.remove('open');toggle?.setAttribute('aria-expanded','false')}
});

document.querySelectorAll('[data-copy]').forEach(btn=>btn.addEventListener('click',async()=>{
  const id=btn.getAttribute('data-copy');const el=document.getElementById(id);if(!el)return;
  try{await navigator.clipboard.writeText(el.innerText);const old=btn.textContent;btn.textContent=document.documentElement.lang.startsWith('mi')?'Kua tāruatia':'Copied';setTimeout(()=>btn.textContent=old,1200)}catch{}
}));

const success=params.get('success');
if(success==='1')document.getElementById('success')?.classList.add('show');

const reduceMotion=matchMedia('(prefers-reduced-motion: reduce)').matches;
if(!reduceMotion&&'IntersectionObserver'in window){
  const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');observer.unobserve(entry.target)}}),{threshold:.08,rootMargin:'0px 0px -18px'});
  document.querySelectorAll('[data-reveal]').forEach(el=>observer.observe(el));
}else document.querySelectorAll('[data-reveal]').forEach(el=>el.classList.add('visible'));

addEventListener('pageshow',()=>{if(location.hash){const target=document.querySelector(location.hash);if(target)setTimeout(()=>target.scrollIntoView({block:'start'}),0)}});
