# puzzle 2 - reports

with open("inputs\input_02.txt", "r") as f:
   lines = f.readlines()

safe_reports = 0

for i in range(0, len(lines)):
    report = [int(x) for x in lines[i].split()]
    
    # check all ascending/descending
    diffs = [report[n] - report[n-1] for n in range(1, len(report))]
    # checks
    check_minmax = all([abs(x) >= 1 and abs(x) <=3 for x in diffs])
    check_samedir_pos = all(i < j for i, j in zip(report, report[1:]))
    check_samedir_neg = all(i > j for i, j in zip(report, report[1:]))

       
    # testing
    print(report)
    print(diffs)
    print("results: ", check_minmax, ", ", (check_samedir_pos|check_samedir_neg))
    if check_minmax & (check_samedir_pos | check_samedir_neg):
        safe_reports += 1
        print("safe rporets now ", safe_reports)
    

print("number safe reports: ", safe_reports)    
    

