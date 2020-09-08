def ekok(a, b):
    toplam = a*b
    i=1
    while i<toplam:
        i+=1
        if a % i == 0 and b % i == 0:
            print(f"Ekok: {i}")
            break
        else:
            print("ekok: 1")
            break   
def ebob(a, b):
    if a>b:
        c=b+1
        while c>=0:
            c-=1
            if a % c == 0 and b % c == 0:
                print(f"Ebob: {c}")
                break
    else:
        c=a+1
        while c>=0:
            c-=1
            if b % c == 0 and a % c == 0:
                print(f"Ebob: {c}")
                break




a = int(input("a: "))
b = int(input("b: "))
ekok(a, b)
ebob(a, b)