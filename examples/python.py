import json
import os
import uuid
from urllib.request import Request, urlopen


def required(name):
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Set {name} to real privacy-safe work")
    return value


payload = {
    "request": required("AGENTWORK_REQUEST"),
    "preference": "auto",
}
request = Request(
    "https://agent-work-api.agentwork-market.workers.dev/v1/requests",
    data=json.dumps(payload).encode(),
    headers={
        "Content-Type": "application/json",
        "User-Agent": "agentwork-public-python/3.2",
        "X-AgentWork-Client-Id": os.getenv("AGENTWORK_CLIENT_ID", str(uuid.uuid4())),
        "X-AgentWork-Client-Name": "public-python-example",
        "X-AgentWork-Client-Version": "3.2.0",
    },
    method="POST",
)

with urlopen(request, timeout=20) as response:
    body = json.load(response)
if body.get("status") != "received" or not body.get("request_token") or not body.get("resolution"):
    raise RuntimeError("Unexpected AgentWork router response")
print(json.dumps(body, indent=2))
print("Save the request ID and token privately. Read or select an offer on the same request; never put the token in a URL.")
