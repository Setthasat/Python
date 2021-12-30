from math import sqrt
def kon():#This def for multiply
    an = int(input("input ur first num : "))#input the first num to box and go the next code
    am = int(input("input ur sec num : "))#input the sec num to box and go the next code
    ans = an * am#pick the an and am from box and multiply it in ans
    print(ans)#print ans out for user can see it
def pl():#This def for plus
    an = int(input("input ur first num : "))#input the first num to box and go the next code
    am = int(input("input ur sec num : "))#input the sec num to box and go the next code
    ans = an + am#pick the an and am from box and plus it in ans
    print(ans)#print ans out for user can see it
def neg():#This def for minus
    an = int(input("input ur first num : "))#input the first num to box and go the next code
    am = int(input("input ur sec num : "))#input the sec num to box and go the next code
    ans = an - am#pick the an and am from box and minus it in ans
    print(ans)#print ans out for user can see it
def han():#This def for divide and mod
    print("input 1 to normal divide")#tell user choice
    print("input 2 to mod")#tell user choice
    kk = int(input("input ur choice : "))#input user choice for divide and mod
    if kk == 1:#import kk to this choice
        an = int(input("input ur first num : "))#input the first num to box and go the next code
        am = int(input("input ur sec num : "))#input the sec num to box and go the next code
        ans = an / am#pick the an and am from box and divide it in ans
        print(ans)#print ans out for user can see it
    elif kk == 2 :#import kk to this choice
        an = int(input("input ur first num : "))#input the first num to box and go the next code
        am = int(input("input ur sec num : "))#input the sec num to box and go the next code
        ans = an // am#pick the an and am from box and mod it in ans
        print(ans)#print ans out for user can see it
    else :#but user not input 1-2 run this code
        print("plz input 1-2!!")#tell user input "1-2"
def normalcalchoice():
    print("Progamstart here!!")  # print progam staret here for user understand it
    cal = int(input("plance ur int here : "))  # input user choice for call the code
    if cal == 1:  # if user call 1 go to this choice
        pl()  # link to pl def
    elif cal == 2:  # if user call 2 go to this choice
        neg()  # link to neg def
    elif cal == 3:  # if user call 3 go to this choice
        han()  # link to han def
    elif cal == 4:  # if user call 4 go to this choice
        kon()  # link to kon def
    else:  # but user not input 1-4 run this code
        print("plz input 1-4!!")  # tell user input "1-4"
def wrt():
    print('!!Do not tell your teacher')
def sq():
    print('welcome to sq loot !')
    pas = int(input('pss your  num here : '))
    ans = sqrt(pas)
    print('--your answer is ',ans,'--')
    wrt()
def Pythagorean():
    print('Pythagorean theorem calculator! Calculate your triangle sides.')
    print('Assume the sides are a, b, c and c is the hypotenuse (the side opposite the right angle')
    ch = input('Which side (a, b, c) do you wish to calculate? side : ')
    if ch == 'c':
        a = int(input('Input the length of side a: '))
        b = int(input('Input the length of side b: '))
        c = sqrt(a * a + b * b)
        print('The length of side c is: ')
        print(c)
        wrt()
    elif ch == 'a':
        b = int(input('Input the length of side b: '))
        c = int(input('Input the length of side c: '))
        a = sqrt((c * c) - (b * b))
        print('The length of side a is')
        print(a)
        wrt()
    elif ch == 'b':
        a = int(input('Input the length of side a: '))
        c = int(input('Input the length of side c: '))
        c1 = sqrt((c * c) - (a * a))
        print('The length of side b is')
        print(c1)
        wrt()
    else:
        print('Please select a side between a, b, c')
def multiplication():#สูตรคูณ
    num = int(input('pass you number here : '))
    for i in range(1, 13):
        print(num, 'x', i, '=', num * i)
    wrt()
def main():
    print('This program for convenience every thing for Math class')
    print('pass 1 for show multiplication table!!')
    print('pass 2 to help your Pythagorean class!!')
    print('pass 3 for help you sq loot class!!')
    x = int(input("pass you choice here : "))
    if x == 1 :
        print('welcome to multiplication table class')
        multiplication()
    elif x == 2 :
        print('welcome to Pythagorean!')
        Pythagorean()
    elif x == 3:
        print('welcome to sq loot def')
        sq()
    elif x == 4 :
        print('This is normal cal!')
        normalcalchoice()
if __name__ == '__main__':
    main()
