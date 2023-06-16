un = input('Username : ')
pw = input('Password(8 characters) : ')
if len(pw) == 8:
    print("---You're welcome.---")
    print('product list')
    print('ดินสอ(D) 5 THB')
    print('กบเหลาดินสอ(K) 12 THB')
    print('สมุดโน็ต(N) 25 THB')
    x = input('คุณอยากได้อะไร(พิมพ์ D or K or N) :')
    n = int(input('จำนวนเท่าไหร่ :'))
    if x == 'D':
        price = 5
        D = 'ดินสอ'
    elif x == 'K':
        price = 12
        D = 'กบเหลาดินสอ'
    else:
        price = 25
        D = 'สมุดโน็ต'
    sum = n*price
    print(f'X{n}', D, n*price, 'THB')
    m = input('ต้องการซื้อรายการนอกจากนี้หรือไม่(ตอบ Y or N):')
    if m == 'Y':
        x = input('คุณอยากได้อะไร(พิมพ์ D or K or N) :')
        n = int(input('จำนวนเท่าไหร่ :'))
        if x == 'D':
            price = 5
            D = 'ดินสอ'
        elif x == 'K':
            price = 12
            D = 'กบเหลาดินสอ'
        else:
            price = 25
            D = 'สมุดโน็ต'
        sum = sum + (n*price)
        print(f'X{n}',D,n*price,'THB')
        m = input('ต้องการซื้อรายการนอกจากนี้หรือไม่(ตอบ Y or N):')
        if m == 'Y':
            x = input('คุณอยากได้อะไร(พิมพ์ D or K or N) :')
            n = int(input('จำนวนเท่าไหร่ :'))
            if x == 'D':
                price = 5
                D = 'ดินสอ'
            elif x == 'K':
                price = 12
                D = 'กบเหลาดินสอ'
            else:
                price = 25
                D = 'สมุดโน็ต'
            sum = sum + (n * price)
            print(f'X{n}', D,n*price, 'THB')
    print('ราคารวมทั้งหมด',sum)
else:
    print('กรอกpasswordผิดแล่วไอโง่')

