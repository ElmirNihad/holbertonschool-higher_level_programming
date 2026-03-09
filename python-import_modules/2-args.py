#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1  # script adı çıxılmalıdır
    
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print(f"{argc} arguments:")
    
    # arqumentləri çap et
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
