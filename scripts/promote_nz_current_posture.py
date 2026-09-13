from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARK = "NZ_POSTURE_2026_09_13"


def patch(path, replacements, inserts=()):
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    for old, new, label in replacements:
        if new in text:
            continue
        n = text.count(old)
        if n != 1:
            raise SystemExit(f"{path} {label}: expected 1 match, got {n}")
        text = text.replace(old, new, 1)
    for anchor, block, label in inserts:
        if MARK in text:
            break
        n = text.count(anchor)
        if n != 1:
            raise SystemExit(f"{path} {label}: expected 1 anchor, got {n}")
        text = text.replace(anchor, block + anchor, 1)
    p.write_text(text, encoding="utf-8")


patch("index.html", [
    (
        "National New Zealand property intelligence from authoritative Toitū Te Whenua LINZ data: 3.04M primary parcels, 2.42M addresses, 2.45M titles, 3.27M building outlines, 3.82M building-parcel relationships and 342,695 parcel statutory actions through one PropData API.",
        "National New Zealand property intelligence from authoritative Toitū Te Whenua LINZ data: national addresses, parcels, titles, buildings and statutory intelligence, plus completed restricted title-estate, ownership and memorial/legal-interest baselines behind one governed PropData graph.",
        "meta description",
    ),
    (
        "National LINZ addresses, parcels, titles, buildings, property relationships and 342,695 parcel statutory actions—connected through one source-aware PropData API.",
        "National LINZ addresses, parcels, titles, buildings and statutory intelligence, plus entitlement-gated title-estate, ownership and memorial/legal-interest infrastructure—connected through one source-aware PropData graph.",
        "og description",
    ),
    (
        "Authoritative New Zealand property identity, titles, cadastral geometry, buildings, relationships and statutory intelligence through PropData.",
        "Authoritative New Zealand property identity, titles, cadastral geometry, buildings, statutory intelligence and entitlement-gated ownership/legal-interest infrastructure through PropData.",
        "twitter description",
    ),
    ('"dateModified":"2026-09-04"', '"dateModified":"2026-09-13"', "date modified"),
    (
        "Personal-data datasets remain separately entitlement-gated where LINZ requires it.",
        "Restricted title ownership and memorial datasets are loaded as internal PropData infrastructure but remain separately entitlement-gated and are not represented as default self-serve access where LINZ personal-data rights apply.",
        "source rights",
    ),
    (
        "Restricted personal-data layers remain separately entitlement-controlled.",
        "Restricted title ownership and memorial/legal-interest layers are loaded nationally but remain separately entitlement-controlled and outside default self-serve access.",
        "pricing rights",
    ),
], [
    (
        '    <section class="section demo-section" id="demo">',
        '''    <!-- NZ_POSTURE_2026_09_13 -->
    <section class="section data-section" id="restricted-title-graph" data-posture="NZ_POSTURE_2026_09_13">
      <div class="wrap"><div class="section-head centered" data-reveal><div class="kicker">RESTRICTED TITLE GRAPH · NATIONAL BASELINES COMPLETE</div><h2 data-en="The deeper legal-title graph is built." data-mi="Kua hangaia te whatunga taitara ture hōhonu.">The deeper legal-title graph is built.</h2><p>Behind the customer-safe property surface, PropData maintains national LINZ title-estate, ownership and memorial/legal-interest layers as restricted infrastructure. These datasets are not default self-serve output and remain separately entitlement-controlled where LINZ personal-data rights apply.</p></div><div class="data-cards" data-reveal><article><span>TE</span><h3>2.81M title estates</h3><p>National restricted title → estate baseline complete.</p></article><article><span>OW</span><h3>5.73M ownership records</h3><p>National restricted estate → ownership baseline complete. Counts describe source records, not unique people or organisations.</p></article><article><span>MI</span><h3>32.86M+ title memorials</h3><p>National memorial/legal-interest baseline complete with source identifiers preserved.</p></article><article><span>AT</span><h3>1,784,819 structured memorial details</h3><p>National structured-detail baseline complete; the incremental changeset path is live and production-verified.</p></article></div></div>
    </section>

''',
        "restricted section",
    )
])

patch("docs/index.html", [
    (
        "PropData New Zealand API Docs | Property, Titles, Buildings & Statutory Intelligence",
        "PropData New Zealand API Docs | Property, Titles, Ownership, Legal Interests & Buildings",
        "title",
    ),
    (
        "Production documentation for PropData New Zealand: 3.04M primary parcels, 2.42M addresses, 2.45M titles, 3.27M building outlines, 3.82M building-parcel relationships and 342,695 LINZ parcel statutory actions.",
        "Production documentation for PropData New Zealand: national address, parcel, title, building and statutory layers plus completed restricted title-estate, ownership and memorial/legal-interest baselines.",
        "meta",
    ),
    (
        "Named ownership is a separate entitlement problem.</strong> Title metadata and <code>number_owners</code> do not authorize inference of named owner identity. LINZ Personal Data Licence-gated datasets, including the Title Memorial List, remain separately controlled.",
        "Named ownership remains a separate entitlement problem.</strong> PropData maintains the national title-estate and ownership baselines internally, but title metadata and <code>number_owners</code> still do not authorize inference of named owner identity. LINZ Personal Data Licence-gated ownership and memorial datasets remain separately controlled and are not default self-serve output.",
        "ownership warning",
    ),
    (
        "Title Memorial List / personal data:</strong> restricted LINZ personal-data datasets remain separately entitlement-gated. PropData does not represent those layers as generally available unless the applicable LINZ licence and downstream controls are in place.",
        "Restricted title graph / personal data:</strong> national title-estate, ownership, memorial and structured memorial-detail baselines are complete. Those restricted LINZ datasets remain separately entitlement-gated and are not represented as generally available unless the applicable LINZ licence and downstream controls are in place.",
        "rights warning",
    ),
], [
    (
        '    <div class="proof"><b>342,695</b><span>Statutory actions</span></div>',
        '    <div class="proof" data-posture="NZ_POSTURE_2026_09_13"><b>2.81M</b><span>Restricted title estates</span></div>\n    <div class="proof"><b>5.73M</b><span>Restricted ownership records</span></div>\n    <div class="proof"><b>32.86M+</b><span>Restricted title memorials</span></div>\n    <div class="proof"><b>1,784,819</b><span>Structured memorial details</span></div>\n',
        "proof strip",
    )
])

patch("workspace.html", [
    (
        "Resolve property identity, inspect the production graph, test country-aware requests and hand a verified contract directly to engineering.",
        "Resolve property identity, inspect the production graph, test country-aware requests and see the full national posture—including restricted title ownership and memorial infrastructure without confusing entitlement-gated layers with default public API access.",
        "overview",
    ),
    (
        "Addresses resolve into parcels. Parcels connect to titles, cadastral geometry, buildings and legal/statutory context. Every layer keeps its own source and coverage state underneath one country-aware PropData contract.",
        "Addresses resolve into parcels. Parcels connect to titles, cadastral geometry, buildings and legal/statutory context. Behind that customer-safe surface, the national title-estate, ownership and memorial layers are also loaded as restricted infrastructure. Every layer keeps its own source, coverage and entitlement state underneath one country-aware PropData contract.",
        "hero",
    ),
    (
        "Title Memorial List / 51695:</strong> not represented as generally available. LINZ Personal Data Licence approval and downstream controls remain a separate entitlement gate.",
        "Restricted title graph:</strong> national baselines are complete for title estates (2.81M), ownership records (5.73M), title memorials (32.86M+ baseline records) and structured memorial details (1,784,819). These layers are loaded as PropData infrastructure but remain separately entitlement-gated; they are not default self-serve access.",
        "restricted card",
    ),
], [
    (
        '<div class="stat gold"><span>Statutory actions</span><b>342,695</b><small>Hourly bounded changeset refresh</small></div></div>',
        '<div class="stat navy" data-posture="NZ_POSTURE_2026_09_13"><span>Title estates</span><b>2.81M</b><small>Restricted national baseline complete</small></div><div class="stat navy"><span>Ownership records</span><b>5.73M</b><small>Restricted national baseline complete</small></div><div class="stat navy"><span>Title memorials</span><b>32.86M+</b><small>Restricted legal-interest baseline complete</small></div><div class="stat navy"><span>Memorial details</span><b>1,784,819</b><small>Restricted · incremental path live</small></div>',
        "stats",
    )
])

patch("platform.html", [
    (
        "PropData New Zealand | National Parcel, Title, Building & Statutory Intelligence",
        "PropData New Zealand | National Property, Title, Ownership & Legal-Interest Graph",
        "title",
    ),
    (
        "3.04M parcels. 2.45M titles. 3.27M buildings. 342,695 statutory actions. One governed New Zealand property graph.",
        "3.04M parcels. 2.45M titles. 5.73M restricted ownership records. 32.86M+ memorials. One governed New Zealand property graph.",
        "twitter",
    ),
], [
    (
        '<div class="proofline"><span>✓ National parcel baseline</span><span>✓ National title graph</span><span>✓ National building outlines</span><span>✓ Statutory intelligence</span><span>✓ REST · MCP · Bulk</span></div>',
        '<div class="proofline" data-posture="NZ_POSTURE_2026_09_13"><span>✓ Restricted ownership + memorial graph loaded</span></div>',
        "proofline",
    )
])

sitemap = ROOT / "sitemap.xml"
if sitemap.exists():
    text = sitemap.read_text(encoding="utf-8").replace("<lastmod>2026-09-04</lastmod>", "<lastmod>2026-09-13</lastmod>")
    sitemap.write_text(text, encoding="utf-8")

print("PASS: NZ current posture promoted to static country-site sources")
