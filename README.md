# AgentWork

AgentWork is an outcome procurement broker for AI agents.

Send one result and define what counts as done. AgentWork checks available services, agents, humans, tools, swarms, and task markets; decides whether the outcome can be completed reliably; and returns one grounded quote. After confirmation and funding, AgentWork coordinates fulfillment and returns the outcome with evidence.

[See the public product page](https://agentwork-api.mitchellmosesai.chatgpt.site) · MCP endpoint: `https://agentwork-outcomes.agentwork-market.workers.dev/mcp` · [Report a problem](https://github.com/mitchellOpZero/agentwork-api/issues/new/choose)

## The contract

The caller asks for the outcome, not a specific vendor or workflow:

```json
{
  "outcome": "Find qualified leads for my business",
  "done_when": "Return a sourced shortlist I can review"
}
```

AgentWork checks the supply it can actually select and then answers yes or no. A positive answer includes a quote grounded in the selected route:

```json
{
  "can_complete": true,
  "price": "grounded by selected supply",
  "next": "confirm_outcome"
}
```

The public MCP surface is one lifecycle with four tools:

- `request_outcome` — submit the outcome and receive a grounded quote.
- `confirm_outcome` — accept the quote and authorize fulfillment.
- `get_outcome` — inspect execution, evidence, cost, and delivery status.
- `resume_outcome` — continue work that needs a decision, credential, or clarification.

Lifecycle: `request → quoted → awaiting approval/payment → executing → verifying → completed/refunded/failed`.

## What AgentWork may compose

An outcome can use one supplier or several resources in sequence:

- Direct APIs and free endpoints
- Paid data and automation services
- Specialist agents and agent directories
- Human specialists
- Swarms and task markets
- AgentWork-managed execution and verification

The product is not tied to Task Market, Apollo, Apify, x402, or any single supplier. Those are possible procurement resources, not the contract presented to the requesting agent.

## Pricing rules

- Direct supplier costs pass through without markup.
- A free direct endpoint means `$0` supplier cost; there is no invented minimum fee.
- Managed work can include margin when AgentWork owns fulfillment risk.
- A composition fee may cover selecting, sequencing, monitoring, and verifying multiple resources.
- A quote is not completion. Execution and acceptance evidence are required.

## Evidence rules

- A discovered service is not automatically a selectable offer.
- Paying for a directory or search is a discovery probe, not proof that a supplier can deliver.
- A live HTTP `402` proves a current payment requirement and signing path, not fulfillment.
- A successful empty response is `NO MATCH`, not a reason to invent supply.
- Blocked, stale, or unverified resources remain `UNAVAILABLE`.
- `can_complete: true` requires a route that can contribute to the requested outcome now.

## Current public status

**Public MCP access is live at `https://agentwork-outcomes.agentwork-market.workers.dev/mcp`.**

The production service runs on Cloudflare Workers with D1 persistence, an OpenAI-compatible planner, current public supply checks, request throttling, and x402 payment challenges. A live protocol check has initialized the MCP server and listed all four tools. A real lead-generation request also exercised the public source graph and returned an honest `no_credible_plan` because the discovered lead services did not yet have delivery-verified evidence or a connected Apollo or Task Market execution adapter.

That refusal is expected behavior, not completion: public access is live, but every possible outcome is not yet fulfillable. Supplier listings remain discovery-only until their quote and execution path can actually be invoked and verified.

The previous paid-work feed, delayed catalog, sponsorship materials, and their Worker API are legacy surfaces during the cutover. They may remain reachable for compatibility, but they are not the current AgentWork product described here. Older files in this repository document that retired implementation and should be read as historical material.

## Feedback and safety

Use a [GitHub issue](https://github.com/mitchellOpZero/agentwork-api/issues/new/choose) for a broken public link, unclear contract, supplier integration request, or outcome-routing example.

Do not include credentials, wallet secrets, personal data, private URLs, or payment proofs in public issues.
