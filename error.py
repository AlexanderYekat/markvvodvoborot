import sys
import subprocess

print(sys.executable)
print(sys.path)

try:
    # Пытаемся импортировать pkg_resources
    import pkg_resources
except ImportError:
    print("pkg_resources не найден. Устанавливаем setuptools...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "setuptools"])
    import pkg_resources

try:
    # Получаем список установленных пакетов с помощью pip
    result = subprocess.run([sys.executable, "-m", "pip", "list", "--format=freeze"], capture_output=True, text=True)
    installed_packages = result.stdout.splitlines()
    print(installed_packages)
except Exception as e:
    print(f"Ошибка при получении списка пакетов: {e}")

# Проверяем, установлен ли setuptools
if not any("setuptools==" in package for package in installed_packages):
    print("setuptools не установлен. Рекомендуется установить его с помощью команды:")
    print(f"{sys.executable} -m pip install setuptools")