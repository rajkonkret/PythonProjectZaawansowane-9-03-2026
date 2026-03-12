from homework import Homework
from exam import Exam
from grade import ExamG
from weakgrade import ExamH

print("----homework-----")
g = Homework()
g.grade = 93
assert g.grade >= 90
print(f"Ocena za projekt: {g.grade}")