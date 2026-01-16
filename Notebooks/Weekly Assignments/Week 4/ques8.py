import statistics

temps = []

while True:
    temp = input("Enter temperature (e.g. 20C) or press Enter to finish: ")

    if temp == "":
        break

    temps.append(float(temp[:-1]))

if temps:
    print("Maximum:", max(temps))
    print("Minimum:", min(temps))
    print("Mean:", statistics.mean(temps))
else:
    print("No temperatures entered")
