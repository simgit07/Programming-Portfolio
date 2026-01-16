import sys

def nl(filename):
    with open(filename, 'r') as f:
        for i, line in enumerate(f, start=1):
            print(f"{i}\t{line.rstrip()}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nl.py <filename>")
        sys.exit(1)

    nl(sys.argv[1])
