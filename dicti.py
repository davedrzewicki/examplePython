student = dict()
names = ['John', 'Mary', 'Dave', 'Joe']
values = [1, 4, 2, 1]

for i in range(len(names)):
	student[names[i]] = values[i]


print(student)
which = max(student, key=student.get)
print(which, student[which])