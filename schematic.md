Absolutely. Here's the **clean reference schematic** I would use going forward. No Streamlit, no PyMuPDF, and no unnecessary AI/vision complexity.

# Detail Library — MVP Schematic

> **Core idea:** images are the source. The **Detail Database** is the product. Tags enable retrieval; LLM descriptions enable understanding and ranking.

```text
                 ┌─────────────────────┐
                 │     SOURCE FILES     │
                 │   Images /    │
                 │  Project Folders    │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │   DETAIL INGESTION  │
                 │                     │
                 │ Identify/store      │
                 │ individual details  │
                 └──────────┬──────────┘
                            ↓
        ┌─────────────────────────────────────┐
        │          DETAIL DATABASE            │
        │                                     │
        │ Source metadata                     │
        │ Project / Year / PDF / Sheet        │
        │ Detail / Version                    │
        │                                     │
        │ Classification                      │
        │ Category / Subcategory              │
        │                                     │
        │ Tags                                │
        │ Controlled + AI + Human             │
        │                                     │
        │ Architectural description           │
        │ Strengths / limitations / context   │
        │ Regional / product information      │
        │                                     │
        │ Usage / popularity                  │
        └──────────────┬──────────────────────┘
                       │
             ┌─────────┴──────────┐
             ↓                    ↓
   ┌──────────────────┐  ┌──────────────────┐
   │   AI METADATA    │  │   HUMAN REVIEW   │
   │                  │  │                  │
   │ Generate tags    │  │ Edit / approve   │
   │ Generate blurb   │  │ Add knowledge    │
   │ Assign confidence│  │ Override AI      │
   └────────┬─────────┘  └────────┬─────────┘
            └──────────┬──────────┘
                       ↓
              ┌─────────────────┐
              │  SEARCH ENGINE  │
              │                 │
              │ Tags + metadata │
              │ + descriptions  │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │  QUERY LLM      │
              │                 │
              │ Understand user │
              │ request         │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │   RETRIEVAL     │
              │                 │
              │ Find candidates  │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │  LLM RERANKING  │
              │                 │
              │ Compare request │
              │ to candidates   │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │    WEB UI       │
              │                 │
              │ Search          │
              │ Filters         │
              │ Browse          │
              │ Detail viewer   │
              │ Metadata editor │
              └─────────────────┘
```

### The four things we're actually building

**1. Detail Database**
The permanent architectural knowledge base.

**2. AI Metadata Generator**
Runs once per detail and creates structured tags + a 2–3 sentence architectural description.

**3. Search + LLM Reranking**
Fast database retrieval first, then LLM reasoning over the smaller candidate set.

**4. Simple Local Web UI**
Search, browse, review, edit, and view details.

### MVP deliberately excludes

* Computer vision
* OCR
* CLIP
* Vector database
* Automatic detail detection
* Cloud infrastructure
* Streamlit
* PyMuPDF dependency

Those can be added **only when the actual workflow proves they are necessary**.

**One sentence to keep at the top of the project:**

> **Retrieve with structured metadata; understand with descriptions; rank with an LLM; trust the human.**
