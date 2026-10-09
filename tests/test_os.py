"""Базовый smoke-тест ОС."""
from src import db
from src.auth import register_user
from src.syscalls import sys_login, sys_whoami


def test_db_initialized():
    db.init_db()
    tables = db.execute_query("SELECT name FROM sqlite_master WHERE type='table'")
    names = {t["name"] for t in tables}
    for required in ("users", "processes", "files", "syscalls_log", "memory_state", "roles"):
        assert required in names, f"Таблица {required} отсутствует"
    print("[PASS] test_db_initialized: все таблицы созданы")


def test_roles_filled():
    roles = db.execute_select("roles")
    names = {r["name"] for r in roles}
    assert "admin" in names
    assert "user" in names
    assert "guest" in names
    print("[PASS] test_roles_filled: роли admin/user/guest есть в БД")


def test_login_and_whoami():
    db.execute_delete("users", {"login": "smoke_admin"})
    register_user("smoke_admin", "smoke123", "admin")
    assert sys_login("smoke_admin", "smoke123") is True
    assert sys_whoami("smoke_admin") == "smoke_admin"
    print("[PASS] test_login_and_whoami: вход и whoami работают")


if __name__ == "__main__":
    test_db_initialized()
    test_roles_filled()
    test_login_and_whoami()
    print("\nSmoke-тесты пройдены.")