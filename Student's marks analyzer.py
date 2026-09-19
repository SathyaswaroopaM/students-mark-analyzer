student_name=input("Enter your name:")

subject1_mark=int(input("Enter marks for subject 1:"))
subject2_mark=int(input("Enter marks for subject 2:"))
subject3_mark=int(input("Enter marks for subject 3:"))


marks=[subject1_mark,subject2_mark,subject3_mark]

total_marks=sum(marks)

average_marks=(total_marks)/len(marks)

highest_marks=max(marks)
lowest_marks=min(marks)

if average_marks>=90:
    grade="A"
elif average_marks>=80:
    grade="B"
elif average_marks>=70:
    grade="C"
elif average_marks>=60:
    grade="D"
else:
    grade="F"

print("******************************************************STUDENT RESULT******************************************************************")
print("Student's name: ",student_name)
print("Total Marks: ",total_marks)
print("Average marks: ",average_marks)
print("Highest marks: ",highest_marks)
print("Lowest marks: ",lowest_marks)
print("Grade :",grade)

