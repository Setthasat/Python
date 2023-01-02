import time
import datetime

def check_write_date(x):
    print('ok i will record it now')
    file_date = open('date.txt','w')
    file_date.write(x.year)
    file_date.write('\n')
    file_date.write(x.day)
    file_date.write('\n')
    file_date.write(x.strftime("%A"))
    file_date.write('\n')
    file_date.write(x.hour)
    file_date.write(x.minute)
    file_date.write(x.second)
    file_date.close()
    print('finish record!!')
    check_read_date()
    
def check_read_date():
    check_read_date_file = open('date.txt','r')
    check_read_date_file.read()
    check_read_date_file.close()
    print(check_read_date_file)
    
def check_date():
    x = datetime.datetime.now()
    print('this year is ',x.year,)
    print('this day is ',x.day,)
    print('today is ',x.strftime("%A"))
    print(x.hour,':',x.minute,':',x.second,'o clock')
    c = int(input('Do u want to record it?(pass 1 to yes/pass 2 to no) : '))
    if c == 1 :
        check_write_date(x)
        
def check_time():
    start = time.time()
    x = int(input('Enter ur range here : '))
    for i in range(x):
        for j in range(1, (2 * i)):
            print("*", end=" ")
        print("\n")
    end = time.time()
    print(end - start, 'second')
    
def main():
    print('pass 1 to check time')
    print('pass 2 to check date')
    inp = int(input('what do u want to check : '))
    if inp == 1:
        check_time()
    elif inp == 2:
        check_date()
    else :
        print('plz pass only 1-2!!!')
        
if __name__ == '__main__' :
    main()
