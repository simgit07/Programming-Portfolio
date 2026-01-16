import sys
import statistics

args = sys.argv[1:]

if not args:
    print("Error: No temperatures provided")
    sys.exit()

temps = []

for t in args:
    try:
        temps.append(float(t))
    except ValueError:
        print("Invalid temperature:", t)
        sys.exit()

print("Maximum:", max(temps))
print("Minimum:", min(temps))
print("Mean:", statistics.mean(temps))
