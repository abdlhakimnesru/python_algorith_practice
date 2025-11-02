import random
import os
questions = {
"What is the keyword to define a function in Python?": "def",
"Which data type is used to store True or False values?": "boolean",
"What is the correct file extension for Python files?": ".py",
"Which symbol is used to comment in Python?": "#",
"What function is used to get input from the user?": "input",
"How do you start a for loop in Python?": "for",
"What is the output of 2 ** 3 in Python?": "8",
"What keyword is used to import a module in Python?": "import",
"What does the len() function return?": "length",
"What is the result of 10 // 3 in Python?": "3"
}

  
def questions_sample_random():
    questions_sample=list(questions.keys())
    numbder_question=5
    score= 0
    questions_sample_list=random.sample(questions_sample, numbder_question)
    print(questions_sample_list)
    for inx, question in enumerate(questions_sample_list):
        print(f"{inx +1}.{question}")
        correct_ans=questions[question]
        user_ans=input("inter the correct ans.\n")
        if user_ans==questions[question]:
            print("correct \n")
            score+=1
        else:
            print(f"wrong. the correct answer is {correct_ans}\n ")
    
    print(f"gameover {score}/{numbder_question}")


questions_sample_random()















# def random_selct_quasion():
#     total_quasion=5
#     score=0
#     questions_list =list(questions.keys())

#     selected_questions_list=random.sample(questions_list,total_quasion)
#     # print(selected_questions_list)
#     for inx, question in enumerate(selected_questions_list):
#         print(f"{inx+1}.{question}")
#         user_ans=input("your answer: ").lower().strip()
#         correct_ans=questions[question].lower()
#         if user_ans == questions[question]:
#             print("correct\n")
#             score+=1
#         else:
#             print(f"Wrong! The correct answer is:{correct_ans}\n")
    

#     print(f"gameover {score}/{total_quasion}")



# random_selct_quasion()














            

            


    











