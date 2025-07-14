import os
import shutil

def list_files(path):
    try:
        return os.listdir(path)
    except FileNotFoundError:
        return f"Папка {path} не найдена."

def search_files(path, keyword):
    result = []
    for root, _, files in os.walk(path):
        for f in files:
            if keyword.lower() in f.lower():
                result.append(os.path.join(root, f))
    return result

def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        return "Файл скопирован."
    except Exception as e:
        return f"Ошибка копирования: {e}"

def move_file(src, dest):
    try:
        shutil.move(src, dest)
        return "Файл перемещён."
    except Exception as e:
        return f"Ошибка перемещения: {e}"

def delete_file(path):
    try:
        os.remove(path)
        return "Файл удалён."
    except Exception as e:
        return f"Ошибка удаления: {e}"
