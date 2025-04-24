n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
for name,scores in student_marks.items():
    if query_name == name:
         average = sum(scores)/len(scores)
print(f"{average:.2f}")