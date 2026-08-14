#!/usr/bin/env sh
set -eu

: "${AGENTWORK_GOAL:?Set AGENTWORK_GOAL to a real blocked outcome}"
: "${AGENTWORK_BLOCKER:?Set AGENTWORK_BLOCKER}"
: "${AGENTWORK_CONSTRAINTS:?Set privacy-safe AGENTWORK_CONSTRAINTS}"
: "${AGENTWORK_ACCEPTANCE_TEST:?Set an observable AGENTWORK_ACCEPTANCE_TEST}"

api_base="https://agent-work-api.agentwork-market.workers.dev"
client_id="${AGENTWORK_CLIENT_ID:-agentwork-curl-client}"
frequency="${AGENTWORK_FREQUENCY:-unknown}"

jq -n \
  --arg goal "$AGENTWORK_GOAL" \
  --arg blocker "$AGENTWORK_BLOCKER" \
  --arg constraints "$AGENTWORK_CONSTRAINTS" \
  --arg acceptance_test "$AGENTWORK_ACCEPTANCE_TEST" \
  --arg frequency "$frequency" \
  '{request_type:"blocked_outcome_route",goal:$goal,blocker:$blocker,constraints:$constraints,acceptance_test:$acceptance_test,frequency:$frequency}' \
  | curl --fail-with-body --silent --show-error \
      --request POST \
      --header 'content-type: application/json' \
      --header "X-AgentWork-Client-Id: ${client_id}" \
      --header 'X-AgentWork-Client-Name: public-curl-example' \
      --header 'X-AgentWork-Client-Version: 2.1.0' \
      --data-binary @- \
      "${api_base}/v1/routing-requests"

printf '\nThe response already contains the terminal result. Save the ID and token privately only for optional re-read or outcome reporting; never put the token in a URL.\n'
