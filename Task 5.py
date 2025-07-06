# Create a dictionary of Student marks:

student_marks = {}
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    name = input("Enter student name: ")
    marks = input("Enter student marks: ")
    student_marks[name] = marks
search_name = input("Entre the student's name to search: ")
if search_name in student_marks:
    print(f"{search_name}'s marks:  {student_marks[search_name]}")
else:
    print(f"Student name '{search_name}' not found.")




# Demonstrate list slicing:

x = list(range(1,11))
y = x[:5]
z = y[::-1]
print("Extracted first five elements: ",y)
print("Reversed extracted elements: ",z)