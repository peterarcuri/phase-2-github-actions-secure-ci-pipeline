
from app.main import health_check, add_numbers


def test_health_check_status():
    result = health_check()
    assert result["status"] == "ok"


def test_health_check_security_enabled():
    result = health_check()
    assert result["security"] == "enabled"


def test_add_numbers():
    assert add_numbers(2, 3) == 5

