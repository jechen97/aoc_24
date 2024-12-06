with open("inputs\input_01.txt", "r") as f:
    data = f.readlines()

numbers1 = [0]*len(data)
numbers2 = [0]*len(data)

for i in range(0, len(data)):
    num = data[i].rstrip('\n')
    numbers1[i] = int(num.split()[0])
    numbers2[i] = int(num.split()[1])

num_counts = dict((x, numbers2.count(x)) for x in numbers2)

sim_score = 0
for i in numbers1:
    sim_score += i * num_counts.get(i, 0)

print("similarity score: ", sim_score)
