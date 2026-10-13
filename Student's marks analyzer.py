student_name=input("Enter your name : ")

n=int(input("Enter the number of subjects : "))

marks=[]

for i in range(1,n+1):
    marks.append(float(input(f"Enter the marks of sub_{i} : ")))


total_marks=sum(marks)

average_marks=(total_marks)/n

highest_marks=max(marks)
lowest_marks=min(marks)

grade="A" if average_marks>=90 else "B" if average_marks>=80 else "C" if average_marks>=70 else "D" if average_marks>=60 else "F"

print("******************************************************STUDENT RESULT******************************************************************")
print("Student's name: ",student_name)
print("Total Marks: ",total_marks)
print("Average marks: ",average_marks)
print("Highest marks: ",highest_marks)
print("Lowest marks: ",lowest_marks)
print("Grade :",grade)


