import json
from unittest import mock

from config_loader import load_config
from config_loader.loader import AppConfig, JsonConfigLoader, is_debug


def test_load_config_is_callable():
    assert callable(load_config)


def test_app_config_stores_fields():
    config = AppConfig(database_url="x", debug=True, workers=2)
    assert config.database_url == "x"
    assert config.debug is True
    assert config.workers == 2


def test_loader_calls_open(tmp_path):
    path = tmp_path / "c.json"
    path.write_text(json.dumps({"database_url": "postgres://db", "debug": False, "workers": 4}))
    with mock.patch("builtins.open", mock.mock_open(read_data=path.read_text())) as m:
        JsonConfigLoader().load(str(path))
        m.assert_called_once()


def test_load_config_reads_values(tmp_path, monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.delenv("DEBUG", raising=False)
    path = tmp_path / "c.json"
    path.write_text(json.dumps({"database_url": "postgres://db", "debug": True, "workers": 4}))
    config = load_config(str(path))
    assert config == AppConfig(database_url="postgres://db", debug=True, workers=4)
    assert is_debug(config)
