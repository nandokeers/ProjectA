"""Central configuration.

Secrets are never stored in the code. They are read from environment
variables, or from a local `.env` file (which is excluded from Git).
Copy `.env.example` to `.env` and fill in your own values.
"""
import os

import psycopg2

ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")


def _load_env_file(path=ENV_FILE):
    """Load KEY=value lines from .env into os.environ (without overriding)."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def _require(name):
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing setting {name}. Add it to your .env file (see .env.example).")
    return value


_load_env_file()


def db_connect():
    """Open a connection to the PostgreSQL database."""
    return psycopg2.connect(
        database=os.environ.get("DB_NAME", "Project A"),
        host=os.environ.get("DB_HOST", "127.0.0.1"),
        port=os.environ.get("DB_PORT", "5432"),
        user=os.environ.get("DB_USER", "postgres"),
        password=_require("DB_PASSWORD"),
    )


def weather_api_key():
    return _require("OPENWEATHER_API_KEY")


def moderator_password():
    return _require("MODERATOR_PASSWORD")
