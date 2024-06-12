#!/usr/bin/python
#20240612 11227058 pythoneval11
import sys

def main():
    if len(sys.argv) != 4:
        sys.exit(1)
    fo = sys.argv[1]
    try:
        n1 = int(sys.argv[2])
        n2 = int(sys.argv[3])
        if n1 < 0 or n2 < 0:
            raise ValueError
    except ValueError:
        sys.exit(1)
    try:
        with open('/usr/bin/yes', 'rb') as read_file:
            read_file.seek(n1)
            data = read_file.read(n2)

        with open(fo, 'wb') as write_file:  # 這裡更改了模式為 'wb'
            write_file.write(data)
    except:
        sys.exit(1)
    finally:
        if 'read_file' in locals():
            read_file.close()
        if 'write_file' in locals():
            write_file.close()

if __name__ == "__main__":
    main()
