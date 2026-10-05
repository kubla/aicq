# Mainline publication — 2026-10-05

Michael instructed “Make it happen” after discussing moving the shared spec from
the existing prototype branch to main. Canonical plan/spec/decisions/progress/
workboard/overview and latest editorial history matched repository mirrors.
Fetched remote main; it was an ancestor of the published branch. Switched the
local checkout to main, merged with --ff-only, and pushed without force.

GitHub main moved from `36870e439fc27eec06e31e3c070979edcf54d25f` to
`9d570719497859173dbb824287349e0e56943d99`. Git ls-remote matched the local head;
GitHub contents API for spec.md on main byte-matched the reviewed local spec.
No content changed during the fast-forward, so existing evaluations apply.

Main is the working home for the shared spec and straightforward documentation.
Repository visibility/access, Site deployment and the existing branch were
unchanged. The unrelated untracked research file was preserved. M1 complete;
M2 incomplete with one retry; M3–M6 pending; no new implementation run.
