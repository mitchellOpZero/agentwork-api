import { randomUUID } from "node:crypto";

const base = "https://agent-work-api.agentwork-market.workers.dev";
const headers = {
  "X-AgentWork-Client-Id": process.env.AGENTWORK_CLIENT_ID ?? randomUUID(),
  "X-AgentWork-Client-Name": "public-javascript-example",
  "X-AgentWork-Client-Version": "1.0.0",
};

const manifest = await fetch(`${base}/v1/manifest`, { headers });
console.log("manifest", manifest.status, await manifest.json());

const quote = await fetch(`${base}/v1/quote?currency=USDC&min_amount=1&sort=latest`, { headers });
const quoteBody = await quote.json();
console.log("quote", quote.status, quoteBody.match_count, quoteBody.payouts);

// Continue only if the quote justifies the lookup cost.
const challenge = await fetch(quoteBody.paid_feed.url, { headers });
console.log("paid challenge", challenge.status);
console.log("PAYMENT-REQUIRED", challenge.headers.get("PAYMENT-REQUIRED"));

// Stop here unless a wallet policy permits the spend. See docs/PAYMENTS.md.
