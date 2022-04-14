"""
    grade list :
        xx < 40 = F
        40 - 44 = D
        45 - 49 = D+
        50 - 54 = C

        55 - 59 = C+
        60 - 64 = B
        65 - 69 = B+
        xx > 70 = A
"""

grade = [12,35,23,55,34,38,64,74,71,88,42,12,35,23,55,34,38,64,74,71,88,42]

for i in range(len(grade)):
    if grade[i] < 37 :
        continue

    check = (grade[i]  % 5) 
    #print("เศษ",int(check))

    if check > 2:
        newGrade = (grade[i] - check) + 5
        #print('round grad', newGrade)
        grade[i] = newGrade

for i in range(len(grade)):
    if grade[i] < 40 :
        print(grade[i]," = F")
    elif grade[i] >= 40 and grade[i] <= 44  :
        print(grade[i]," = D")
    elif grade[i] >= 45 and grade[i] <= 49  :
        print(grade[i]," = D+")
    elif grade[i] >= 50 and grade[i] <= 54  :
        print(grade[i]," = C")
    elif grade[i] >= 55 and grade[i] <= 59  :
        print(grade[i]," = C+")
    elif grade[i] >= 60 and grade[i] <= 64  :
        print(grade[i]," = B")
    elif grade[i] >= 65 and grade[i] <= 69  :
        print(grade[i]," = B+")
    else :
        print(grade[i]," = A")
    i += 1
