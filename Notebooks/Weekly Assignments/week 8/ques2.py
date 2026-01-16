import sys

def diff(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        if f1.read() == f2.read():
            print("Files are the same")
        else:
            print("Files are different")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff.py <file1> <file2>")
        sys.exit(1)

    diff(sys.argv[1], sys.argv[2])
