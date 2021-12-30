# check-in , check-out program! (+date time)
import datetime


def see_check_out():  # แสดง check-out ทั้งหมด
    file = open('check_out.txt', 'r')  # เปิดไฟล์ check-out แบบอ่าน
    lines = file.readlines()  # ให้ lines = ตัวของ check-out เองเพื่อเอามาอ่านค่า
    for line in lines:  # ให้ line print ทั้งหมดออกมาโดย for loop ให้้ line ใน lines
        print(line)  # print line ออกมาให้ user เห็น


def see_check_in():  # แสดง check-in ทั้งหมด
    file = open('check_in.txt', 'r')  # เปิดไฟล์ check-in แบบอ่าน
    lines = file.readlines()  # ให้ lines = ตัวของ check-out เองเพื่อเอามาอ่านค่า
    for line in lines:  # ให้ line print ทั้งหมดออกมาโดย for loop ให้้ line ใน lines
        print(line)  # print line ออกมาให้ user เห็น


def check_all():  # def นี้เอาไว้เชื่อม check-in check-out
    print('pass 1 to see check-in')
    print('pass 2 to see check-out')
    inp = int(input('pass your choice here : '))  # กำหนดค่าให้ inp เป็นตัวเลือก
    if inp == 1:  # ถ้า user ใส่ 1 ให้มาข้อนี้
        see_check_in()  # ส่งไป see_check_in
    elif inp == 2:  # ถ้า user ใส่ 2 ให้มาข้อนี้
        see_check_out()  # ส่งไป see_check_out


def name_check_out(date_time):  # ข้อนี่เอาไว้ check-out และรับ date_time มาจาก main
    name = input('put your name here : ')  # รับ input ชื่อ
    check_out = open('check_out.txt', 'a')  # เปิดไฟล์ check-out แบบเพิ่ม
    check_out.write('------------------------------------------')  # สร้างบรรทัดเฉยๆให้อ่านง่าย
    check_out.write('\n')  # เว้นบรรทัด
    date_time_day = date_time.strftime('%x')  # สร้าง datetime ที่ชื่อว่า date_time_day ที่เป็น เดือน/วันที่/ปี
    date_time = date_time.strftime('%X')  # สร้าง datetime ที่ชื่อว่า date_time ที่เป็นเวลา เช่น 06:30:00
    check_out.write(str(date_time_day))  # เปลี่ยนเป็น string แล้วเขียนลงในไฟล์
    check_out.write('-->')  # แค่ลูกษร
    check_out.write(str(date_time))  # เปลี่ยนเป็น string แล้วเขียนลงในไฟล์
    check_out.write('\n')  # เว้นบรรทัด
    check_out.write('Your name is : ')  # ให้เขียนเพิ่มในไฟล์ว่า  your name is แล้วต่อด้วย name แบบไม่เว้นบรรทัด
    check_out.write(name)  # เอา name จาก input ด้านบนมาเพิ่มด้านในไฟล์
    check_out.write('\n')  # เว้นบรรทัด
    check_out.write('------------------------------------------')  # สร้างบรรทัดเฉยๆให้อ่านง่าย
    check_out.write('\n')  # เว้นบรรทัด
    check_out.close()  # ปิดไฟล์
    print('check out complete!')


def name_check_in(date_time):  # ข้อนี่เอาไว้ check-in และรับ date_time มาจาก main
    name = input('put your name here : ')  # รับ input ชื่อ
    check_in = open('check_in.txt', 'a')  # เปิดไฟล์ check-in แบบเพิ่ม
    check_in.write('------------------------------------------')  # สร้างบรรทัดเฉยๆให้อ่านง่าย
    check_in.write('\n')  # เว้นบรรทัด
    date_time_day = date_time.strftime('%x')   # สร้าง datetime ที่ชื่อว่า date_time_day ที่เป็น เดือน/วันที่/ปี
    date_time = date_time.strftime('%X')    # สร้าง datetime ที่ชื่อว่า date_time ที่เป็นเวลา เช่น 06:30:00
    check_in.write(str(date_time_day))  # เปลี่ยนเป็น string แล้วเขียนลงในไฟล์
    check_in.write('-->')  # แค่ลูกษร
    check_in.write(str(date_time))  # เปลี่ยนเป็น string แล้วเขียนลงในไฟล์
    check_in.write('\n')  # เว้นบรรทัด
    check_in.write('Your name is : ')  # ให้เขียนเพิ่มในไฟล์ว่า  your name is แล้วต่อด้วย name แบบไม่เว้นบรรทัด
    check_in.write(name)  # เอา name จาก input ด้านบนมาเพิ่มด้านในไฟล์
    check_in.write('\n')  # เว้นบรรทัด
    check_in.write('------------------------------------------')  # สร้างบรรทัดเฉยๆให้อ่านง่าย
    check_in.write('\n')  # เว้นบรรทัด
    check_in.close()  # ปิดไฟล์
    print('check in complete!')


def main():  # สร้าง main เพื่อ link เข้ากับหัวข้อต่างๆ
    date_time = datetime.datetime.now()  # กำหนด date time ให้เป็นปัจจุบัน
    print('if you want to check in  pass 1!!')
    print('if you want to check out pass 2!!')
    print('if you want to see all check-in and check-out pass 3!!')
    choice = int(input('put your choice here : '))  # รับ input เพื่อไปข้ที่ต้องการ
    if choice == 1:  # ถ้าเลือก 1 ให้ไปหัวข้อ name_check_in และส่ง date time ไปด้วย
        name_check_in(date_time)
    elif choice == 2:  # ถ้าเลือก 2 ให้ไปหัวข้อ name_check_out และส่ง date time ไปด้วย
        name_check_out(date_time)
    elif choice == 3:  # ถ้าเลือก 3 ให้ไปหัวข้อ check_all
        check_all()
    else:  # ถ้าไม่ตรงกับหัวข้อที่กำหนดให้ให้มาข้อนี่เพื่อบอกให้ user ใส่เฉพาะ 1-3
        print('please input only 1-3!!')


if __name__ == '__main__':
    main()
