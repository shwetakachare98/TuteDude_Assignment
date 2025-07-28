student_marks={'sanika':'45','jiya':'67','priya':'55','Alice':'85'}
student_name=input("Enter your name : ")

if student_name in student_marks:

   print(student_name+"'s Marks:",student_marks[student_name])

else:
   print("Student not found")
