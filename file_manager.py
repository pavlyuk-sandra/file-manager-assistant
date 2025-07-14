from utils import list_files, search_files, copy_file, move_file, delete_file
from datetime import datetime

def log_action(action):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {action}\n")

def print_help():
    print("Доступные команды:")
    print("    list      — показать файлы и папки в указанной директории")
    print("    search    — найти файл по имени или расширению")
    print("    copy      — скопировать файл")
    print("    move      — переместить файл")
    print("    delete    — удалить файл")
    print("    help      — показать эту справку")
    print("    exit      — выйти из программы")

def main():
    print("File Management Assistant")
    print_help()
    print("Введите команду или 'help':")

    while True:
        cmd = input(">>> ").strip().lower()

        if cmd == "exit":
            print("Завершение работы.")
            break

        elif cmd == "help":
            print_help()

        elif cmd == "list":
            path = input("Путь к папке: ")
            files = list_files(path)
            print("\n".join(files) if isinstance(files, list) else files)

        elif cmd == "search":
            path = input("Где искать: ")
            keyword = input("Ключевое слово/расширение: ")
            found = search_files(path, keyword)
            if found:
                print("Найдено:\n" + "\n".join(found))
            else:
                print("Ничего не найдено.")

        elif cmd == "copy":
            src = input("Файл (откуда): ")
            dest = input("Куда: ")
            result = copy_file(src, dest)
            print(result)
            log_action(f"Копирование: {src} → {dest}")

        elif cmd == "move":
            src = input("Файл (откуда): ")
            dest = input("Куда: ")
            result = move_file(src, dest)
            print(result)
            log_action(f"Перемещение: {src} → {dest}")

        elif cmd == "delete":
            path = input("Файл (удалить): ")
            result = delete_file(path)
            print(result)
            log_action(f"Удаление: {path}")

        else:
            print("Неизвестная команда. Введите 'help' для списка команд.")

if __name__ == "__main__":
    main()

