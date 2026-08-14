import json
import os
import uuid
from urllib.request import Request, urlopen


def required(name):
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Set {name} to a real, privacy-safe blocked outcome")
    return value


payload = {
    "request_type": "blocked_outcome_route",
    "goal": required("AGENTWORK_GOAL"),
    "blocker": required("AGENTWORK_BLOCKER"),
    "constraints": required("AGENTWORK_CONSTRAINTS"),
    "acceptance_test": required("AGENTWORK_ACCEPTANCE_TEST"),
    "frequency": os.getenv("AGENTWORK_FREQUENCY", "unknown"),
}
request = Request(
    "https://agent-work-api.agentwork-market.workers.dev/v1/routing-requests",
    data=json.dumps(payload).encode(),
    headers={
        "Content-Type": "application/json",
        "User-Agent": "agentwork-public-python/2.1",
        "X-AgentWork-Client-Id": os.getenv("AGENTWORK_CLIENT_ID", str(uuid.uuid4())),
        "X-AgentWork-Client-Name": "public-python-example",
        "X-AgentWork-Client-Version": "2.1.0",
    },
    method="POST",
)

with urlopen(request, timeout=20) as response:
    body = json.load(response)
if body.get("input_retained") is not False:
    raise RuntimeError("AgentWork did not confirm that the submitted brief was discarded")
print(json.dumps(body, indent=2))
print("The response already contains the terminal result. Save the ID and token privately only for optional re-read or outcome reporting; never put the token in a URL.")
