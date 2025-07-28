student_marks={'Siya':'45','Jiya':'67','Priya':'55','Alice':'85'}
student_name=input("Enter your student's name : ")

if student_name in student_marks:
   print(student_name+"'s Marks:",student_marks[student_name])
else:
   print("Student not found")
