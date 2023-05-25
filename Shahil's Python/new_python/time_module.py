# compare time

import time

initial = time.time()
k = 0
while k < 5:
    print("This is right")
    k += 1
print("while loop ran in", time.time()-initial, "second")


initial1 = time.time()
for i in range(5):
    print("This is wrong")
print("while loop ran in", time.time()-initial, "second")


# print present time

a = time.asctime(time.localtime(time.time()))
print(a)


# sleep time
x = 0
while x < 5:
    print("This is right")
    time.sleep(2)
    x += 1
