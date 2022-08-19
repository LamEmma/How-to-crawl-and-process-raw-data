import csv 
import matplotlib.pyplot as plt
import numpy as np 

import pandas as pd  

# import plat

# read file 
with open('clean_data.csv', encoding='utf-8-sig') as file:
    data = file.read().split('\n')

header = data[0]
students = data[1:]
students.pop()

total_student = len(students)


# split header
header = header.split(',')

#  split each student in list 
for i in range(len(students)):
    students[i] = students[i].split(',')


not_take_exam =  [0,0,0,0,0,0,0,0,0,0,0]

# loop through all students:
for s in students:
    for i in range(len(s)):
        if s[i] == '-1':
            not_take_exam[i-5] += 1

not_take_exam_percentage=  [0,0,0,0,0,0,0,0,0,0,0]

for i in range(0,11):
    not_take_exam_percentage[i] = round(not_take_exam[i]*100/total_student,1)


num_student_by_age = [0,0,0,0,0,0,0,0,0,0,0]  

for s in students:
    age = 2020 - int(s[4])
    if age >=27:
        age = 27
    num_student_by_age[age-17] += 1

print(num_student_by_age)

subject_not_taken = [0,0,0,0,0,0,0,0,0,0,0]


sbd = header[5:16]

for s in students:
    for i in range(len(s)):
        if s[i] in sbd and s[i] not in subject_not_taken:
            subject_not_taken[i-5] +=1
        else:
            subject_not_taken[i-5] +=1 

num_subject_taken = [0,0,0,0,0,0,0,0,0,0,0] 

for s in students:
    count = 0
    for i in range(11):
        if s[i+5] !='-1':
            count+=1
    if count == 1:
        print(s)
    num_subject_taken[count] +=1
print(num_subject_taken)



# fig, ax = plt.subplots()

# objects = ('toán', 'ngữ văn', 'khxh', 'khtn', 'lịch sử', 'địa lí', 'gdcd', 'sinh học', 'vật lí', 'hóa học', 'tiếng anh')
# y_pos = np.arange(len(objects))
# ax.set_ylim(0,100) 

# performance = not_take_exam_percentage


# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('%')
# plt.xlabel('Môn học')
# plt.title('Tỷ lệ phần trăm học sinh bỏ thi theo từng môn học')

# rects = ax.patches
# for rect, label in zip(rects, not_take_exam):
#     height = rect.get_height()
#     ax.text(rect.get_x() + rect.get_width()/ 2, height+2, label, 
#     ha ='center', va='bottom')



# plt.show()










   
   




