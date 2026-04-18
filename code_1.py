print("Сайн байна уу! Escape тоглоомонд тавтай морилно уу!"
      "\nТа элсэн цөл дунд байдаг шоронгоос оргож байгаа ба зугтахын тулд харгалзагчийн тэмээг хулгайлах болно."
      "\nМэдээж цагдаа нар таныг барихыг хичээх болно, тиймээс та аль болох хурдан байх хэрэгтэй!"
      "\nТа 200км замыг туулж нуувчиндаа хүрэх хэрэгтэй. Хэрэв та 200км замыг туулж чадвал та ялна!"
      "\nТаны эсэн мэнд зугтах нь таны шийдвэрээс хамаарна. Амжилт хүсье!")

import random

km_traveled    = 0
drink          = 5
police_distance = -20  
thirst         = 0
camel_tired    = 0
done           = False
weather        = "Нарлаг"
is_day         = True
weather_modifiers = {
    "Нарлаг":      (1.0, "Сайхан өдөр, тэмээн явахад таатай.") ,
    "Салхитай":    (0.9, "Салхи үлээж байна. Хурд бага зэрэг саарна."),
    "Бороотой":    (0.8, "Бороо орж байна. Зам илүү удаан байна."),
}

while not done:
    weather = random.choice(list(weather_modifiers.keys()))
    modifier, description = weather_modifiers[weather]
    time_of_day = "Өдөр" if is_day else "Шөнө"
    print(f"\nОдоогийн цаг агаар: {weather}. {description}")
    print(f"Одоогийн цаг: {time_of_day}")

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
        gap = km_traveled - police_distance
        print(f"\nТаны зам туулсан км : {km_traveled} км")
        print(f"Усны үлдэгдэл : {drink} ширхэг")
        print(f"Цангаа : {thirst}/5")
        print(f"Тэмээний ядаргаа : {camel_tired * 10}%  ({camel_tired}/5)")
        print(f"Цагдаагийн зай : {gap} км")

    elif user_choice == "A":
        if drink > 0:
            drink  -= 1
            thirst  = 0
            print(f"\nТа нэг аяга ус уулаа. Үлдэгдэл: {drink} ширхэг.")
        else:
            print("\nУс дууссан байна! Уух ус байхгүй.")

    elif user_choice == "B":
        base_speed = random.randint(5, 12)
        speed = max(1, int(base_speed * modifier))
        km_traveled += speed
        police_distance += random.randint(4, 9)
        thirst      += 1
        camel_tired += 1
        print(f"\nТа дундаж хурдаар явлаа. Цаг агаар: {weather}. +{speed} км → нийт {km_traveled} км.")

    elif user_choice == "C":
        base_speed = random.randint(10, 20)
        speed = max(1, int(base_speed * modifier))
        km_traveled += speed
        police_distance += random.randint(7, 12)
        thirst += 2   
        camel_tired += 2   
        print(f"\nТа хурдлав! Цаг агаар: {weather}. +{speed} км → нийт {km_traveled} км.")

    elif user_choice == "D":
        camel_tired  = 0
        police_distance += random.randint(4, 9)   
        thirst      += 1
        print("\nТа амарлаа. Тэмээний ядаргаа арилсан.")

    else:
        print("\nБуруу сонголт. A, B, C, D, E, Q-аас сонгоно уу.")
        continue  

    if km_traveled >= 200:
        print(f"\nБаяр хүргэе! Та {km_traveled} км туулж нуувчиндаа хүрлээ. Та ялсан!")
        done = True
        continue

    if police_distance >= km_traveled:
        print("\nЦагдаа нар таныг баривчиллаа! Тоглоом дууслаа.")
        done = True
        continue

    if camel_tired >= 6:
        print("\nТэмээ ядарч унав! Тоглоом дууслаа.")
        done = True
        continue

    if thirst >= 6:
        print("\n💀Та цангаж үхлээ! Тоглоом дууслаа.")
        done = True
        continue

    gap = km_traveled - police_distance
    if gap < 15:
        print(f"\nЦагдаа нар ердөө {gap} км-ийн зайд байна! Болгоомжтой!")

    if thirst >= 4:
        print(f"\nТа маш цангаж байна! ({thirst}/5) Ус ууна уу!")

    if random.randint(1, 20) == 10:
        drink = 5
        camel_tired = 0
        thirst = 0
        print("\n Та нууцлаг Баянбүрдийг оллоо! Ус, цангаа болон тэмээний ядаргаа бүгд ариллаа.")

    is_day = not is_day

