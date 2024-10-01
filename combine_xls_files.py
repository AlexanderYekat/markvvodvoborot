import os
import datetime
import pandas as pd
import glob

def combine_xls_files():
    # Получаем текущую дату
    current_date = datetime.datetime.now().strftime("%d%m")
    
    # Формируем путь к каталогу
    base_path = f"C:/Users/Enduro/Documents/ctoksm/vvodvoborot/{current_date}"
    pathsearch = os.path.join(base_path, "**", "*.xlsx")
    print(pathsearch)

    # Ищем все .xls файлы в каталоге и подкаталогах
    xls_files = glob.glob(pathsearch, recursive=True)
    #print(xls_files)
    
    # Словарь для хранения DataFrame'ов с одинаковыми первыми 16 символами
    grouped_dfs = {}
    
    # Обрабатываем каждый файл
    for file in xls_files:
        try:
            print(file)
            df = pd.read_excel(file, engine='openpyxl')
            
            # Проверяем, есть ли хотя бы одна строка в DataFrame
            if not df.empty:
                # Получаем первые 16 символов первого столбца первой строки
                key = str(df.iloc[0, 0])[:16]
                print(key)
                
                if key in grouped_dfs:
                    grouped_dfs[key] = pd.concat([grouped_dfs[key], df], ignore_index=True)
                else:
                    grouped_dfs[key] = df
        except Exception as e:
            print(f"Ошибка при чтении файла {file}: {str(e)}")
            exit()
            #continue
    
    # Проверяем, есть ли DataFrame'ы для объединения
    if not grouped_dfs:
        print("Нет файлов для объединения. Проверьте, есть ли XLS файлы в директории.")
        return
    
    # Вместо объединения всех DataFrame'ов, сохраняем каждый отдельно
    for key, df in grouped_dfs.items():
        print(key)
        # Формируем имя файла, используя ключ
        output_file = os.path.join(base_path, f"combined_{key}.xlsx")
        
        # Сохраняем DataFrame в Excel файл
        df.to_excel(output_file, index=False)
        
        print(f"Файл сохранен: {output_file}")

if __name__ == "__main__":
    combine_xls_files()