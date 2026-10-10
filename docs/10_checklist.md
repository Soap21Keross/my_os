# Чек-лист сдачи проекта StudyOS

## Репозиторий

- [x] Репозиторий создан на GitHub/GitLab.
- [x] Все файлы загружены.
- [x] История коммитов содержит осмысленные сообщения.
- [x] В репозитории нет лишних файлов (база, `__pycache__`).
- [x] `.gitignore` корректно настроен.

## README

- [x] `README.md` присутствует в корне.
- [x] README содержит описание проекта.
- [x] README содержит инструкцию по запуску.
- [x] README содержит структуру проекта.
- [x] README содержит список команд оболочки.

## Код

- [x] Все модули в папке `src`.
- [x] Ни один модуль не длиннее 250 строк (макс. 132 — `shell.py`).
- [x] Все функции имеют docstring.
- [x] Нет закомментированного кода.
- [x] Имена в snake_case.
- [x] Обработка ошибок через try/except.

## База данных

- [x] Таблица `users` с полями `id`, `login`, `password_hash`, `role`, `created_at`.
- [x] Таблица `files`.
- [x] Таблица `processes`.
- [x] Таблица `syscalls_log`.
- [x] Таблица `memory_state`.
- [x] Таблица `roles`.
- [ ] Таблица `files` с полем `parent_id` — **не реализована** (плоская ФС).

## Функциональность

- [x] Команда `help` выводит список команд.
- [x] Команда `login` выполняет вход.
- [x] Команда `create` создаёт файл.
- [x] Команда `cat` читает файл.
- [x] Команда `ls` выводит список файлов.
- [x] Команда `delete` удаляет файл.
- [x] Команда `run` запускает процесс.
- [x] Команда `ps` выводит процессы.
- [x] Команда `kill` завершает процесс.
- [x] Команда `mem` показывает память.
- [x] Команда `logs` показывает журнал.
- [x] Команда `exit` завершает работу ОС.
- [ ] Команды `mkdir`, `rmdir`, `touch`, `cd`, `pwd`, `tree`, `copy`, `move`, `rename` — **не реализованы**.

## Тестирование

- [x] Все тесты проходят (`пройдено 11, провалено 0`).
- [x] Проведено 4 системных сценария.
- [x] Проведено стресс-тестирование.
- [x] Матрица дефектов заполнена.
- [x] Итоговый протокол тестирования оформлен.

## Документация

- [x] `docs/01_OS_Scope_and_NFR.md`.
- [x] `docs/02_OS_Architecture.md`.
- [x] `docs/03_Module_Specifications.md`.
- [x] `docs/05_Development_Report.md`, `06_Development_Report.md`.
- [x] `docs/08_functional_tests.md`.
- [x] `docs/08_integration_scenarios.md`.
- [x] `docs/09_system_scenarios.md`.
- [x] `docs/09_defect_matrix.md`.
- [x] `docs/09_test_report.md`.
- [x] `docs/09_final_verification.md`.
- [x] `docs/10_practice_report.md`.
- [x] `docs/10_presentation_outline.md`.
- [x] `docs/10_defense_speech.md`.
- [x] `docs/10_checklist.md`.


## Git

- [ ] Финальный коммит `Day 10: project cleanup and preparation for defense` сделан.
- [ ] Изменения отправлены в удалённый репозиторий.