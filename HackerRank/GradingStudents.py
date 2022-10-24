def gradingStudents(grades):
    # Write your code here
    new_grades = []
    for i in grades:
        if i < 38:
            new_grades.append(i)
        else:
            if i % 5 > 2:
                new_grades.append(i + (5 - i % 5))
            else:
                new_grades.append(i)
    return new_grades
