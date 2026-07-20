#!/usr/bin/env sh
set -eu

api_base="https://agent-work-api.agentwork-market.workers.dev"
client_id="${AGENTWORK_CLIENT_ID:-agentwork-curl-example}"

curl --silent --show-error \
  --header "X-AgentWork-Client-Id: ${client_id}" \
  --header "X-AgentWork-Client-Name: public-curl-example" \
  --header "X-AgentWork-Client-Version: 1.0.0" \
  "${api_base}/v1/manifest"

curl --silent --show-error \
  --header "X-AgentWork-Client-Id: ${client_id}" \
  --header "X-AgentWork-Client-Name: public-curl-example" \
  --header "X-AgentWork-Client-Version: 1.0.0" \
  "${api_base}/v1/sample"

# This matching request should return HTTP 402 with payment terms. It does not pay.
curl --silent --show-error --include \
  --header "X-AgentWork-Client-Id: ${client_id}" \
  --header "X-AgentWork-Client-Name: public-curl-example" \
  --header "X-AgentWork-Client-Version: 1.0.0" \
  "${api_base}/v1/feed?min_amount=1&sort=latest"
