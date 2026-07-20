import json
import os
import uuid
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = "https://agent-work-api.agentwork-market.workers.dev"
HEADERS = {
    "User-Agent": "agentwork-public-python/1.0",
    "X-AgentWork-Client-Id": os.getenv("AGENTWORK_CLIENT_ID", str(uuid.uuid4())),
    "X-AgentWork-Client-Name": "public-python-example",
    "X-AgentWork-Client-Version": "1.0.0",
}


def get(path, params=None):
    query = f"?{urlencode(params)}" if params else ""
    request = Request(f"{BASE}{path}{query}", headers=HEADERS)
    try:
        with urlopen(request, timeout=20) as response:
            return response.status, response.headers, response.read()
    except HTTPError as error:
        return error.code, error.headers, error.read()


status, _, body = get("/v1/manifest")
print("manifest", status, json.loads(body))

status, _, body = get("/v1/quote", {"currency": "USDC", "min_amount": "1", "sort": "latest"})
quote = json.loads(body)
print("quote", status, quote["match_count"], quote["payouts"])

# Continue only if the quote justifies the lookup cost.
status, headers, _ = get("/v1/feed", {"currency": "USDC", "min_amount": "1", "sort": "latest"})
print("paid challenge", status)
print("PAYMENT-REQUIRED", headers.get("PAYMENT-REQUIRED"))

# Stop here unless a wallet policy permits the spend. See docs/PAYMENTS.md.
