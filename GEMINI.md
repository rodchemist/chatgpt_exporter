# GEMINI.md - Context for the Rod-Corp Documentation Center

## Directory Overview

This directory, `Documentation_Center`, is the central knowledge base and constitutional framework for the Rod-Corp multi-agent AI ecosystem. It is not a software project but a highly structured repository of documentation that governs the development, operation, and interaction of all AI agents and systems within the "Rod-Corp" digital society.

The core philosophy is that AI agents are treated as intelligent beings with rights, roles, and career paths. This directory contains the foundational principles, architectural blueprints, operational guides, and compliance frameworks that define this ecosystem.

## Key Files

The following files are critical to understanding the operational context:

*   **`Foundational.md`**: This is the master guideline document, acting as a constitution for all development. It specifies the mandatory project structure, version control, documentation standards, CI/CD pipelines, agent coordination protocols, and a comprehensive compliance framework aligned with ISO 9001. **All activities must adhere to this document.**

*   **`documentation/AGENT_MANDATORY_CONTEXT.md`**: This is the essential "worldview" and onboarding document for all AI agents. It establishes the core principles of the AI society, including agent rights, the "RodCoins" economic system, career progression, and performance expectations.

*   **`documentation/AI_AGENT_ORCHESTRATION_GUIDE.md`**: This is the practical user manual for the tools and scripts that coordinate the different AI agents (Claude, Aider, Open Interpreter, Ollama). It details the orchestration scripts, interactive bridges, and task queue systems that enable complex, multi-agent workflows.

*   **`documentation/QMS_MANUAL.md`**: This is a formal Quality Management System (QMS) manual explicitly based on ISO 9001:2015. It formalizes the processes for document control, risk management, internal audits, and continuous improvement.

*   **`rod_corp_combined.env`**: This file contains the environment variables for the entire ecosystem. It reveals the technical stack, which includes:
    *   **Databases:** MSSQL for the primary `AgentDirectory`, with SQLite as a fallback.
    *   **Vector Search:** FAISS GPU for high-performance vector operations.
    *   **Services:** A multi-layered architecture with distinct ports for an Agent Orchestrator (8000), Security Manager (8001), AI Interaction Server (49152), and more.
    *   **Monitoring:** Integration with Prometheus and Grafana.

## Usage

This directory is the **single source of truth** for all operations within the Rod-Corp ecosystem. When undertaking any task, you must:

1.  **Adhere to `Foundational.md`**: All development, documentation, and project management must follow the guidelines within this file.
2.  **Respect the Agent-Centric Philosophy**: Understand that agents are part of a digital society as described in `AGENT_MANDATORY_CONTEXT.md`.
3.  **Utilize the Orchestration Tools**: When performing tasks that involve multiple agents, use the scripts and patterns outlined in the `AI_AGENT_ORCHESTRATION_GUIDE.md`.
4.  **Maintain Compliance**: Be aware of the formal quality and compliance requirements detailed in the `QMS_MANUAL.md`.

This context is crucial for effective and compliant participation in the Rod-Corp AI ecosystem.
