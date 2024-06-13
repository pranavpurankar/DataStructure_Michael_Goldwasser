# /usr/bin/env python3

# 1.1.2 Preview of Python Program


print('Welcome to the GPA calculator.')
print('Please enter all your letter grade, one per line.')
print('Enter a blank line to designate the end.')
# Map from letter frade to point value
points = {'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67,
        'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0}
num_courses = 0
total_points = 0
done = False
print('Bool of done intiail', done)
while not done:
    print('Bool of Done', done)
    grade = input() # read line from user
    if grade == '': # emplty line was entered
        done = True
    elif grade not in points:   # unrecognized grade entered
        print("Unkown grade '{0}' being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]
if num_courses > 0: # avoid division by zero
    print('Your GPA is {0:.3}'.format(total_points / num_courses))


# ----------------------------------------------------------------------------
# Functions


def compute_gpa(grades, points={'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33,
    'B': 3.0, 'B-': 2.67, 'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33, 'D':
    1.0, 'F': 0.0}):
    num_courses = 0
    total_points = 0
    for g in grades:
        if g in points:
            num_courses += 1
            total_points += points[g]
    return total_points / num_courses


print('Compute GPA Function', compute_gpa('A'))
