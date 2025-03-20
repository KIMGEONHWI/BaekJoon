# 첫번째 방법

grade_dict = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0 }
sum_credit = 0
sum_credit_by_grade = 0

for i in range(20):
    subject, credit, grade = input().split()
    if grade != "P":
        sum_credit = sum_credit + float(credit)
        sum_credit_by_grade = sum_credit_by_grade + float(credit) * grade_dict[grade]

print(sum_credit_by_grade/sum_credit)




# 두번째 방법
rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0	
result = 0	
for _ in range(20) :
    s, p, g = input().split()
    p = float(p)
    if g != 'P' :	
        total += p
        result += p * grade[rating.index(g)]


print(format(result / total, ".6f"))