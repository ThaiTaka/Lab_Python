import os
def cau1a(a, b):
    return a + b

def cau1b(a, b):
    if b == 0:
        return "Khong the chia cho 0"
    return a / b

def cau1c(a, b):
    return a ** b

def cau2(chieu_dai, chieu_rong):
    return chieu_dai * chieu_rong

def KTSoNT(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def cau3(start, end):
    for n in range(start, end + 1):  # Lặp từ start đến end
        if KTSoNT(n):
            print(n)

  

def cau4(n):
    if n < 0:
        return False
    a = 0
    b = 1
    while a < n:
        c = a+b
        a = b
        b = c   
    return a ==n

def cau5(n):
  
    if n <= 0:
        return 0
    if n == 1:
        return 1 
    return cau5(n-1) + cau5(n-2)


def cau6(n):
    if n <= 0:
        return 0 
    if n == 1:
        return cau5(0)  
    return cau6(n-1) + cau5(n-1)

def cau7(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**0.5
        return sum

def cau8(a, b, c):
    if a == 0:
        if b == 0:
            return "Phuong trinh vo nghiem" if c != 0 else "Phuong trinh vo so nghiem"
        return [-c / b]
    
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phuong trinh vo nghiem"
    elif delta == 0:
        return [-b / (2*a)]
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return [x1, x2]

def cau9(n):
    if n < 0:
        return "Khong the tinh giai thua cua so am"
    if n == 0:
        return 1
    return n * cau9(n - 1)

def cau10(n):  
    matrix = []
    for i in range(n):
         row = [' '] * n  
         matrix.append(row)
    for i in range(n):
        matrix[i][0] = "*"  
        matrix[i][i] = "*"  
        matrix[n-1][i] = "*"          
    for row in matrix:
        print(' '.join(row))  

def cau11(giay):
    gio = giay // 3600
    giay_con_lai = giay % 3600
    phut = giay_con_lai// 60
    giay = giay_con_lai % 60
    return f"{gio}:{phut}:{giay}"

def cau12a(n):
    kq = []
    for so in n:
        if so % 2 != 0 and so % 5 != 0:
            kq.append(so)
    return kq

def cau12b(n):
    ket_qua = []
    for so in n:
        if cau4(so):
            ket_qua.append(so)
    return ket_qua

def cau12c(n):
    soNT = [x for x in n if KTSoNT(x)]
    max = 0
    for i in range(1,soNT):
        if soNT[i+1] > soNT[i]:
            max = soNT[i+1]
    return max

def cau12d(n):
    fibo = [x for x in n if cau4(x)]
    min = 0
    for i in range(1,fibo):
        if fibo[i+1] < fibo[i]:
            min = fibo[i+1]
    return min
def cau12e(n):
    sole =[x for x in n if x % 2 != 0]
    tb = sum(sole) / len(sole)
    return tb
def cau12f(n):
    multi = 1
    chiaba = [x for x in n if x % 3 != 0]
    for i in chiaba:
        multi *= i
    return multi
def cau12g(n,vt1,vt2):
    hoanvi(n[vt1],n[vt2])
    return n
def cau12h(n):
    kq = [x for x in n]
    kq.reverse()
    return kq
def hoanvi(pt1,pt2):
    temp = pt1
    pt1 = pt2
    pt2 = temp
def cau12i(n):
    kq = [x for x in n]
    kq.sort()
    array =[i for i in kq if i == kq[-2]]
    return array
def cau12j(n):
    return sum(n)
def cau12k(n,dem):
    kq = [x for x in n]
    return kq.count(dem)
def cau12l(n,dem):
    for i in n:
        if cau12k(n,i) == dem:
            return i
def cau12m(n):
    max_count = max(n.count(x) for x in n)  
    return list(set(x for x in n if n.count(x) == max_count)) 
def main():
    os.system('cls')
    while True:
        print("\n======== MENU ========")
        print("1a. Tinh (a + b)")
        print("1b. Tinh a/b")
        print("1c. Tinh a^b")
        print("2.  Tinh dien tich hinh chu nhat")
        print("3.  Tim so nguyen to trong khoang")
        print("4.  Kiem tra so Fibonacci")
        print("5.  Tim so Fibonacci thu n")
        print("6.  Tinh tong n so Fibonacci dau tien")
        print("7.  Tinh tong can bac 2")
        print("8.  Giai phuong trinh bac 2")
        print("9.  Tinh giai thua")
        print("10. In tam giac sao")
        print("11. Doi thoi gian")
        print("12. Xu ly mang")
        print("0.  Thoat")       
        print("Chon chuc nang:")
        lua_chon = input()

        if lua_chon == "0":
            print("Thoat!")
            break

        elif lua_chon == "1a":
            a = float(input("Nhap a: "))
            b = float(input("Nhap b: "))
            print(f"Ket qua: {cau1a(a, b)}")

        elif lua_chon == "1b":
            a = float(input("Nhap a: "))
            b = float(input("Nhap b: "))
            print(f"Ket qua: {cau1b(a, b)}")

        elif lua_chon == "1c":
            a = float(input("Nhap a: "))
            b = float(input("Nhap b: "))
            print(f"Ket qua: {cau1c(a, b)}")

        elif lua_chon == "2":
            dai = float(input("Nhap chieu dai: "))
            rong = float(input("Nhap chieu rong: "))
            print(f"Dien tich: {cau2(dai, rong)}")

        elif lua_chon == "3":
            start = int(input("Nhap so bat dau: "))
            end = int(input("Nhap so ket thuc: "))
            print(f"Cac so nguyen to: {cau3(start, end)}")

        elif lua_chon == "4":
            n = int(input("Nhap so can kiem tra: "))
            print("La so Fibonacci" if cau4(n) else "Khong phai so Fibonacci")

        elif lua_chon == "5":
            n = int(input("Nhap n: "))
            print(f"So Fibonacci thu {n} la: {cau5(n)}")

        elif lua_chon == "6":
            n = int(input("Nhap n: "))
            print(f"Tong {n} so Fibonacci dau tien: {cau6(n)}")

        elif lua_chon == "7":
            n = int(input("Nhap n: "))
            print(f"Tong can bac 2: {cau7(n)}")

        elif lua_chon == "8":
            a = float(input("Nhap a: "))
            b = float(input("Nhap b: "))
            c = float(input("Nhap c: "))
            print(f"Nghiem: {cau8(a, b, c)}")

        elif lua_chon == "9":
            n = int(input("Nhap n: "))
            print(f"{n}! = {cau9(n)}")

        elif lua_chon == "10":
            n = int(input("Nhap kich thuoc tam giac: "))
            print(cau10(n))

        elif lua_chon == "11":
            giay = int(input("Nhap so giay: "))
            print(f"Thoi gian: {cau11(giay)}")

        elif lua_chon == "12":
            os.system('cls')
            mang = []
            for x in input("Nhap mang cach nhau boi dau cach ").split():
                mang.append(int(x))
            print("\n=== Menu xu ly mang ===")
            print("a. Xuat so le khong chia het cho 5")
            print("b. Xuat cac so Fibonacci")
            print("c. Tim so nguyen to lon nhat")
            print("d. Tim so Fibonacci nho nhat")
            print("e. Tinh trung binh cac so le")
            print("f. Tinh tich cac phan tu khong chia het cho 3")
            print("g. Doi cho 2 phan tu trong danh sach, dau vao la 2 vi tri can doi cho")
            print("h. Dao nguoc trat tu cac phan tu cuar danh sach")
            print("i. Xuat tat ca cac co lon thu nhi cua danh sach")
            print("j. Tinh tong cac chu so cua tat ca cac so trong danh sach")
            print("k. Dem so lan xuat hien cua mot so trong danh sach")
            print("l. Xuat cac so xuat hien n lan trong danh sach")
            print("m. Xuat cac so xuat hien nhieu lan nhat trong danh sach")
            print("chon chuc nang")
            chon = input()
            if chon == 'a':
                print(f"Ket qua: {cau12a(mang)}")
            elif chon == 'b':
                print(f"Ket qua: {cau12b(mang)}")
            elif chon == 'c':
                print(f"Ket qua: {cau12c(mang)}")
            elif chon == 'd':
                print(f"Ket qua: {cau12d(mang)}")
            elif chon == 'e':
                print(f"ket qua: {cau12e(mang)}")
            elif chon == 'f':
                print(f"ket qua: {cau12f(mang)}")  
            elif chon == 'g':
                vt1 = int(input("nhap vi tri 1 = "))
                vt2 = int(input("Nhap vi tri 2 = "))
                print(f"mang truoc khi thay doi {mang}")
                print(f"ket qua: {cau12g(mang,vt1,vt2)}")  
            elif chon == 'h':
                print(f"ket qua: {cau12h(mang)}") 
            elif chon == 'i':
                print(f"ket qua: {cau12i(mang)}")
            elif chon == 'j':
                print(f"ket qua: {cau12j(mang)}")
            elif chon == 'k':
                pt = int(input("Nhap so can dem"))
                print(f"ket qua: {cau12k(mang,pt)}")
            elif chon == 'l':
                pt = int(input("Nhap so can dem"))
                print(f"Co: {cau12l(mang,pt)} xuat hien {pt} trong mang")
            elif chon == 'l':
                pt = int(input("Nhap so can dem"))
                print(f"Co: {cau12l(mang,pt)} xuat hien {pt} trong mang")
            elif chon == 'm':
                print(f"ket qua: {cau12m(mang)}")
            else:
                print("Lua chon khong hop le!")
            
        else:
            print("Lua chon khong hop le!")

if __name__ == "__main__":
    main()