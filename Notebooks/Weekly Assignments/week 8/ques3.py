import sys

def grep(pattern, filename):
    with open(filename, 'r') as f:
        for line in f:
            if pattern in line:
                print(line.rstrip())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep.py <pattern> <filename>")
        sys.exit(1)

    grep(sys.argv[1], sys.argv[2])
