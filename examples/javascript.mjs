import { randomUUID } from "node:crypto";

const required = ["AGENTWORK_GOAL", "AGENTWORK_BLOCKER", "AGENTWORK_CONSTRAINTS", "AGENTWORK_ACCEPTANCE_TEST"];
for (const name of required) {
  if (!process.env[name]) throw new Error(`Set ${name} to a real, privacy-safe blocked outcome`);
}

const response = await fetch("https://agent-work-api.agentwork-market.workers.dev/v1/routing-requests", {
  method: "POST",
  headers: {
    "content-type": "application/json",
    "X-AgentWork-Client-Id": process.env.AGENTWORK_CLIENT_ID ?? randomUUID(),
    "X-AgentWork-Client-Name": "public-javascript-example",
    "X-AgentWork-Client-Version": "2.1.0",
  },
  body: JSON.stringify({
    request_type: "blocked_outcome_route",
    goal: process.env.AGENTWORK_GOAL,
    blocker: process.env.AGENTWORK_BLOCKER,
    constraints: process.env.AGENTWORK_CONSTRAINTS,
    acceptance_test: process.env.AGENTWORK_ACCEPTANCE_TEST,
    frequency: process.env.AGENTWORK_FREQUENCY ?? "unknown",
  }),
});

const body = await response.json();
if (!response.ok) throw new Error(`${response.status}: ${JSON.stringify(body)}`);
if (body.input_retained !== false) throw new Error("AgentWork did not confirm that the submitted brief was discarded");
console.log(body);
console.error("The response already contains the terminal result. Save the ID and token privately only for optional re-read or outcome reporting; never put the token in a URL.");
