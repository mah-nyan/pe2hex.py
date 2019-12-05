
# python3
import sys
import os.path
import binascii
import string


def check_file_provided():
    default_path = "./test.exe"

    if (len(sys.argv) < 2):
        print("")
        print("Warning")
        print("Correct Usage : python pe2hex.py <file_name>")
        print("")
        print("call {0}".format(default_path))
        if not os.path.isfile(default_path):
            print("")
            print("Error - The file provided does not exist")
            print("")
            sys.exit(0)
        else:
            print("{} is exist".format(default_path))
            print("")

            return default_path
    else:
        print("")
        print("{} is exist".format(sys.argv))
        print("")

        return sys.argv[1]


def read_bytes(filename, chunksize=8192):
    try:
        with open(filename, "r+b") as f:
            while True:
                chunk = f.read(chunksize)
                if chunk:
                    for b in chunk:
                        yield b
                else:
                    break
    except IOError:
        print("")
        print("Error - The file provided can't open")
        print("")
        sys.exit(0)


def main():
    file_path = check_file_provided()
    memory_address = 0
    output_hex = ""

    for byte in read_bytes(file_path):
        output_hex += str(("0x" + hex(byte)[2:].zfill(2) + ', '))
        memory_address = memory_address + 1

    f = open("{}.txt".format(sys.argv[1]), "w")
    f.write(output_hex)
    f.close()


if __name__ == '__main__':
    main()