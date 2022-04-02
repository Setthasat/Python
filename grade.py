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
grade = [38,39,43,44,48,49,53,54,58,59,63,64,68,69]

i = 0
 
nu = len(grade)

for i in range(nu):
    if grade[i] < 40 :
        if grade[i] == 38 :
            new_grade = grade[i] + 2
            print(f"{new_grade} = D")
        elif grade == 39 :
            new_grade = grade[i] + 1
            print(f"{new_grade} = D")
        else :
            print(grade[i]," = F")

    elif grade[i] >= 40 and grade[i] <= 44  :
        if grade[i] == 43 :
            new_grade = grade[i] + 2
            print(f"{new_grade} = D+")
        elif grade[i] == 44 :
            new_grade = grade[i] + 1 
            print(f"{new_grade} = D+")
        else :
            print(grade[i]," = D")

    elif grade[i] >= 45 and grade[i] <= 49  :
        if grade[i] == 48 :
            new_grade = grade[i] + 2
            print(f"{new_grade} = C")
        elif grade[i] == 49 :
            new_grade = grade[i] + 1 
            print(f"{new_grade} = C")
        else :
            print(grade[i]," = D+")

    elif grade[i] >= 50 and grade[i] <= 54  :
        if grade[i] == 53 :
            new_grade = grade[i] + 2
            print(f"{new_grade} = C+")
        elif grade[i] == 54 :
            new_grade = grade[i] + 1 
            print(f"{new_grade} = C+")
        else :
            print(grade[i]," = C")

    elif grade[i] >= 55 and grade[i] <= 59  :
        if grade[i] == 58 :
            new_grade = grade[i] + 2
            print(f"{new_grade} = B")
        elif grade[i] == 59 :
            new_grade = grade[i] + 1 
            print(f"{new_grade} = B")
        else :
            print(grade[i]," = C+")

    elif grade[i] >= 60 and grade[i] <= 64  :
        if grade[i] == 64 :
            new_grade = grade[i] + 2
            print(f"{new_grade} = B+")
        elif grade[i] == 65 :
            new_grade = grade[i] + 1 
            print(f"{new_grade} = B+")
        else :
            print(grade[i]," = B")

    elif grade[i] >= 65 and grade[i] <= 69  :
        if grade[i] == 68 :
            new_grade = grade[i] + 2
            print(f"{new_grade} = A")
        elif grade[i] == 69 :
            new_grade = grade[i] + 1 
            print(f"{new_grade} = A")
        else :
            print(grade[i]," = B+")

    else :
        print(grade[i]," = A")
    i += 1



