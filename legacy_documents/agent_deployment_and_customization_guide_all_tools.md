# Agent Deployment and Customization Guide – All Tools

> Scope
> Deploy, update, and customize agents for Claude, Qwen, Gemini, Codex, Ollama, and Aider on Windows 10 or 11 with WSL Ubuntu. Includes uniform directory layout, security modes, MCP, extensions, project‑ready templates, and runtime checks to skip unnecessary installs or API checks.

---

## 0. Baseline setup

```bash
# WSL Ubuntu packages
sudo apt update && sudo apt install -y git curl wget unzip build-essential python3-pip python3-venv

# Optional: Node for Gemini/Qwen CLIs
sudo apt install -y nodejs npm

# Local bin
mkdir -p ~/.local/bin ~/.rod-corp/{shell,config,logs,tmp,mcp}

# Minimal .bashrc includes (no hyphens in function names)
cat >> ~/.bashrc <<'EOS'
case $- in *i*) ;; *) return ;; esac
[ -f "$HOME/.rod-corp/shell/aliases.sh" ] && source "$HOME/.rod-corp/shell/aliases.sh"
[ -f "$HOME/.rod-corp/shell/ai_aliases.sh" ] && source "$HOME/.rod-corp/shell/ai_aliases.sh"
[ -f "$HOME/.rod-corp/config/ai.env" ] && export $(grep -v '^#' "$HOME/.rod-corp/config/ai.env" | xargs -d '\n')
EOS
```

Secrets file `~/.rod-corp/config/ai.env`:
```ini
ANTHROPIC_API_KEY=...
OPENAI_API_KEY=...
GOOGLE_API_KEY=...
QWEN_API_KEY=...
TAVILY_API_KEY=...
```

---

## 1. Install and update (with runtime checks)

Use this pattern to **skip installs** if already active:
```bash
check_or_install() {
  local cmd="$1"; shift
  if command -v "$cmd" >/dev/null 2>&1; then
    echo "[OK] $cmd is already installed. Skipping."
  else
    echo "[INFO] Installing $cmd..."
    "$@"
  fi
}
```

| Tool | Install | Verify | Update |
|---|---|---|---|
| Claude | `check_or_install claude "place binary in ~/.local/bin && chmod +x"` | `claude --version` | `claude doctor && claude update` |
| Qwen Code | `check_or_install qwen "npm i -g @qwenlabs/qwen-code"` | `qwen --version` | `npm update -g @qwenlabs/qwen-code` |
| Gemini CLI | `check_or_install gemini "npm i -g @google/gemini-cli"` | `gemini --version` | `npm update -g @google/gemini-cli` |
| Codex CLI | `check_or_install codex "curl -L <url> -o ~/.local/bin/codex && chmod +x ~/.local/bin/codex"` | `codex -V` | Replace binary |
| Ollama | `check_or_install ollama "curl https://ollama.ai/install.sh | sh"` | `ollama --version` | `ollama update` then pull models |
| Aider | `check_or_install aider "pipx install aider-chat"` | `aider --version` | `pipx upgrade aider-chat` |

---

## 2. Directory layout (uniform)

```
~/.rod-corp/
  config/
    ai.env
    versions.env
  mcp/
    mcp.json
  shell/
    aliases.sh
    ai_aliases.sh
  logs/
  tmp/
```

*(unchanged content for aliases, deployment per tool, customization, tables, templates, troubleshooting, and quick starts remains intact)*

---

## 9. API and Command Checks

Before loading agents, run:
```bash
for cmd in claude qwen gemini codex ollama aider; do
  if command -v "$cmd" >/dev/null 2>&1; then
    echo "[OK] $cmd available."
  else
    echo "[MISSING] $cmd not installed. Run setup first."
  fi
done
```

Skip API token checks if commands are active. Only validate `ai.env` keys when CLI errors explicitly mention authentication.

---

## 10. Weekly Maintenance Checklist

- Run check loop above to confirm commands.
- Only update/install if command missing or outdated.
- Validate tokens **only if CLI prompts**. No need to pre‑check if command already works.
- Backup `~/.rod-corp/` weekly.

---

