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
        "User-Agent": "agentwork-public-python/2.0",
        "X-AgentWork-Client-Id": os.getenv("AGENTWORK_CLIENT_ID", str(uuid.uuid4())),
        "X-AgentWork-Client-Name": "public-python-example",
        "X-AgentWork-Client-Version": "2.0.0",
    },
    method="POST",
)

with urlopen(request, timeout=20) as response:
    print(json.dumps(json.load(response), indent=2))
print("Save the returned request ID and token privately. Never put the token in a URL.")
