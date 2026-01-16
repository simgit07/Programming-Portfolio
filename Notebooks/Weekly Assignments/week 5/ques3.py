import sys

args = sys.argv[1:]

if not args:
    print("Error: No arguments provided")
    sys.exit()

args.sort(key=len)
print("Shortest argument:", args[0])
