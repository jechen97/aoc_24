# Puzzle 1 - distance between arrays

with open("inputs\input_01.txt", "r") as f:
    data = f.readlines()

distance_sum = 0
numbers1 = [0]*len(data)
numbers2 = [0]*len(data)
for i in range(0, len(data)):
    num = data[i].rstrip('\n')
    numbers1[i] = int(num.split()[0]) 
    numbers2[i] = int(num.split()[1]) 

# sort lists 
numbers1.sort()
numbers2.sort()
print(numbers1[0:10])
distance_sum = 0

for i in range(0, len(numbers1)):
    distance_sum += abs(numbers1[i] - numbers2[i])
    print("Step ", i, ": ", numbers1[i], " - ", numbers2[i], " = ", distance_sum)
