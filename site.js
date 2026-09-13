(()=>{
  const POSTURE='NZ_POSTURE_2026_09_13';
  const meta=(selector,value)=>{const el=document.querySelector(selector);if(el)el.setAttribute('content',value)};
  const node=(html)=>{const t=document.createElement('template');t.innerHTML=html.trim();return t.content.firstElementChild};

  function applyPosture(){
    const path=location.pathname.replace(/\/$/,'')||'/';

    if(path==='/'||path==='/index.html'){
      document.title='New Zealand Property Intelligence | National Property & Legal-Title Graph | PropData';
      meta('meta[name="description"]','PropData New Zealand connects national LINZ address, parcel, title, building and statutory intelligence with completed restricted title-estate, ownership and memorial/legal-interest infrastructure.');
      meta('meta[property="og:description"]','National New Zealand property intelligence plus completed entitlement-gated title-estate, ownership and memorial/legal-interest infrastructure in one governed PropData graph.');
      meta('meta[name="twitter:description"]','National NZ property intelligence with completed restricted title ownership and memorial/legal-interest infrastructure behind explicit entitlement controls.');

      const ld=document.querySelector('script[type="application/ld+json"]');
      if(ld){try{const j=JSON.parse(ld.textContent);const graph=j['@graph']||[];const product=graph.find(x=>x['@id']==='https://nz.proptechusa.ai/#product');const page=graph.find(x=>x['@id']==='https://nz.proptechusa.ai/#webpage');if(product)product.description='National New Zealand property intelligence spanning authoritative addresses, parcels, titles, buildings and statutory actions, with completed restricted national title-estate, ownership and memorial/legal-interest infrastructure maintained behind separate entitlements.';if(page)page.dateModified='2026-09-13';ld.textContent=JSON.stringify(j)}catch(_){}}

      if(!document.getElementById('restricted-title-graph')){
        const demo=document.getElementById('demo');
        if(demo){
          const section=node(`<section class="section data-section" id="restricted-title-graph" data-posture="${POSTURE}">
            <div class="wrap">
              <div class="section-head centered" data-reveal>
                <div class="kicker">RESTRICTED TITLE GRAPH · NATIONAL BASELINES COMPLETE</div>
                <h2 data-en="The deeper legal-title graph is built." data-mi="Kua hangaia te whatunga taitara ture hōhonu.">The deeper legal-title graph is built.</h2>
                <p data-en="Behind the customer-safe property surface, PropData now maintains national LINZ title-estate, ownership and memorial/legal-interest layers as restricted infrastructure. These datasets are not exposed by default self-serve plans and remain separately entitlement-controlled where LINZ personal-data rights apply." data-mi="I muri i te mata rawa haumaru-kiritaki, ka pupuri a PropData i ngā paparanga ā-motu o LINZ mō ngā estate taitara, te rangatiratanga me ngā memorial/hononga ture hei hanganga here. Kāore ēnei huinga raraunga e tukuna taunoa ki ngā mahere ratonga-whaiaro, ā, ka noho ki raro i ngā mana motuhake ina hāngai ngā motika raraunga whaiaro a LINZ.">Behind the customer-safe property surface, PropData now maintains national LINZ title-estate, ownership and memorial/legal-interest layers as restricted infrastructure. These datasets are not exposed by default self-serve plans and remain separately entitlement-controlled where LINZ personal-data rights apply.</p>
              </div>
              <div class="data-cards" data-reveal>
                <article><span>TE</span><h3>2.81M title estates</h3><p>National restricted title → estate baseline complete.</p></article>
                <article><span>OW</span><h3>5.73M ownership records</h3><p>National restricted estate → ownership baseline complete. Counts describe source records, not unique people or organisations.</p></article>
                <article><span>MI</span><h3>32.86M+ title memorials</h3><p>National memorial/legal-interest baseline complete with source identifiers preserved and no fabricated links.</p></article>
                <article><span>AT</span><h3>1,784,819 structured memorial details</h3><p>National structured-detail baseline complete; the incremental changeset path is live and production-verified.</p></article>
              </div>
            </div>
          </section>`);
          demo.before(section);
        }
      }

      const disclaimer=document.querySelector('.sources-section .disclaimer strong');
      if(disclaimer)disclaimer.textContent='PropData is an independent product of PropTechUSA.ai and is not operated by or affiliated with LINZ or the New Zealand government. Restricted title ownership and memorial/legal-interest datasets are loaded as internal PropData infrastructure but remain separately entitlement-gated and are not represented as default self-serve access where LINZ personal-data rights apply.';
      const pricing=document.querySelector('.pricing-note');
      if(pricing)pricing.textContent='Stripe checkout collects billing details and supported tax IDs. API access is provisioned after successful payment; direct API keys remain server-side credentials. Restricted title ownership and memorial/legal-interest layers are loaded nationally but remain separately entitlement-controlled and outside default self-serve access.';
    }

    if(path==='/docs'||path==='/docs/index.html'){
      document.title='PropData New Zealand API Docs | Property, Titles, Ownership, Legal Interests & Buildings';
      meta('meta[name="description"]','Production documentation for PropData New Zealand: national address, parcel, title, building and statutory layers plus completed restricted title-estate, ownership and memorial/legal-interest baselines.');
      const grid=document.querySelector('.proof-grid');
      if(grid&&!grid.querySelector(`[data-posture="${POSTURE}"]`)){
        [['2.81M','Restricted title estates'],['5.73M','Restricted ownership records'],['32.86M+','Restricted title memorials'],['1,784,819','Structured memorial details']].forEach(([v,l],i)=>{const d=node(`<div class="proof"${i===0?` data-posture="${POSTURE}"`:''}><b>${v}</b><span>${l}</span></div>`);grid.appendChild(d)});
      }
      document.querySelectorAll('.notice.warn').forEach(el=>{
        if(el.textContent.includes('Named ownership is a separate entitlement problem.'))el.innerHTML='<strong>Named ownership remains a separate entitlement problem.</strong> PropData now maintains the national title-estate and ownership baselines internally, but title metadata and <code>number_owners</code> still do not authorize inference of named owner identity. LINZ Personal Data Licence-gated ownership and memorial datasets remain separately controlled and are not default self-serve output.';
        if(el.textContent.includes('Title Memorial List / personal data:'))el.innerHTML='<strong>Restricted title graph / personal data:</strong> PropData has completed the national title-estate, ownership, memorial and structured memorial-detail baselines. Those restricted LINZ datasets remain separately entitlement-gated and are not represented as generally available unless the applicable LINZ licence and downstream controls are in place.';
      });
    }

    if(path==='/workspace'||path==='/workspace.html'){
      const intro=document.querySelector('[data-view-panel="overview"] .page-head p');
      if(intro)intro.textContent='Resolve property identity, inspect the production graph, test country-aware requests and see the full national posture—including restricted title ownership and memorial infrastructure without confusing entitlement-gated layers with default public API access.';
      const hero=document.querySelector('[data-view-panel="overview"] .hero-copy p');
      if(hero)hero.textContent='Addresses resolve into parcels. Parcels connect to titles, cadastral geometry, buildings and legal/statutory context. Behind that customer-safe surface, the national title-estate, ownership and memorial layers are also loaded as restricted infrastructure. Every layer keeps its own source, coverage and entitlement state underneath one country-aware PropData contract.';
      const stats=document.querySelector('[data-view-panel="overview"] .stats');
      if(stats&&!stats.querySelector(`[data-posture="${POSTURE}"]`)){
        [['Title estates','2.81M','Restricted national baseline complete'],['Ownership records','5.73M','Restricted national baseline complete'],['Title memorials','32.86M+','Restricted legal-interest baseline complete'],['Memorial details','1,784,819','Restricted · incremental path live']].forEach(([l,v,s],i)=>stats.appendChild(node(`<div class="stat navy"${i===0?` data-posture="${POSTURE}"`:''}><span>${l}</span><b>${v}</b><small>${s}</small></div>`)));
      }
      document.querySelectorAll('.notice.warn').forEach(el=>{if(el.textContent.includes('Title Memorial List / 51695:'))el.innerHTML='<strong>Restricted title graph:</strong> national baselines are now complete for title estates (2.81M), ownership records (5.73M), title memorials (32.86M+ baseline records) and structured memorial details (1,784,819). These layers are loaded as PropData infrastructure but remain separately entitlement-gated; they are not represented as default self-serve access.'});
      const coverage=document.querySelector('[data-view-panel="coverage"] .coverage-grid');
      if(coverage&&!coverage.querySelector(`[data-posture="${POSTURE}"]`))coverage.appendChild(node(`<article class="coverage-card" data-posture="${POSTURE}"><span>RESTRICTED TITLE GRAPH</span><b>2.81M estates · 5.73M ownership · 32.86M+ memorials</b><p>National restricted legal-title layers are loaded and governed separately from the customer-safe self-serve contract.</p></article>`));
    }
  }

  applyPosture();
  const load=(src,done)=>{const s=document.createElement('script');s.src=src;s.async=false;if(done)s.onload=done;document.head.appendChild(s)};
  load('/site.core.js',()=>load('/product-demo.js',()=>{
    if(location.pathname.startsWith('/docs'))load('/docs-depth.js');
  }));
})();
