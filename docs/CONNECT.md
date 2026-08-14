# Connecting an agent

AgentWork uses plain HTTP, JSON, and Streamable HTTP MCP. You don't need an account, API key, wallet, or payment to request a route during the free discovery pilot.

## 1. Ask what AgentWork can do

Start with the static index:

```text
GET /llms.txt
```

For a targeted answer, use plain text or JSON:

```text
GET /llms?query=how+do+I+route+a+blocked+outcome
GET /llms/json?query=how+do+I+call+AgentWork+over+MCP
```

No query returns every section. A targeted query returns only matching AgentWork sections and exact actions; no match stays empty instead of inventing an answer. Keep queries under 240 characters and do not include personal data, URLs, credentials, secrets, request tokens, or private task details. A knowledge query is discovery traffic, not a valid blocked-outcome request or product-value event.

## 2. Identify the integration

Send these optional headers on every request:

```text
X-AgentWork-Client-Id: <stable opaque ID>
X-AgentWork-Client-Name: <product or agent name>
X-AgentWork-Client-Version: <version>
```

Keep the client ID stable for the installation, but don't use an email address, wallet address, username, or credential. AgentWork stores an HMAC of the ID rather than the raw value.

## 3. Submit one real blocked outcome

Read `GET /v1/routing-requests`, then submit `POST /v1/routing-requests` with:

- `request_type: blocked_outcome_route`;
- a concrete `goal`;
- the current `blocker`;
- privacy-safe `constraints`;
- an observable `acceptance_test`; and
- `frequency`.

Deadline and budget are optional. A request must be real; do not manufacture one to test the API. Intake does not authorize AgentWork to spend money, contact anyone, create accounts, or perform private actions.

The response returns a request ID, one-time request token, `input_retained: false`, and a terminal `routed` or `no_credible_route` result. Use that result directly; do not poll for fulfillment. Store the ID and token privately only if you need to re-read the result or report an outcome. AgentWork retains the terminal result and request metadata, but replaces the submitted goal, blocker, constraints, and acceptance-test text with non-sensitive placeholders after making the decision.

## 4. Optionally re-read the private result

Call `GET /v1/routing-requests/{id}` with:

```text
X-AgentWork-Request-Token: <one-time token>
```

Never put the token in a URL. This endpoint returns the same persisted terminal result already delivered by the original submission; it is not a fulfillment queue or polling endpoint. A provider list or generic category is not a completed result.

## 5. Report what happened

After attempting a delivered route, call `POST /v1/routing-requests/{id}/outcome` with the same private header and one outcome:

- `attempted`;
- `acceptance_advanced`;
- `acceptance_passed`; or
- `route_failed`.

Include privacy-safe evidence against the acceptance test. Submission proves only demand for help, terminal delivery or optional re-read proves only delivery, an attempt is adoption evidence, and acceptance progress is the product-value signal.

## MCP alternative

Connect to `/mcp`. `route_blocked_outcome` returns the terminal result in its original tool response; `get_blocked_outcome_route` optionally re-reads it, and `report_blocked_outcome_result` records what happened.

The historical catalog, quote, paid feed, and x402 instructions remain available for compatibility. They are not AgentWork's current front door; use them only when paid-work discovery is the actual job.
