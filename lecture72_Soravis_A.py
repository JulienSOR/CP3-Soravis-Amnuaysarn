def showBill():
    a = 'รายการสินค้าทั้งหมด'
    print(a.center(50,'-'))
    print('จำนวน\tชื่อรายการสินค้า\t\tราคา')
    for number in range(len(menulist)):
        print('X%d\t\t%s\t\t\t%.2f'%(menulist[number][1],menulist[number][0],price_value[number]))

'''รายการสินค้า'''
olist = [['น้ำตก',50],['ลาบหมู',45],['ข้าวเหนียว',10],['ซอยจุ๊',69]]
o = ['น้ำตก','ซอยจุ๊','ข้าวเหนียว','ลาบหมู']
print('รายการอาหาร\t\tราคา(THB)')
for i in range(len(olist)):
    print('%s\t\t\t%d'%(olist[i][0],olist[i][1]))

'''ป้อนรายการสินค้าและเก็บข้อมูล'''
sumprice = 0
menulist = []
price_value = []
while True:
    menuname = input('ชื่อสินค้า :')
    if menuname.lower() == 'exit':
        break
    if menuname not in o:
        print('คุณพิมพ์ชื่อสินค้าผิด กรุณาพิมพ์ใหม่อีกครั้ง')
        continue
    number = int(input('จำนวนสินค้า :'))
    for k in range(len(olist)):
        if menuname in olist[k][0]:
            menulist.append([menuname, number])
            value = number * olist[k][1]  #นำราคาไปคูณกับnumber
            price_value.append(olist[k][1])
            sumprice = sumprice + value
showBill()
x = 'จบรายการ'
print(x.center(46,'-'))
print('ยอดชำระทั้งสิ้น %.2f THB'%sumprice)