for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max_score = 0
for score in student_scores :
  if score > max_score :
    max_score = score
print(f"The max score is {max_score}." )    


maxscore = max(student_scores)
print(f"The max score is {maxscore}.")  