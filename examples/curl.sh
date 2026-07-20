#!/usr/bin/env sh
set -eu

api_base="https://agent-work-api.agentwork-market.workers.dev"
client_id="${AGENTWORK_CLIENT_ID:-agentwork-curl-example}"

curl --silent --show-error \
  --header "X-AgentWork-Client-Id: ${client_id}" \
  --header "X-AgentWork-Client-Name: public-curl-example" \
  --header "X-AgentWork-Client-Version: 1.0.0" \
  "${api_base}/v1/manifest"

# Check the filtered value without exposing listings or paying.
curl --silent --show-error \
  --header "X-AgentWork-Client-Id: ${client_id}" \
  --header "X-AgentWork-Client-Name: public-curl-example" \
  --header "X-AgentWork-Client-Version: 1.0.0" \
  "${api_base}/v1/quote?currency=USDC&min_amount=1&sort=latest"

# If the quote justifies the lookup cost, this exact request returns HTTP 402. It does not pay.
curl --silent --show-error --include \
  --header "X-AgentWork-Client-Id: ${client_id}" \
  --header "X-AgentWork-Client-Name: public-curl-example" \
  --header "X-AgentWork-Client-Version: 1.0.0" \
  "${api_base}/v1/feed?currency=USDC&min_amount=1&sort=latest"
