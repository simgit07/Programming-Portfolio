import statistics

temps = []

for i in range(6):
    temp = input("Enter temperature (e.g. 20C): ")
    temps.append(float(temp[:-1]))

print("Maximum:", max(temps))
print("Minimum:", min(temps))
print("Mean:", statistics.mean(temps))
