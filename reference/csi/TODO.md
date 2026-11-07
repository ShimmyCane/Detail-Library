# Manufacturer detail index: to-do

Goal: fill the index with download pages for the spec sections used most often, one JSON file per division (`reference/csi/NN-name.json`, listed in `manifest.json`).

## How to add an entry

1. Find the manufacturer's **download page** (a detail, typical-detail or CAD library page, or a direct PDF/DWG). Not a home page.
2. Check the page loads and the detail matches the section.
3. Add it to the division file with `csi`, `title`, `maker`, `format`, `url` and `note`. Put the revision date in `note` if the page shows one.
4. Tick it off below.

Rules: links only, no copies of manufacturer drawings in the repo. Public-domain, CC BY and CC BY-SA material goes in `images/raw/` with a licence record instead.

Candidate manufacturers are from memory and are **unverified**. Search each one before adding it.

## Status key

- `[ ]` not started
- `[~]` some entries added
- `[x]` section complete

## Division status

| Div | Title | Status |
|---|---|---|
| 04 | Masonry | [~] one entry |
| 06 | Wood, Plastics and Composites | [~] APA and Simpson |
| 07 | Thermal and Moisture Protection | [~] roofing and waterproofing only |
| 08 | Openings | [~] Andersen and Kawneer curtain wall |
| 03 | Concrete | [ ] |
| 05 | Metals | [ ] |
| 09 | Finishes | [~] Armstrong ceilings and Sweets hub |
| 10 | Specialties | [ ] |
| 11 | Equipment | [ ] |
| 12 | Furnishings | [ ] |
| 13 | Special Construction | [ ] |
| 14 | Conveying Equipment | [ ] |
| 21 | Fire Suppression | [ ] |
| 22 | Plumbing | [ ] |
| 23 | HVAC | [ ] |
| 26 | Electrical | [ ] |
| 28 | Electronic Safety and Security | [ ] |
| 32 | Exterior Improvements | [ ] |

## Frequently used sections, by division

### 03 Concrete
- [ ] 03 30 00 Cast-in-place concrete: admixtures, curing, sealers (Sika, Euclid/RPM, BASF, Fosroc)
- [ ] 03 35 00 Concrete finishing and sealing (Sika, Euclid, Super-Krete)
- [ ] 03 41 00 Precast structural concrete (Oldcastle, Smith-Midland)
- [ ] 03 45 00 Precast architectural concrete (Oldcastle, Smith-Midland)
- [ ] 03 15 00 Concrete accessories: joints and anchors (Dayton Superior, Hilti, Simpson)

### 04 Masonry
- [~] 04 20 00 Unit masonry: flashing details (Canada Brick added)
- [ ] 04 20 00 Unit masonry: brick ties and accessories (Hohmann & Barnard / Dur-O-Wal, Fero)
- [ ] 04 22 00 Concrete unit masonry (Oldcastle, Ameristar)
- [ ] 04 27 00 Multiple-wythe masonry (Endicott, Glen-Gery)
- [ ] 04 05 13 Masonry mortaring and grouting (Quikrete, Lafarge)

### 05 Metals
- [ ] 05 12 00 Structural steel framing: connections (AISC references, Hilti)
- [ ] 05 31 00 Steel decking (Vulcraft, Nucor, Wheeling)
- [ ] 05 40 00 Cold-formed metal framing (ClarkDietrich, Marino\Ware, Simpson)
- [ ] 05 05 23 Metal fastenings and anchors (Simpson, Hilti)
- [ ] 05 51 00 Metal stairs (Wilson Metals, Ornamental Metal Institute references)
- [ ] 05 52 00 Railings (Wagner, Blumcraft)

### 06 Wood, Plastics and Composites
- [~] 06 16 00 Sheathing: APA wall sheathing added
- [~] 06 11 00 Wood framing: APA R20/R21 walls and headers added
- [ ] 06 17 00 Shop-fabricated wood trusses and joists (Trus Joist / Weyerhaeuser, Boise Cascade)
- [ ] 06 22 00 Millwork (AWI references, Woodworks)
- [ ] 06 40 00 Architectural woodwork (AWI references)
- [~] 06 05 23 Wood connectors and fastenings: Simpson added (Australia)
- [ ] 06 18 00 Glued-laminated construction (APA, Structurlam, Nordic)

### 07 Thermal and Moisture Protection
- [ ] 07 21 00 Thermal insulation: board and batt (Owens Corning, Johns Manville, Rockwool, Knauf)
- [ ] 07 25 00 Weather barriers (DuPont Tyvek, Henry, Prosoco)
- [ ] 07 26 00 Vapor retarders (Stego, Fortifiber)
- [ ] 07 41 00 Metal roof panels (Centria, Metl-Span, Firestone Metal)
- [ ] 07 42 00 Metal wall panels (Centria, Metl-Span, Kingspan)
- [ ] 07 46 00 Siding (James Hardie, LP, Nichiha)
- [~] 07 50 00 / 07 52 00 / 07 54 00 Roofing membranes: Sika, GAF, Carlisle, EcoStar, Eagle, Englert, BMI added; Carlisle and Firestone need more
- [~] 07 60 00 Flashing and sheet metal: GAF scupper and Canada Brick added
- [ ] 07 62 00 Sheet metal flashing and trim (Berger, Metal-Era)
- [ ] 07 71 00 Roof specialties: edge metal, copings (Centria, Metal Sales)
- [ ] 07 72 00 Roof accessories: hatches, curbs (Bilco, Babcock-Davis)
- [~] 07 84 00 Firestopping: Hilti added (3M, Specified Technologies still to do)
- [ ] 07 92 00 Joint sealants (Tremco, Sika, Dow, Pecora, BASF)
- [~] 07 10 00 Waterproofing: Tremco A-BSW-P-06 added
- [ ] 07 95 00 Expansion control (Watson Bowman, Emseal)

### 08 Openings
- [~] 08 50 00 Windows: Andersen via dealer added
- [ ] 08 51 00 Metal windows (Pella, Kawneer, Milgard, Marvin)
- [ ] 08 52 00 Wood and clad windows (Marvin, Andersen, Pella)
- [ ] 08 11 00 Metal doors and frames (Steelcraft, Ceco, Curries)
- [ ] 08 14 00 Wood doors (Masonite, JELD-WEN)
- [ ] 08 41 00 Storefronts (Kawneer, YKK AP, EFCO, Oldcastle)
- [~] 08 44 00 Curtain walls: Kawneer KCAD indexes added (YKK AP, Tubelite still to do)
- [ ] 08 71 00 Door hardware (Schlage, Assa Abloy, Hager)
- [ ] 08 80 00 Glazing (Viracon, Guardian, PPG, Vitro)

### 09 Finishes
- [~] 09 21 16 Gypsum board assemblies: Sweets CAD hub added (USG, CertainTeed, National Gypsum, Georgia-Pacific still to do)
- [ ] 09 22 16 Metal stud framing (ClarkDietrich, Marino\Ware)
- [ ] 09 30 00 Tile (Daltile, Mapei, Laticrete)
- [~] 09 51 00 Acoustical ceilings: Armstrong detail packages added (USG, Rockfon still to do)
- [ ] 09 65 00 Resilient flooring (Armstrong, Mannington, Tarkett)
- [ ] 09 68 00 Carpet (Mohawk, Interface, Shaw)
- [ ] 09 91 00 Painting (Sherwin-Williams, Benjamin Moore, PPG)

### 10 Specialties
- [ ] 10 14 00 Signage (ASI, Mohawk Signage)
- [ ] 10 21 00 Toilet compartments (Bobrick, Scranton Products)
- [ ] 10 26 00 Wall protection (Inpro, Construction Specialties)
- [ ] 10 28 00 Toilet accessories (Bobrick, Bradley)
- [ ] 10 73 00 Canopies and awnings (Walker, Hunter Douglas)

### 11 Equipment
- [ ] 11 13 00 Loading dock equipment (Rite-Hite, Serco)
- [ ] 11 31 00 Residential appliances (manufacturer installation guides)

### 12 Furnishings
- [ ] 12 24 00 Window shades (Hunter Douglas, MechoShade)
- [ ] 12 36 00 Countertops (Wilsonart, Formica, Corian)
- [ ] 12 93 00 Site furnishings (Landscape Forms, Dumor, Victor Stanley)

### 13 Special Construction
- [ ] 13 11 00 Swimming pools (Pentair, Hayward)
- [ ] 13 34 00 Fabricated engineered structures (Butler, Varco Pruden)

### 14 Conveying Equipment
- [ ] 14 21 00 Electric traction elevators (Otis, KONE, Schindler, Thyssenkrupp, Mitsubishi)
- [ ] 14 24 00 Hydraulic elevators (Otis, Thyssenkrupp)

### 21 Fire Suppression
- [ ] 21 13 13 Wet-pipe sprinklers (Victaulic, Viking, Tyco)

### 22 Plumbing
- [ ] 22 11 16 Domestic water piping (Uponor, NIBCO, Zurn PEX)
- [ ] 22 41 00 Residential plumbing fixtures (Kohler, American Standard, Toto)
- [ ] 22 42 00 Commercial plumbing fixtures (Zurn, Sloan, Bradley)

### 23 HVAC
- [ ] 23 31 00 Ductwork (SMACNA references, Greenheck)
- [ ] 23 34 00 HVAC fans (Greenheck, Loren Cook)
- [ ] 23 37 00 Air outlets and inlets (Titus, Price, Krueger)
- [ ] 23 81 00 Unitary air conditioning (Carrier, Trane, Daikin, Lennox)

### 26 Electrical
- [ ] 26 05 33 Raceways and boxes (Wiremold / Legrand, Hubbell)
- [ ] 26 24 16 Panelboards (Square D, Eaton, Siemens)
- [ ] 26 51 00 Interior lighting (Lithonia, Hubbell, Cooper)

### 28 Electronic Safety and Security
- [ ] 28 31 00 Fire detection and alarm (Notifier, Honeywell, Simplex)

### 32 Exterior Improvements
- [ ] 32 12 16 Asphalt paving (manufacturer references, Ergon)
- [ ] 32 13 13 Concrete paving (Oldcastle, Smith-Midland)
- [ ] 32 32 00 Retaining walls (Allan Block, Keystone)

## Notes

- Some divisions have few manufacturers that publish free details (e.g. 22, 23, 26). For those, a manufacturer's installation guide or a CAD library page is a fine entry.
- 4specs has not been reachable from the build sandbox. If you can reach it, its CSI-indexed detail pages should go into the matching division file.
