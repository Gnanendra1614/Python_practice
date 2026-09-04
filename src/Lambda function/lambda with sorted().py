students = [
    ("charan", 80),
    ("nani", 95),
    ("raju", 70)
]

result = sorted(students, key=lambda x: x[1])

print(result)