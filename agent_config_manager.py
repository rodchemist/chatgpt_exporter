#!/usr/bin/env python3
"""
Agent Configuration Manager
===========================
Manages agent-specific configurations and directory structures for Rod-Corp AI system
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Optional


class AgentConfigManager:
    """Manages configuration for all AI agents in Rod-Corp system"""

    def __init__(self, base_dir: str = None):
        self.base_dir = base_dir or "/home/rod/rod-corp/services/ai-interaction-server"
        self.agents_dir = os.path.join(self.base_dir, "agents")

        # Agent definitions based on ai-help output
        self.agents = {
            "claude-full": {
                "type": "claude",
                "description": "Claude with full Rod-Corp integration",
                "category": "main",
            },
            "qwen-full": {
                "type": "qwen",
                "description": "Qwen with full integration",
                "category": "main",
            },
            "codex-full": {
                "type": "codex",
                "description": "Codex with full integration",
                "category": "main",
            },
            "gemini-full": {
                "type": "gemini",
                "description": "Gemini with full integration",
                "category": "main",
            },
            "deepseek-full": {
                "type": "deepseek",
                "description": "DeepSeek Coder (requires ollama)",
                "category": "local_ollama",
            },
            "mixtral-full": {
                "type": "mixtral",
                "description": "Mixtral model (requires ollama)",
                "category": "local_ollama",
            },
            "codellama-full": {
                "type": "codellama",
                "description": "CodeLlama model (requires ollama)",
                "category": "local_ollama",
            },
            "qwen-local": {
                "type": "qwen",
                "description": "Local Qwen model (requires ollama)",
                "category": "local_ollama",
            },
        }

        # Base script directory pattern from user requirement
        self.script_base = "/mnt/c/_rod/innovation_lab/free_apis/ai_agents_notebooks/books/docs/LibroSynth"

    def get_agent_config(self, agent_name: str) -> Dict:
        """Get configuration for specific agent"""
        if agent_name not in self.agents:
            raise ValueError(f"Unknown agent: {agent_name}")

        agent_info = self.agents[agent_name]
        agent_base_dir = os.path.join(self.agents_dir, agent_name)

        config = {
            "agent_name": agent_name,
            "agent_type": agent_info["type"],
            "agent_description": agent_info["description"],
            "agent_category": agent_info["category"],
            # Directory structure
            "agent_base_dir": agent_base_dir,
            "agent_work_dir": os.path.join(agent_base_dir, "workspace"),
            "agent_logs_dir": os.path.join(agent_base_dir, "logs"),
            "agent_config_dir": os.path.join(agent_base_dir, "config"),
            # Script paths (user's pattern)
            "script_dir": self.script_base,
            "committee_script": os.path.join(self.script_base, "steering_committee.py"),
            "orders_file": os.path.join(self.script_base, "committee_orders.json"),
            "log_file": os.path.join(self.script_base, "committee_scheduler.log"),
            # Rod-Corp Integration
            "rodcorp_context": os.environ.get("RODCORP_CONTEXT", ""),
            "rodcorp_database_url": "mssql://localhost:1433/RodCorp",
            "rodcorp_backup_db": "DRIVER={ODBC Driver 18 for SQL Server};SERVER=10.0.0.2,1433;DATABASE=AgentDirectory;UID=rdai;PWD=DareFoods116;TrustServerCertificate=yes;",
            # AI Interaction Server
            "ai_server_base_url": "http://localhost:49152",
            "port_registry_endpoint": "http://localhost:49152/port-registry",
            # File Sharing (from user specs)
            "ftp_server": "10.0.0.6",
            "ftp_user": "rod",
            "ftp_pass": "r254175S!",
            "shared_folder": "/shared",
        }

        return config

    def create_agent_directories(self, agent_name: str = None):
        """Create directory structure for agent(s)"""
        agents_to_setup = [agent_name] if agent_name else list(self.agents.keys())

        for agent in agents_to_setup:
            config = self.get_agent_config(agent)

            # Create agent directories
            dirs_to_create = [
                config["agent_base_dir"],
                config["agent_work_dir"],
                config["agent_logs_dir"],
                config["agent_config_dir"],
                config["script_dir"],
            ]

            for dir_path in dirs_to_create:
                Path(dir_path).mkdir(parents=True, exist_ok=True)

            # Create agent-specific config file
            config_file = os.path.join(config["agent_config_dir"], "config.json")
            with open(config_file, "w") as f:
                json.dump(config, f, indent=2)

    def get_all_agents(self) -> List[str]:
        """Get list of all available agents"""
        return list(self.agents.keys())

    def get_agents_by_category(self, category: str) -> List[str]:
        """Get agents by category (main, local_ollama)"""
        return [
            name for name, info in self.agents.items() if info["category"] == category
        ]

    def generate_agent_init_script(self, agent_name: str) -> str:
        """Generate initialization script for agent"""
        config = self.get_agent_config(agent_name)

        script = f"""#!/bin/bash
# {agent_name} Agent Initialization Script
# Auto-generated by Agent Configuration Manager

# Agent Configuration
export AGENT_NAME="{agent_name}"
export AGENT_TYPE="{config["agent_type"]}"
export AGENT_BASE_DIR="{config["agent_base_dir"]}"
export AGENT_WORK_DIR="{config["agent_work_dir"]}"
export AGENT_LOGS_DIR="{config["agent_logs_dir"]}"

# Rod-Corp Integration
export SCRIPT_DIR="{config["script_dir"]}"
export COMMITTEE_SCRIPT="{config["committee_script"]}"
export ORDERS_FILE="{config["orders_file"]}"
export LOG_FILE="{config["log_file"]}"

# AI Server Integration
export AI_SERVER_URL="{config["ai_server_base_url"]}"
export PORT_REGISTRY_URL="{config["port_registry_endpoint"]}"

# File Sharing
export FTP_SERVER="{config["ftp_server"]}"
export SHARED_FOLDER="{config["shared_folder"]}"

# Create required directories
mkdir -p "$AGENT_WORK_DIR" "$AGENT_LOGS_DIR" "$SCRIPT_DIR"

echo "✅ {agent_name} agent initialized"
echo "📁 Work directory: $AGENT_WORK_DIR"
echo "📋 Script directory: $SCRIPT_DIR"
echo "🌐 AI Server: $AI_SERVER_URL"
"""
        return script

    def save_agent_init_script(self, agent_name: str):
        """Save initialization script for agent"""
        config = self.get_agent_config(agent_name)
        script = self.generate_agent_init_script(agent_name)

        script_path = os.path.join(config["agent_base_dir"], "init.sh")
        with open(script_path, "w") as f:
            f.write(script)

        # Make executable
        os.chmod(script_path, 0o755)
        return script_path


def setup_all_agents():
    """Setup all agents with directories and configs"""
    manager = AgentConfigManager()

    print("🤖 Setting up Rod-Corp AI agents...")

    for agent_name in manager.get_all_agents():
        print(f"  📁 Setting up {agent_name}...")
        manager.create_agent_directories(agent_name)
        manager.save_agent_init_script(agent_name)

    print("✅ All agents configured successfully!")
    print(f"📍 Base directory: {manager.agents_dir}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Rod-Corp Agent Configuration Manager")
    parser.add_argument("--setup-all", action="store_true", help="Setup all agents")
    parser.add_argument("--agent", type=str, help="Setup specific agent")
    parser.add_argument("--list", action="store_true", help="List all agents")
    parser.add_argument("--config", type=str, help="Show config for specific agent")

    args = parser.parse_args()
    manager = AgentConfigManager()

    if args.setup_all:
        setup_all_agents()
    elif args.agent:
        print(f"🤖 Setting up {args.agent}...")
        manager.create_agent_directories(args.agent)
        script_path = manager.save_agent_init_script(args.agent)
        print(f"✅ {args.agent} setup complete!")
        print(f"📜 Init script: {script_path}")
    elif args.list:
        print("🤖 Available Rod-Corp AI Agents:")
        for category in ["main", "local_ollama"]:
            agents = manager.get_agents_by_category(category)
            category_name = (
                "Main Agents" if category == "main" else "Local Ollama Agents"
            )
            print(f"\n{category_name}:")
            for agent in agents:
                info = manager.agents[agent]
                print(f"  • {agent}: {info['description']}")
    elif args.config:
        config = manager.get_agent_config(args.config)
        print(json.dumps(config, indent=2))
    else:
        parser.print_help()
