# 🇳🇿 PropData New Zealand

### New Zealand property intelligence. One API. National coverage.

**PropData New Zealand** is the New Zealand commercial property-intelligence surface of the broader PropData platform.

The product normalizes authoritative New Zealand address, parcel, title, title↔parcel and geospatial source data into a governed developer contract built for PropTech, GIS, AI, underwriting, due diligence and property-data applications.

**Production domain:** `https://nz.proptechusa.ai`

## National property graph

Current audited PropData New Zealand infrastructure includes:

| Layer | Current status |
|---|---:|
| LINZ primary parcels | **3,040,571 · national baseline complete** |
| Authoritative addresses | **2,424,415 · national baseline complete** |
| Property titles | **2,450,998 · national baseline complete** |
| Title ↔ parcel associations | **2,988,279 · national baseline complete** |
| LINZ building outlines | **3,268,141 national target · baseline actively loading** |

The building-outline layer preserves source geometry plus capture metadata such as capture method, capture-source name/group, source date ranges, last-modified context and LINZ provenance where published.

## Property model

PropData New Zealand is designed around the property graph underneath an address:

```text
ADDRESS
   ↓
PROPERTY IDENTITY
   ↓
PRIMARY PARCEL
   ↓
PARCEL GEOMETRY
   ↓
PROPERTY TITLES
   ↓
TITLE ↔ PARCEL RELATIONSHIPS
   ↓
BUILDING OUTLINES
   ↓
DERIVED PROPERTY INTELLIGENCE
   ↓
NORMALIZED API RESPONSE
```

The goal is not to provide another address autocomplete service. The goal is to give software a structured, source-aware representation of New Zealand real property.

## Verified property example

A live normalized example used throughout the site and docs:

**Address:** `221/66 Mabey Road, Avalon, Lower Hutt`

**Authoritative address ID:** `2064090`

**Coordinates:** `-41.1886269490596, 174.943031500008`

**Primary parcel:** `3818618`

**Appellation:** `Lot 1 DP 90132`

**Land district:** `Wellington`

**Calculated parcel area:** `35,805 m²`

The parcel is linked to multiple current title records in the LINZ title graph, including unit titles such as `1006231`, `1007115`, and `1011310`.

## Core developer workflows

```http
GET /v1/property?country=NZ&address=221%2F66%20Mabey%20Road%2C%20Avalon%2C%20Lower%20Hutt
```

```http
GET /v1/property?country=NZ&parcel=3818618
```

```http
GET /v1/property/by-location?country=NZ&lat=-41.1886269490596&lng=174.943031500008
```

The broader production surface also includes `/v1/countries`, `/v1/health`, `/v1/stats`, and `/v1/changelog`.

## Source-aware by design

PropData preserves source-native identifiers, match semantics, coverage state, geometry availability and provenance rather than manufacturing missing property facts.

**If the source does not verify a fact, PropData does not pretend it does.**

Primary New Zealand layers are sourced from **Toitū Te Whenua Land Information New Zealand (LINZ)** and other official/public sources as additional enrichment is promoted.

PropData is an independent product of **PropTechUSA.ai** and is not operated by or affiliated with the New Zealand government or LINZ.

## Commercial delivery

The New Zealand product is being packaged for:

- REST API
- PropData MCP workflows
- RapidAPI distribution
- bulk/data licensing
- custom endpoints and response contracts
- white-label integrations
- embedded property infrastructure
- enterprise and multi-country delivery

Direct commercial pricing is NZD-first, with USD reference pricing for international buyers.

## PropData network

- New Zealand: `https://nz.proptechusa.ai`
- Estonia: `https://ee.proptechusa.ai`
- PropData: `https://propdata.proptechusa.ai`
- Global coverage: `https://global.proptechusa.ai`
- Data solutions: `https://data.proptechusa.ai`
- PropTechUSA.ai: `https://proptechusa.ai`
- Sales: `sales@proptechusa.ai`

---

## Build the product. We'll handle the property infrastructure.

**Authoritative source data. Structured property identity. Titles. Geometry. Buildings. Explicit provenance. One API.**