# student_names = ['Sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michelle']
# student_marks = [80, 56, 78, 90]
# #Print from Patricia to Phionah
# #Add marsha at the fouth position
# #Update  the name Phionah to Phionah Aladddina
# #Display the length of the students' list
# #Print all the students' name using a for loop.
# #Calculate the total marks for the student marks' variable. 

# #question1
student_names = ['Sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michelle']
print(student_names[1:4])

# #question2
student_names = ['Sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michelle']
student_names.insert(4,"Marsha")
print(student_names)

#question3
student_names = ['Sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michelle']
student_names[3]="Phionah Aladinah"
print(student_names)

#question4
student_names = ['Sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michelle']
print(len(student_names))

#question5
student_names = ['Sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michelle']
for name in student_names:
    print(name)

#question6
def total_mark_of_students():
    student_marks = [80, 56, 78, 90]
    sum=(80+56+78+90)
    print(f'The total marks for student mark is {sum}')
total_mark_of_students()
    
