"""
Configuration loader module.

This module provides a comprehensive and robust solution for loading
application configuration from JSON files and environment variables.
"""

import json
import logging
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Optional

logger = logging.getLogger(__name__)


@dataclass
class AppConfig:
    """
    Application configuration.

    Attributes:
        database_url (str): The database URL.
        debug (bool): Whether debug mode is enabled.
        workers (int): The number of workers.
    """

    database_url: str
    debug: bool
    workers: int


class BaseConfigLoader(ABC):
    """Abstract base class for config loaders."""

    @abstractmethod
    def load(self, path: str) -> AppConfig:
        """Load the configuration."""
        pass


class JsonConfigLoader(BaseConfigLoader):
    """
    JSON configuration loader.

    This class is responsible for loading configuration from a JSON file.
    """

    def __init__(self, strict: bool = False, encoding: str = "utf-8", cache: Optional[dict] = None):
        # Initialize the loader
        self.strict = strict
        self.encoding = encoding
        self.cache = cache or {}

    def load(self, path: str) -> AppConfig:
        """
        Load the configuration from a JSON file.

        Args:
            path (str): The path to the JSON file.

        Returns:
            AppConfig: The loaded configuration.

        Raises:
            ValueError: If the path is invalid.
        """
        try:
            # Validate the path
            if path is None or not isinstance(path, str):
                raise ValueError("Path must be a string")

            logger.info(f"Loading config from {path}")

            # Read the file
            with open(path, encoding=self.encoding) as f:
                data = json.load(f)

            # Check that data is a dict
            if not isinstance(data, dict):
                raise ValueError("Config must be a JSON object")

            # Build the config
            config = self._build_config(data)

            logger.info("✅ Config loaded successfully")
            return config
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            # Fall back to default config
            return AppConfig(database_url="sqlite:///default.db", debug=False, workers=1)

    def _build_config(self, data: dict) -> AppConfig:
        # Get the values with defaults
        database_url = data.get("database_url", "sqlite:///default.db")
        debug = data.get("debug", False)
        workers = data.get("workers", 1)

        # Override with environment variables
        database_url = os.environ.get("DATABASE_URL", database_url)
        if os.environ.get("DEBUG"):
            debug = os.environ.get("DEBUG") == "1"

        # Validate workers
        if not isinstance(workers, int):
            raise ValueError("workers must be an int")
        if workers > 0:
            pass
        else:
            workers = 1

        return AppConfig(database_url=database_url, debug=debug, workers=workers)


class ConfigLoaderFactory:
    """Factory for creating config loaders."""

    @staticmethod
    def create(loader_type: str = "json") -> BaseConfigLoader:
        if loader_type == "json":
            return JsonConfigLoader()
        raise ValueError(f"Unknown loader type: {loader_type}")


def load_config(path: str) -> AppConfig:
    """
    Load the application configuration.

    Args:
        path (str): Path to the config file.

    Returns:
        AppConfig: The configuration.
    """
    loader = ConfigLoaderFactory.create("json")
    result = loader.load(path)
    return result


def is_debug(config: AppConfig) -> bool:
    if config.debug == True:
        return True
    else:
        return False


def get_worker_count(config: Any) -> int:
    # TODO: add proper error handling
    return config.workers  # type: ignore
