k = int(input("ჩაწერე ხუთნიშნა რიცხვი: "))

while k<10000 or k>99999:
    print("რიცხვი არაა ხუთნიშნა სცადეთ ხელახლა")
    k = int(input("ჩაწერე ხუთნიშნა რიცხვი: "))
n = int(str(k)[0])
r = int(str(k)[1])
o = int(str(k)[2])
p = int(str(k)[3])
l = int(str(k)[4])
print((n*r*o*p*l)*2)