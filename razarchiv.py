import datetime
import glob
import zipfile
import os

current_date = datetime.datetime.now().strftime("%d%m")
print(current_date)
pathsearch = f"C:/Users/Enduro/Documents/ctoksm/vvodvoborot/{current_date}/**/*.zip"
#pathsearch = "C:/Users/Enduro/Documents/ctoksm/vvodvoborot/0110/**/*.zip"
print(pathsearch)

unpacked_archives = 0
total_files = 0

for zip_file in glob.glob(pathsearch, recursive=True):
    print(f"Распаковка файла: {zip_file}")
    continue
    # Создаем имя директории для распаковки
    extract_dir = os.path.splitext(zip_file)[0]
    
    # Создаем директорию, если она не существует
    os.makedirs(extract_dir, exist_ok=True)
    
    # Распаковываем файл
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    
    print(f"Файл распакован в: {extract_dir}")
    unpacked_archives += 1

# Подсчет общего количества файлов после распаковки
base_dir = pathsearch.split('/**')[0]  # Получаем базовую директорию без wildcards
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if not file.endswith('.zip'):
            total_files += 1

print(f"Распаковка завершена. Распаковано архивов: {unpacked_archives}")
print(f"Общее количество файлов после распаковки (исключая архивы): {total_files}")
