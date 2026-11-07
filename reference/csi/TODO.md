# Manufacturer detail index: to-do

Last reviewed: 2026-11-07 (after PR #2 merged to `main`). Counts below come from the division files, not from memory. Regenerate them with the script in "Checking the counts" if you edit the JSON.

Goal: fill the index with download pages for the spec sections used most often. One JSON file per division (`reference/csi/NN-name.json`), listed in `manifest.json`.

## Rules for adding entries

1. Link to a **download page** or a direct file (PDF, DWG, DXF). Not a manufacturer home page.
2. **Prefer PDF.** The user's preference. Add DWG too when the page offers it.
3. **No new ARCAT links.** Existing ARCAT entries stay until the user asks for removal.
4. Open the page before adding it, and check the detail matches the section. Search results alone are a lead, not a verification.
5. Add `csi`, `title`, `maker`, `format`, `url` and `note`. Put a revision date in `note` if the page shows one. Flag licence walls (ARCAT, Sweets, accounts), regional sites (Sika Ireland/UK, Hilti Canada) and third-party aggregators in `note`.
6. Not found? Record it in `reference/research/leads.json` with status `not_found`, not as an invented link.
7. Links only. No manufacturer drawings or images are copied into the repo. Manufacturer JPGs are rare and cannot be stored in `images/raw/` unless the owner releases them under CC BY, CC BY-SA or public domain.

## Status key

- `[ ]` not started
- `[~]` some entries added, gaps remain
- `[x]` section complete

## Division status (current counts)

| Div | Title | Entries | ARCAT | Status | Still to do |
|---|---|---|---|---|---|
| 03 | Concrete | 8 | 0 | [~] | Precast (Oldcastle, Smith-Midland, Coreslab) not found; Euclid specs |
| 04 | Masonry | 4 | 0 | [~] | Ties and accessories, mortar, multi-wythe |
| 05 | Metals | 2 | 0 | [~] | Structural connections, metal stairs, railings (Blumcraft not found), anchors |
| 06 | Wood, Plastics and Composites | 16 | 0 | [~] | Millwork and woodwork (AWI), composite decking connection details, Accoya |
| 07 | Thermal and Moisture Protection | 45 | 13 | [~] | Insulation (OC/JM partly), weather barriers, vapor retarders, metal panels, sealants, 3M/Tremco firestop |
| 08 | Openings | 21 | 5 | [~] | Pella (not found), wood doors, storefronts, hardware (Schlage/Hager not found), glazing |
| 09 | Finishes | 17 | 2 | [~] | USG and CertainTeed ceilings, tile (Laticrete, Mapei), flooring, paint, carpet |
| 10 | Specialties | 3 | 0 | [~] | Toilet partitions, accessories, wall protection, canopies |
| 11 | Equipment | 0 | 0 | [ ] | Loading dock (Rite-Hite, Serco), residential appliances |
| 12 | Furnishings | 0 | 0 | [ ] | Countertops (Wilsonart lead; Corian and Formica sites listed), window shades, site furnishings |
| 13 | Special Construction | 0 | 0 | [ ] | Pools, fabricated structures |
| 14 | Conveying Equipment | 0 | 0 | [ ] | Elevators: planning portals only so far (Otis, KONE, Schindler) |
| 21 | Fire Suppression | 2 | 0 | [~] | Sprinkler penetrations (Viking: contact only), Tyco |
| 22 | Plumbing | 2 | 0 | [~] | Floor and trench drains (Zurn not found), fixtures, water piping |
| 23 | HVAC | 1 | 0 | [~] | Ductwork, fans, air outlets (Greenheck and Price not found), unitary AC |
| 26 | Electrical | 2 | 0 | [~] | Panelboards, lighting, raceways beyond Hubbell and Legrand |
| 28 | Electronic Safety and Security | 0 | 0 | [ ] | Fire detection (Notifier, Honeywell, Simplex) |
| 31 | Earthwork | 0 | 0 | [ ] | Geosynthetics (Mirafi entries are filed under 32 for now) |
| 32 | Exterior Improvements | 7 | 3 | [~] | Asphalt and concrete paving, retaining walls (more PDFs), site drainage |
| 33 | Utilities | 0 | 0 | [ ] | Storm drainage (ADS lead, not confirmed) |

## Open items by section

### 03 Concrete
- [ ] 03 30 00 Admixtures and sealers (Sika, Euclid, BASF, Fosroc). Euclid guide is a lead only
- [ ] 03 35 00 Finishing and sealing
- [ ] 03 41 00 Precast structural (Oldcastle, Smith-Midland, Coreslab). Not found; FHWA and Molin added
- [ ] 03 45 00 Precast architectural. CPCI added

### 04 Masonry
- [~] 04 20 00 Flashing details (Canada Brick added)
- [ ] 04 20 00 Brick ties and accessories (Hohmann & Barnard / Dur-O-Wal, Fero)
- [ ] 04 22 00 Concrete unit masonry. NCMA TEK originals to check at ncma.org; Scribd copies are not reliable
- [ ] 04 27 00 Multiple-wythe (Endicott, Glen-Gery)
- [ ] 04 05 13 Mortaring and grouting (Quikrete, Lafarge)

### 05 Metals
- [ ] 05 12 00 Structural steel connections
- [~] 05 31 00 Steel deck: Vulcraft 2026 LRFD catalogue (product catalogue, not detail set)
- [ ] 05 05 23 Anchors and fastenings (Simpson US library, Hilti)
- [ ] 05 40 00 Cold-formed framing (see 09 22 16)
- [ ] 05 51 00 Metal stairs. Wagner is a lead on CADdetails
- [ ] 05 52 00 Railings. Blumcraft not found

### 06 Wood, Plastics and Composites
- [~] 06 16 00 Sheathing (APA)
- [~] 06 11 00 Wood framing (APA R20/R21 walls and headers)
- [~] 06 17 00 Trusses and joists: TJI evaluation report, Boise BCI and AJS data. Weyerhaeuser own PDFs not found
- [ ] 06 22 00 Millwork (AWI references)
- [ ] 06 40 00 Architectural woodwork
- [~] 06 05 23 Connectors (Simpson Australia; US library still to open)
- [~] 06 18 00 Glulam and mass timber: APA glulam page and WoodWorks index added
- [~] 06 63 00 Composite decking: TimberTech and Trex specs and AZEK guide added. Structural details not found in PDFs

### 07 Thermal and Moisture Protection
- [~] 07 21 00 Insulation: OC foundation, JM BID 340 added. Board and batt still to do
- [ ] 07 25 00 Weather barriers (DuPont Tyvek, Henry, Prosoco)
- [ ] 07 26 00 Vapor retarders (Stego, Fortifiber)
- [ ] 07 41 00 Metal roof panels (Centria, Metl-Span, Firestone Metal)
- [~] 07 42 13 Composite panels: 3A Composites (ARCAT pages; ARCAT, avoid further)
- [~] 07 46 00 Siding: Hardie (ARCAT), Nichiha design review guide added. LP not searched
- [~] 07 50 00 / 07 52 00 / 07 54 00 Roofing membranes: Sika, GAF, Carlisle, EcoStar, Eagle, Englert, BMI added. Carlisle and Firestone need more PDFs
- [~] 07 60 00 Flashing: GAF scupper and Canada Brick added
- [~] 07 84 00 Firestop: Hilti (Canada and US) and STI added. 3M and Tremco not found
- [~] 07 10 00 Waterproofing: Tremco below-grade details, Carlisle composite (ARCAT)
- [~] 07 14 00 Fluid-applied: Sikalastic 320 catalogue added
- [~] 07 95 00 Expansion joints: Sika PMR and Emseal added
- [~] 07 31 00 Shingles: CertainTeed construction details added. GAF and Owens Corning not found
- [ ] 07 62 00 Sheet metal flashing (Berger, Metal-Era)
- [ ] 07 71 00 Roof specialties (Centria, Metal Sales)
- [ ] 07 72 00 Roof accessories (Bilco, Babcock-Davis)
- [ ] 07 92 00 Joint sealants (Tremco, Sika, Dow, Pecora, BASF)
- [~] 07 62 00 Base flashing on gypsum wall (Malarkey, ARCAT)

### 08 Openings
- [~] 08 11 00 Metal doors and frames: SDI drawings added. Steelcraft not found
- [ ] 08 14 00 Wood doors (Masonite, JELD-WEN)
- [~] 08 42 00 Entrances: ASSA ABLOY on ARCAT
- [~] 08 44 00 Curtain walls: Kawneer KCAD indexes, YKK AP, Tubelite, Riot Glass. Oldcastle and EFCO not searched
- [ ] 08 41 00 Storefronts (Kawneer, YKK AP, EFCO, Oldcastle)
- [~] 08 50 00 / 08 51 00 / 08 52 00 Windows: Marvin, Andersen (dealer). Pella not found
- [~] 08 62 00 Skylights: VELUX pages added. Kalwall and Major not searched
- [ ] 08 71 00 Hardware: Schlage, Hager not found. ASSA ABLOY locks not found
- [ ] 08 80 00 Glazing (Viracon, Guardian, PPG, Vitro)

### 09 Finishes
- [~] 09 21 16 Gypsum: Sweets hub, USG Design Studio UL U419. CertainTeed BIM library is a lead
- [~] 09 22 16 Metal stud framing: ClarkDietrich Pilot Trak PDFs and framing library
- [~] 09 30 00 Tile: Schluter ARCAT listings (ARCAT). Laticrete and Mapei not searched
- [~] 09 51 00 Ceilings: Armstrong packages, Rockfon tech notes and CDX guide. USG and CertainTeed ceilings still to do
- [ ] 09 65 00 Resilient flooring (Armstrong, Mannington, Tarkett)
- [ ] 09 68 00 Carpet (Mohawk, Interface, Shaw)
- [ ] 09 91 00 Painting (Sherwin-Williams, Benjamin Moore, PPG)

### 10 Specialties
- [~] 10 14 00 Signage: 290signs and Intersign added, RIT standard. ASI drawings restricted
- [ ] 10 21 00 Toilet compartments (Bobrick, Scranton)
- [ ] 10 26 00 Wall protection (Inpro, Construction Specialties)
- [ ] 10 28 00 Toilet accessories (Bobrick, Bradley)
- [ ] 10 73 00 Canopies (Walker, Hunter Douglas)

### 11–14, 28, 31, 33 (no entries yet)
- [ ] 11 13 00 Loading docks (Rite-Hite, Serco); 11 31 00 Residential appliances
- [ ] 12 36 00 Countertops (Wilsonart lead); 12 24 00 Shades (Hunter Douglas, MechoShade); 12 93 00 Site furnishings
- [ ] 13 11 00 Pools (Pentair, Hayward); 13 34 00 Fabricated structures
- [ ] 14 21 00 Traction elevators; 14 24 00 Hydraulic (Otis, KONE, Schindler: planning portals only)
- [ ] 28 31 00 Fire detection (Notifier, Honeywell, Simplex)
- [ ] 31 32 19 Geosynthetics (Mirafi brochures are filed under 32 for now)
- [ ] 33 41 00 Storm drainage (ADS lead; not confirmed)

### 21, 22, 23, 26
- [~] 21 13 13 Victaulic instructions. Viking: contact only
- [~] 22 13 19 Jay R. Smith drain CAD page. Zurn and Sloan not found
- [~] 23 37 13 Titus grilles (third-party host aggregator). Greenheck and Price not found
- [~] 26 05 33 Hubbell CFB10NEMA spec and Legrand EFB template

### 32 Exterior Improvements
- [~] 32 14 00 Unilock DuraMat and ADA pavers (ARCAT). Belgard via LADetails only
- [~] 32 32 00 Retaining walls: Mirafi brochures, FDOT temporary wall standard. Allan Block and Keystone not searched
- [ ] 32 12 16 Asphalt paving; 32 13 13 Concrete paving (Oldcastle, Smith-Midland)

## Checking the counts

```
python3 - <<'PY'
import json
man = json.load(open('reference/csi/manifest.json'))
for f in man['files']:
    d = json.load(open('reference/csi/' + f))
    print(d['division'], len(d['entries']))
PY
```

## Notes

- 4specs has not been reachable from the build sandbox. If you can reach it, its CSI-indexed detail pages should go into the matching division file.
- The reference page's research section (`reference/research/leads.json`) holds leads and not-found items. Check it before searching a manufacturer again.
