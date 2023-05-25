import random
import time

random_number = random.randint(0,50) # it print random number from 0 to 50
rand = random.random() * 100 # it print random number from 0 to 100 with floating numbers
lst = ["star plus", "DD1", "aaj tak", "star sports", "zee tv"]
a = random.choice(lst) # it prints random choice from lst
# print(a)
print(random_number)
# print(rand)


b = time.time() # it print current time and date 
timeStamp = time.ctime(b)
print(timeStamp)