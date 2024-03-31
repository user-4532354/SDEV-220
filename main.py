#Nailah Pierre
#3/30/24
#M02 Programming Assignment - Loops and Conditionals

student_lastname = input("Enter your last name: ")    #code asks for students last name
student_firstname = input("Enter your first name: ")  # codes asks for students first name
student_gpa = input("Enter GPA as a float: ")         # code asks for students GPA

if student_lastname == "ZZZ":  #access is denied if the students last name is ZZZ
    print("Denied")
else:
    if float(student_gpa) > 3.5 or float(student_gpa) == 3.5: #compares the input to 3.5 and ouutputs the students name and GPA if it is 3.5 or higher
        print(student_firstname + " " + student_lastname + " have made the Dean's list!")
    if float(student_gpa) > 3.25 or float(student_gpa) == 3.25: #compares the input to 3.5 and ouutputs the students name and GPA if it is 3.5 or higher
        print(student_firstname + " " + student_lastname + " has made the Honor Roll!")


