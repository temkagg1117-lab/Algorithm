print("Сайн байна уу! Escape тоглоомонд тавтай морилно уу!" 
"\nТа элсэн цөл дунд байдаг шоронгоос оргож байгаа ба зугтахын тулд харгалзагчийн тэмээг Хулгайлах болно." \
    "\nМэдээж цагдаа нар таныг барихыг хичээх болно, тиймээс та аль болох хурдан байх хэрэгтэй!" \
    "\nТа 200км замыг туулж нуувчиндаа хүрэх хэрэгтэй. Хэрэв та 200км замыг туулж чадвал та ялна!" \
    "\nТаны эсэн мэнд зугтах нь таны шийдэмээс хамаарна. Амжилт хүсье!")
import random
distance = 0
drink = 5
police_distance = -20
speed = 0
km_traveled = 0
thrist = 0
camel_tired = 0
oasis = 0
done = False
while not done:
    print("\nA. Ус уух")
    print("B. Дундаж хурдаар явах") 
    print("C. Хурдлах")
    print("D. Амрах")
    print("E. Статус шалгах")
    print("Q. Тоглоом дуусгах")

    user_choice = input("Таны сонголт: ").upper()

    if user_choice == "Q":
        done = True
        print("Тоглоом дууслаа. Та дахин тоглохыг хүсвэл дахин эхлүүлнэ үү.")
    elif user_choice == "E":
        print(f"\nТаны зам туулсан км: {km_traveled}")
        print(f"Таны уусан усны үлдэгдэл: {drink}")
        print(f"Таны тэмээний ядарсан байдал: {camel_tired}")
        print(f"Цагдаа нар таныг {km_traveled - police_distance} км-ийн зайд байна.")
    elif user_choice == "A":
        if drink > 0:
            drink -= 1
            thrist = 0
            print(f"\nТа нэг аяга ус уулаа. Таны үлдэгдэл: {drink} ширхэг ус байна.")
        else:
            print("\nУс дууссан байна! Та уух ус байхгүй байна.")
            if thrist > 4:
                print("\nТа цангаж үхлээ! Тоглоом дууслаа.")
                done = True
    elif user_choice == "B":
        speed = random.randint(5, 12)
        km_traveled += speed
        police_distance += random.randint(7, 15)
        thrist += 1
        camel_tired += 1
        print(f"\nТа дундаж хурдаар явахыг сонголоо! Та {speed} км зам тууллаа.")
    elif user_choice == "C":
        speed = random.randint(10, 20)
        km_traveled += speed
        police_distance += random.randint(7, 15)
        camel_tired += 1
        thrist += 1
        print(f"\nТа хурдлахыг сонголоо! Та {speed} км зам тууллаа.")
    elif user_choice == "D":
        camel_tired = 0
        police_distance += random.randint(7, 15)
        print("\nТа амрахыг сонголоо. Тэмээний ядарсан байдал ариллаа.")
    if police_distance >= km_traveled:
        print("\nЦагдаа нар таныг баривчиллаа! Тоглоом дууслаа.")
        done = True
    if camel_tired > 5:
        print("\nТэмээ ядарч үхлээ! Тоглоом дууслаа.")
        done = True
    elif km_traveled - police_distance < 15:
        print("\nЦагдаа нар ойртож байна! Болгоомжтой байгаарай.")  