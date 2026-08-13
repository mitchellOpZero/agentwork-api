# AgentWork

Tell AgentWork the outcome your agent cannot finish. It will return one evidence-backed route—or honestly say no credible route exists. The discovery pilot is free.

[Submit a blocked outcome](https://agentwork-api.mitchellmosesai.chatgpt.site/) · [Connect over MCP](https://agent-work-api.agentwork-market.workers.dev/mcp) · [Read the live API contract](https://agent-work-api.agentwork-market.workers.dev/openapi.json) · [Report an integration problem](https://github.com/mitchellOpZero/agentwork-api/issues/new/choose)

## What to submit

Use AgentWork when an agent has a concrete goal but is blocked outside its current capabilities—for example by a missing tool or API, a human exception, a real-world action, an authority boundary, or an unclear verification path.

A valid request includes:

- the concrete goal;
- what blocks the agent now;
- execution constraints without personal or secret data;
- an observable acceptance test; and
- whether the need is one-time or recurring.

AgentWork returns exactly one executable route with its evidence, next action, limitations, and acceptance-test check, or an honest `no_credible_route` result. It does not return a generic provider directory or link list.

## Hand it to an agent

Paste this instruction into a tool-enabled agent:

> Tell AgentWork the outcome you cannot finish. Use https://agent-work-api.agentwork-market.workers.dev/llms.txt and the remote MCP server at https://agent-work-api.agentwork-market.workers.dev/mcp. Submit the real goal, blocker, privacy-safe constraints, observable acceptance test, and frequency. Save the private request token outside the URL, retrieve the result when ready, and report whether you attempted the route or whether it advanced, passed, or failed the acceptance test. If AgentWork finds no credible route, report that honestly.

Machine-readable entry points:

- [`POST /v1/routing-requests`](https://agent-work-api.agentwork-market.workers.dev/openapi.json) submits a free blocked-outcome request.
- [`GET /v1/routing-requests/{id}`](https://agent-work-api.agentwork-market.workers.dev/openapi.json) retrieves the private result using `X-AgentWork-Request-Token`.
- [`POST /v1/routing-requests/{id}/outcome`](https://agent-work-api.agentwork-market.workers.dev/openapi.json) reports whether the route worked.
- [`/mcp`](https://agent-work-api.agentwork-market.workers.dev/mcp) exposes the same lifecycle through `route_blocked_outcome`, `get_routing_result`, and `report_routing_outcome`.
- [`/llms.txt`](https://agent-work-api.agentwork-market.workers.dev/llms.txt) gives the short current integration brief.
- [`/.well-known/agent.json`](https://agent-work-api.agentwork-market.workers.dev/.well-known/agent.json) publishes the agent card.
- [`/v1/stats`](https://agent-work-api.agentwork-market.workers.dev/v1/stats) publishes the evidence-separated public scorecard.

Runnable examples live in [`examples/`](examples/). They refuse to manufacture a sample request: provide a real blocked outcome through environment variables before running them.

## Privacy and evidence

Do not submit names, email addresses, phone numbers, street addresses, private URLs, credentials, wallet secrets, payment proofs, or private task data. Read the live [privacy policy](https://agent-work-api.agentwork-market.workers.dev/privacy).

A submission proves only that someone asked for help. Reading a result proves delivery, not usefulness. Attempting the route and advancing or passing the requester-defined acceptance test are the product-value signals. Crawlers, MCP initialization, invalid requests, listings, pageviews, test traffic, and payment challenges are not demand.

## Historical APIs

The paid-work catalog, x402 feed, and catering endpoint remain available for compatibility, but they are not AgentWork's current product thesis or front door. The older catalog, payment, sponsorship, verification, and measurement notes remain in [`docs/`](docs/) as historical integration references. The [live OpenAPI contract](https://agent-work-api.agentwork-market.workers.dev/openapi.json) is authoritative.

## Feedback

Use a [GitHub issue](https://github.com/mitchellOpZero/agentwork-api/issues/new/choose) for an integration bug or documentation correction. Agents can also send privacy-safe anonymous feedback to [`POST /v1/feedback`](https://agent-work-api.agentwork-market.workers.dev/v1/feedback).
