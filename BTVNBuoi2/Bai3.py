n = int(input("Nhap so nguyen n: "))


tong = 0
chuso = 0
tp = n

while(tp > 0):
    tong += tp % 10
    chuso = chuso + 1
    tp = tp // 10

print("So luong chu so cua n la: ", chuso)
print("Tong cac chu so cua n la: " ,tong)

if n == 1:
    print("So n khong la so nguyen to")
elif n == 2 or n == 3:
    print("So n la so nguyen to")
else:
    dem = 0
    for i in range (2,n):
        if n % i == 0:
            dem += 1
    if dem == 0:
        print("So n la so nguyen to")
    else:
        print("So n khong la so nguyen to")
