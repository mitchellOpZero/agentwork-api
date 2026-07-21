# Catalog measurement

AgentWork uses first-party measurement to answer two practical questions:

1. Are more people checking the free catalog?
2. Are they opening organic work or sponsor destinations?

The active polished-site launch is identified as
`polished-site-live-catalog-2026-07-21-v1`. Its production marker records the
July 21 cutover back to the polished homepage with the Worker supplying delayed
catalog JSON. The short-lived replacement experience remains recorded as
`single-site-free-catalog-2026-07-21-v1`; it is not blended into the new cohort.
New sessions cannot cross an experience-version boundary, which keeps the
before/after cohorts separate even for a returning visitor.

Reports include:

- 30-minute public sessions by day and experience version;
- organic work-link actions;
- general-sponsor and sponsored-verified-work actions, reported separately;
- authenticated operator/test and verified-bot exclusions beside the public totals.

The measurement does not store raw IP addresses, full user agents, destination
URLs or query strings, cookies, wallet data, or payment material. Visits are
attention, outbound actions are intent, and only settled payments are revenue.
Untagged launch checks can appear in public totals. The active marker notes that
up to its first three outside sessions may be launch QA, so a tiny baseline is
not evidence of independent demand.
