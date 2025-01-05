n,m,k = map(int,input().split())
schdule = []
for _ in range(n):
    schdule.append(list(map(int,input().split())))

result = [0] * k
for day in range(1,k+1):
    exams = set()
    for person in range(n):
        for exam_num in range(m):
            if schdule[person][exam_num] == day:
                exams.add(exam_num)
    result[day - 1] = len(exams)

print(*result)

# Âå¹È²»³¬Ê±°æ±¾
'''
n, m, k = map(int, input().split())
schedule = []
for _ in range(n):
    schedule.append(list(map(int, input().split())))

counts = [([0] * (m + 1)) for _ in range(k + 1)]

for person in range(n):
    for exam_num in range(m):
        day = schedule[person][exam_num]
        counts[day][exam_num+1] +=1

final_result = [0] * k
for d in range(1,k+1):
    count = 0
    for e in range(1,m+1):
        if counts[d][e] > 0:
            count+=1
    final_result[d-1] = count

print(*final_result)

'''