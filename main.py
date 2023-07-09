from roster import student_roster
from classroom_organizer import ClassroomOrganizer
import itertools

iterator_s = iter(student_roster)

alphabet = ClassroomOrganizer()

for i in range(len(student_roster)):
  print(next(alphabet))

# print(alphabet.sitting(student_roster))

fav_math = alphabet.get_students_with_subject('Math')
fav_science = alphabet.get_students_with_subject('Science')
combined = itertools.chain(fav_math, fav_science)

combined_students = list(itertools.combinations(combined, 4))
print(combined_students)







