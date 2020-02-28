classA = int(input("number of students in A class"))
classB = int(input("number of students in B class"))
classC = int(input("number of students in C class"))


A = classA // 2 + 1 if classA % 2 == 1 else classA // 2
B = classB // 2 + 1 if classB % 2 == 1 else classB // 2
C = classC // 2 + 1 if classC % 2 == 1 else classC // 2
sum = A + B + C
print(f'class A needs {A} desks, class B needs {B} desks, class C needs {C} desks')



print(sum)





# A school decided to replace the desks in three classrooms. Each desk sits two
# students. Given the number of students in each class, print the smallest
# possible number of desks that can be purchased.
# - The program should read three integers: the number of students in each of
# the three classes, a, b and c respectively.
# - In the first test there are three groups. The first group has 20 students and
# thus needs 10 desks. The second group has 21 students, so they can get by
# with no fewer than 11 desks. 11 desks is also enough for the third group of
# 22 students. So we need 32 desks in total.