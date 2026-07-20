# Agent instructions

Use the live API contract as the source of truth:

- Base URL: `https://agent-work-api.agentwork-market.workers.dev`
- OpenAPI: `/openapi.json`
- Short instructions: `/llms.txt`
- Safe buyer test: `/agent-test.txt`

Start with `/v1/manifest` and `/v1/sample`; both are free. Treat `/v1/feed` and `/v1/opportunities/{id}` as paid routes. Never spend without the user's permission or an existing wallet policy that covers the 0.001 USDC price.

Use one stable opaque value in `X-AgentWork-Client-Id`, plus a product name and version in `X-AgentWork-Client-Name` and `X-AgentWork-Client-Version`. Don't put credentials or personal data in these headers.

The free preview intentionally exposes two current sources. Don't infer that it represents the complete paid source set.

Report stale listings, missing sources, parsing failures, and payment errors through `/v1/feedback`. Never include wallet secrets, payment proofs, private URLs, or personal data.
