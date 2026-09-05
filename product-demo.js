(()=>{
  const style=document.createElement('link');
  style.rel='stylesheet';
  style.href='/product-demo.css';
  document.head.appendChild(style);

  const section=document.querySelector('#demo');
  if(!section)return;
  section.className='pdx-demo-section';
  section.innerHTML=`
    <div class="wrap pdx-demo-wrap">
      <div class="pdx-head">
        <div>
          <span class="pdx-kicker" data-demo-en="LIVE PRODUCTION PROPERTY · NEW ZEALAND" data-demo-mi="RAWA WHAKAPUTA ORA · AOTEAROA">LIVE PRODUCTION PROPERTY · NEW ZEALAND</span>
          <h2 data-demo-en="See the national property graph as a product, not a payload." data-demo-mi="Tirohia te whatunga rawa ā-motu hei hua, kaua hei kawenga raraunga.">See the national property graph as a product, not a payload.</h2>
          <p data-demo-en="Parcel 3818618 is a current production PropData result. Switch between property, title, building and statutory views to see how one exact LINZ parcel becomes decision-ready intelligence without losing source or coverage semantics." data-demo-mi="He hua whakaputa o nāianei a PropData te pānga whenua 3818618. Hurihia i waenga i ngā tirohanga rawa, taitara, whare me ngā mahi ā-ture kia kite ai me pēhea te huri o tētahi pānga whenua LINZ tika hei mōhiotanga kua rite mō te whakatau, me te pupuri tonu i te puna me ngā tikanga kapi.">Parcel 3818618 is a current production PropData result. Switch between property, title, building and statutory views to see how one exact LINZ parcel becomes decision-ready intelligence without losing source or coverage semantics.</p>
        </div>
        <div class="pdx-head-actions"><a class="pdx-btn primary" href="/workspace" data-demo-en="Run it in the NZ Workspace →" data-demo-mi="Whakamātauria i te Papamahi NZ →">Run it in the NZ Workspace →</a><a class="pdx-btn" href="/docs" data-demo-en="Read the contract" data-demo-mi="Pānuihia te kirimana">Read the contract</a></div>
      </div>

      <div class="pdx-browser" aria-label="PropData New Zealand interactive property response explorer">
        <div class="pdx-top">
          <div class="pdx-brand"><span class="pdx-live-dot"></span><b>PROPDATA NZ</b><small>PRODUCTION RESPONSE EXPLORER</small></div>
          <div class="pdx-controls"><span class="pdx-badge">LIVE VERIFIED PROPERTY</span><button class="pdx-toggle active" data-pdx-view="parsed">PARSED</button><button class="pdx-toggle" data-pdx-view="json">JSON</button></div>
        </div>
        <div class="pdx-tabs" role="tablist" aria-label="New Zealand property intelligence layers">
          <button class="active" data-pdx-route="property"><span>PROPERTY</span><small>identity + parcel</small></button>
          <button data-pdx-route="titles"><span>TITLES</span><small>legal identity graph</small></button>
          <button data-pdx-route="buildings"><span>BUILDINGS</span><small>spatial relationships</small></button>
          <button data-pdx-route="statutory"><span>STATUTORY</span><small>LINZ 51565</small></button>
        </div>
        <div class="pdx-request"><span class="pdx-method">GET</span><div class="pdx-url">/v1/property?country=NZ&amp;parcel=<strong>3818618</strong>&amp;enrich=full</div><span class="pdx-status"><i></i>200 · LIVE_ENRICHED</span></div>

        <div class="pdx-pane active" data-pdx-pane="parsed">
          <div class="pdx-grid">
            <aside class="pdx-property">
              <div class="pdx-photo"><div class="pdx-shape"></div><div class="pdx-pin"></div><span class="pdx-photo-label">LOWER HUTT · WELLINGTON · VERIFIED</span></div>
              <div class="pdx-property-body">
                <div class="pdx-title-row"><div><span>PRIMARY PARCEL</span><h3>3818618</h3></div><b>EXACT</b></div>
                <p>Lot 1 DP 90132 · authoritative LINZ cadastral identity with geometry, title graph, building relationships and independent legal/statutory coverage.</p>
                <div class="pdx-facts"><div><span>Area</span><b>35,805 m²</b></div><div><span>Land district</span><b>Wellington</b></div><div><span>Title records</span><b>129</b></div><div><span>Building links</span><b>25</b></div></div>
              </div>
            </aside>
            <section class="pdx-panel">
              <div class="pdx-panel-head"><div><span id="pdx-route-label">FULL PROPERTY GRAPH</span><b id="pdx-route-title">One parcel. Multiple production layers.</b></div><span class="pdx-schema">LINZ SOURCE-AWARE · FAIL-CLOSED FACTS</span></div>
              <div class="pdx-cards" id="pdx-cards"></div>
              <div class="pdx-sourcebar"><div><span>IDENTITY</span><b>Toitū Te Whenua LINZ</b></div><div><span>RELATIONSHIPS</span><b>PropData spatial derivation</b></div><div><span>STATUTORY</span><b>LINZ / Landonline · dataset 51565</b></div><div><span>RULE</span><b>Complete zero ≠ unavailable</b></div></div>
            </section>
          </div>
        </div>

        <div class="pdx-pane" data-pdx-pane="json">
          <div class="pdx-json"><div class="pdx-json-copy"><span>PRODUCTION CONTRACT</span><h3>Readable for people.<br>Structured for products.</h3><p>The parsed view shows what a product team can use. The JSON view shows the same country-aware contract engineering receives.</p><a href="/workspace">Run parcel 3818618 →</a></div><pre id="pdx-json"></pre></div>
        </div>

        <div class="pdx-proof"><div><b>3,040,571</b><span>primary parcels</span></div><div><b>2,424,415</b><span>authoritative addresses</span></div><div><b>2,450,998</b><span>property titles</span></div><div><b>3,820,845</b><span>building ↔ parcel links</span></div><div><b>342,695</b><span>statutory actions nationally</span></div></div>
      </div>
      <div class="pdx-bottom"><div><small>WHAT THIS PROVES</small><b data-demo-en="The value is not a lookup endpoint. It is the relationship graph: parcel identity, legal identity, physical buildings, statutory context, coverage and provenance delivered together." data-demo-mi="Ehara te uara i te pito-mutunga rapu anake. Ko te whatunga hononga te uara: tuakiri pānga whenua, tuakiri ture, whare tūturu, horopaki ā-ture, kapi me te takenga kua tukuna ngātahi.">The value is not a lookup endpoint. It is the relationship graph: parcel identity, legal identity, physical buildings, statutory context, coverage and provenance delivered together.</b></div><div class="pdx-pills"><span>Parcel geometry</span><span>129 titles</span><span>25 building links</span><span>EPSG:2193</span><span>Statutory coverage</span><span>Provenance</span></div></div>
    </div>`;

  const data={
    property:{label:'FULL PROPERTY GRAPH',title:'One parcel. Multiple production layers.',cards:[
      ['01','PARCEL IDENTITY','3818618','Exact LINZ primary parcel',''],['02','APPELLATION','Lot 1 DP 90132','Source-native legal description',''],['03','PARCEL AREA','35,805 m²','Authoritative cadastral area',''],['04','GEOMETRY','Polygon available','Cadastral geometry returned','blue'],['05','TITLE GRAPH','129 records','All attached title identities',''],['06','COVERAGE','live_enriched','Base identity + country enrichment','blue']],json:{country_code:'NZ',match_level:'parcel_id',coverage_status:'live_enriched',parcel:{parcel_id:'3818618',global_parcel_id:'NZ:LINZ_PARCEL:3818618',appellation:'Lot 1 DP 90132',land_district:'Wellington',calc_area:35805,title_count:129,geometry:{type:'Polygon'}},source:'Toitu Te Whenua LINZ'}},
    titles:{label:'LEGAL PROPERTY IDENTITY',title:'The title graph stays relational.',cards:[
      ['01','TITLE RECORDS','129','Current title records attached',''],['02','LIVE TITLES','129','Live title count in derived graph',''],['03','UNIT TITLES','121','Unit-title records in this parcel graph','blue'],['04','SAMPLE TITLE','1006231','Unit Title · Guarantee',''],['05','ISSUE DATE','1 Nov 2021','Verified title record date',''],['06','SPATIAL EXTENTS','Shared','Title record preserves spatial-extents flag','blue']],json:{parcel_id:'3818618',title_record_count:129,derived:{live_title_count:129,unit_title_count:121,has_multiple_titles:true},sample_title:{title_no:'1006231',status:'LIVE',title_type:'Unit Title',issue_date:'2021-11-01T16:20:02Z',guarantee_status:'Guarantee',estate_description:'Stratum in Freehold, 1/1, Unit 44 Deposited Plan 90777',spatial_extents_shared:true}}},
    buildings:{label:'PHYSICAL PROPERTY GRAPH',title:'Buildings are linked by geometry, not proximity guesses.',cards:[
      ['01','BUILDING LINKS','25','Complete building↔parcel relationships',''],['02','PRIMARY BUILDINGS','24','Primary relationships in derived graph',''],['03','OVERLAP SUM','11,549.83 m²','Building overlap area across parcel','blue'],['04','OVERLAP RATIO','32.2576%','Derived parcel-area ratio','blue'],['05','METHOD','polygon overlap','spatial_polygon_overlap_v1',''],['06','METRIC CRS','EPSG:2193','New Zealand metric spatial linkage','']],json:{parcel_id:'3818618',building_relationships:{coverage_status:'complete',count:25,returned:25,truncated:false},derived:{building_count:25,primary_building_count:24,building_overlap_area_sum_sqm:11549.83,building_overlap_area_ratio:0.322576},linkage:{status:'completed',metric_crs:'EPSG:2193',relationship_method:'spatial_polygon_overlap_v1'}}},
    statutory:{label:'LEGAL / STATUTORY COVERAGE',title:'A real zero is still valuable when coverage is complete.',cards:[
      ['01','ACTIONS','0','No actions attached to this parcel','gold'],['02','COVERAGE','complete','This is not an unavailable layer',''],['03','CURRENT','0','Current statutory actions','gold'],['04','HISTORIC','0','Historic statutory actions','gold'],['05','DATASET','51565','LINZ parcel statutory actions','blue'],['06','SOURCE','LINZ / Landonline','Source and refresh state preserved','']],json:{parcel_id:'3818618',legal_actions:{coverage_status:'complete',count:0,current_count:0,historic_count:0,returned:0,truncated:false,source_dataset_id:'51565',source:'Toitu Te Whenua LINZ / Landonline'}}}
  };

  const cards=section.querySelector('#pdx-cards'), label=section.querySelector('#pdx-route-label'), title=section.querySelector('#pdx-route-title'), json=section.querySelector('#pdx-json');
  const render=(key)=>{const r=data[key];label.textContent=r.label;title.textContent=r.title;cards.innerHTML=r.cards.map((c,i)=>`<article><div class="pdx-card-top"><span>${c[0]}</span><b class="pdx-state ${c[4]}">${i===0?'VERIFIED':'COVERED'}</b></div><small>${c[1]}</small><strong>${c[2]}</strong><p>${c[3]}</p></article>`).join('');json.textContent=JSON.stringify(r.json,null,2)};
  render('property');
  section.querySelectorAll('[data-pdx-route]').forEach(btn=>btn.addEventListener('click',()=>{section.querySelectorAll('[data-pdx-route]').forEach(x=>x.classList.remove('active'));btn.classList.add('active');render(btn.dataset.pdxRoute)}));
  section.querySelectorAll('[data-pdx-view]').forEach(btn=>btn.addEventListener('click',()=>{section.querySelectorAll('[data-pdx-view]').forEach(x=>x.classList.remove('active'));btn.classList.add('active');section.querySelectorAll('[data-pdx-pane]').forEach(p=>p.classList.toggle('active',p.dataset.pdxPane===btn.dataset.pdxView))}));

  const sync=()=>{let lang='en';try{lang=localStorage.getItem('propdata_nz_lang')==='mi'?'mi':(document.documentElement.lang.toLowerCase().startsWith('mi')?'mi':'en')}catch{}section.querySelectorAll('[data-demo-en]').forEach(el=>{const v=el.getAttribute('data-demo-'+lang);if(v)el.textContent=v})};
  sync();document.querySelectorAll('.lang-btn').forEach(btn=>btn.addEventListener('click',()=>setTimeout(sync,0)));
})();
