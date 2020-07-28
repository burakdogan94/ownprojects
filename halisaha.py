import random
import time

secilen = []
secilenskor = []
rakipskor = []
rakip = []

kadro = {
    'Efe':{'ad':'Efe','puan':6.5},
    'Doğan':{'ad':'Doğan','puan':7.5},
    'Cebeci':{'ad':'Cebeci','puan':8.5},
    'Ömer':{'ad':'Ömer','puan':6},
    'Barış':{'ad':'Barış','puan':8.2},
    'Şafak':{'ad':'Şafak','puan':5.2},
    'Burak':{'ad':'Burak','puan':8.8},
    'Emre':{'ad':'Emre','puan':7},
    'Özer':{'ad':'Özer','puan':8},
    'Ercan':{'ad':'Ercan','puan':5.9}
    }



def kadrosayisec(kadrosayi):
    if kadrosayi < 3 or kadrosayi > 5:
        print("Uygun kadro girilmedi")
        raise ValueError(" ")
    

while True:
    efe = 0
    dogan = 0
    cebeci = 0
    omer = 0
    baris = 0
    safak = 0
    burak = 0
    emre = 0
    ozer = 0
    ercan = 0
    print("Menu".center(50,"-"))
    secim = input("1- OYNA\n2- AYARLAR\n3- ÇIKIŞ\nSeçiminiz(1,2,3): ")
    if secim == '3':
        break
    elif secim == '2':     
        kadrosayi = int(input("Tercih edilen kadro sayısı(min/max - 3/5): "))
        kadrosayisec(kadrosayi)
            
    elif secim == '1':

        kadrosayi = int(input("Tercih edilen kadro sayısı(min/max - 3/5): "))
        kadrosayisec(kadrosayi)

        if kadrosayi is None:
            kadrosayisec(kadrosayi)
            kadrosayi = 3

        else:

            for i in range(1,kadrosayi+1):
                print("Menu".center(50,"-"))
                secim2 = input(f"Takımına {kadrosayi} kişi seç\n1. Efe\n2. Dogan\n3. Cebeci\n4. Omer\n5. Baris\n6. Safak\n7. Burak\n8. Emre\n9. Ozer\n10. Ercan\nSecimizi(1-10):   ")
                if secim2 == '1':
                    print(f"{i} secim: Efe\n")
                    secilen.append(kadro['Efe']['ad'])
                    secilenskor.append(kadro['Efe']['puan'])
                    efe += 1
                    kadro.pop("Efe")
                    if efe >= 2:
                        print("Sadece bir tane efe var")
                        time.sleep(2)
                        break
                elif secim2 == '2':
                    print(f"{i} secim: Doğan\n")
                    secilen.append(kadro['Doğan']['ad'])
                    secilenskor.append(kadro['Doğan']['puan'])
                    dogan += 1
                    kadro.pop("Doğan")
                    if dogan >= 2:
                        print("Sadece bir tane dogan var")
                        time.sleep(2)
                        break
                elif secim2 == '3':
                    print(f"{i} secim: Cebeci\n")
                    secilen.append(kadro['Cebeci']['ad'])
                    secilenskor.append(kadro['Cebeci']['puan'])
                    cebeci += 1
                    kadro.pop("Cebeci")
                    if cebeci >= 2:
                        print("Sadece bir tane cebeci var")
                        time.sleep(2)
                        break
                elif secim2 == '4':
                    print(f"{i} secim: Ömer\n")
                    secilen.append(kadro['Ömer']['ad'])
                    secilenskor.append(kadro['Ömer']['puan'])
                    omer += 1
                    kadro.pop("Ömer")
                    if omer >= 2:
                        print("Sadece bir tane Ömer var")
                        time.sleep(2)
                        break
                elif secim2 == '5':
                    print(f"{i} secim: Barış\n")
                    secilen.append(kadro['Barış']['ad'])
                    secilenskor.append(kadro['Barış']['puan'])
                    baris += 1
                    kadro.pop("Barış")
                    if baris >= 2:
                        print("Sadece bir tane Barış var")
                        time.sleep(2)
                        break
                elif secim2 == '6':
                    print(f"{i} secim: Şafak\n")
                    secilen.append(kadro['Şafak']['ad'])
                    secilenskor.append(kadro['Şafak']['puan'])
                    safak += 1
                    kadro.pop("Şafak")
                    if safak >= 2:
                        print("Sadece bir tane Şafak var")
                        time.sleep(2)
                        break
                elif secim2 == '7':
                    print(f"{i} secim: Burak\n")
                    secilen.append(kadro['Burak']['ad'])
                    secilenskor.append(kadro['Burak']['puan'])
                    burak += 1
                    kadro.pop("Burak")
                    if burak >= 2:
                        print("Sadece bir tane Burak var")
                        time.sleep(2)
                        break
                elif secim2 == '8':
                    print(f"{i} secim: Emre\n")
                    secilen.append(kadro['Emre']['ad'])
                    secilenskor.append(kadro['Emre']['puan'])
                    emre += 1
                    kadro.pop("Emre")
                    if emre >= 2:
                        print("Sadece bir tane Emre var")
                        time.sleep(2)
                        break
                elif secim2 == '9':
                    print(f"{i} secim: Özer\n")
                    secilen.append(kadro['Özer']['ad'])
                    secilenskor.append(kadro['Özer']['puan'])
                    ozer += 1
                    kadro.pop("Özer")
                    if ozer >= 2:
                        print("Sadece bir tane Özer var")
                        time.sleep(2)
                        break
                elif secim2 == '10':
                    print(f"{i} secim: Ercan\n")
                    secilen.append(kadro['Ercan']['ad'])
                    secilenskor.append(kadro['Ercan']['puan'])
                    ercan += 1
                    if ercan >= 2:
                        print("Sadece bir tane Ercan var")
                        time.sleep(2)
                        break
                
                else:
                    print("Yanlış Seçim")
                    time.sleep(2)
                    break
                
                if i >=kadrosayi:
                    secilensonuc=0
                    rakipsonuc=0
                    for b in secilenskor:
                        secilensonuc += b
                    
                    if kadrosayi == 3:

                        sampled_dict = random.sample(kadro.items(), 3)
                        rakip = [sampled_dict[0][0],sampled_dict[1][0],sampled_dict[2][0]]
                        
                        rakipskor = [sampled_dict[0][1]['puan'],sampled_dict[1][1]['puan'],sampled_dict[2][1]['puan']]
                        for c in rakipskor:
                            rakipsonuc += c

                    elif kadrosayi == 4:

                        sampled_dict = random.sample(kadro.items(), 4)
                        rakip = [sampled_dict[0][0],sampled_dict[1][0],sampled_dict[2][0],sampled_dict[3][0]]
                        
                        rakipskor = [sampled_dict[0][1]['puan'],sampled_dict[1][1]['puan'],sampled_dict[2][1]['puan'],sampled_dict[3][1]['puan']]
                        for c in rakipskor:
                            rakipsonuc += c
                    elif kadrosayi == 5:

                        sampled_dict = random.sample(kadro.items(), 5)
                        rakip = [sampled_dict[0][0],sampled_dict[1][0],sampled_dict[2][0],sampled_dict[3][0],sampled_dict[4][0]]
                        
                        rakipskor = [sampled_dict[0][1]['puan'],sampled_dict[1][1]['puan'],sampled_dict[2][1]['puan'],sampled_dict[3][1]['puan'],sampled_dict[4][1]['puan']]
                        for c in rakipskor:
                            rakipsonuc += c
                    else:

                        sampled_dict = random.sample(kadro.items(), 3)
                        rakip = [sampled_dict[0][0],sampled_dict[1][0],sampled_dict[2][0]]
                        
                        rakipskor = [sampled_dict[0][1]['puan'],sampled_dict[1][1]['puan'],sampled_dict[2][1]['puan']]
                        for c in rakipskor:
                            rakipsonuc += c
                    
                    print(f"Takımın: {secilen}\n\nRakipTakım: {rakip}\n")
                    time.sleep(1)
                    print("Hesaplanıyor.\n")
                    time.sleep(1)
                    print("Hesaplanıyor..\n")
                    time.sleep(1)
                    print("Hesaplanıyor...\n")
                    time.sleep(1)
                    
                    if secilensonuc > rakipsonuc:
                        print(f"Tebrikler {secilen} kadro kazandı ({secilensonuc} - {rakipsonuc})\n")
                    else:
                        print(f"Malesef {rakip} kadro kazandı ({rakipsonuc} - {secilensonuc})\n")
                    secilen = []
                    secilenskor = []
                    rakipskor = []
                    rakip = []
                    kadro = {
                            'Efe':{'ad':'Efe','puan':6.5},
                            'Doğan':{'ad':'Doğan','puan':7.5},
                            'Cebeci':{'ad':'Cebeci','puan':8.5},
                            'Ömer':{'ad':'Ömer','puan':6},
                            'Barış':{'ad':'Barış','puan':8.2},
                            'Şafak':{'ad':'Şafak','puan':5.2},
                            'Burak':{'ad':'Burak','puan':8.8},
                            'Emre':{'ad':'Emre','puan':7},
                            'Özer':{'ad':'Özer','puan':8},
                            'Ercan':{'ad':'Ercan','puan':5.9}
                            }
    else:
        raise ValueError("Yanlış Seçim")
        break 
                
                    
                        
                    
                    

