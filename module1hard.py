grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

a = grades[0]
sum_a = sum (a)
len_a = len (grades[0])
mean_a = sum_a / len_a

b = grades[1]
sum_b = sum (b)
len_b = len (grades[1])
mean_b = sum_b / len_b

c = grades[2]
sum_c = sum (c)
len_c = len (grades[2])
mean_c = sum_c / len_c

d = grades[3]
sum_d = sum (d)
len_d = len (grades[3])
mean_d = sum_d / len_d

e = grades[4]
sum_e = sum (e)
len_e = len (grades[4])
mean_e = sum_a / len_e


students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students = list (frozenset (students))
list_students = sorted(students)
grades_students = {list_students [0] : mean_a, list_students[1]: mean_b,list_students[2]: mean_c,list_students[3]: mean_d, list_students[4]: mean_e}
print(grades_students)