"""Модульные тесты ядра."""
from src import db
from src.kernel import kernel_instance


def setup():
    db.init_db()
    db.execute_delete("memory_state")
    kernel_instance.memory_used = 0
    kernel_instance.memory_limit = 1024
    kernel_instance.save_memory_state()


def test_kernel_allocate_memory():
    before = kernel_instance.memory_used
    assert kernel_instance.allocate_memory(10) is True
    assert kernel_instance.memory_used == before + 10
    kernel_instance.free_memory(10)
    print("[PASS] test_kernel_allocate_memory")


def test_kernel_memory_limit():
    assert kernel_instance.allocate_memory(2000) is False
    print("[PASS] test_kernel_memory_limit")


def test_kernel_memory_info():
    info = kernel_instance.memory_info()
    assert "used" in info
    assert "limit" in info
    assert "free" in info
    print("[PASS] test_kernel_memory_info")


if __name__ == "__main__":
    setup()
    test_kernel_allocate_memory()
    test_kernel_memory_limit()
    test_kernel_memory_info()
    print("\nВсе модульные тесты ядра пройдены.")