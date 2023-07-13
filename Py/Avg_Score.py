# 🚨 Don't change the code below 👇
student_scores = 0
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# #Write your code below this row 👇

max_score = 0
for score in student_scores :
  if score > max_score :
    max_score = score
print(f"The max score is {max_score}." )    


maxscore = max(student_scores)
print(f"T'''he max score is {maxscore}.")  

# Steps for Average Score and Max Score
# Input the number of students: number
# Input the score of student : score
# Average score of class : average
# Max score of class : max

# 1. Input the number of students 
# 2. Input the score of student     
# 3. Average score of class 
# 4. Max score of class

