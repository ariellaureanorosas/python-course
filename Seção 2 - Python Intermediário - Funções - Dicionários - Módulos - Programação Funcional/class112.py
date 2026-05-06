# Groupby - grouping values

from itertools import groupby

students = [
    {"name": "Luiz", "note": "A"},
    {"name": "Letícia", "note": "B"},
    {"name": "Fabrício", "note": "A"},
    {"name": "Rosemary", "note": "C"},
    {"name": "Joana", "note": "D"},
    {"name": "João", "note": "A"},
    {"name": "Eduardo", "note": "B"},
    {"name": "André", "note": "A"},
    {"name": "Anderson", "note": "C"},
]


def orders(students):
    return students["note"]


grouped_students = sorted(students, key=orders)
groups = groupby(grouped_students, key=orders)

for student, group in groups:
    print(student)
    print()
    for student in group:
        print(student["name"])
    print()
