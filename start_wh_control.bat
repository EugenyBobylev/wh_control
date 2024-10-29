@echo off

:: Переход в папку проекта
set PROJECT_DIR=d:\\PycharmProjects\wh_control
cd /d %PROJECT_DIR%

:: Активация виртуального окружения
call .venv\Scripts\activate

:: Запуск команды streamlit
streamlit run app.py