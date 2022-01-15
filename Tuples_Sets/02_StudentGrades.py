def avg(values):
    return sum(values) / len(values)


n = int(input())

student_records = {}

for _ in range(n):
    name, grade_string = input().split()
    grade = float(grade_string)

    if name not in student_records:
        student_records[name] = []
    student_records[name].append(grade)

for name, grade in student_records.items():
    average_grade = avg(grade)
    grade_str = ' '.join(str(f'{x:.2f}') for x in grade)
    print(f'{name} -> {grade_str} (avg: {average_grade:.2f})')
