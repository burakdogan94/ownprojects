import random
import time

deste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
decktype = ["Maça","Karo","Kupa","Sinek"]
hand = []
rakiphand = []


for i in deste:

    if i == 11:
        deste[i-1] = 'K'
    if i == 12:
        deste[i-1] = 'Q'
    if i == 13:
        deste[i-1] = 'J'
    if i == 14:
        deste[i-1] = 'A'

kartcek = random.sample(deste,2)
hand.append(kartcek)
tip = random.sample(decktype, 2)

total= 0
for a in kartcek:
        if a == "J" or a == "Q" or a == "K":
            total+=10
        elif a == "A":
            if total >= 11:
                total+=1
            else:
                total+=11
        else:
            total+=a
#-----------------rakip---------------------
for i in deste:

    if i == 11:
        deste[i-1] = 'K'
    if i == 12:
        deste[i-1] = 'Q'
    if i == 13:
        deste[i-1] = 'J'
    if i == 14:
        deste[i-1] = 'A'

kartcek2 = random.sample(deste,2)
rakiphand.append(kartcek2)
tip2 = random.sample(decktype, 2)

total2= 0
for b in kartcek2:
        if b == "J" or b == "Q" or b == "K":
            total2+=10
        elif b == "A":
            if total2 >= 11:
                total2+=1
            else:
                total2+=11
        else:
            total2+=b

print(f"{tip[0]} {kartcek[0]} -- {tip[1]} {kartcek[1]} -- {total}")

while True:
    secim = input("1- Kart Çek\n2- Bitir\n3- Çıkış\nSeciminiz: ")
    
    if secim == '3':
        break

    elif secim == '2':

        print(f"Sen -- {hand} {total}")
        print(f"Rakip -- {rakiphand} {total2}")
        if total > total2:
            print("Kazandınız")
            break
        else:
            print("Kaybettiniz")
            break

    elif secim == '1':
        kartcek = random.sample(deste,1)
        hand.append(kartcek)
        tip = random.sample(decktype, 1)


        for a in kartcek:
                if a == "J" or a == "Q" or a == "K":
                    total+=10
                elif a == "A":
                    if total >= 11:
                        total+=1
                    else:
                        total+=11
                else:
                    total+=a
        #-----------------rakip---------------------
        

        kartcek2 = random.sample(deste,1)
        rakiphand.append(kartcek2)
        tip2 = random.sample(decktype, 1)

        
        for b in kartcek:
                if b == "J" or b == "Q" or b == "K":
                    total2+=10
                elif b == "A":
                    if total2 >= 11:
                        total2+=1
                    else:
                        total2+=11
                else:
                    total2+=b

        print(f"{tip[0]} {kartcek[0]} -- {total}")

        if total > 21 and total2 <= 21:
            print(f"Sen --{hand} {total}")
            print(f"Rakip --{rakiphand} {total2}")
            print("Kaybettiniz")
            break
        elif total <= 21 and total2 > 21:
            print(f"Sen --{hand} {total}")
            print(f"Rakip --{rakiphand} {total2}")
            print("Kazandınız")
            break
        elif total > 21 and total2 > 21:
            print(f"Sen --{hand} {total}")
            print(f"Rakip --{rakiphand} {total2}")
            print("Berabere")
            break

            
        


