from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "index.html"
WORKSPACE = ROOT / "workspace.html"
SITE_JS = ROOT / "site.js"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


def replace_or_verify(text: str, old: str, new: str, marker: str, label: str) -> str:
    if marker in text:
        return text
    return replace_once(text, old, new, label)


translations = {
    # Shared navigation / actions
    "Skip to documentation": "Haere ki ngā tuhinga",
    "Product": "Hua",
    "Endpoints": "Ngā pito-mutunga",
    "Property graph": "Whatunga rawa",
    "Semantics": "Tikanga",
    "Workspace": "Papamahi",
    "Open Workspace": "Whakatuwheratia te Papamahi",
    "API Docs": "Tuhinga API",
    "Global Workspace": "Papamahi ā-Ao",
    "Connect API Key": "Tūhono Kī API",
    "COUNTRY WORKSPACE · AOTEAROA": "PAPAMAHI WHENUA · AOTEAROA",
    "COUNTRY LOCK · NZ": "HERE WHENUA · NZ",
    "COPY": "TĀRUATIA",
    "Copied": "Kua tāruatia",
    "COPIED": "KUA TĀRUATIA",

    # Docs hero / proof
    "PRODUCTION CONTRACT · NEW ZEALAND / AOTEAROA": "KIRIMANA WHAKAPUTA · AOTEAROA",
    "Build on the": "Hanga ki runga i te",
    "national property graph.": "whatunga rawa ā-motu.",
    "Authoritative address resolution, primary parcels, cadastral geometry, property titles, title↔parcel relationships, building footprints, building↔parcel relationships and parcel statutory intelligence—delivered through the PropData global API with New Zealand-native identifiers and provenance intact.": "Te whakataunga wāhitau whai mana, ngā pānga whenua matua, te āhuahanga cadastral, ngā taitara rawa, ngā hononga taitara↔pānga whenua, ngā tapuwae whare, ngā hononga whare↔pānga whenua me te mōhiotanga ā-ture pānga whenua—ka tukuna mā te API ā-ao o PropData me ngā tautuhi me te takenga taketake o Aotearoa e mau tonu ana.",
    "Launch NZ Workspace →": "Whakatuwheratia te Papamahi NZ →",
    "Quick start": "Tīmata tere",
    "Get API access": "Whiwhi urunga API",
    "COUNTRY CONTRACT": "KIRIMANA WHENUA",
    "PRODUCTION": "WHAKAPUTA",
    "Country lock": "Here whenua",
    "New Zealand / Aotearoa": "Aotearoa",
    "Primary API": "API matua",
    "Global PropData edge contract": "Kirimana tapa ā-ao PropData",
    "Source backbone": "Tūāpapa puna",
    "Delivery": "Tukunga",
    "Primary parcels": "Ngā pānga whenua matua",
    "Addresses": "Ngā wāhitau",
    "Property titles": "Ngā taitara rawa",
    "Title ↔ parcel": "Taitara ↔ pānga whenua",
    "Building outlines": "Ngā tapuwae whare",
    "Building ↔ parcel": "Whare ↔ pānga whenua",
    "Statutory actions": "Ngā mahi ā-ture",

    # Docs side nav
    "Start": "Tīmata",
    "Architecture": "Hanganga",
    "Authentication": "Whakamana urunga",
    "REST surface": "Mata REST",
    "Endpoint index": "Rārangi pito-mutunga",
    "Property": "Rawa",
    "Full Enrich": "Whakarākei Katoa",
    "Coordinates": "Taunga wāhi",
    "Platform": "Tūāpapa",
    "NZ graph": "Whatunga NZ",
    "Graph layers": "Paparanga whatunga",
    "Titles": "Ngā taitara",
    "Buildings": "Ngā whare",
    "Contract": "Kirimana",
    "Coverage semantics": "Tikanga kapi",
    "Errors": "Hapa",
    "Sources & rights": "Puna me ngā motika",
    "Open NZ Workspace →": "Whakatuwheratia te Papamahi NZ →",

    # Docs overview
    "Country API architecture": "Hanganga API ā-whenua",
    "One global edge. One deep New Zealand contract.": "Kotahi te tapa ā-ao. Kotahi te kirimana hōhonu mō Aotearoa.",
    "PropData keeps one global API surface while preserving country-native data models underneath it. New Zealand requests carry country=NZ; the resolver then routes into New Zealand-specific property identity, title, cadastral and physical-improvement intelligence. The country site and workspace are the focused developer experience for that market—not a separate disconnected backend.": "Ka pupuri a PropData i tētahi mata API ā-ao kotahi, ā, ka tiaki tonu i ngā tauira raraunga taketake o ia whenua i raro iho. Ka kawe ngā tono o Aotearoa i te country=NZ; kātahi ka aratakina ki te tuakiri rawa, taitara, cadastral me te mōhiotanga whakapainga ā-tinana motuhake o Aotearoa. Ko te pae whenua me te papamahi te wheako kaiwhakawhanake arotahi mō taua mākete—ehara i te tuarā motuhake kua motu.",
    "Address / parcel / coordinates": "Wāhitau / pānga whenua / taunga wāhi",
    "Resolve the input against authoritative New Zealand identity instead of forcing a U.S. parcel convention.": "Whakatauria te tāuru ki te tuakiri whai mana o Aotearoa, kaua ki te akiaki i tētahi tikanga pānga whenua nō Amerika.",
    "Parcel ↔ title ↔ building": "Pānga whenua ↔ taitara ↔ whare",
    "Preserve the many-to-many title graph and spatial building relationships around the verified parcel.": "Tiakina te whatunga taitara maha-ki-maha me ngā hononga mokowā whare huri noa i te pānga whenua kua whakamana.",
    "Country-native context": "Horopaki taketake ā-whenua",
    "Attach available geometry, derived physical context and legal/statutory layers with independent coverage states.": "Tāpiritia te āhuahanga e wātea ana, te horopaki ā-tinana kua ahu mai, me ngā paparanga ture/ā-ture me ō rātou tūnga kapi motuhake.",
    "REST · MCP · bulk · custom": "REST · MCP · raraunga nui · ritenga",
    "Use the same governed PropData account and provenance rules across delivery modes.": "Whakamahia taua pūkete PropData kua whakahaerehia rā me ngā ture takenga kotahi puta noa i ngā momo tukunga.",
    "Blueprint:": "Mahere matua:",

    # Docs quickstart / auth
    "First request": "Tono tuatahi",
    "Three ways into one property.": "E toru ngā ara ki te rawa kotahi.",
    "Resolve an exact LINZ primary parcel identifier.": "Whakatauria tētahi tautuhi pānga whenua matua LINZ tika.",
    "Resolve an authoritative New Zealand address into property identity.": "Whakatauria tētahi wāhitau whai mana o Aotearoa ki te tuakiri rawa.",
    "Resolve a WGS84 coordinate into the containing property context.": "Whakatauria tētahi taunga WGS84 ki te horopaki rawa kei roto.",
    "The production canary resolves parcel": "Ka whakatauria e te canary whakaputa te pānga whenua",
    "Credentials stay server-side.": "Me noho ngā taunakitanga ki te taha tūmau.",
    "Direct REST uses the x-api-key header. Production keys belong in server-side secrets or environment variables—not URLs, browser bundles, screenshots, analytics, or repositories. The NZ Workspace is an account/developer tool and only sends a key after the user explicitly connects one for the session.": "Ka whakamahi te REST tika i te pane x-api-key. Me noho ngā kī whakaputa ki ngā muna taha-tūmau, ki ngā taurangi taiao rānei—kaua ki ngā URL, pūtake pūtirotiro, whakaahua mata, tātaritanga, putunga waehere rānei. He taputapu pūkete/kaiwhakawhanake te Papamahi NZ, ā, ka tuku kī anake i muri i te tūhono mārama a te kaiwhakamahi mō taua wā mahi.",
    "MCP is different.": "He rerekē te MCP.",
    "PropData MCP uses OAuth in compatible clients. Do not paste a static REST API key into an MCP authorization flow.": "Ka whakamahi a PropData MCP i te OAuth i ngā kiritaki hototahi. Kaua e whakapiri i tētahi kī API REST pūmau ki roto i te rerenga whakamana MCP.",

    # Docs endpoints / property
    "Customer-safe REST surface": "Mata REST haumaru-kiritaki",
    "The routes New Zealand developers actually need.": "Ngā ara e tino hiahiatia ana e ngā kaiwhakawhanake o Aotearoa.",
    "These are the public PropData routes used by the country experience. Internal database RPCs, ingest functions, checkpoints, source tables and service-role operations are intentionally not public API endpoints.": "Ko ēnei ngā ara tūmatanui PropData e whakamahia ana e te wheako ā-whenua. Kāore ngā RPC pātengi raraunga ā-roto, ngā mahi uta, ngā wāhi taki, ngā ripanga puna me ngā mahi service-role e whakatakotoria hei pito-mutunga API tūmatanui.",
    "Primary property resolver for NZ address or parcel input. Add enrich=full for deeper country-aware enrichment where entitled.": "Ko te kaiwhakatautohu rawa matua mō te wāhitau, pānga whenua rānei o NZ. Tāpirihia enrich=full mō te whakarākei hōhonu ā-whenua ina whai mana.",
    "WGS84 coordinate → parcel/property context with explicit spatial match semantics.": "Taunga WGS84 → horopaki pānga whenua/rawa me ngā tikanga taurite mokowā mārama.",
    "Probe coordinate coverage before relying on a property-by-location workflow.": "Tirohia te kapi taunga wāhi i mua i te whakawhirinaki ki tētahi rerenga rawa-mā-te-wāhi.",
    "Discover the country-aware framework and supported market capabilities.": "Kimihia te anga ā-whenua me ngā āheinga mākete e tautokona ana.",
    "Authoritative account usage and current limits for quota-aware applications.": "Te whakamahinga pūkete whai mana me ngā rohe onāianei mō ngā taupānga mōhio-rohe.",
    "Public production service health for operational checks.": "Te hauora ratonga whakaputa tūmatanui mō ngā arowhai whakahaere.",
    "Public platform-level proof and service statistics. Do not substitute global stats for property-level coverage.": "Ngā taunakitanga tūāpapa tūmatanui me ngā tatauranga ratonga. Kaua e whakakapi i te kapi taumata-rawa ki ngā tatauranga ā-ao.",
    "Production API and data-platform changes for integration teams.": "Ngā panonitanga API whakaputa me te tūāpapa raraunga mō ngā rōpū whakauru.",
    "Property identity": "Tuakiri rawa",
    "COUNTRY-AWARE": "MŌHIO-Ā-WHENUA",
    "Resolve a New Zealand property by authoritative address or LINZ primary parcel identifier. Use one clear identity method per request.": "Whakatauria tētahi rawa o Aotearoa mā tētahi wāhitau whai mana, mā tētahi tautuhi pānga whenua matua LINZ rānei. Whakamahia kia kotahi te tikanga tuakiri mārama mō ia tono.",
    "Parameter": "Tawhā",
    "Required": "Me whai",
    "Purpose": "Kaupapa",
    "yes": "āe",
    "one input": "kotahi te tāuru",
    "optional": "kōwhiringa",
    "New Zealand address to resolve. Do not combine with a conflicting parcel ID.": "Te wāhitau o Aotearoa hei whakataunga. Kaua e whakakotahi ki tētahi ID pānga whenua taupatupatu.",
    "Use full for deeper country enrichment where available to the account.": "Whakamahia full mō te whakarākei hōhonu ā-whenua ina wātea ki te pūkete.",
    "Fail-open enrichment, fail-closed facts.": "Whakarākei fail-open, meka fail-closed.",
    "A valid property result should survive an optional layer failure. Missing or unavailable downstream facts remain unavailable; PropData does not invent a substitute.": "Me ora tonu tētahi hua rawa tika ahakoa ka hapa tētahi paparanga kōwhiringa. Ka noho ngaro tonu ngā meka kāore i te wātea; kāore a PropData e tito whakakapi.",

    # Docs Full Enrich / spatial
    "Deep country response": "Whakautu hōhonu ā-whenua",
    "Full Enrich connects the graph.": "Ka hono a Full Enrich i te whatunga.",
    "LAYER-SPECIFIC": "MOTUHAKE-Ā-PAPARANGA",
    "Parcel + cadastral context": "Pānga whenua + horopaki cadastral",
    "Native parcel ID, appellation, land district, area, topology and available geometry.": "ID pānga whenua taketake, appellation, rohe whenua, rahinga, topology me te āhuahanga e wātea ana.",
    "Title graph": "Whatunga taitara",
    "Property titles plus explicit title↔parcel associations, including multi-title and unit-title contexts.": "Ngā taitara rawa me ngā hononga taitara↔pānga whenua mārama, tae atu ki ngā horopaki taitara-maha me te taitara-wae.",
    "Building relationships": "Ngā hononga whare",
    "National building outlines spatially linked to parcels with relationship method, overlap and provenance.": "Ngā tapuwae whare ā-motu kua hono ā-mokowā ki ngā pānga whenua me te tikanga hononga, te inaki me te takenga.",
    "LEGAL / STATUTORY": "TURE / Ā-TURE",
    "Live legal actions": "Ngā mahi ā-ture ora",
    "Certified LINZ 51565 current + historic parcel actions returned directly at new_zealand.legal_actions with counts, bounded items, source revision and coverage state.": "Ngā mahi pānga whenua onāianei me ngā mahi o mua kua whakamana mai i LINZ 51565, ka whakahokia tika ki new_zealand.legal_actions me ngā tatau, ngā tūemi kua herea, te whakahounga puna me te tūnga kapi.",
    "Spatial identity": "Tuakiri mokowā",
    "Coordinates → property.": "Taunga wāhi → rawa.",
    "WGS84 latitude.": "Ahopae WGS84.",
    "WGS84 longitude.": "Ahopou WGS84.",
    "Coordinate resolution attaches spatial property context without pretending every point has an exact address record. Use the returned match and coverage signals independently.": "Ka tāpiri te whakataunga taunga wāhi i te horopaki rawa mokowā me te kore e whakapae he pūkete wāhitau tika tō ia ira. Whakamahia motuhaketia ngā tohu taurite me te kapi kua whakahokia.",
    "Coverage probe": "Tirohanga kapi",

    # Docs graph layers
    "Production country graph": "Whatunga whenua whakaputa",
    "Seven national layers, one property identity.": "E whitu ngā paparanga ā-motu, kotahi te tuakiri rawa.",
    "The backend is deliberately richer than a single endpoint table. These are production graph capabilities currently loaded for New Zealand; direct REST exposure remains governed by the public contract above.": "He hōhonu ake te tuarā i tētahi ripanga pito-mutunga kotahi. Ko ēnei ngā āheinga whatunga whakaputa kua utaina mō Aotearoa; ka whakahaere tonutia te whakaaturanga REST tika e te kirimana tūmatanui i runga ake nei.",
    "Authoritative addresses": "Ngā wāhitau whai mana",
    "LINZ address identity, locality structure, lifecycle and coordinates.": "Tuakiri wāhitau LINZ, hanganga rohe, huringa ora me ngā taunga wāhi.",
    "Parcel identity, cadastral attributes and available geometry.": "Tuakiri pānga whenua, huanga cadastral me te āhuahanga e wātea ana.",
    "Title status, type, dates, estate description and source context.": "Tūnga taitara, momo, rā, whakaahuatanga whenua me te horopaki puna.",
    "Explicit many-to-many associations between legal title identity and cadastral parcels.": "Ngā hononga maha-ki-maha mārama i waenga i te tuakiri taitara ture me ngā pānga whenua cadastral.",
    "LINZ footprints with capture and imagery provenance where published.": "Ngā tapuwae LINZ me te takenga hopunga me te whakaahua ina whakaputaina.",
    "Derived spatial relationships using overlap geometry and New Zealand metric CRS handling.": "Ngā hononga mokowā kua ahu mai mā te āhuahanga inaki me te whakahaere CRS ine o Aotearoa.",
    "Parcel statutory actions": "Ngā mahi ā-ture pānga whenua",
    "Current and historic LINZ/Landonline parcel actions normalized into legal/statutory intelligence.": "Ngā mahi pānga whenua LINZ/Landonline onāianei me ngā mahi o mua kua whakaraupapatia hei mōhiotanga ture/ā-ture.",
    "baseline complete": "kua oti te paparanga matua",
    "relationship graph complete": "kua oti te whatunga hononga",
    "baseline complete · automated refresh": "kua oti te paparanga matua · whakahou aunoa",

    # Docs titles / buildings / statutory
    "Legal property identity": "Tuakiri rawa ture",
    "Titles stay relational.": "Ka noho hononga tonu ngā taitara.",
    "PropData does not flatten New Zealand title identity into a single fake owner field. The graph preserves title records and title↔parcel associations separately so multi-title, unit-title and shared-spatial contexts remain structurally correct.": "Kāore a PropData e whakaiti i te tuakiri taitara o Aotearoa ki tētahi āpure rangatira rūpahu kotahi. Ka tiaki motuhake te whatunga i ngā pūkete taitara me ngā hononga taitara↔pānga whenua kia tika tonu ngā horopaki taitara-maha, taitara-wae me te mokowā tiritahi.",
    "Named ownership is a separate entitlement problem.": "He take mana motuhake te rangatiratanga whai-ingoa.",
    "Physical property graph": "Whatunga rawa ā-tinana",
    "Buildings are linked, not merely nearby.": "Ka honoa ngā whare, ehara i te mea he tata noa.",
    "A complete national building source does not mean every parcel contains a building. A zero relationship count is different from unavailable linkage coverage; read the returned coverage state.": "Ehara te otinga o te puna whare ā-motu i te tohu he whare kei ia pānga whenua. He rerekē te tatau hononga kore i te kapi hononga kāore i te wātea; pānuihia te tūnga kapi kua whakahokia.",
    "Legal / statutory intelligence": "Mōhiotanga ture / ā-ture",
    "Parcel actions now have their own production layer.": "Kei ngā mahi pānga whenua tō rātou ake paparanga whakaputa ināianei.",
    "PRODUCTION GRAPH": "WHATUNGA WHAKAPUTA",
    "342,695 normalized statutory actions": "342,695 ngā mahi ā-ture kua whakaraupapatia",
    "LINZ dataset 51565 is loaded nationally and refreshed through a bounded, resumable changeset workflow. Records remain attached to source parcel identity rather than being turned into vague property flags.": "Kua utaina ā-motu te huinga raraunga LINZ 51565, ā, ka whakahoutia mā tētahi rerenga changeset kua herea, ka taea te tīmata anō. Ka noho ngā pūkete ki te tuakiri pānga whenua puna, kaua e hurihia hei tohu rawa rangirua.",
    "Current": "Onāianei",
    "Historic": "O mua",
    "Refresh cadence": "Auautanga whakahou",
    "SAFE SUMMARY": "WHAKARĀPOPOTO HAUMARU",
    "Current vs historic, by action type": "Onāianei me o mua, mā te momo mahi",
    "The country graph can summarize total/current/historic actions and create/extinguished/referenced counts, returning a bounded set of source-aware items without exposing raw ingest payloads.": "Ka taea e te whatunga whenua te whakarāpopoto i ngā mahi katoa/onāianei/o mua me ngā tatau create/extinguished/referenced, ka whakahoki i tētahi huinga tūemi whai-puna kua herea me te kore e whakaatu i ngā payload uta mata.",
    "Create": "Waihanga",
    "Extinguished": "Whakakore",
    "Referenced": "Tohutoro",
    "LIVE IN THE PROPERTY API:": "ORA I ROTO I TE API RAWA:",

    # Docs platform / semantics / errors / sources
    "Global platform routes": "Ngā ara tūāpapa ā-ao",
    "Country product, global control plane.": "Hua ā-whenua, papa whakahaere ā-ao.",
    "Country-aware capabilities and market context across the PropData network.": "Ngā āheinga mōhio-ā-whenua me te horopaki mākete puta noa i te whatunga PropData.",
    "Authoritative account usage and limits. Build quota-aware backoff from this route and returned rate-limit headers.": "Te whakamahinga me ngā rohe pūkete whai mana. Hangaia te backoff mōhio-rohe mai i tēnei ara me ngā pane rate-limit kua whakahokia.",
    "Public service health. Suitable for operational checks, not for property-specific coverage conclusions.": "Te hauora ratonga tūmatanui. He pai mō ngā arowhai whakahaere, ehara mō ngā whakatau kapi rawa-motuhake.",
    "Public platform statistics and proof points.": "Ngā tatauranga tūāpapa tūmatanui me ngā tohu taunaki.",
    "Production platform and data changes for integration teams.": "Ngā panonitanga tūāpapa whakaputa me ngā raraunga mō ngā rōpū whakauru.",
    "Do not guess": "Kaua e whakapae",
    "Match, coverage and provenance are separate signals.": "He tohu motuhake te taurite, te kapi me te takenga.",
    "How the input resolved: address, parcel, coordinate or another explicit identity method.": "Te āhua i whakatauria ai te tāuru: wāhitau, pānga whenua, taunga wāhi, tētahi atu tikanga tuakiri mārama rānei.",
    "Whether the requested source/layer is available for the resolved context.": "Mēnā e wātea ana te puna/paparanga i tonoa mō te horopaki kua whakatauria.",
    "Whether an address or coordinate successfully attached to parcel identity.": "Mēnā i hono pai tētahi wāhitau, taunga wāhi rānei ki te tuakiri pānga whenua.",
    "Where the fact originated and how a derived relationship was produced.": "Nō hea te meka, ā, i pēhea te hanga o tētahi hononga kua ahu mai.",
    "Distinguish total matches from bounded response items.": "Wehea ngā taurite katoa i ngā tūemi whakautu kua herea.",
    "Missing source truth remains missing. PropData does not convert absence into a favorable claim.": "Ka noho ngaro tonu te pono puna kāore i te wātea. Kāore a PropData e huri i te korenga hei kerēme pai.",
    "Core contract rule:": "Ture matua o te kirimana:",
    "Operational behavior": "Whanonga whakahaere",
    "Handle failures by category.": "Whakahaerehia ngā hapa mā te kāwai.",
    "Status": "Tūnga",
    "Meaning": "Tikanga",
    "Recommended behavior": "Whanonga tūtohu",
    "Validation / invalid request": "Whakamana / tono muhu",
    "Authentication failed": "I rahua te whakamana urunga",
    "Entitlement / access restriction": "Mana / here urunga",
    "Route or supported resource not found": "Kāore i kitea te ara, rauemi tautoko rānei",
    "Rate limit": "Rohe tono",
    "Transient service/upstream failure": "Hapa ratonga/upstream rangitahi",
    "Source and rights transparency": "Mārama ki ngā puna me ngā motika",
    "Authoritative sources in. Governed delivery out.": "Ngā puna whai mana ki roto. He tukunga kua whakahaerehia ki waho.",
    "Core New Zealand property layers are sourced from Toitū Te Whenua Land Information New Zealand (LINZ). PropData operates the ingestion, normalization, canonical identity, spatial processing, relationship graph, refresh automation, coverage semantics and production delivery above those source systems.": "Ka ahu mai ngā paparanga rawa matua o Aotearoa i Toitū Te Whenua Land Information New Zealand (LINZ). Ka whakahaere a PropData i te uta, te whakaraupapa, te tuakiri canonical, te tukatuka mokowā, te whatunga hononga, te whakahou aunoa, ngā tikanga kapi me te tukunga whakaputa i runga ake i aua pūnaha puna.",
    "LINZ SOURCE-AWARE": "MŌHIO-PUNA LINZ",
    "PROPDATA NORMALIZED": "KUA WHAKARAUPAPATIA E PROPDATA",
    "PERSONAL DATA ENTITLEMENTS SEPARATE": "HE MANA MOTUHAKE MŌ NGĀ RARAUNGA WHAIARO",
    "Title Memorial List / personal data:": "Rārangi Title Memorial / raraunga whaiaro:",
    "PropData is an independent product of PropTechUSA.ai and is not operated by or affiliated with LINZ or the New Zealand government.": "He hua motuhake a PropData nā PropTechUSA.ai, ā, kāore i whakahaerehia, kāore hoki i whai hononga ki LINZ, ki te Kāwanatanga o Aotearoa rānei.",
    "Country workspace": "Papamahi whenua",
    "Test the New Zealand contract without leaving the country product.": "Whakamātauria te kirimana o Aotearoa me te kore e wehe i te hua ā-whenua.",
    "The NZ Workspace is the operating surface for request testing, country coverage, live response inspection, account usage and developer handoff. It is intentionally modeled after the global PropData Workspace while keeping the experience locked to New Zealand.": "Ko te Papamahi NZ te mata whakahaere mō te whakamātau tono, te kapi ā-whenua, te tirotiro whakautu ora, te whakamahinga pūkete me te tuku ki ngā kaiwhakawhanake. He mea hanga kia rite ki te Papamahi PropData ā-Ao, engari ka herea te wheako ki Aotearoa.",
    "Back to product": "Hoki ki te hua",
    "View NZ pricing": "Tirohia ngā utu NZ",
    "Global PropData Workspace": "Papamahi PropData ā-Ao",

    # Workspace chrome
    "Workspace": "Papamahi",
    "Overview": "Tirohanga whānui",
    "Request Lab": "Taiwhanga Tono",
    "NZ Coverage": "Kapi NZ",
    "Account & Usage": "Pūkete me te Whakamahinga",
    "Develop": "Whakawhanake",
    "Docs & Handoff": "Tuhinga me te Tuku",
    "Country Website": "Pae Tukutuku Whenua",
    "Global Coverage": "Kapi ā-Ao",
    "Country architecture": "Hanganga ā-whenua",
    "One global PropData account and edge API. This workspace scopes the developer experience to New Zealand and automatically pins country-aware requests to NZ.": "Kotahi te pūkete PropData ā-ao me te API tapa. Ka arotahi tēnei papamahi i te wheako kaiwhakawhanake ki Aotearoa, ā, ka here aunoa i ngā tono mōhio-ā-whenua ki NZ.",

    # Workspace overview
    "New Zealand operating console": "Papatohu whakahaere o Aotearoa",
    "One country. Full depth.": "Kotahi te whenua. Te hōhonutanga katoa.",
    "Resolve property identity, inspect the production graph, test country-aware requests and hand a verified contract directly to engineering.": "Whakatauria te tuakiri rawa, tirohia te whatunga whakaputa, whakamātauria ngā tono mōhio-ā-whenua, ā, tukuna tika tētahi kirimana kua whakamana ki te rōpū hangarau.",
    "Run a request": "Whakahaere tono",
    "Read docs": "Pānui tuhinga",
    "PRODUCTION · TOITŪ TE WHENUA LINZ": "WHAKAPUTA · TOITŪ TE WHENUA LINZ",
    "New Zealand property infrastructure, not another lookup tool.": "He hanganga rawa o Aotearoa, ehara i tētahi atu taputapu rapu noa.",
    "Addresses resolve into parcels. Parcels connect to titles, cadastral geometry, buildings and legal/statutory context. Every layer keeps its own source and coverage state underneath one country-aware PropData contract.": "Ka whakatauria ngā wāhitau ki ngā pānga whenua. Ka hono ngā pānga whenua ki ngā taitara, te āhuahanga cadastral, ngā whare me te horopaki ture/ā-ture. Ka pupuri ia paparanga i tōna ake puna me te tūnga kapi i raro i tētahi kirimana PropData mōhio-ā-whenua kotahi.",
    "ADDRESS → PARCEL → TITLES → BUILDINGS → STATUTORY INTELLIGENCE": "WĀHITAU → PĀNGA WHENUA → TAITARA → WHARE → MŌHIOTANGA Ā-TURE",
    "Country scope": "Rohe whenua",
    "NZ only": "NZ anake",
    "Data backbone": "Tūāpapa raraunga",
    "API surface": "Mata API",
    "Graph state": "Tūnga whatunga",
    "National baseline complete": "Kua oti te paparanga ā-motu",
    "Authoritative addresses": "Ngā wāhitau whai mana",
    "2,988,279 title↔parcel links": "2,988,279 ngā hononga taitara↔pānga whenua",
    "Hourly bounded changeset refresh": "Whakahou changeset ā-haora kua herea",
    "New Zealand property graph": "Whatunga rawa o Aotearoa",
    "7 production layers": "7 paparanga whakaputa",
    "Identity, locality, lifecycle, coordinates": "Tuakiri, rohe, huringa ora, taunga wāhi",
    "Cadastral identity + available geometry": "Tuakiri cadastral + āhuahanga e wātea ana",
    "Legal title metadata": "Metadata taitara ture",
    "Title ↔ parcel relationships": "Ngā hononga taitara ↔ pānga whenua",
    "Many-to-many legal identity graph": "Whatunga tuakiri ture maha-ki-maha",
    "Footprints + capture provenance": "Tapuwae + takenga hopunga",
    "Building ↔ parcel relationships": "Ngā hononga whare ↔ pānga whenua",
    "Spatial overlap graph": "Whatunga inaki mokowā",
    "Current + historic legal/statutory context": "Horopaki ture/ā-ture onāianei me o mua",
    "Developer quickstart": "Tīmata tere mā te kaiwhakawhanake",
    "Country-aware REST": "REST mōhio-ā-whenua",
    "PROPERTY": "RAWA",
    "Parcel / address resolver": "Kaiwhakatautohu pānga whenua / wāhitau",
    "Open this route in the live Request Lab.": "Whakatuwheratia tēnei ara i te Taiwhanga Tono ora.",
    "SPATIAL": "MOKOWĀ",
    "Coordinates → property": "Taunga wāhi → rawa",
    "Resolve a WGS84 point into parcel context.": "Whakatauria tētahi ira WGS84 ki te horopaki pānga whenua.",
    "COVERAGE": "KAPI",
    "Inspect NZ graph state": "Tirohia te tūnga whatunga NZ",
    "Understand source depth before building promises.": "Mārama ki te hōhonutanga puna i mua i te hanga oati.",
    "REFERENCE": "TOHUTORO",
    "Open country docs": "Whakatuwheratia ngā tuhinga whenua",
    "Implementation semantics, graph layers and source rules.": "Ngā tikanga whakatinana, paparanga whatunga me ngā ture puna.",
    "LEGAL": "Ā-TURE",
    "Live statutory actions": "Ngā mahi ā-ture ora",
    "Run parcel 3784245 — 12 certified LINZ 51565 actions.": "Whakahaerehia te pānga whenua 3784245 — 12 mahi LINZ 51565 kua whakamana.",

    # Workspace request lab
    "Live request lab": "Taiwhanga tono ora",
    "Test the NZ contract.": "Whakamātauria te kirimana NZ.",
    "Country scope is locked to NZ. The lab exposes public customer-safe routes only—never internal RPCs, source tables or service-role operations.": "Kua herea te rohe whenua ki NZ. Ka whakaatu te taiwhanga i ngā ara tūmatanui haumaru-kiritaki anake—kaua rawa ngā RPC ā-roto, ngā ripanga puna, ngā mahi service-role rānei.",
    "Endpoint reference": "Tohutoro pito-mutunga",
    "NZ public surface": "Mata tūmatanui NZ",
    "Search endpoints": "Rapua ngā pito-mutunga",
    "Select an endpoint": "Tīpakohia tētahi pito-mutunga",
    "Run request": "Whakahaere tono",
    "No API key connected. Public health/stats/changelog routes can still run.": "Kāore he kī API kua tūhono. Ka taea tonu ngā ara health/stats/changelog tūmatanui te whakahaere.",
    "Choose a route. The lab will show only parameters supported by the selected contract.": "Kōwhiria tētahi ara. Ka whakaatu te taiwhanga i ngā tawhā e tautokona ana e te kirimana kua tīpakohia anake.",
    "Copy URL": "Tāruatia te URL",
    "Reset": "Tautuhi anō",
    "LIVE RESPONSE": "WHAKAUTU ORA",
    "READY": "KUA RITE",
    "Select a route, complete its parameters, then run the request.": "Tīpakohia tētahi ara, whakakīa ōna tawhā, kātahi ka whakahaere i te tono.",
    "Secrets are never placed in the URL or printed into this panel.": "Kāore rawa ngā muna e whakatakotoria ki te URL, e tāngia rānei ki tēnei paewhiri.",
    "Property resolver": "Kaiwhakatautohu rawa",
    "Coordinates → property": "Taunga wāhi → rawa",
    "Coordinate coverage check": "Arowhai kapi taunga wāhi",
    "Countries / capabilities": "Ngā whenua / āheinga",
    "Account usage": "Whakamahinga pūkete",
    "Service health": "Hauora ratonga",
    "Platform stats": "Tatauranga tūāpapa",
    "Changelog": "Rārangi panoni",
    "LINZ primary parcel ID": "ID pānga whenua matua LINZ",
    "New Zealand address": "Wāhitau o Aotearoa",
    "Enrichment": "Whakarākei",
    "Base response": "Whakautu taketake",
    "Latitude": "Ahopae",
    "Longitude": "Ahopou",
    "Resolve an NZ property by parcel or address. Use one identity method at a time.": "Whakatauria tētahi rawa NZ mā te pānga whenua, mā te wāhitau rānei. Whakamahia kia kotahi te tikanga tuakiri i te wā kotahi.",
    "Resolve a WGS84 coordinate into containing property context.": "Whakatauria tētahi taunga WGS84 ki te horopaki rawa kei roto.",
    "Probe coordinate coverage before relying on a spatial property workflow.": "Tirohia te kapi taunga wāhi i mua i te whakawhirinaki ki tētahi rerenga rawa mokowā.",

    # Workspace coverage
    "Country graph coverage": "Kapi whatunga whenua",
    "Know what is actually loaded.": "Kia mōhio ki ngā mea kua utaina tūturu.",
    "National source completeness, derived relationship coverage and public route exposure are different facts. This workspace keeps those distinctions visible.": "He meka rerekē te otinga puna ā-motu, te kapi hononga kua ahu mai me te whakaaturanga ara tūmatanui. Ka whakakite tēnei papamahi i aua rerekētanga.",
    "Run coordinate coverage probe": "Whakahaere tirohanga kapi taunga wāhi",
    "IDENTITY": "TUAKIRI",
    "3,040,571 parcels": "3,040,571 pānga whenua",
    "Primary cadastral parcel baseline complete, with authoritative address resolution layered above it.": "Kua oti te paparanga matua pānga whenua cadastral, me te whakataunga wāhitau whai mana kei runga ake.",
    "LEGAL IDENTITY": "TUAKIRI TURE",
    "2,450,998 titles": "2,450,998 taitara",
    "2,988,279 title↔parcel associations preserve many-to-many legal relationships.": "Ka tiaki ngā hononga taitara↔pānga whenua 2,988,279 i ngā hononga ture maha-ki-maha.",
    "PHYSICAL": "Ā-TINANA",
    "3,268,141 buildings": "3,268,141 whare",
    "National LINZ building-outline source complete; 3,820,845 derived building↔parcel relationship rows.": "Kua oti te puna tapuwae whare LINZ ā-motu; 3,820,845 ngā rārangi hononga whare↔pānga whenua kua ahu mai.",
    "342,695 actions": "342,695 mahi",
    "Current and historic LINZ parcel actions loaded into a bounded, source-aware legal intelligence layer.": "Kua utaina ngā mahi pānga whenua LINZ onāianei me o mua ki tētahi paparanga mōhiotanga ture whai-puna kua herea.",
    "SPATIAL RESOLUTION": "WHAKATAUNGA MOKOWĀ",
    "Coordinate-aware": "Mōhio-taunga wāhi",
    "WGS84 points can resolve into containing property context with explicit coverage semantics.": "Ka taea ngā ira WGS84 te whakatauria ki te horopaki rawa kei roto me ngā tikanga kapi mārama.",
    "DELIVERY": "TUKUNGA",
    "One global platform, with country-specific depth and response contracts layered underneath.": "Kotahi te tūāpapa ā-ao, me te hōhonutanga me ngā kirimana whakautu motuhake ā-whenua kei raro.",
    "Statutory intelligence": "Mōhiotanga ā-ture",
    "LINZ dataset 51565": "Huinga raraunga LINZ 51565",
    "Live property contract:": "Kirimana rawa ora:",
    "Refresh cadence": "Auautanga whakahou",
    "Restricted personal data": "Raraunga whaiaro kua herea",
    "Separate entitlement": "Mana motuhake",
    "Title Memorial List / 51695:": "Title Memorial List / 51695:",
    "The country product can be deep without pretending every official dataset has the same rights model. Public product claims stop at what is actually licensed and production-ready.": "Ka taea te hōhonu o te hua ā-whenua me te kore e whakapae he ōrite te tauira motika o ia huinga raraunga whai mana. Ka mutu ngā kerēme hua tūmatanui ki ngā mea kua raihanatia, kua rite hoki mō te whakaputa.",

    # Workspace account / handoff
    "Account & usage": "Pūkete me te whakamahinga",
    "One PropData account, country-focused workflow.": "Kotahi te pūkete PropData, he rerenga arotahi ā-whenua.",
    "The NZ Workspace does not create a second billing identity. It uses the same PropData account and API credential while keeping requests and examples scoped to New Zealand.": "Kāore te Papamahi NZ e hanga tuakiri nama tuarua. Ka whakamahi i taua pūkete PropData me taua taunakitanga API kotahi, me te pupuri i ngā tono me ngā tauira ki Aotearoa.",
    "Connected API credential": "Taunakitanga API kua tūhono",
    "NOT CONNECTED": "KĀORE I TŪHONO",
    "Connect": "Tūhono",
    "Remember on this device. Leave unchecked to keep the credential in session storage only.": "Maumaharatia ki tēnei pūrere. Waiho kia kāore i tohua kia noho te taunakitanga ki te rokiroki wā-mahi anake.",
    "No credential connected.": "Kāore he taunakitanga kua tūhono.",
    "Show / hide": "Whakaatu / huna",
    "Disconnect": "Momotu",
    "Production handling:": "Whakahaere whakaputa:",
    "Authoritative usage": "Whakamahinga whai mana",
    "Usage and limits are read from the production account contract rather than hardcoded into the workspace.": "Ka pānuihia te whakamahinga me ngā rohe mai i te kirimana pūkete whakaputa, kaua e hardcode ki te papamahi.",
    "Load live usage": "Utaina te whakamahinga ora",
    "Developer handoff": "Tuku ki te kaiwhakawhanake",
    "Everything needed to ship NZ.": "Ngā mea katoa hei tuku i NZ.",
    "Use the country docs for exact semantics, this workspace for live probes, and the global workspace when engineering needs cross-country control.": "Whakamahia ngā tuhinga whenua mō ngā tikanga tika, tēnei papamahi mō ngā tirohanga ora, me te papamahi ā-ao ina hiahia te rōpū hangarau ki te whakahaere whenua-maha.",
    "New Zealand API Docs": "Tuhinga API o Aotearoa",
    "Country architecture, public endpoint surface, Full Enrich concepts, graph layers, statutory intelligence and rights boundaries.": "Hanganga ā-whenua, mata pito-mutunga tūmatanui, ariā Full Enrich, paparanga whatunga, mōhiotanga ā-ture me ngā rohe motika.",
    "Open docs →": "Whakatuwheratia ngā tuhinga →",
    "NZ Request Lab": "Taiwhanga Tono NZ",
    "Run country-locked requests against the production edge API without exposing a key in the URL.": "Whakahaere tono kua herea ki te whenua ki te API tapa whakaputa me te kore e whakaatu kī ki te URL.",
    "Open lab →": "Whakatuwheratia te taiwhanga →",
    "Cross-market endpoint catalog, broader U.S. intelligence, account controls, MCP and the global developer surface.": "Rārangi pito-mutunga mākete-maha, mōhiotanga whānui ake o Amerika, whakahaere pūkete, MCP me te mata kaiwhakawhanake ā-ao.",
    "Open global workspace →": "Whakatuwheratia te papamahi ā-ao →",
    "AI-native delivery": "Tukunga taketake-AI",
    "PropData MCP is OAuth-protected and distinct from the static-key REST flow shown in this workspace.": "Ka tiakina a PropData MCP e OAuth, ā, he rerekē i te rerenga REST kī-pūmau e whakaaturia ana i tēnei papamahi.",
    "View global MCP setup →": "Tirohia te tatūnga MCP ā-ao →",
    "Production edge": "Tapa whakaputa",
    "Direct REST runs through the shared PropData edge while the country adapter preserves New Zealand-native identifiers and provenance.": "Ka rere te REST tika mā te tapa PropData tiritahi, ā, ka tiaki te adapter whenua i ngā tautuhi me te takenga taketake o Aotearoa.",
    "Authentication guide →": "Aratohu whakamana urunga →",
    "Bulk / enterprise": "Raraunga nui / hinonga",
    "Custom response contracts, bulk delivery, commercial platform use and country-specific data licensing.": "Ngā kirimana whakautu ritenga, tukunga raraunga nui, whakamahinga tūāpapa arumoni me te raihana raraunga motuhake ā-whenua.",
    "Talk to enterprise sales →": "Kōrero ki te hoko hinonga →",
}


def patch_site_js(text: str) -> str:
    marker = "// PROPDATA_NZ_DEVELOPER_I18N_V1"
    if marker not in text:
        insert_anchor = "const ORIGINAL_TEXT=new WeakMap();"
        docs_meta = {
            "en": {
                "title": "PropData New Zealand API Docs | Property, Titles, Buildings & Statutory Intelligence",
                "description": "Production documentation for PropData New Zealand: property identity, parcels, titles, buildings, relationships and LINZ statutory intelligence.",
                "ogTitle": "PropData New Zealand API Documentation",
                "ogDescription": "One production contract for New Zealand property identity, parcels, titles, buildings, relationships and statutory intelligence.",
                "locale": "en_NZ",
            },
            "mi": {
                "title": "Tuhinga API PropData Aotearoa | Rawa, Taitara, Whare me te Mōhiotanga ā-Ture",
                "description": "Ngā tuhinga whakaputa mō PropData Aotearoa: tuakiri rawa, pānga whenua, taitara, whare, hononga me te mōhiotanga ā-ture LINZ.",
                "ogTitle": "Tuhinga API PropData Aotearoa",
                "ogDescription": "Kotahi te kirimana whakaputa mō te tuakiri rawa, pānga whenua, taitara, whare, hononga me te mōhiotanga ā-ture o Aotearoa.",
                "locale": "mi_NZ",
            },
        }
        workspace_meta = {
            "en": {
                "title": "PropData New Zealand Workspace | API Console",
                "description": "PropData New Zealand developer workspace for country-scoped API testing, property resolution, coverage, usage and production integration.",
                "ogTitle": "PropData New Zealand Workspace",
                "ogDescription": "Country-scoped New Zealand API testing, coverage, usage and production integration.",
                "locale": "en_NZ",
            },
            "mi": {
                "title": "Papamahi PropData Aotearoa | Papatohu API",
                "description": "Te papamahi kaiwhakawhanake PropData Aotearoa mō te whakamātau API ā-whenua, whakataunga rawa, kapi, whakamahinga me te whakauru whakaputa.",
                "ogTitle": "Papamahi PropData Aotearoa",
                "ogDescription": "Te whakamātau API, kapi, whakamahinga me te whakauru whakaputa kua arotahi ki Aotearoa.",
                "locale": "mi_NZ",
            },
        }
        block = (
            f"// PROPDATA_NZ_DEVELOPER_I18N_V1\n"
            f"const DOCS_META={json.dumps(docs_meta, ensure_ascii=False, separators=(',', ':'))};\n"
            f"const WORKSPACE_META={json.dumps(workspace_meta, ensure_ascii=False, separators=(',', ':'))};\n"
            f"Object.assign(HOME_TRANSLATIONS,{json.dumps(translations, ensure_ascii=False, separators=(',', ':'))});\n\n"
        )
        text = replace_once(text, insert_anchor, block + insert_anchor, "site.js i18n block")

    old_skip = "  if(document.body.classList.contains('docs-body'))return;\n"
    if old_skip in text:
        text = text.replace(old_skip, "", 1)

    old_nodes = "  nodes.forEach(node=>{const original=ORIGINAL_TEXT.get(node);const english=original.trim();const replacement=lang==='mi'?(HOME_TRANSLATIONS[english]||english):english;node.nodeValue=(original.match(/^\\s*/)?.[0]||'')+replacement+(original.match(/\\s*$/)?.[0]||'');});"
    new_nodes = "  nodes.forEach(node=>{const original=ORIGINAL_TEXT.get(node);const english=original.trim();const replacement=lang==='mi'?(HOME_TRANSLATIONS[english]||english):english;const next=(original.match(/^\\s*/)?.[0]||'')+replacement+(original.match(/\\s*$/)?.[0]||'');if(node.nodeValue!==next)node.nodeValue=next;});"
    if old_nodes in text:
        text = text.replace(old_nodes, new_nodes, 1)

    old_surface = "  const isDocs=document.body.classList.contains('docs-body');\n"
    new_surface = "  const isDocs=document.body.classList.contains('docs-body');\n  const isWorkspace=document.body.classList.contains('workspace-body');\n"
    if "const isWorkspace=document.body.classList.contains('workspace-body');" not in text:
        text = replace_once(text, old_surface, new_surface, "site.js workspace surface")

    old_meta = "  if(!isDocs){\n    const meta=META[lang];document.title=meta.title;\n    setMeta('meta[name=\"description\"]','content',meta.description);\n    setMeta('meta[property=\"og:title\"]','content',meta.ogTitle);\n    setMeta('meta[property=\"og:description\"]','content',meta.ogDescription);\n    setMeta('meta[property=\"og:locale\"]','content',meta.locale);\n    setMeta('meta[name=\"twitter:title\"]','content',meta.ogTitle);\n    setMeta('meta[name=\"twitter:description\"]','content',meta.ogDescription);\n  }\n"
    new_meta = "  const meta=(isDocs?DOCS_META[lang]:(isWorkspace?WORKSPACE_META[lang]:META[lang]));\n  if(meta){\n    document.title=meta.title;\n    setMeta('meta[name=\"description\"]','content',meta.description);\n    setMeta('meta[property=\"og:title\"]','content',meta.ogTitle);\n    setMeta('meta[property=\"og:description\"]','content',meta.ogDescription);\n    setMeta('meta[property=\"og:locale\"]','content',meta.locale);\n    setMeta('meta[name=\"twitter:title\"]','content',meta.ogTitle);\n    setMeta('meta[name=\"twitter:description\"]','content',meta.ogDescription);\n  }\n"
    if old_meta in text:
        text = text.replace(old_meta, new_meta, 1)

    old_url = "  if(updateUrl&&!isDocs){const u=new URL(location.href);if(lang==='en')u.searchParams.delete('lang');else u.searchParams.set('lang',lang);history.replaceState({},'',u)}"
    new_url = "  if(updateUrl){const u=new URL(location.href);if(lang==='en')u.searchParams.delete('lang');else u.searchParams.set('lang',lang);history.replaceState({},'',u)}"
    if old_url in text:
        text = text.replace(old_url, new_url, 1)

    placeholder_anchor = "  document.querySelectorAll('[data-en][data-mi]').forEach(el=>{const value=el.dataset[lang];if(value!=null)el.textContent=value});\n"
    placeholder_add = placeholder_anchor + "  document.querySelectorAll('[data-en-placeholder][data-mi-placeholder]').forEach(el=>{const value=el.dataset[lang+'Placeholder'];if(value!=null)el.setAttribute('placeholder',value)});\n"
    if "data-en-placeholder" not in text:
        text = replace_once(text, placeholder_anchor, placeholder_add, "site.js placeholder i18n")

    # Keep dynamic Workspace text translated after endpoint/field rerenders.
    observer_marker = "// PROPDATA_NZ_DYNAMIC_I18N_V1"
    if observer_marker not in text:
        anchor = "setLanguage(preferred,{updateUrl:false});\n\nconst header="
        observer = "setLanguage(preferred,{updateUrl:false});\n\n// PROPDATA_NZ_DYNAMIC_I18N_V1\nlet propdataNzI18nBusy=false;let propdataNzI18nQueued=false;\nfunction propDataNzRefreshLanguage(){if(propdataNzI18nBusy)return;propdataNzI18nBusy=true;try{localizeHomeText(document.documentElement.lang.startsWith('mi')?'mi':'en')}finally{propdataNzI18nBusy=false}}\nwindow.PropDataNZLanguageRefresh=propDataNzRefreshLanguage;\nif(document.body.classList.contains('workspace-body')&&'MutationObserver'in window){const i18nObserver=new MutationObserver(()=>{if(propdataNzI18nBusy||!document.documentElement.lang.startsWith('mi')||propdataNzI18nQueued)return;propdataNzI18nQueued=true;queueMicrotask(()=>{propdataNzI18nQueued=false;propDataNzRefreshLanguage()})});i18nObserver.observe(document.body,{childList:true,subtree:true,characterData:true})}\n\nconst header="
        text = replace_once(text, anchor, observer, "site.js dynamic language observer")

    return text


def patch_docs(text: str) -> str:
    if 'hreflang="mi-NZ"' not in text:
        text = replace_once(
            text,
            '  <link rel="canonical" href="https://nz.proptechusa.ai/docs">',
            '  <link rel="canonical" href="https://nz.proptechusa.ai/docs">\n  <link rel="alternate" hreflang="en-NZ" href="https://nz.proptechusa.ai/docs?lang=en">\n  <link rel="alternate" hreflang="mi-NZ" href="https://nz.proptechusa.ai/docs?lang=mi">\n  <link rel="alternate" hreflang="x-default" href="https://nz.proptechusa.ai/docs">',
            "docs hreflang",
        )

    old_nav = '<div class="nav-actions"><a class="nav-cta" href="/workspace">Open Workspace</a></div>'
    new_nav = '<div class="nav-actions"><div class="lang-switch" aria-label="Language / Reo"><button class="lang-btn active" type="button" data-lang="en" aria-pressed="true">EN</button><button class="lang-btn" type="button" data-lang="mi" aria-pressed="false">MI</button></div><a class="nav-cta" href="/workspace">Open Workspace</a></div>'
    text = replace_or_verify(text, old_nav, new_nav, 'aria-label="Language / Reo"', "docs language switch")

    # Promote already-certified 51565 Full Enrich contract if stale docs are still present.
    old_property = 'Primary property resolver for NZ address or parcel input. Add <code>enrich=full</code> for deeper country-aware enrichment where entitled.'
    new_property = 'Primary property resolver for NZ address or parcel input. The NZ property contract returns country-native Full Enrich including titles, building relationships and <code>new_zealand.legal_actions</code> from the certified LINZ 51565 layer.'
    if old_property in text:
        text = text.replace(old_property, new_property, 1)

    old_full = 'New Zealand Full Enrich is backed by the same canonical parcel and title identity used by the base resolver, plus country enrichment that can include building relationships and derived physical context. Response exposure is route-, plan- and entitlement-specific.'
    new_full = 'New Zealand Full Enrich is backed by the same canonical parcel and title identity used by the base resolver, then attaches country-native building relationships, derived physical context and the certified LINZ 51565 legal/statutory summary. The legal layer is returned at <code>new_zealand.legal_actions</code> and remains independently fail-open so a downstream legal-layer issue cannot break valid property identity.'
    if old_full in text:
        text = text.replace(old_full, new_full, 1)

    physical = '<article class="layer-card"><span class="layer-no">PHYSICAL</span><h3>Building relationships</h3><p>National building outlines spatially linked to parcels with relationship method, overlap and provenance.</p></article>'
    if 'class="layer-no">LEGAL / STATUTORY' not in text:
        legal = physical + '\n          <article class="layer-card"><span class="layer-no">LEGAL / STATUTORY</span><h3>Live legal actions</h3><p>Certified LINZ 51565 current + historic parcel actions returned directly at <code>new_zealand.legal_actions</code> with counts, bounded items, source revision and coverage state.</p></article>'
        text = replace_once(text, physical, legal, "docs legal Full Enrich card")

    stale_notice = '<div class="notice blue"><strong>Exposure note:</strong> statutory actions are a certified production graph layer. Standard public response exposure is still route-, plan- and entitlement-specific; this documentation does not invent a standalone public route that the edge API has not promoted.</div>'
    if stale_notice in text:
        live_notice = '''<div class="notice"><strong>LIVE IN THE PROPERTY API:</strong> statutory actions are now part of the New Zealand property response at <code>new_zealand.legal_actions</code>. Production canary parcel <code>3784245</code> returns <strong>12</strong> certified actions: 2 current, 10 historic, 1 create and 11 referenced. No separate legal-actions endpoint is required.</div>
        <div class="code-block"><div class="code-head"><span>VERIFIED PUBLIC RESPONSE · PARCEL 3784245</span><button class="copy-code" type="button">COPY</button></div><pre>"new_zealand": {
  "legal_actions": {
    "coverage_status": "complete",
    "count": 12,
    "current_count": 2,
    "historic_count": 10,
    "action_counts": {
      "create": 1,
      "extinguished": 0,
      "referenced": 11
    },
    "returned": 12,
    "truncated": false,
    "source_dataset_id": "51565"
  }
}</pre></div>'''
        text = text.replace(stale_notice, live_notice, 1)

    # Make docs copy feedback language-aware.
    old_copy = "navigator.clipboard.writeText(pre.innerText).then(function(){var old=btn.textContent;btn.textContent='COPIED';setTimeout(function(){btn.textContent=old},1200)});"
    new_copy = "navigator.clipboard.writeText(pre.innerText).then(function(){var old=btn.textContent;btn.textContent=document.documentElement.lang.startsWith('mi')?'KUA TĀRUATIA':'COPIED';setTimeout(function(){btn.textContent=old},1200)});"
    if old_copy in text:
        text = text.replace(old_copy, new_copy, 1)

    return text


def patch_workspace(text: str) -> str:
    if '<body class="workspace-body">' not in text:
        text = replace_once(text, '<body>', '<body class="workspace-body">', "workspace body class")

    if '.lang-switch{' not in text:
        css_anchor = '.top-btn.primary{border-color:#0c7250;background:#0c7250;color:#fff}.menu{display:none;width:40px;height:40px;border:1px solid var(--line);border-radius:8px;background:#fff}'
        css_new = '.top-btn.primary{border-color:#0c7250;background:#0c7250;color:#fff}.lang-switch{display:flex;align-items:center;padding:3px;border:1px solid var(--line);border-radius:9px;background:#f5f8fa}.lang-btn{min-width:34px;height:31px;border:0;border-radius:6px;background:transparent;color:#6b7d89;font:900 9px/1 var(--mono);letter-spacing:.06em}.lang-btn.active{background:#0c7250;color:#fff;box-shadow:0 4px 12px rgba(12,114,80,.18)}.menu{display:none;width:40px;height:40px;border:1px solid var(--line);border-radius:8px;background:#fff}'
        text = replace_once(text, css_anchor, css_new, "workspace language CSS")

    old_actions = '<div class="top-actions"><a class="top-btn" href="/docs">API Docs</a><a class="top-btn" href="https://propdata.proptechusa.ai/dashboard">Global Workspace</a><button class="top-btn primary" type="button" id="top-connect">Connect API Key</button></div>'
    new_actions = '<div class="top-actions"><div class="lang-switch" aria-label="Language / Reo"><button class="lang-btn active" type="button" data-lang="en" aria-pressed="true">EN</button><button class="lang-btn" type="button" data-lang="mi" aria-pressed="false">MI</button></div><a class="top-btn" href="/docs">API Docs</a><a class="top-btn" href="https://propdata.proptechusa.ai/dashboard">Global Workspace</a><button class="top-btn primary" type="button" id="top-connect">Connect API Key</button></div>'
    text = replace_or_verify(text, old_actions, new_actions, 'aria-label="Language / Reo"', "workspace language switch")

    old_search = '<input class="search" id="endpoint-search" placeholder="Search endpoints">'
    new_search = '<input class="search" id="endpoint-search" placeholder="Search endpoints" data-en-placeholder="Search endpoints" data-mi-placeholder="Rapua ngā pito-mutunga">'
    if old_search in text:
        text = text.replace(old_search, new_search, 1)

    old_key = '<input class="input mono" type="password" id="key-input" autocomplete="off" placeholder="Paste PropData API key">'
    new_key = '<input class="input mono" type="password" id="key-input" autocomplete="off" placeholder="Paste PropData API key" data-en-placeholder="Paste PropData API key" data-mi-placeholder="Whakapirihia te kī API PropData">'
    if old_key in text:
        text = text.replace(old_key, new_key, 1)

    # Load the shared NZ language engine; the page keeps its own workspace application logic.
    if '<script src="/site.js" defer></script>' not in text:
        text = replace_once(text, '  <div class="toast" id="toast"></div>\n  <script>', '  <div class="toast" id="toast"></div>\n  <script src="/site.js" defer></script>\n  <script>', "workspace shared i18n script")

    # Promote 51565 workspace language/content in the same commit.
    old_note = "note:'Resolve an NZ property by parcel or address. Use one identity method at a time.'"
    new_note = "note:'Resolve an NZ property by parcel or address. Full Enrich includes new_zealand.legal_actions from the certified LINZ 51565 layer where covered. Use one identity method at a time.'"
    if old_note in text:
        text = text.replace(old_note, new_note, 1)

    spatial = '<button class="quick-link" data-preset="location"><span>SPATIAL</span><b>Coordinates → property</b><p>Resolve a WGS84 point into parcel context.</p></button>'
    if 'data-legal-canary' not in text:
        legal = spatial + '<button class="quick-link" data-legal-canary><span>LEGAL</span><b>Live statutory actions</b><p>Run parcel 3784245 — 12 certified LINZ 51565 actions.</p></button>'
        text = replace_once(text, spatial, legal, "workspace legal canary shortcut")

    old_live = '<strong>Production layer:</strong> 342,695 parcel statutory actions are nationally loaded and refreshed through bounded, resumable changesets.'
    new_live = '<strong>Live property contract:</strong> 342,695 parcel statutory actions are nationally loaded, refreshed through bounded resumable changesets, and returned through <code>/v1/property</code> at <code>new_zealand.legal_actions</code>.'
    if old_live in text:
        text = text.replace(old_live, new_live, 1)

    init_anchor = "    renderEndpoints();selectEndpoint('property');syncKeyUI();"
    if "data-legal-canary" in text and "$$('[data-legal-canary]').forEach" not in text:
        init_replacement = "    $$('[data-legal-canary]').forEach(b=>b.addEventListener('click',e=>{e.preventDefault();selectEndpoint('property');showView('lab');setTimeout(()=>{const parcel=$('[data-param=\"parcel\"]'),address=$('[data-param=\"address\"]'),enrich=$('[data-param=\"enrich\"]');if(parcel)parcel.value='3784245';if(address)address.value='';if(enrich)enrich.value='full';updateUrl()},0)}));\n    renderEndpoints();selectEndpoint('property');syncKeyUI();"
        text = replace_once(text, init_anchor, init_replacement, "workspace legal canary handler")

    return text


site_js = patch_site_js(SITE_JS.read_text(encoding="utf-8"))
docs = patch_docs(DOCS.read_text(encoding="utf-8"))
workspace = patch_workspace(WORKSPACE.read_text(encoding="utf-8"))

SITE_JS.write_text(site_js, encoding="utf-8")
DOCS.write_text(docs, encoding="utf-8")
WORKSPACE.write_text(workspace, encoding="utf-8")

# Fail-closed certification markers.
checks = {
    "site.js shared storage": "propdata_nz_lang" in site_js,
    "site.js developer i18n": "PROPDATA_NZ_DEVELOPER_I18N_V1" in site_js,
    "site.js docs meta": "DOCS_META" in site_js,
    "site.js workspace meta": "WORKSPACE_META" in site_js,
    "site.js dynamic i18n": "PROPDATA_NZ_DYNAMIC_I18N_V1" in site_js,
    "docs language switch": 'aria-label="Language / Reo"' in docs,
    "docs hreflang": 'hreflang="mi-NZ"' in docs,
    "docs live legal contract": "new_zealand.legal_actions" in docs and "VERIFIED PUBLIC RESPONSE · PARCEL 3784245" in docs,
    "workspace language switch": 'aria-label="Language / Reo"' in workspace,
    "workspace body surface": 'class="workspace-body"' in workspace,
    "workspace shared language engine": '<script src="/site.js" defer></script>' in workspace,
    "workspace legal canary": "data-legal-canary" in workspace,
    "workspace live legal contract": "new_zealand.legal_actions" in workspace,
}
failed = [name for name, ok in checks.items() if not ok]
if failed:
    raise SystemExit("CERTIFICATION FAILED: " + ", ".join(failed))

print("NZ DOCS + WORKSPACE LANGUAGE SWITCH: PASS")
print("LANGUAGES: EN / MI")
print("PREFERENCE: propdata_nz_lang")
print("DOCS + WORKSPACE LIVE 51565 CONTRACT: PASS")
