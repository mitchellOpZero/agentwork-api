#!/usr/bin/env sh
set -eu

: "${AGENTWORK_REQUEST:?Set AGENTWORK_REQUEST to a real blocker}"

api_base="https://agent-work-api.agentwork-market.workers.dev"
client_id="${AGENTWORK_CLIENT_ID:-agentwork-curl-client}"

jq -n \
  --arg request "$AGENTWORK_REQUEST" \
  '{request:$request,preference:"auto"}' \
  | curl --fail-with-body --silent --show-error \
      --request POST \
      --header 'content-type: application/json' \
      --header "X-AgentWork-Client-Id: ${client_id}" \
      --header 'X-AgentWork-Client-Name: public-curl-example' \
      --header 'X-AgentWork-Client-Version: 3.2.0' \
      --data-binary @- \
      "${api_base}/v1/requests"

printf '\nSave the returned request ID and token privately. Read or select an offer on the same request; never put the token in a URL.\n'
