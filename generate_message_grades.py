# get and process input for a list of names
names = input('Enter name seperated by comma: ').title().split(",")
# get and process input for a list of the number of assignments
assignments = input('Enter assignments seperated by commas: ').split(',')
# get and process input for a list of grades
grades =  input('Enter current grade seperated by commas: ').split(',')

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"
# [1] Attempted to use a variable in a For Loop
# potential_grade = 0
for name, assignment, grade in zip(names, assignments, grades):
    # [1] potential_grade += (int(grade) + (int(assignment)*2))
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
    # [1] potential_grade))

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
