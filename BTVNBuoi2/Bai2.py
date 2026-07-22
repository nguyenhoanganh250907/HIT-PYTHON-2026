day = int(input("Nhap ngay sinh: "))
month = int(input("Nhap month sinh: "))

check = True

if month == 2:
    if day < 1 or day > 29:
        check = False
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day < 1 or day > 30:
        check = False
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day < 1 or day > 31:
        check = False
elif month < 1 or month > 12:
    check = False

if check == False:
    print("Ngay thang khong hop le")
else:
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        print("Cung Bach Duong")
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        print("Cung Kim Nguu")
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        print("Cung Song Tu")
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        print("Cung Cu Giai")
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        print("Cung Su Tu")
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        print("Cung Xu Nu")
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        print("Cung Thien Binh")
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        print("Cung Bo Cap")
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        print("Cung Nhan Ma")
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        print("Cung Ma Ket")
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        print("Cung Bao Binh")
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        print("Cung Song Ngu")


