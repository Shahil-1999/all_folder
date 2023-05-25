# if i want to print student score
def studentScore(name, score):
    print(name, " scored", score, "marks")
studentScore("Manish", 70)



#default parameters.
# You can set default values
def studentScore(name="shahil", score=0):
    print(name, " scored", score, "marks")
studentScore()  #you dont need to put any values (purpose= if the user will not pass any values as an arguements then default value will be taken)
studentScore("manish",45)    # otherwiswe user enter some valid name.



#you can choose to pass the 1st parameters skip the 2nd parameters.
def studentScore(name="shahil", score=0):
    print(name, " scored", score, "marks")
studentScore("shiwani")



#you can choose to pass the 2nd parameters skip the 1st parameters.
def studentScore(name="shahil", score=0):
    print(name, " scored", score, "marks")
studentScore(score=99)




#multiple parameters
def studentScore(name, *score):    #"*" this abstract means 'score' parameters will be passed as one or multiple parameters also.
    print("student name is:", name)
    print("student score is:", score)
studentScore("Shahil",55, 25, 58)    #you cannot delete or modify in this tuples

