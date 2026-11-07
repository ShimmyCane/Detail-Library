# Lessons learned: Detail Library build

Short notes from the build sessions, so the same problems are not solved twice.

## Sourcing images

- **Public-domain first, then open licences.** Rules are `Public domain`, `CC0`, `CC BY`, `CC BY-SA`. Every file needs a record in `images/raw/licences.json`. Missing records show as `unverified`.
- **Wikimedia Commons is the only image source reachable from the build sandbox.** The API works. The original-file host (`upload.wikimedia.org`) rate-limits with HTTP 429. The thumbnail host (`thumb.wikimedia.org`) is refused by the proxy (403). Pace requests, do not retry a 429 in a loop, and wait for the window to reset.
- **Library of Congress, archive.org, the Met, Art Institute of Chicago, Smithsonian, NREL/DOE, NIST, 4specs, Sweets and most manufacturer sites are not reachable from the sandbox.** Do not try to route around the proxy. Record them in `sources/sources.json` with `reachable_from_sandbox: false` and pull them manually.
- **Commons category listings are mostly photographs.** Search with detail words (section, detail, flashing, sheet) and filter by mime type and size. Photo captions ("Photographer", "VIEW") are a reliable exclusion.
- **Keep a per-image log.** `images/raw/image-log.json` is written by `generate_library.py` (hash, size, pixels, licence, first-seen date).

## Manufacturer details (links only)

- **Links only.** Manufacturer drawings are copyrighted and are not copied into the repo. Index entries link to download pages, not home pages.
- **Search results are a lead, not a verification.** Many results are scraped mirrors on odd domains (web.app, dev., spam). Prefer the manufacturer's own domain. Mark anything not opened as unverified.
- **Say what is not found.** Steelcraft, Schlage, Hager, 3M firestop CAD, Carlisle WIP, Pella and Euclid had no usable results. Record them as not found rather than inventing links.
- **Licence walls matter.** ARCAT and Sweets need a licence agreement or account. Label these in each note.
- **Regional sites differ.** Sika Ireland, Sika UK and Hilti Canada are not the US product. Confirm before use.

## Build and tooling

- **Use absolute paths in scratch scripts.** A quoted heredoc (`<<'EOF'`) does not expand shell variables, so `SP` inside the JavaScript is undefined. Substitute the literal path.
- **JSON loads need a web server.** The reference index uses `fetch`, which fails on `file://`. Test with `python3 -m http.server`.
- **Test in a browser, not only by reading.** Playwright tests caught a wrong selector and a checkbox state issue that reading the code did not.
- **Block external requests in tests.** Route non-local requests to abort, so tests do not hang on CDNs or blocked sites.
- **Re-read files changed by others.** When a file changed on disk, take it as the current state and check the diff before editing.

## Repository and PRs

- **Draft PRs must be marked ready before merging.** The merge API refuses drafts.
- **Subscription events are not CI results.** A `subscription.created` notice carries no check runs. Check the PR state directly.
- **Attribution.** Commits and PRs carry the session link and the Claude Code line, without a model name.
- **Scheduled retries.** Use the scheduler for rate-limited work, and state the retry time in the reply.

## Cloud library

- The cloud library is the Supabase project "Architecture" (`xabgankckrcuhcgdolrg`). Quick Detail owns the `sketch_*` tables. The Quick Detail code is in `ShimmyCane/quick-detail` (read-only from this session).
- Do not write to Supabase from the library. The library is GitHub files only.

## Later sessions

- **Follow the user's format preference.** The user asked for PDFs and no new ARCAT links. Search for PDFs first and filter out ARCAT results. Existing ARCAT entries stay until asked to remove them.
- **JPG detail images are rare.** Manufacturers publish PDF or DWG. Export images from the PDF or DWG yourself. Manufacturer images stay link-only in the index unless the owner releases them under an allowed licence.
- **Counts drift.** Hand-written counts in the to-do went stale after several rounds. Read them from the JSON (see the to-do's counting script) before reporting progress.
- **Merging with `main`.** When `main` has a merge commit the branch lacks, merge `main` into the branch first, then open the PR. The PR is then clean and merges with a normal merge commit.
- **Draft PRs.** Mark a draft ready (`draft: false`) before merging. Creating the PR with `draft: false` avoids the second step.
- **Subscription notices are not CI.** The PR-activity wakes for PR #1 and PR #2 carried no check runs. Check the PR directly before reporting status.
- **Third-party aggregators.** aecinfo, CADdetails and LADetails host manufacturer files, and designscad/cadbull host unverified uploads. Label each one, and keep the manufacturer's own page as the first choice.
- **Browser checks on static pages.** A quick Playwright pass (load, click, sort, filter, reload, phone width) caught real bugs each time. Keep a short check script per page in the scratchpad.

## Interpretation log

- "Egyptian for the fire ratings" was read as "especially for the fire ratings".
- "CCY BY" was read as CC BY.
