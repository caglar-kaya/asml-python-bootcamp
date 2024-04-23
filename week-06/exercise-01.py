students = [
        {
            'name': 'Alice',
            'id': 1,
            'grades': [88, 76, 92]
        },
        {
            'name': 'Bob',
            'id': 2,
            'grades': [75, 85, 79]
        },
        {
            'name': 'Charlie',
            'id': 3,
            'grades': [50, 60, 58]
        },
        {
            'name': 'Diana',
            'id': 4,
            'grades': [98, 92, 95]
        },
        {
            'name': 'Evan',
            'id': 5,
            'grades': [65, 70, 65]
        },
    ]

successful_students = list(filter(lambda student: sum(student['grades']) / len(student['grades']) >= 70, students))

for student in successful_students:
    student['final_grade'] = round(sum(student['grades']) / len(student['grades']))

successful_students.sort(key=lambda student: student['final_grade'], reverse=True)

print(successful_students)
