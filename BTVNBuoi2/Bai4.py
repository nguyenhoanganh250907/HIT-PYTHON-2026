xu = int(input("Nhap so xu ma ban co: "))

bia = xu // 28
vobia = bia
while(vobia >= 3):
    bia += vobia // 3
    vobiasau = vobia // 3
    vobia = vobia - vobiasau*3 + vobiasau
    
print("So chai bia ban co the mua dc la: ",bia)