# Unified Agent CLI Commands Reference (Claude, Qwen, Gemini, Codex, Ollama, Aider)

> This document consolidates **all CLI commands** from the official sources:
> - OpenAI Codex CLI ([docs](https://developers.openai.com/codex/cli))
> - Gemini CLI ([docs](https://github.com/google-gemini/gemini-cli/tree/main/docs))
> - Claude CLI ([docs](https://docs.claude.com/en/docs/claude-code/cli-reference), [templates](https://github.com/davila7/claude-code-templates))
> - Qwen CLI ([research](https://qwen.ai/research), [docs](https://github.com/QwenLM/qwen-code/tree/9fce177bd8cb3629cbf2dcab8b9d7e8825b02892/docs))

---

## 1. Claude CLI (`claude`)

```bash
claude [options] [command] [prompt]
```

### Core Commands
- `claude` → Start interactive session
- `claude -p "Prompt"` → One-shot print
- `claude config` → Manage configuration
- `claude mcp` → Configure/manage MCP servers
- `claude migrate-installer` → Migrate from global npm to local install
- `claude setup-token` → Configure authentication token
- `claude doctor` → Diagnose CLI
- `claude update` → Check/install updates
- `claude install [target]` → Install CLI native build

### Key Options
- `--model <model>` → Select model (e.g., `claude-sonnet-4-20250514`)
- `--fallback-model <model>` → Define fallback
- `--append-system-prompt <prompt>` → Extend default system prompt
- `--permission-mode <mode>` → Execution safety: `acceptEdits`, `sandboxBashMode`, `bypassPermissions`, `plan`
- `--agents <json>` → Define custom agents inline
- `--add-dir <directories>` → Allow additional directories
- `--mcp-config <files>` → Load MCP configs
- `--strict-mcp-config` → Ignore implicit configs
- `--resume / --continue` → Resume sessions
- `--output-format <format>` → `text`, `json`, `stream-json`

---

## 2. Qwen CLI (`qwen`)

```bash
qwen [options] [command]
```

### Core Commands
- `qwen` → Launch Qwen CLI (interactive)
- `qwen -p "Prompt"` → One-shot run
- `qwen mcp` → Manage MCP servers

### Key Options
- `-m, --model <name>` → Model alias (e.g., `qwen2.5-coder`)
- `-i, --prompt-interactive` → Execute prompt, then enter interactive
- `-s, --sandbox` → Enable sandbox
- `-y, --yolo` → Auto-approve all actions
- `--approval-mode <mode>` → `default`, `auto_edit`, `yolo`
- `--checkpointing` → Enable edit checkpointing
- `-e, --extensions <list>` → Load specific extensions
- `-l, --list-extensions` → List available extensions
- `--openai-api-key <key>` → Direct API key integration
- `--telemetry-*` → Control telemetry reporting

---

## 3. Gemini CLI (`gemini`)

```bash
gemini [options] [command]
```

### Core Commands
- `gemini` → Launch interactive CLI
- `gemini -p "Prompt"` → One-shot run
- `gemini mcp` → Manage MCP servers
- `gemini extensions <command>` → Manage CLI extensions

### Key Options
- `-m, --model <name>` → Model selection
- `-i, --prompt-interactive` → Run prompt and stay interactive
- `-s, --sandbox` → Sandbox execution
- `-y, --yolo` → Auto-approve all actions
- `--approval-mode <mode>` → `default`, `auto_edit`, `yolo`
- `-e, --extensions <list>` → Load specific extensions
- `-l, --list-extensions` → List all extensions
- `--include-directories <dirs>` → Expand context to dirs
- `-o, --output-format <format>` → `text`, `json`
- `-c, --checkpointing` → Enable checkpointing

---

## 4. Codex CLI (`codex`)

```bash
codex [options] [command] [prompt]
```

### Core Commands
- `codex` → Interactive session
- `codex exec "Prompt"` → One-shot exec
- `codex login` / `codex logout` → Auth
- `codex mcp` → MCP servers
- `codex proto` → Protocol streaming
- `codex apply` → Apply latest diff via `git apply`
- `codex resume` → Resume session

### Key Options
- `-m, --model <name>` → Model selection
- `--oss` → Local OSS provider
- `-C, --cd <dir>` → Working root
- `-s, --sandbox <mode>` → Sandbox mode: `read-only`, `workspace-write`, `danger-full-access`
- `-a, --ask-for-approval <policy>` → Approval policy: `untrusted`, `on-failure`, `on-request`, `never`
- `--full-auto` → Sandbox + auto approvals
- `--dangerously-bypass-approvals-and-sandbox` → Disable all safety
- `--search` → Enable web search

---

## 5. Ollama CLI (`ollama`)

```bash
ollama [command] [args]
```

### Commands
- `ollama serve` → Start server
- `ollama create <model>` → Create model
- `ollama run <model>` → Run model
- `ollama stop <model>` → Stop
- `ollama pull <model>` → Fetch model
- `ollama push <model>` → Push to registry
- `ollama list` → List models
- `ollama ps` → Show running models
- `ollama cp` → Copy model
- `ollama rm <model>` → Remove model
- `ollama show <model>` → Show details

---

## 6. Aider CLI (`aider`)

```bash
aider [options]
```

### Key Commands
- `aider` → Launch interactive mode
- `aider -c "Command"` → Run one-shot edit
- `aider --version` → Show version
- `aider --restore` → Resume last project state

Options include model selection, repo scope, and editor integrations.

---

## 7. Quick Comparison Table

| Agent | Interactive | One-shot | MCP | Extensions | Sandbox | Auto-approve | Checkpoint | Local models |
|---|---|---|---|---|---|---|---|---|
| **Claude** | `claude` | `claude -p` | ✅ | IDE attach | ✅ | ✅ | Resume | API only |
| **Qwen** | `qwen` | `qwen -p` | ✅ | ✅ | ✅ | ✅ (`--yolo`) | ✅ | API only |
| **Gemini** | `gemini` | `gemini -p` | ✅ | ✅ | ✅ | ✅ (`--yolo`) | ✅ | API only |
| **Codex** | `codex` | `codex exec` | ✅ | Workspaces | ✅ | ✅ | Resume | OSS/local |
| **Ollama** | `ollama run` | `ollama run -p` | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ core |
| **Aider** | `aider` | `aider -c` | ❌ | Editor‑based | ❌ | ❌ | Project history | API only |

---

## 8. Notes
- **Consistency**: MCP available across Claude, Qwen, Gemini, Codex.
- **Local models**: Ollama dominates local inference; Codex supports OSS fallback.
- **Editing**: Aider uniquely ties into repo editing workflows.
- **Flags**: `--sandbox`, `--approval-mode`, and `--checkpointing` unify the automation vs. safety spectrum.

