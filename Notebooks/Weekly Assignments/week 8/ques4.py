import sys

def wc(filename):
    with open(filename, 'r') as f:
        text = f.read()
        lines = text.count('\n')
        chars = len(text)

    print(f"Lines: {lines}")
    print(f"Characters: {chars}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wc.py <filename>")
        sys.exit(1)

    wc(sys.argv[1])
