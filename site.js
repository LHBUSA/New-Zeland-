const META={
  en:{
    title:'New Zealand Property Intelligence API | PropData New Zealand',
    description:'National New Zealand property intelligence from authoritative Toitū Te Whenua LINZ data: 3.04M primary parcels, 2.42M addresses, 2.45M titles and 3.27M building outlines through one PropData API.',
    ogTitle:'New Zealand Property Intelligence. One API. National Coverage.',
    ogDescription:'3.04M primary parcels, 2.42M authoritative addresses, 2.45M property titles and 3.27M LINZ building outlines—connected through one source-aware property API.',
    locale:'en_NZ'
  },
  mi:{
    title:'Mōhiotanga Rawa o Aotearoa | PropData New Zealand',
    description:'He mōhiotanga rawa ā-motu mō Aotearoa mai i ngā raraunga whai mana o Toitū Te Whenua LINZ: 3.04M pānga whenua matua, 2.42M wāhitau, 2.45M taitara me 3.27M tapuwae whare mā tētahi API PropData kotahi.',
    ogTitle:'Mōhiotanga Rawa o Aotearoa. Kotahi te API. Kapi ā-motu.',
    ogDescription:'3.04M pānga whenua matua, 2.42M wāhitau whai mana, 2.45M taitara rawa me 3.27M tapuwae whare LINZ—kua hono ki tētahi API rawa whai-puna.',
    locale:'mi_NZ'
  }
};

const FX={NZD_TO_USD:0.584444,USD_TO_NZD:1.71144,asOf:'2 Sep 2026'};

const HOME_TRANSLATIONS={
  'Addresses → parcels → titles → buildings':'Wāhitau → pānga whenua → taitara → whare',
  'Footprints + capture provenance':'Tapuwae whare + takenga hopunga',
  'Property products and maps':'Hua rawa me ngā mahere',
  'AI & Agents':'AI me ngā māngai',
  'Structured property identity':'Tuakiri rawa kua whakaraupapatia',
  'Bulk & Enterprise':'Raraunga nui me te hinonga',
  'Custom delivery and licensing':'Tukunga ritenga me te raihana',
  'Core global platform':'Tūāpapa matua ā-ao',
  'Country coverage overview':'Tirohanga kapi whenua',
  'Estonia property intelligence':'Mōhiotanga rawa o Estonia',
  'Data Solutions':'Rongoā Raraunga',
  'Bulk and custom data':'Raraunga nui me te raraunga ritenga',
  'Company':'Kamupene',
  'LIVE GRAPH':'WHATUNGA ORA',
  '✓ VERIFIED':'✓ KUA WHAKAMANA',
  'VERIFIED':'KUA WHAKAMANA',
  'Address ID':'ID Wāhitau',
  'Parcel ID':'ID Pānga Whenua',
  'Appellation':'Ingoa ture whenua',
  'Land district':'Rohe whenua',
  'Calculated area':'Rohe kua tātaihia',
  'Title graph':'Whatunga taitara',
  'Multiple current titles':'He maha ngā taitara onāianei',
  'ADDRESS':'WĀHITAU',
  'PARCEL':'PĀNGA WHENUA',
  'TITLES':'TAITARA',
  'Primary national source':'Puna matua ā-motu',
  'Fail-closed':'Kati-haumaru',
  'No invented source facts':'Kāore he meka puna tito',
  'Parcel & Title Intelligence':'Mōhiotanga Pānga Whenua me te Taitara',
  '3.04M primary parcels linked into a 2.45M-title national graph.':'3.04M ngā pānga whenua matua kua hono ki tētahi whatunga ā-motu e 2.45M ngā taitara.',
  'Building Footprints':'Tapuwae Whare',
  'LINZ outline geometry with capture and imagery provenance where published.':'Āhuahanga tapuwae LINZ me te takenga hopunga me te whakaahua, ina whakaputaina.',
  'Coordinate Resolution':'Whakataunga Taunga Wāhi',
  'Latitude/longitude into containing parcel and connected property context.':'Ka whakatauria te ahopae/ahopou ki te pānga whenua me te horopaki rawa e hono ana.',
  'Developer First':'Mō ngā Kaiwhakawhanake',
  'Production REST, MCP workflows, bulk delivery and custom contracts.':'REST whakaputa, rerengamahi MCP, tukunga raraunga nui me ngā kirimana ritenga.',
  'NATIONAL PROPERTY GRAPH':'WHATUNGA RAWA Ā-MOTU',
  'LINZ primary parcels':'Ngā pānga whenua matua LINZ',
  'authoritative addresses':'ngā wāhitau whai mana',
  'property titles':'ngā taitara rawa',
  'title ↔ parcel associations':'ngā hononga taitara ↔ pānga whenua',
  'National baseline complete':'Kua oti te paparanga ā-motu',
  'National building-outline baseline complete':'Kua oti te paparanga tapuwae whare ā-motu',
  'LINZ Building Outlines':'Ngā Tapuwae Whare LINZ',
  'building outlines':'tapuwae whare',
  'COMPLETE':'KUA OTI',
  'national baseline':'paparanga ā-motu',
  'VERIFIED IN THE PRODUCTION GRAPH':'KUA WHAKAMANA I TE WHATUNGA WHAKAPUTA',
  'VERIFIED PROPERTY GRAPH':'WHATUNGA RAWA KUA WHAKAMANA',
  'Primary parcel':'Pānga whenua matua',
  'Attached title graph':'Whatunga taitara kua hono',
  '+ more':'+ anō',
  'PARCEL ID':'ID PĀNGA WHENUA',
  'COORDINATES':'TAUNGA WĀHI',
  'Copy':'Tārua',
  'Open the developer docs →':'Whakatuwheratia ngā tuhinga kaiwhakawhanake →',
  'SOURCE-AWARE PROPERTY LAYERS':'NGĀ PAPARANGA RAWA WHAI-PUNA',
  'Authoritative addresses':'Ngā wāhitau whai mana',
  'LINZ identity, road/locality structure, lifecycle and coordinates.':'Tuakiri LINZ, hanganga rori/rohe, huringa ora me ngā taunga wāhi.',
  'Primary parcels':'Ngā pānga whenua matua',
  'Parcel ID, appellation, land district, area, topology and available geometry.':'ID pānga whenua, ingoa ture, rohe whenua, rahinga, āhuatanga topological me te āhuahanga e wātea ana.',
  'Property titles':'Ngā taitara rawa',
  'Title status, type, issue date, estate description and source context.':'Tūnga taitara, momo, rā tuku, whakaahuatanga whenua me te horopaki puna.',
  'Title ↔ parcel graph':'Whatunga taitara ↔ pānga whenua',
  'Explicit associations supporting multi-title and unit-title property contexts.':'Ngā hononga mārama mō ngā rawa taitara-maha me ngā taitara-wae.',
  'Coordinate resolution':'Whakataunga taunga wāhi',
  'WGS84 latitude/longitude into containing property context.':'Ahopae/ahopou WGS84 ki te horopaki rawa kei roto.',
  'Building outlines':'Ngā tapuwae whare',
  '3,268,141 national LINZ building outlines with capture and imagery provenance preserved where published.':'3,268,141 ngā tapuwae whare LINZ ā-motu, me te takenga hopunga me te whakaahua e tiakina ana ina whakaputaina.',
  'BUILT FOR PRODUCT TEAMS':'HE MEA HANGA MŌ NGĀ RŌPŪ HUA',
  'Search, property profiles, parcel-aware workflows and product differentiation.':'Rapu, kōtaha rawa, rerengamahi mōhio-pānga-whenua me te rerekētanga hua.',
  'GIS & Mapping':'GIS me te Mahere',
  'Coordinate resolution, parcel geometry, building footprints and source context.':'Whakataunga taunga wāhi, āhuahanga pānga whenua, tapuwae whare me te horopaki puna.',
  'Structured property identity instead of unverified web-search output.':'Tuakiri rawa kua whakaraupapatia, kaua ko ngā hua rapu tukutuku kāore i whakamana.',
  'Underwriting':'Aromatawai Pūtea',
  'Traceable title, parcel and property context for internal decision systems.':'Horopaki taitara, pānga whenua me te rawa ka taea te whai mō ngā pūnaha whakatau ā-roto.',
  'Construction':'Hangahanga',
  'Building footprint context, capture provenance and cadastral relationships.':'Horopaki tapuwae whare, takenga hopunga me ngā hononga cadastral.',
  'Data Platforms':'Ngā Tūāpapa Raraunga',
  'Skip the national ingestion and reconciliation stack and ship the customer layer.':'Kaua e hanga i te pūnaha uta me te whakatikatika ā-motu; tukuna kē te paparanga kiritaki.',
  'SOURCE TRANSPARENCY':'MĀRAMA KI NGĀ PUNA',
  'PropData is an independent product of PropTechUSA.ai and is not operated by or affiliated with LINZ or the New Zealand government.':'He hua motuhake a PropData nā PropTechUSA.ai, ā, kāore i whakahaerehia, kāore hoki i whai hononga ki LINZ, ki te Kāwanatanga o Aotearoa rānei.',
  'PRIMARY NATIONAL SOURCE':'PUNA MATUA Ā-MOTU',
  'DEVELOPER GEOMETRY':'ĀHUHANGA MŌ NGĀ KAIWHAKAWHANAKE',
  'BUILDING-LAYER ATTRIBUTION':'TAKENGA PAPARANGA WHARE',
  'FAIL-CLOSED':'KATI-HAUMARU',
  'NO INVENTED SOURCE FACTS':'KĀORE HE MEKA PUNA TITO',
  'LIVE STRIPE CHECKOUT · NZD':'STRIPE ORA · UTU NZD',
  'DEVELOPER':'KAIWHAKAWHANAKE',
  'Build & evaluate':'Hanga me te aromatawai',
  '10,000 requests / month':'10,000 tono / marama',
  'National address, parcel & title graph':'Whatunga wāhitau, pānga whenua me te taitara ā-motu',
  'Coordinate-to-property resolution':'Whakataunga taunga wāhi ki te rawa',
  'Available parcel geometry':'Āhuahanga pānga whenua e wātea ana',
  'LINZ provenance':'Takenga LINZ',
  'REST API access':'Urunga REST API',
  'Subscribe with Stripe →':'Ohauru mā Stripe →',
  'MOST POPULAR':'TINO RONGONUI',
  'BUILDER':'KAIHANGA',
  'Production applications':'Ngā taupānga whakaputa',
  '50,000 requests / month':'50,000 tono / marama',
  'Everything in Developer':'Ngā mea katoa o te mahere Kaiwhakawhanake',
  'Production PropTech & GIS use':'Whakamahinga PropTech me GIS whakaputa',
  'Title relationship workflows':'Rerengamahi hononga taitara',
  'National building-outline layer':'Paparanga tapuwae whare ā-motu',
  'Priority integration support':'Tautoko whakaurunga matua',
  'SCALE':'TAUMATA NUI',
  'High-volume systems':'Ngā pūnaha rōrahi nui',
  '250,000 requests / month':'250,000 tono / marama',
  'Everything in Builder':'Ngā mea katoa o te mahere Kaihanga',
  'High-volume production':'Whakaputa rōrahi nui',
  'GIS / AI workloads':'Ngā kawenga GIS / AI',
  'Priority support':'Tautoko matua',
  'Commercial platform use':'Whakamahinga tūāpapa arumoni',
  'ENTERPRISE':'HINONGA',
  'Infrastructure contracts':'Ngā kirimana hanganga',
  'Custom':'Ritenga',
  'Bulk, white-label & custom delivery':'Tukunga raraunga nui, tapanga mā me te ritenga',
  'Bulk/data licensing':'Raihana raraunga nui',
  'Custom endpoints & contracts':'Ngā pito-mutunga me ngā kirimana ritenga',
  'White-label infrastructure':'Hanganga tapanga mā',
  'Commercial SLA':'SLA arumoni',
  'Multi-country PropData':'PropData whenua-maha',
  'Talk to enterprise sales →':'Kōrero ki te rōpū hoko hinonga →',
  'Stripe checkout collects billing details and supported tax IDs. API access is provisioned after successful payment; direct API keys remain server-side credentials.':'Ka kohia e Stripe ngā taipitopito nama me ngā ID tāke e tautokona ana. Ka whakaritehia te urunga API i muri i te utu angitu; ka noho tonu ngā kī API tika ki te taha tūmau.',
  'Choose a plan →':'Kōwhiria he mahere →',
  'Developer docs':'Tuhinga kaiwhakawhanake',
  'A standalone New Zealand property-intelligence product powered by the PropData global property infrastructure.':'He hua mōhiotanga rawa motuhake mō Aotearoa, e whakahaeretia ana e te hanganga rawa ā-ao o PropData.',
  'New Zealand':'Aotearoa',
  'Coverage':'Kapi',
  'Verified property':'Rawa kua whakamana',
  'API documentation':'Tuhinga API',
  'Pricing':'Utu',
  'Developers':'Ngā Kaiwhakawhanake',
  'Quick start':'Tīmata tere',
  'Property lookup':'Rapunga rawa',
  'Coverage semantics':'Tikanga kapi',
  'Support':'Tautoko',
  'PropData Network':'Whatunga PropData',
  'PropData Platform':'Tūāpapa PropData',
  'Global Coverage':'Kapi ā-Ao',
  'Commercial':'Arumoni',
  'Enterprise':'Hinonga',
  'Source statement:':'Tauākī puna:'
};

const ORIGINAL_TEXT=new WeakMap();
function setMeta(selector,attribute,value){const el=document.querySelector(selector);if(el)el.setAttribute(attribute,value)}

function promoteBuildingBaseline(){
  if(document.body.classList.contains('docs-body'))return;
  const heroBuilding=document.querySelector('.hero-metrics > div:nth-child(4)');
  if(heroBuilding){
    const value=heroBuilding.querySelector('b');
    const label=heroBuilding.querySelector('small');
    if(value)value.textContent='3.27M';
    if(label){label.dataset.en='Building outlines';label.dataset.mi='Tapuwae whare';label.textContent='Building outlines';}
  }

  const coverageCopy=document.querySelector('.coverage-section .section-head p');
  if(coverageCopy){
    coverageCopy.dataset.en='The national parcel, address, title, title↔parcel and building-outline baselines are complete. PropData now exposes 3,268,141 LINZ building outlines as a completed national source layer, with capture and source provenance preserved where published.';
    coverageCopy.dataset.mi='Kua oti ngā paparanga ā-motu mō ngā pānga whenua, ngā wāhitau, ngā taitara, ngā hononga taitara↔pānga whenua me ngā tapuwae whare. Kua whakaratohia e PropData he 3,268,141 tapuwae whare LINZ hei paparanga puna ā-motu kua oti, me te takenga hopunga me te puna e tiakina ana ina whakaputaina.';
    coverageCopy.textContent=coverageCopy.dataset.en;
  }

  const block=document.querySelector('.building-progress');
  if(block){
    block.classList.add('complete');
    const status=block.querySelector('small');
    if(status){status.dataset.en='National building-outline baseline complete';status.dataset.mi='Kua oti te paparanga tapuwae whare ā-motu';status.textContent=status.dataset.en;}
    const nums=block.querySelector('.progress-numbers');
    if(nums)nums.innerHTML='<b>3,268,141</b><span data-en="building outlines" data-mi="tapuwae whare">building outlines</span><i>·</i><b data-en="COMPLETE" data-mi="KUA OTI">COMPLETE</b><span data-en="national baseline" data-mi="paparanga ā-motu">national baseline</span>';
  }

  const buildingCard=document.querySelector('.data-cards article:last-child p');
  if(buildingCard){
    buildingCard.dataset.en='3,268,141 national LINZ building outlines with capture and imagery provenance preserved where published.';
    buildingCard.dataset.mi='3,268,141 ngā tapuwae whare LINZ ā-motu, me te takenga hopunga me te whakaahua e tiakina ana ina whakaputaina.';
    buildingCard.textContent=buildingCard.dataset.en;
  }

  const builderBuilding=document.querySelector('.pricing-grid .plan.featured ul li:nth-child(4)');
  if(builderBuilding){builderBuilding.dataset.en='National building-outline layer';builderBuilding.dataset.mi='Paparanga tapuwae whare ā-motu';builderBuilding.textContent=builderBuilding.dataset.en;}
}

function localizeHomeText(lang){
  if(document.body.classList.contains('docs-body'))return;
  const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,{acceptNode(node){
    const parent=node.parentElement;if(!parent)return NodeFilter.FILTER_REJECT;
    if(parent.closest('script,style,pre,code,[data-en][data-mi]'))return NodeFilter.FILTER_REJECT;
    const text=node.nodeValue.trim();if(!text)return NodeFilter.FILTER_REJECT;
    if(!ORIGINAL_TEXT.has(node))ORIGINAL_TEXT.set(node,node.nodeValue);
    return HOME_TRANSLATIONS[ORIGINAL_TEXT.get(node).trim()]?NodeFilter.FILTER_ACCEPT:NodeFilter.FILTER_REJECT;
  }});
  const nodes=[];while(walker.nextNode())nodes.push(walker.currentNode);
  nodes.forEach(node=>{const original=ORIGINAL_TEXT.get(node);const english=original.trim();const replacement=lang==='mi'?(HOME_TRANSLATIONS[english]||english):english;node.nodeValue=(original.match(/^\s*/)?.[0]||'')+replacement+(original.match(/\s*$/)?.[0]||'');});
}

function setLanguage(lang,{updateUrl=true}={}){
  if(!META[lang])lang='en';
  document.documentElement.lang=lang==='mi'?'mi-NZ':'en-NZ';
  try{localStorage.setItem('propdata_nz_lang',lang)}catch{}
  document.querySelectorAll('[data-en][data-mi]').forEach(el=>{const value=el.dataset[lang];if(value!=null)el.textContent=value});
  localizeHomeText(lang);
  document.querySelectorAll('.lang-btn').forEach(btn=>{const active=btn.dataset.lang===lang;btn.classList.toggle('active',active);btn.setAttribute('aria-pressed',String(active))});
  const meta=META[lang];document.title=meta.title;
  setMeta('meta[name="description"]','content',meta.description);
  setMeta('meta[property="og:title"]','content',meta.ogTitle);
  setMeta('meta[property="og:description"]','content',meta.ogDescription);
  setMeta('meta[property="og:locale"]','content',meta.locale);
  setMeta('meta[name="twitter:title"]','content',meta.ogTitle);
  setMeta('meta[name="twitter:description"]','content',meta.ogDescription);
  updateCurrencyUI(currentCurrency,lang);
  if(updateUrl){const u=new URL(location.href);if(lang==='en')u.searchParams.delete('lang');else u.searchParams.set('lang',lang);history.replaceState({},'',u)}
}

function injectCurrencyStyles(){
  if(document.getElementById('fx-style'))return;
  const style=document.createElement('style');style.id='fx-style';
  style.textContent='.currency-console{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px;margin:20px auto 0;padding:10px 12px;width:fit-content;max-width:100%;border:1px solid rgba(19,126,90,.18);border-radius:14px;background:rgba(255,255,255,.82);box-shadow:0 8px 28px rgba(10,40,54,.05)}.currency-console-label{font-size:10px;font-weight:850;color:#5f7381;letter-spacing:.03em}.currency-toggle{display:flex;padding:3px;border:1px solid #d9e5e3;border-radius:10px;background:#eef5f3}.currency-btn{border:0;background:transparent;color:#657d7b;padding:7px 11px;border-radius:7px;cursor:pointer;font-size:10px;font-weight:900;letter-spacing:.05em}.currency-btn.active{background:#0c6f51;color:#fff;box-shadow:0 5px 14px rgba(12,111,81,.18)}.currency-billing-badge{font-size:9px;font-weight:850;color:#0d6f52;background:#e7f7f1;border:1px solid #c7e9dc;padding:6px 8px;border-radius:999px}.price .fx-sub{display:block;margin-top:3px;font-size:10px;line-height:1.35;font-weight:700;color:#75868c;letter-spacing:0}.price .fx-billed{color:#0c7757}.fx-disclosure{max-width:880px;margin:18px auto 0;padding:12px 14px;border:1px solid #dce6e3;border-radius:12px;background:#f8fbfa;color:#667b79;text-align:center;font-size:10px;line-height:1.6}.fx-disclosure strong{color:#163b34}@media(max-width:620px){.currency-console{width:100%;justify-content:space-between}.currency-console-label,.currency-billing-badge{width:100%;text-align:center}}';
  document.head.appendChild(style);
}

const PRICE_PLANS=[{nzd:99,usd:58},{nzd:299,usd:175},{nzd:799,usd:467}];
let currentCurrency='NZD';

function initCurrencyUI(){
  const pricing=document.querySelector('.pricing-section');if(!pricing)return;
  injectCurrencyStyles();const head=pricing.querySelector('.section-head');
  if(head&&!head.querySelector('.currency-console')){const el=document.createElement('div');el.className='currency-console';el.innerHTML='<span class="currency-console-label"></span><div class="currency-toggle" role="group" aria-label="Currency display"><button class="currency-btn" data-currency="NZD">NZD</button><button class="currency-btn" data-currency="USD">USD</button></div><span class="currency-billing-badge"></span>';head.appendChild(el);el.querySelectorAll('.currency-btn').forEach(btn=>btn.addEventListener('click',()=>{currentCurrency=btn.dataset.currency;try{localStorage.setItem('propdata_nz_currency',currentCurrency)}catch{}updateCurrencyUI(currentCurrency,document.documentElement.lang.startsWith('mi')?'mi':'en')}));}
  if(!pricing.querySelector('.fx-disclosure')){const note=document.createElement('div');note.className='fx-disclosure';pricing.querySelector('.wrap')?.appendChild(note)}
  let stored='';try{stored=localStorage.getItem('propdata_nz_currency')||''}catch{}currentCurrency=(stored==='NZD'||stored==='USD')?stored:((navigator.language||'').toLowerCase().includes('en-us')?'USD':'NZD');
}

function updateCurrencyUI(currency,lang){
  const pricing=document.querySelector('.pricing-section');if(!pricing)return;
  pricing.querySelectorAll('.currency-btn').forEach(btn=>btn.classList.toggle('active',btn.dataset.currency===currency));
  const label=pricing.querySelector('.currency-console-label');const badge=pricing.querySelector('.currency-billing-badge');
  if(label)label.textContent=lang==='mi'?'Whakaaturia ngā utu ki:':'Show prices in:';
  if(badge)badge.textContent=lang==='mi'?'Ka nama tonu a Stripe ki te NZD':'Stripe always bills in NZD';
  [...pricing.querySelectorAll('.pricing-grid .plan')].slice(0,3).forEach((plan,i)=>{const price=plan.querySelector('.price');if(!price)return;const p=PRICE_PLANS[i];price.innerHTML=currency==='USD'?`≈US$${p.usd}<small>/mo</small><span class="fx-sub fx-billed">${lang==='mi'?`Ka namahia hei NZ$${p.nzd} / marama`:`Charged as NZ$${p.nzd} / month`}</span>`:`NZ$${p.nzd}<small>/mo</small><span class="fx-sub">${lang==='mi'?`≈US$${p.usd} i te reiti tohutoro o nāianei`:`≈US$${p.usd} at the current reference rate`}</span>`;});
  const d=pricing.querySelector('.fx-disclosure');if(d)d.innerHTML=lang==='mi'?`<strong>Moni nama: NZD.</strong> Reiti tohutoro ${FX.asOf}: NZ$1 ≈ US$${FX.NZD_TO_USD.toFixed(4)} · US$1 ≈ NZ$${FX.USD_TO_NZD.toFixed(4)}. He tatauranga anake ngā utu USD. Ka whakatau tō pēke, tō whatunga kāri rānei i te utu whakawhiti whakamutunga, ā, tērā pea ka tāpiri utu whakawhiti.`:`<strong>Billing currency: NZD.</strong> Reference rate ${FX.asOf}: NZ$1 ≈ US$${FX.NZD_TO_USD.toFixed(4)} · US$1 ≈ NZ$${FX.USD_TO_NZD.toFixed(4)}. USD prices are estimates only. Your bank or card network determines the final converted USD amount and may add foreign-exchange fees.`;
  document.querySelectorAll('.site-footer a[href*="buy.stripe.com"]').forEach((link,i)=>{const p=PRICE_PLANS[i];if(!p)return;const name=link.textContent.split('·')[0].trim();link.textContent=currency==='USD'?`${name} · ≈US$${p.usd} (billed NZ$${p.nzd})`:`${name} · NZ$${p.nzd} (≈US$${p.usd})`;});
}

promoteBuildingBaseline();
initCurrencyUI();
document.querySelectorAll('.lang-btn').forEach(btn=>btn.addEventListener('click',()=>setLanguage(btn.dataset.lang)));
const params=new URLSearchParams(location.search);let storedLang='';try{storedLang=localStorage.getItem('propdata_nz_lang')||''}catch{}const requested=params.get('lang');const preferred=requested&&META[requested]?requested:(storedLang&&META[storedLang]?storedLang:((navigator.language||'').toLowerCase().startsWith('mi')?'mi':'en'));
setLanguage(preferred,{updateUrl:false});

const header=document.getElementById('site-header')||document.querySelector('.site-header');const nav=document.getElementById('primary-nav')||document.querySelector('.nav-links');const toggle=document.getElementById('menu-toggle')||document.querySelector('.menu-toggle');const onScroll=()=>header?.classList.toggle('scrolled',scrollY>12);addEventListener('scroll',onScroll,{passive:true});onScroll();
toggle?.addEventListener('click',()=>{const open=nav?.classList.toggle('open');toggle.setAttribute('aria-expanded',String(Boolean(open)))});nav?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');toggle?.setAttribute('aria-expanded','false');nav.querySelectorAll('details[open]').forEach(d=>d.removeAttribute('open'))}));
document.addEventListener('click',event=>{document.querySelectorAll('.nav-menu[open]').forEach(details=>{if(!details.contains(event.target))details.removeAttribute('open')});if(nav?.classList.contains('open')&&!nav.contains(event.target)&&!toggle?.contains(event.target)){nav.classList.remove('open');toggle?.setAttribute('aria-expanded','false')}});
document.querySelectorAll('[data-copy]').forEach(btn=>btn.addEventListener('click',async()=>{const id=btn.getAttribute('data-copy');const el=document.getElementById(id);if(!el)return;try{await navigator.clipboard.writeText(el.innerText);const old=btn.textContent;btn.textContent=document.documentElement.lang.startsWith('mi')?'Kua tāruatia':'Copied';setTimeout(()=>btn.textContent=old,1200)}catch{}}));
if(params.get('success')==='1')document.getElementById('success')?.classList.add('show');
const reduceMotion=matchMedia('(prefers-reduced-motion: reduce)').matches;if(!reduceMotion&&'IntersectionObserver'in window){const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');observer.unobserve(entry.target)}}),{threshold:.08,rootMargin:'0px 0px -18px'});document.querySelectorAll('[data-reveal]').forEach(el=>observer.observe(el));}else document.querySelectorAll('[data-reveal]').forEach(el=>el.classList.add('visible'));
addEventListener('pageshow',()=>{if(location.hash){const target=document.querySelector(location.hash);if(target)setTimeout(()=>target.scrollIntoView({block:'start'}),0)}});
