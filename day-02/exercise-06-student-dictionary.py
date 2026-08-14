"Exercise 6: Student Score Dictionary"

# Given
student_scores = {
    "Anisha": 78,
    "Ravi": 55,
    "Maya": 92,
    "Sagar": 61,
    "Nima": 48
}
# using loop every student and score
for name, score in student_scores.items():
  print(f"student: {name} and Score: {score}")

# dictionary containing only students who scored at least 60
passing_students = {
    name: score for name, score in student_scores.items() 
    if score >= 60
}

# student with the highest score  
highest_student = max(student_scores, key=student_scores.get)
highest_score = student_scores[highest_student]

# calculation for the average score
total_score = sum(student_scores.values()) 
average_score = total_score / len(student_scores)

# Output
print(f"(Passing_student (>=60): {passing_students})")
print(f"Highest Scorer: {highest_student} with a score of {highest_score}")
print(f"Average Class Score : {average_score}")
