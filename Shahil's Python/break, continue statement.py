# Break

a = [0, 1, 2, 3, 4, 5]
for x in a:
    if x == 3:
        break           # It has printed until '2' from '0' because as soon as this 'x' value becomes '3' and we called break the loop is terminated immediately and our programme will come out the loop immediately as soon as this 'break' keyword is called.
    print(x)



q = 0
while q < 5:
    if q == 3:
        break 
    print(q)
    q += 1



# Continue

a = [0, 1, 2, 3, 4, 5]
for x in a:
    if x == 3:
        continue        # For loop starts from printing '0', '1', '2'(output) and as soos as the value of x becomes '2' 'if' condition is met and continue is called and as soos as this continue keyword is called everything whatever codes comes after this continue keyword will be skipped and your programme execution goes once again to a for loop for the next value.
    print(x)



q = 0
while q < 5:
    if q == 3:
        continue        # When ever if condition is satisfied this code will end no code after continue will executed
    print(q)
    q += 1


q = 0
while q < 5:
    q += 1
    if q == 3:
        continue
    print(q)
