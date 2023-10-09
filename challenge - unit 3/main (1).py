class student:

  def __init__(self, name, roll_no, cgpa):
    self.name = name
    self.roll_no = roll_no
    self.cgpa = cgpa


def sort_students(student_list):
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


students = [
    student("hari", "A123", 7.8),
    student("kisan", "A124", 8.8),
    student("vimala", "A125", 6.3),
    student("vijaya", "A126", 9.2),
]

sorted_students = sort_students(students)

for student in sorted_students:
  print("Name:{}, Roll No:{}, CGPA:{}".format(student.name, student.roll_no,
                                              student.cgpa))