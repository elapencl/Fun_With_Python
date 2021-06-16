student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}


for i in  student_scores:
  # student_grades[i] = student_scores[i]
  if int(student_scores[i]) <= 70:
    student_grades[i] = "Fail"
  elif 71 <= int(student_scores[i]) <= 80:
    student_grades[i] = "Acceptable"
  elif 81 <= int(student_scores[i]) <= 90:
    student_grades[i] = "Exceeds Epectations"
  elif int(student_scores[i]) > 90:
    student_grades[i] = "Outstanding"
    
print(student_grades)
