num = int(input())
li = []
for i in range(num):
    name = input()
    score = input()
    li.append([name,score])

scores = []
for name,score in li:
    scores.append(score)
scores =list(set(scores))
scores.sort()
second_lowest_score = scores[1]

name_li = []
for name,score in li:
    if second_lowest_score == score:
        name_li.append(name)

name_li.sort()

for name in name_li:
    print(name)
    