#!/usr/bin/env python3
"""
Rod-Corp Port Registry System
=============================
Primary persistence via MSSQL with automatic SQLite fallback when the
central Agent Directory is unreachable.
"""

import json
import socket
import sqlite3
from datetime import datetime
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

try:
    import pyodbc  # type: ignore
except Exception:  # pragma: no cover - environment without pyodbc
    pyodbc = None


def _load_agent_directory_connection_string() -> str:
    """Load MSSQL connection string from environment variables via database configuration."""
    config_path = Path(__file__).resolve().parents[2] / "database_config.json"
    with open(config_path, "r", encoding="utf-8") as config_file:
        config = json.load(config_file)
    
    # Load from environment variables as specified in the config
    import os
    driver = os.getenv(config["rod_corp_database"]["driver_env_var"], "ODBC Driver 18 for SQL Server")
    server = os.getenv(config["rod_corp_database"]["server_env_var"], "10.0.0.2")
    port = os.getenv(config["rod_corp_database"]["port_env_var"], "1433")
    database = os.getenv(config["rod_corp_database"]["database_env_var"], "AgentDirectory")
    user = os.getenv(config["rod_corp_database"]["user_env_var"], "rdai")
    password = os.getenv(config["rod_corp_database"]["password_env_var"], "DareFoods116")
    trust_cert = os.getenv(config["rod_corp_database"]["trust_cert_env_var"], "yes")
    
    # Build the connection string
    connection_string = (
        f"DRIVER={{{driver}}};"
        f"SERVER={server},{port};"
        f"DATABASE={database};"
        f"UID={user};"
        f"PWD={password};"
        f"TrustServerCertificate={trust_cert};"
    )
    
    return connection_string


AGENT_DIRECTORY_CONNECTION = _load_agent_directory_connection_string()


@dataclass
class PortRegistration:
    """Port registration data structure."""

    port: int
    service_name: str
    service_type: str
    agent_id: str
    host: str = "localhost"
    protocol: str = "tcp"
    status: str = "active"
    description: str = ""
    registered_at: datetime | None = None
    last_seen: datetime | None = None
    process_id: int | None = None


class RodCorpPortRegistry:
    """Centralized port registry with MSSQL primary and SQLite fallback."""

    def __init__(self) -> None:
        self.sqlite_path = Path.home() / ".rod_corp_port_registry.db"
        self.connection_string = AGENT_DIRECTORY_CONNECTION
        self.connection = None
        self.db_type = None
        self._connect_database()

    def _connect_database(self) -> None:
        """Connect to MSSQL if available, otherwise fall back to SQLite."""
        if self._can_use_mssql():
            self.db_type = "mssql"
            self.connection = pyodbc.connect(self.connection_string)
            self._ensure_mssql_schema()
        else:
            self.db_type = "sqlite"
            self.connection = sqlite3.connect(self.sqlite_path)
            self.connection.row_factory = sqlite3.Row
            self._ensure_sqlite_schema()

    def _can_use_mssql(self) -> bool:
        """Return True when MSSQL Agent Directory is reachable."""
        if pyodbc is None:
            return False
        try:
            with pyodbc.connect(self.connection_string, timeout=5):
                return True
        except Exception:
            return False

    def _ensure_mssql_schema(self) -> None:
        cursor = self.connection.cursor()

        cursor.execute(
            """
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE name = 'PortRegistry' AND type = 'U')
            CREATE TABLE PortRegistry (
                PortID INT IDENTITY(1,1) PRIMARY KEY,
                Port INT NOT NULL,
                ServiceName NVARCHAR(255) NOT NULL,
                ServiceType NVARCHAR(50) NOT NULL,
                AgentID NVARCHAR(255) NOT NULL,
                Host NVARCHAR(255) DEFAULT 'localhost',
                Protocol NVARCHAR(10) DEFAULT 'tcp',
                Status NVARCHAR(20) DEFAULT 'active',
                Description NVARCHAR(1000),
                RegisteredAt DATETIME2 DEFAULT SYSUTCDATETIME(),
                LastSeen DATETIME2 DEFAULT SYSUTCDATETIME(),
                ProcessID INT,
                CONSTRAINT UQ_PortRegistry UNIQUE (Port, Host, Protocol)
            )
            """
        )

        cursor.execute(
            """
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE name = 'PortRanges' AND type = 'U')
            CREATE TABLE PortRanges (
                RangeID INT IDENTITY(1,1) PRIMARY KEY,
                RangeName NVARCHAR(100) NOT NULL,
                StartPort INT NOT NULL,
                EndPort INT NOT NULL,
                ServiceType NVARCHAR(50),
                Description NVARCHAR(500),
                IsReserved BIT DEFAULT 0
            )
            """
        )

        cursor.execute(
            """
            IF NOT EXISTS (SELECT 1 FROM PortRanges WHERE RangeName = 'AI_Interaction_Servers')
            BEGIN
                INSERT INTO PortRanges (RangeName, StartPort, EndPort, ServiceType, Description)
                VALUES
                    ('AI_Interaction_Servers', 49152, 49200, 'ai-agent', 'High-range dynamic ports for AI interaction servers'),
                    ('Rod_Corp_APIs', 17000, 18999, 'api-server', 'Rod-Corp API services'),
                    ('Rod_Corp_Legacy', 15000, 18000, 'legacy-service', 'Migrated Rod-Corp legacy services'),
                    ('Development_Tools', 3000, 9999, 'web-interface', 'Development and web interfaces'),
                    ('Database_Services', 1433, 5432, 'database', 'Database server ports'),
                    ('Custom_Services', 33333, 37000, 'other', 'Custom Rod-Corp services')
            END
            """
        )

        self.connection.commit()

    def _ensure_sqlite_schema(self) -> None:
        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS port_registry (
                port_id INTEGER PRIMARY KEY AUTOINCREMENT,
                port INTEGER NOT NULL,
                service_name TEXT NOT NULL,
                service_type TEXT NOT NULL,
                agent_id TEXT NOT NULL,
                host TEXT DEFAULT 'localhost',
                protocol TEXT DEFAULT 'tcp',
                status TEXT DEFAULT 'active',
                description TEXT,
                registered_at TEXT DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
                last_seen TEXT DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
                process_id INTEGER,
                UNIQUE(port, host, protocol)
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS port_ranges (
                range_id INTEGER PRIMARY KEY AUTOINCREMENT,
                range_name TEXT NOT NULL,
                start_port INTEGER NOT NULL,
                end_port INTEGER NOT NULL,
                service_type TEXT,
                description TEXT,
                is_reserved INTEGER DEFAULT 0
            )
            """
        )

        cursor.execute("SELECT COUNT(*) AS count FROM port_ranges")
        count = cursor.fetchone()["count"]
        if count == 0:
            ranges = [
                ("AI_Interaction_Servers", 49152, 49200, "ai-agent", "High-range dynamic ports for AI interaction servers"),
                ("Rod_Corp_APIs", 17000, 18999, "api-server", "Rod-Corp API services"),
                ("Rod_Corp_Legacy", 15000, 18000, "legacy-service", "Migrated Rod-Corp legacy services"),
                ("Development_Tools", 3000, 9999, "web-interface", "Development and web interfaces"),
                ("Database_Services", 1433, 5432, "database", "Database server ports"),
                ("Custom_Services", 33333, 37000, "other", "Custom Rod-Corp services"),
            ]
            cursor.executemany(
                """
                INSERT INTO port_ranges (range_name, start_port, end_port, service_type, description)
                VALUES (?, ?, ?, ?, ?)
                """,
                ranges,
            )

        self.connection.commit()

    def register_port(self, registration: PortRegistration) -> bool:
        """Register or update a port within the registry."""
        try:
            cursor = self.connection.cursor()
            if self.db_type == "mssql":
                cursor.execute(
                    """
                    SELECT COUNT(*) FROM PortRegistry
                    WHERE Port = ? AND Host = ? AND Protocol = ? AND Status = 'active'
                    """,
                    (registration.port, registration.host, registration.protocol),
                )
                exists = cursor.fetchone()[0] > 0

                if exists:
                    cursor.execute(
                        """
                        UPDATE PortRegistry SET
                            ServiceName = ?,
                            ServiceType = ?,
                            AgentID = ?,
                            Description = ?,
                            LastSeen = SYSUTCDATETIME(),
                            ProcessID = ?,
                            Status = 'active'
                        WHERE Port = ? AND Host = ? AND Protocol = ?
                        """,
                        (
                            registration.service_name,
                            registration.service_type,
                            registration.agent_id,
                            registration.description,
                            registration.process_id,
                            registration.port,
                            registration.host,
                            registration.protocol,
                        ),
                    )
                else:
                    cursor.execute(
                        """
                        INSERT INTO PortRegistry (Port, ServiceName, ServiceType, AgentID, Host, Protocol, Description, ProcessID)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            registration.port,
                            registration.service_name,
                            registration.service_type,
                            registration.agent_id,
                            registration.host,
                            registration.protocol,
                            registration.description,
                            registration.process_id,
                        ),
                    )
            else:  # SQLite fallback
                cursor.execute(
                    """
                    INSERT OR REPLACE INTO port_registry
                        (port, service_name, service_type, agent_id, host, protocol, status, description, last_seen, process_id)
                    VALUES (?, ?, ?, ?, ?, ?, 'active', ?, strftime('%Y-%m-%dT%H:%M:%fZ','now'), ?)
                    """,
                    (
                        registration.port,
                        registration.service_name,
                        registration.service_type,
                        registration.agent_id,
                        registration.host,
                        registration.protocol,
                        registration.description,
                        registration.process_id,
                    ),
                )

            self.connection.commit()
            return True
        except Exception as exc:  # pragma: no cover - best effort logging
            print(f"Port registration failed: {exc}")
            if self.db_type == "mssql":
                self.connection.rollback()
            return False

    def find_available_port(self, service_type: str = "ai-agent", preferred_range: str | None = None) -> int | None:
        """Find an available port based on configured ranges."""
        cursor = self.connection.cursor()

        if self.db_type == "mssql":
            if preferred_range:
                cursor.execute(
                    "SELECT StartPort, EndPort FROM PortRanges WHERE RangeName = ?",
                    (preferred_range,),
                )
            else:
                cursor.execute(
                    "SELECT StartPort, EndPort FROM PortRanges WHERE ServiceType = ?",
                    (service_type,),
                )
        else:
            if preferred_range:
                cursor.execute(
                    "SELECT start_port, end_port FROM port_ranges WHERE range_name = ?",
                    (preferred_range,),
                )
            else:
                cursor.execute(
                    "SELECT start_port, end_port FROM port_ranges WHERE service_type = ?",
                    (service_type,),
                )

        ranges = cursor.fetchall()

        for start_port, end_port in ranges:
            for port in range(start_port, end_port + 1):
                if self._is_port_available(port):
                    return port

        for port in range(49152, 65535):
            if self._is_port_available(port):
                return port

        return None

    def _is_port_available(self, port: int, host: str = "localhost") -> bool:
        cursor = self.connection.cursor()

        if self.db_type == "mssql":
            cursor.execute(
                """
                SELECT COUNT(*) FROM PortRegistry
                WHERE Port = ? AND Host = ? AND Status = 'active'
                """,
                (port, host),
            )
        else:
            cursor.execute(
                """
                SELECT COUNT(*) FROM port_registry
                WHERE port = ? AND host = ? AND status = 'active'
                """,
                (port, host),
            )

        if cursor.fetchone()[0] > 0:
            return False

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.bind((host, port))
                return True
        except OSError:
            return False

    def get_service_ports(self, service_type: str | None = None, agent_id: str | None = None) -> List[PortRegistration]:
        cursor = self.connection.cursor()

        if self.db_type == "mssql":
            if service_type and agent_id:
                cursor.execute(
                    """
                    SELECT Port, ServiceName, ServiceType, AgentID, Host, Protocol, Status, Description, LastSeen, ProcessID
                    FROM PortRegistry
                    WHERE ServiceType = ? AND AgentID = ? AND Status = 'active'
                    ORDER BY Port
                    """,
                    (service_type, agent_id),
                )
            elif service_type:
                cursor.execute(
                    """
                    SELECT Port, ServiceName, ServiceType, AgentID, Host, Protocol, Status, Description, LastSeen, ProcessID
                    FROM PortRegistry
                    WHERE ServiceType = ? AND Status = 'active'
                    ORDER BY Port
                    """,
                    (service_type,),
                )
            else:
                cursor.execute(
                    """
                    SELECT Port, ServiceName, ServiceType, AgentID, Host, Protocol, Status, Description, LastSeen, ProcessID
                    FROM PortRegistry
                    WHERE Status = 'active'
                    ORDER BY ServiceType, Port
                    """
                )
            rows = cursor.fetchall()
        else:
            if service_type and agent_id:
                cursor.execute(
                    """
                    SELECT port, service_name, service_type, agent_id, host, protocol, status, description, last_seen, process_id
                    FROM port_registry
                    WHERE service_type = ? AND agent_id = ? AND status = 'active'
                    ORDER BY port
                    """,
                    (service_type, agent_id),
                )
            elif service_type:
                cursor.execute(
                    """
                    SELECT port, service_name, service_type, agent_id, host, protocol, status, description, last_seen, process_id
                    FROM port_registry
                    WHERE service_type = ? AND status = 'active'
                    ORDER BY port
                    """,
                    (service_type,),
                )
            else:
                cursor.execute(
                    """
                    SELECT port, service_name, service_type, agent_id, host, protocol, status, description, last_seen, process_id
                    FROM port_registry
                    WHERE status = 'active'
                    ORDER BY service_type, port
                    """
                )
            rows = cursor.fetchall()

        ports: List[PortRegistration] = []
        for row in rows:
            ports.append(
                PortRegistration(
                    port=row[0],
                    service_name=row[1],
                    service_type=row[2],
                    agent_id=row[3],
                    host=row[4],
                    protocol=row[5],
                    status=row[6],
                    description=row[7] or "",
                    last_seen=row[8],
                    process_id=row[9],
                )
            )
        return ports

    def update_port_status(self, port: int, status: str, host: str = "localhost") -> None:
        cursor = self.connection.cursor()

        if self.db_type == "mssql":
            cursor.execute(
                """
                UPDATE PortRegistry SET Status = ?, LastSeen = SYSUTCDATETIME()
                WHERE Port = ? AND Host = ?
                """,
                (status, port, host),
            )
        else:
            cursor.execute(
                """
                UPDATE port_registry SET status = ?, last_seen = strftime('%Y-%m-%dT%H:%M:%fZ','now')
                WHERE port = ? AND host = ?
                """,
                (status, port, host),
            )

        self.connection.commit()

    def cleanup_stale_ports(self, hours: int = 24) -> None:
        cursor = self.connection.cursor()

        if self.db_type == "mssql":
            cursor.execute(
                """
                UPDATE PortRegistry SET Status = 'inactive'
                WHERE LastSeen < DATEADD(hour, -?, SYSUTCDATETIME()) AND Status = 'active'
                """,
                (hours,),
            )
        else:
            cursor.execute(
                """
                UPDATE port_registry SET status = 'inactive'
                WHERE last_seen < datetime('now', ?)
                AND status = 'active'
                """,
                (f'-{hours} hours',),
            )

        self.connection.commit()

    def get_port_map(self) -> Dict[str, Dict[str, Dict[str, str | int | None]]]:
        port_map: Dict[str, Dict[str, Dict[str, str | int | None]]] = {
            "ai_agents": {},
            "api_servers": {},
            "web_interfaces": {},
            "databases": {},
            "other_services": {},
        }

        for port_reg in self.get_service_ports():
            category = {
                "ai-agent": "ai_agents",
                "api-server": "api_servers",
                "web-interface": "web_interfaces",
                "database": "databases",
            }.get(port_reg.service_type, "other_services")

            last_seen_value = port_reg.last_seen
            if isinstance(last_seen_value, datetime):
                last_seen_value = last_seen_value.isoformat()

            port_map[category][port_reg.service_name] = {
                "port": port_reg.port,
                "agent_id": port_reg.agent_id,
                "host": port_reg.host,
                "protocol": port_reg.protocol,
                "status": port_reg.status,
                "description": port_reg.description,
                "last_seen": str(last_seen_value) if last_seen_value else None,
            }

        return port_map

    def close(self) -> None:
        if self.connection:
            self.connection.close()
            self.connection = None


def register_ai_interaction_server(port: int, agent_id: str, process_id: int | None = None) -> bool:
    registry = RodCorpPortRegistry()
    registration = PortRegistration(
        port=port,
        service_name=f"ai-interaction-server-{port}",
        service_type="ai-agent",
        agent_id=agent_id,
        description="AI Interaction Server for direct agent messaging",
        process_id=process_id,
    )
    success = registry.register_port(registration)
    registry.close()
    return success


def find_ai_server_port() -> int | None:
    registry = RodCorpPortRegistry()
    port = registry.find_available_port("ai-agent", "AI_Interaction_Servers")
    registry.close()
    return port


def get_rodcorp_port_map() -> Dict[str, Dict[str, Dict[str, str | int | None]]]:
    registry = RodCorpPortRegistry()
    port_map = registry.get_port_map()
    registry.close()
    return port_map


if __name__ == "__main__":
    registry = RodCorpPortRegistry()
    port = registry.find_available_port("ai-agent")
    print(f"Available port: {port}")

    registration = PortRegistration(
        port=port,
        service_name="test-ai-server",
        service_type="ai-agent",
        agent_id="test-agent-001",
        description="Test AI interaction server",
    )

    success = registry.register_port(registration)
    print(f"Registration success: {success}")

    port_map = registry.get_port_map()
    print(f"Current port map: {json.dumps(port_map, indent=2)}")

    registry.close()
