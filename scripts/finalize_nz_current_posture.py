from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def apply(path, replacements):
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    for old, new, label in replacements:
        if new in text:
            continue
        n = text.count(old)
        if n < 1:
            raise SystemExit(f"{path} {label}: expected at least 1 match, got {n}")
        text = text.replace(old, new)
    p.write_text(text, encoding="utf-8")


apply("index.html", [
    (
        "<title>New Zealand Property Intelligence API | PropData New Zealand</title>",
        "<title>New Zealand Property Intelligence | National Property & Legal-Title Graph | PropData</title>",
        "title",
    ),
    (
        '"description":"A source-aware New Zealand property intelligence API connecting authoritative addresses, 3.04M primary parcels, 2.45M property titles, title-to-parcel relationships, coordinates, 3,268,141 national LINZ building outlines, 3,820,845 building-parcel relationships and 342,695 parcel statutory actions."',
        '"description":"A source-aware New Zealand property intelligence graph connecting authoritative addresses, parcels, titles, buildings and statutory actions, with completed restricted national title-estate, ownership and memorial/legal-interest layers maintained behind separate entitlements."',
        "jsonld product",
    ),
    (
        "Authoritative source data. Structured identity. Titles. Geometry. Buildings. Relationships. Statutory intelligence. Explicit provenance. One API.",
        "Authoritative source data. Structured identity. Titles. Estates. Restricted ownership and legal interests. Geometry. Buildings. Relationships. Statutory intelligence. Explicit provenance. One governed platform.",
        "final posture",
    ),
])

apply("docs/index.html", [
    ('"dateModified":"2026-09-04"', '"dateModified":"2026-09-13"', "date modified"),
    (
        "One production contract for New Zealand property identity, parcels, titles, buildings, relationships and statutory intelligence.",
        "One production contract for New Zealand property identity, parcels, titles, buildings and statutory intelligence, backed by separately entitlement-gated ownership and legal-interest infrastructure.",
        "og description",
    ),
    (
        "Authoritative address resolution, primary parcels, cadastral geometry, property titles, title↔parcel relationships, building footprints, building↔parcel relationships and parcel statutory intelligence—delivered through the PropData global API with New Zealand-native identifiers and provenance intact.",
        "Authoritative address resolution, parcels, titles, buildings and statutory intelligence are delivered through the customer-safe PropData API. Behind that surface, national title-estate, ownership and memorial/legal-interest baselines are complete as separately entitlement-gated infrastructure.",
        "hero posture",
    ),
    (
        "<div class=\"doc-kicker\">Production country graph</div><h2>Seven national layers, one property identity.</h2>\n        <p>The backend is deliberately richer than a single endpoint table. These are production graph capabilities currently loaded for New Zealand; direct REST exposure remains governed by the public contract above.</p>",
        "<div class=\"doc-kicker\">Production country graph</div><h2>Eleven infrastructure layers, one governed property identity.</h2>\n        <p>Seven customer-safe national layers drive the normal product contract. Four deeper title/legal layers are also loaded nationally as restricted infrastructure and remain separately entitlement-controlled rather than being implied as default REST output.</p>",
        "graph heading",
    ),
    (
        '<article class="layer-card"><span class="layer-no">07</span><h3>Parcel statutory actions</h3><p>Current and historic LINZ/Landonline parcel actions normalized into legal/statutory intelligence.</p><strong>342,695</strong><small>baseline complete · automated refresh</small></article>',
        '<article class="layer-card"><span class="layer-no">07</span><h3>Parcel statutory actions</h3><p>Current and historic LINZ/Landonline parcel actions normalized into legal/statutory intelligence.</p><strong>342,695</strong><small>baseline complete · automated refresh</small></article>\n          <article class="layer-card" data-posture="NZ_POSTURE_2026_09_13"><span class="layer-no">08 · RESTRICTED</span><h3>Title estates</h3><p>National title → estate graph maintained behind entitlement controls.</p><strong>2.81M</strong><small>restricted baseline complete</small></article>\n          <article class="layer-card"><span class="layer-no">09 · RESTRICTED</span><h3>Ownership records</h3><p>Estate-linked ownership source records. Counts are not unique people or organisations.</p><strong>5.73M</strong><small>restricted baseline complete</small></article>\n          <article class="layer-card"><span class="layer-no">10 · RESTRICTED</span><h3>Title memorials</h3><p>National memorial/legal-interest graph with source identity preserved.</p><strong>32.86M+</strong><small>restricted baseline complete</small></article>\n          <article class="layer-card"><span class="layer-no">11 · RESTRICTED</span><h3>Structured memorial details</h3><p>Structured legal-interest detail linked back to memorial identity.</p><strong>1,784,819</strong><small>restricted baseline · incremental path live</small></article>',
        "restricted layer cards",
    ),
])

apply("workspace.html", [
    (
        "ADDRESS → PARCEL → TITLES → BUILDINGS → STATUTORY INTELLIGENCE",
        "ADDRESS → PARCEL → TITLES → ESTATES → RESTRICTED OWNERSHIP / LEGAL INTERESTS → BUILDINGS → STATUTORY INTELLIGENCE",
        "hero path",
    ),
    (
        "<strong>New Zealand property graph</strong><span>7 production layers</span>",
        "<strong>New Zealand property graph</strong><span>11 infrastructure layers · 7 customer-safe + 4 restricted</span>",
        "layer count",
    ),
    (
        '<div class="layer"><div class="layer-icon">SA</div><div><b>Parcel statutory actions</b><small>Current + historic legal/statutory context</small></div><div class="layer-count">342,695</div></div></div>',
        '<div class="layer"><div class="layer-icon">SA</div><div><b>Parcel statutory actions</b><small>Current + historic legal/statutory context</small></div><div class="layer-count">342,695</div></div><div class="layer" data-posture="NZ_POSTURE_2026_09_13"><div class="layer-icon">TE</div><div><b>Title estates</b><small>Restricted title → estate graph</small></div><div class="layer-count">2.81M</div></div><div class="layer"><div class="layer-icon">OW</div><div><b>Ownership records</b><small>Restricted estate → ownership graph</small></div><div class="layer-count">5.73M</div></div><div class="layer"><div class="layer-icon">MI</div><div><b>Title memorials</b><small>Restricted memorial / legal-interest graph</small></div><div class="layer-count">32.86M+</div></div><div class="layer"><div class="layer-icon">AT</div><div><b>Memorial details</b><small>Restricted structured legal-interest details</small></div><div class="layer-count">1.78M</div></div></div>',
        "layer rows",
    ),
    (
        '<article class="coverage-card"><span>SPATIAL RESOLUTION</span><b>Coordinate-aware</b>',
        '<article class="coverage-card" data-posture="NZ_POSTURE_2026_09_13"><span>RESTRICTED TITLE GRAPH</span><b>2.81M estates · 5.73M ownership · 32.86M+ memorials</b><p>National restricted legal-title layers are loaded and governed separately from the customer-safe self-serve contract.</p></article><article class="coverage-card"><span>SPATIAL RESOLUTION</span><b>Coordinate-aware</b>',
        "coverage card",
    ),
])

apply("platform.html", [
    (
        "New Zealand property intelligence built on authoritative LINZ data: 3.04M primary parcels, 2.42M addresses, 2.45M titles, 2.99M title-parcel links, 3.27M building outlines, 3.82M building-parcel relationships and 342,695 parcel statutory actions through one source-aware property graph.",
        "New Zealand property intelligence built on authoritative LINZ data: national address, parcel, title, building and statutory layers plus completed restricted title-estate, ownership and memorial/legal-interest baselines through one governed property graph.",
        "meta description",
    ),
    (
        "Addresses, parcels, titles, buildings, relationships and statutory intelligence — connected through one authoritative New Zealand property layer.",
        "Addresses, parcels, titles, buildings and statutory intelligence, plus entitlement-gated title ownership and memorial/legal-interest infrastructure — connected through one governed New Zealand property graph.",
        "og description",
    ),
    (
        '"description":"National New Zealand property intelligence spanning authoritative addresses, primary parcels, parcel geometry, property titles, title-parcel relationships, building outlines, building-parcel relationships and parcel statutory actions."',
        '"description":"National New Zealand property intelligence spanning addresses, parcels, titles, buildings and statutory actions, with restricted title-estate, ownership and memorial/legal-interest layers maintained behind separate entitlements."',
        "jsonld description",
    ),
    (
        '<div class="proofline" data-posture="NZ_POSTURE_2026_09_13"><span>✓ Restricted ownership + memorial graph loaded</span></div><div class="proofline"><span>✓ National parcel baseline</span><span>✓ National title graph</span><span>✓ National building outlines</span><span>✓ Statutory intelligence</span><span>✓ REST · MCP · Bulk</span></div>',
        '<div class="proofline" data-posture="NZ_POSTURE_2026_09_13"><span>✓ National parcel baseline</span><span>✓ National title graph</span><span>✓ Restricted ownership + memorial graph loaded</span><span>✓ National building outlines</span><span>✓ Statutory intelligence</span><span>✓ REST · MCP · Bulk</span></div>',
        "proofline",
    ),
    (
        '<article class="cap"><span>08 · LEGAL CONTEXT</span><h3>Parcel statutory intelligence</h3><p>342,695 current and historic LINZ/Landonline parcel actions normalized into bounded property context.</p></article>',
        '<article class="cap"><span>08 · LEGAL CONTEXT</span><h3>Parcel statutory intelligence</h3><p>342,695 current and historic LINZ/Landonline parcel actions normalized into bounded property context.</p></article><article class="cap" data-posture="NZ_POSTURE_2026_09_13"><span>09 · TITLE ESTATES</span><h3>National title → estate graph</h3><p>2.81M restricted title-estate records loaded nationally.</p></article><article class="cap"><span>10 · RESTRICTED OWNERSHIP</span><h3>Estate → ownership graph</h3><p>5.73M restricted ownership records maintained behind separate entitlement controls.</p></article><article class="cap"><span>11 · MEMORIALS</span><h3>Legal-interest infrastructure</h3><p>32.86M+ memorial records plus 1,784,819 structured memorial-detail rows loaded nationally as restricted infrastructure.</p></article>',
        "capabilities",
    ),
    (
        '<div class="graph-row"><span>03</span><div><b>Parcel → property titles</b><small>Connect legal title context through explicit LINZ associations.</small></div><span>2.99M LINKS</span></div>',
        '<div class="graph-row"><span>03</span><div><b>Parcel → property titles</b><small>Connect legal title context through explicit LINZ associations.</small></div><span>2.99M LINKS</span></div><div class="graph-row"><span>03A</span><div><b>Title → estate → restricted ownership</b><small>Maintain the national legal-title ownership graph behind entitlement controls.</small></div><span>2.81M / 5.73M</span></div><div class="graph-row"><span>03B</span><div><b>Title → memorials / legal interests</b><small>Preserve national memorial context without treating restricted data as default self-serve output.</small></div><span>32.86M+ / 1.78M</span></div>',
        "graph rows",
    ),
    (
        "Production access with direct Stripe checkout and enterprise paths for licensing, embedded infrastructure and multi-country delivery.",
        "Production access with direct Stripe checkout and enterprise paths for licensing, embedded infrastructure and multi-country delivery. Self-serve plans cover the customer-safe product surface; restricted ownership and memorial/legal-interest layers require separate entitlement.",
        "pricing boundary",
    ),
])

print("PASS: NZ posture finalized across public, docs, workspace and platform surfaces")
