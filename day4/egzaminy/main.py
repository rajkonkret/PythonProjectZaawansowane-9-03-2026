from homework import Homework
from exam import Exam
from grade import ExamG
from weakgrade import ExamH

print("----homework-----")
g = Homework()
g.grade = 93
assert g.grade >= 90
print(f"Ocena za projekt: {g.grade}")

print("-----Exam-----")
ex = Exam()
ex.part_a_grade = 88
ex.part_b_grade = 67

assert ex.part_a_grade >= 80
assert ex.part_b_grade >= 55

print(f"Ocena całosciowa: A -> {ex.part_a_grade}, B -> {ex.part_b_grade}")
# -----Exam-----
# Ocena całosciowa: A -> 88, B -> 67

print("----ExamG -----")
first = ExamG()
first.math_grade = 34
first.alg_grade = 13
first.prog_grade = 55
print(first.math_grade, first.alg_grade, first.prog_grade)  # 34 13 55

sec = ExamG()
sec.math_grade = 34
sec.alg_grade = 13
sec.prog_grade = 55
print(sec.math_grade, sec.alg_grade, sec.prog_grade)  # 34 13 55

print("----ExamH -----")
first = ExamH()
first.math_grade = 34
first.alg_grade = 13
first.prog_grade = 55
print(first.math_grade, first.alg_grade, first.prog_grade)  # 34 13 55

sec = ExamH()
sec.math_grade = 34
sec.alg_grade = 13
sec.prog_grade = 55
print(sec.math_grade, sec.alg_grade, sec.prog_grade)  # 34 13 55


