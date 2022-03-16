#rock paper scissors (เป่ายิ้งฉุบกับบอท)

import random

def main():
     
    while True:
    
    #  ตัวแปร
        player = input("Enter a choice (rock, paper, scissors): ") #  รับ input จาก user 
        Box = ["rock", "paper", "scissors"] #  สร้าง array ชื่อว่า Box
        Bot = random.choice(Box) #  สุ่มค่าจาก Box
    #  จบตัวแปร

        print(f"\nYou chose {player}, computer chose {Bot}.\n") #  แสดงค่าที่บอทกับuserส่งมา

    #  D o n ' t  t o u c h   c o d e   u n d e r   t h i s   c o m m e n t   p l s

        #  เสมอ
        if player == Bot:
            print(f"Both players selected {player}. It's a draw!")
        #  จบเสมอ

        #  user ออกค้อน
        elif player == "rock":
            if Bot == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        #  จบ user ออกค้อน

        #  user ออกกระดาษ
        elif player == "paper":
            if Bot == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        #  จบ user ออกกระดาษ

        #  user ออกกรรไกร
        elif player == "scissors":
            if Bot == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
        #  จบ user ออกกรรไกร

        #  เล่นอีกครั้ง
        play_again = input("Want to play again? (y/n): ") # รับinputเป็น yes กับ no
        if play_again.lower() != "y": # ถ้าไม่ได้ตอบyes
            break #  หยุด while loop



if __name__ == "__main__" :
    main()
