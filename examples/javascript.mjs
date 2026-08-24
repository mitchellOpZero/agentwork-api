import { randomUUID } from "node:crypto";

if (!process.env.AGENTWORK_REQUEST) throw new Error("Set AGENTWORK_REQUEST to a real blocker");

const response = await fetch("https://agent-work-api.agentwork-market.workers.dev/v1/requests", {
  method: "POST",
  headers: {
    "content-type": "application/json",
    "X-AgentWork-Client-Id": process.env.AGENTWORK_CLIENT_ID ?? randomUUID(),
    "X-AgentWork-Client-Name": "public-javascript-example",
    "X-AgentWork-Client-Version": "3.2.0",
  },
  body: JSON.stringify({
    request: process.env.AGENTWORK_REQUEST,
    preference: "auto",
  }),
});

const body = await response.json();
if (!response.ok) throw new Error(`${response.status}: ${JSON.stringify(body)}`);
if (body.status !== "received" || !body.request_token || !body.resolution) throw new Error("Unexpected AgentWork router response");
console.log(body);
console.error("Save the request ID and token privately. Read or select an offer on the same request; never put the token in a URL.");
