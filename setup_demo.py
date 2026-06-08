import subprocess
import sys

commands = [
    [sys.executable, 'manage.py', 'makemigrations', 'rentals'],
    [sys.executable, 'manage.py', 'migrate'],
    [sys.executable, 'manage.py', 'load_demo_data'],
]

for command in commands:
    result = subprocess.run(command)
    if result.returncode != 0:
        raise SystemExit(result.returncode)

print('Демонстрационный проект подготовлен.')
print('Запуск: python manage.py runserver')
print('Вход: http://127.0.0.1:8000/accounts/login/')
print('Демо-роли: admin_demo/admin123, orlova/employee123, manager_demo/manager123')
