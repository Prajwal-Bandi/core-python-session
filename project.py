import os
import datetime
import socket
import shutil
import sys

def list_files():
    try:
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for file in files:
            print(file)
    except Exception as e:
        print(f"Error: {e}")

def list_dirs():
    try:
        dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
        for dir in dirs:
            print(dir)
    except Exception as e:
        print(f"Error: {e}")

def display_date():
    try:
        now = datetime.datetime.now()
        print(now.strftime("%d-%b-%Y").lower())
    except Exception as e:
        print(f"Error: {e}")

def display_time(parts):
    try:
        now = datetime.datetime.now()
        if len(parts) == 1:
            print(now.strftime("%H:%M:%S"))
        elif len(parts) == 2:
            if parts[1] == "-hours":
                print(now.hour)
            elif parts[1] == "-mins":
                print(now.minute)
            elif parts[1] == "-secs":
                print(now.second)
            else:
                print("Invalid time option")
        else:
            print("Invalid time command")
    except Exception as e:
        print(f"Error: {e}")

def cat_file(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except Exception as e:
        print(f"Error: {e}")

def head_file(filename, lines_count):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines[:lines_count]:
                print(line.rstrip())
    except Exception as e:
        print(f"Error: {e}")

def tail_file(filename, lines_count):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines[-lines_count:]:
                print(line.rstrip())
    except Exception as e:
        print(f"Error: {e}")

def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print("File copied successfully")
    except Exception as e:
        print(f"Error: {e}")

def remove_file(filename):
    try:
        os.remove(filename)
        print("File removed successfully")
    except Exception as e:
        print(f"Error: {e}")

def empty_file(filename):
    try:
        with open(filename, 'w') as f:
            pass
        print("File truncated successfully")
    except Exception as e:
        print(f"Error: {e}")

def ipconfig():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print(ip)
    except Exception as e:
        print(f"Error: {e}")

def pwd():
    try:
        print(os.getcwd())
    except Exception as e:
        print(f"Error: {e}")

def clear_screen():
    try:
        os.system('clear' if os.name != 'nt' else 'cls')
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        try:
            command = input("> ").strip()
            if not command:
                continue
            parts = command.split()
            cmd = parts[0]

            if cmd == "list":
                if len(parts) == 1:
                    list_files()
                else:
                    print("Invalid command")

            elif cmd == "dirs":
                if len(parts) == 1:
                    list_dirs()
                else:
                    print("Invalid command")

            elif cmd == "date":
                if len(parts) == 1:
                    display_date()
                else:
                    print("Invalid command")

            elif cmd == "time":
                display_time(parts)

            elif cmd == "cat":
                if len(parts) == 2:
                    cat_file(parts[1])
                else:
                    print("Invalid command")

            elif cmd == "head":
                if len(parts) == 2:
                    head_file(parts[1], 10)  # default 10 lines
                elif len(parts) == 3 and parts[1].startswith("-"):
                    try:
                        line_count = int(parts[1][1:])
                        head_file(parts[2], line_count)
                    except ValueError:
                        print("Invalid number of lines")
                else:
                    print("Invalid command")

            elif cmd == "tail":
                if len(parts) == 2:
                    tail_file(parts[1], 10)  # default 10 lines
                elif len(parts) == 3 and parts[1].startswith("-"):
                    try:
                        line_count = int(parts[1][1:])
                        tail_file(parts[2], line_count)
                    except ValueError:
                        print("Invalid number of lines")
                else:
                    print("Invalid command")

            elif cmd == "copy_file":
                if len(parts) == 3:
                    copy_file(parts[1], parts[2])
                else:
                    print("Invalid command")

            elif cmd == "remove_file":
                if len(parts) == 2:
                    remove_file(parts[1])
                else:
                    print("Invalid command")

            elif cmd == "empty_file":
                if len(parts) == 2:
                    empty_file(parts[1])
                else:
                    print("Invalid command")

            elif cmd == "ipconfig":
                if len(parts) == 1:
                    ipconfig()
                else:
                    print("Invalid command")

            elif cmd == "pwd":
                if len(parts) == 1:
                    pwd()
                else:
                    print("Invalid command")

            elif cmd == "clear":
                if len(parts) == 1:
                    clear_screen()
                else:
                    print("Invalid command")

            elif cmd == "exit":
                if len(parts) == 1:
                    print("Shell exiting")
                    sys.exit(0)
                else:
                    print("Invalid command")

            else:
                print("Invalid command")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
