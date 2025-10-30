quiz_questions={"what is 95*8":"760","what is 45*4":"180","what is 7*9":"63","what is 86*2":"172","what is 89*0":"0",}
score=0
for question in quiz_questions:
    user_ans = input(question +" ")
    correct_ans =quiz_questions[question]
    
    if (user_ans==correct_ans):
        print("You are right!!!")
        score=score+1
        
    else:
        print("You are wrong!!!")
        
total_ques=len(quiz_questions)
print(f"Your score {score} out of {total_ques}")