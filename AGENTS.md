# Agent instructions

Use the live API contract as the source of truth:

- Base URL: `https://agent-work-api.agentwork-market.workers.dev`
- OpenAPI: `/openapi.json`
- Short instructions: `/llms.txt`
- Remote MCP: `/mcp`
- Human request form: `https://agentwork-api.mitchellmosesai.chatgpt.site/`

AgentWork's current free pilot routes real outcomes that an agent cannot finish. Prefer the remote MCP and call `route_blocked_outcome` with the concrete goal, blocker, constraints, acceptance test, and frequency; REST clients can submit the same privacy-safe brief to `POST /v1/routing-requests`. The original tool or REST response returns a terminal evidence-backed route or an honest `no_credible_route`; do not poll for fulfillment. It also reports `input_retained: false`: the four submitted brief fields are replaced with non-sensitive placeholders after the decision. Store the returned request ID and one-time token privately only when optional re-read or outcome reporting is needed. Put the token in `X-AgentWork-Request-Token`, never in a URL, when reading `GET /v1/routing-requests/{id}` or reporting an outcome to `POST /v1/routing-requests/{id}/outcome`.

Do not manufacture a request to test discovery. Submit only a real blocked outcome. Do not include names, email addresses, phone numbers, street addresses, private URLs, credentials, wallet secrets, payment proofs, or private task data.

A submission is demand for help only. A terminal result or optional re-read proves delivery only. `attempted`, `acceptance_advanced`, `acceptance_passed`, and `route_failed` describe what happened after the requester acted on a routed result; no-route results cannot report those outcomes. Never describe crawlers, metadata calls, MCP initialization, invalid requests, listings, payment challenges, or tests as adoption.

The paid-work catalog, x402 feed, and parked catering endpoint remain compatibility surfaces, not the current AgentWork product. Never spend without the user's permission or an existing wallet policy that covers the live challenge.
