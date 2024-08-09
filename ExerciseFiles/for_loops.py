
fruits = ["Apple","Peach","Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
print(fruits)


student_scores = [180, 124, 165, 173, 189, 169, 146]

total_exam_score = sum(student_scores)
print(total_exam_score)
total_exam_score = 0
for score in student_scores:
    total_exam_score+=score

print(total_exam_score)


max_exam_score = max(student_scores)
print(max_exam_score)

max_exam_score = 0
for score in student_scores:
    if score > max_exam_score:
        max_exam_score = score
print(max_exam_score)

#Range function range(a, b), does not include b

for i in range(1, 10):
    print(i)

#range(a,b,step)
for i in range(1,10,3):
    print(i)

#Adding all numbers up to 100
sum = 0
for i in range(1,101):
    sum+=i

print(sum)
