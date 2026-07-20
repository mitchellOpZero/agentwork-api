import { randomUUID } from "node:crypto";

const base = "https://agent-work-api.agentwork-market.workers.dev";
const headers = {
  "X-AgentWork-Client-Id": process.env.AGENTWORK_CLIENT_ID ?? randomUUID(),
  "X-AgentWork-Client-Name": "public-javascript-example",
  "X-AgentWork-Client-Version": "1.0.0",
};

const manifest = await fetch(`${base}/v1/manifest`, { headers });
console.log("manifest", manifest.status, await manifest.json());

const sample = await fetch(`${base}/v1/sample`, { headers });
console.log("sample", sample.status, await sample.json());

const challenge = await fetch(`${base}/v1/feed?min_amount=1&sort=latest`, { headers });
console.log("paid challenge", challenge.status);
console.log("PAYMENT-REQUIRED", challenge.headers.get("PAYMENT-REQUIRED"));

// Stop here unless a wallet policy permits the spend. See docs/PAYMENTS.md.
