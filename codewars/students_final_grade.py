def final_grade_one_hundred(exam, projects):
    if exam > 90 or projects > 10:
        return 100

def final_grade_ninety(exam, projects):
    if exam >= 75 and projects >= 5:
        return 90

def final_grade_seventy_five(exam, projects):
    if exam >= 50 and projects >= 2:
        return 75

def final_grade(exam, projects):
    grades_calc = [
        final_grade_one_hundred,
        final_grade_ninety,
        final_grade_seventy_five
    ]

    for calc in grades_calc:
        result = calc(exam, projects)

        if result:
            return result

    return 0
