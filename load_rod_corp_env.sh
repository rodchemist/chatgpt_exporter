#!/usr/bin/env bash
# Usage: source load_rod_corp_env.sh [path_to_env_file]
# Loads the Rod-Corp combined environment variables into the current shell session.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="${1:-"$SCRIPT_DIR/rod_corp_combined.env"}"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "[load-env] Environment file not found: $ENV_FILE" >&2
  return 1 2>/dev/null || exit 1
fi

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  echo "[load-env] This script should be sourced so variables persist. Use: source $0" >&2
fi

trim() {
  local var="$1"
  var="${var#${var%%[![:space:]]*}}"   # strip leading whitespace
  var="${var%${var##*[![:space:]]}}"   # strip trailing whitespace
  printf '%s' "$var"
}

while IFS= read -r line || [[ -n "$line" ]]; do
  case "$line" in
    ''|\#*)
      continue
      ;;
  esac

  if [[ "$line" != *'='* ]]; then
    continue
  fi

  key="${line%%=*}"
  value="${line#*=}"

  key="$(trim "$key")"
  value="${value%$'\r'}"
  value="$(trim "$value")"

  if [[ ${#value} -ge 2 && "${value:0:1}" == '"' && "${value: -1}" == '"' ]]; then
    value="${value:1:-1}"
  fi

  export "$key=$value"

done < "$ENV_FILE"

echo "[load-env] Loaded environment from $ENV_FILE"
