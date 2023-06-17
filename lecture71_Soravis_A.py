def showBill():
    a = 'รายการสินค้าทั้งหมด'
    print(a.center(50,'*'))
    print('ชื่อรายการสินค้า\t\tราคา')
    for number in range(len(menulist)):
        print('%s\t\t\t%.2f'%(menulist[number],prmenulist[number]))

'''เก็บข้อมูลเข้าคลังเมนูก่อน'''
olist = []
pricelist = []
while True:
    oname = input('please enter your menu(พิมพ์ exit ถ้าต้องการออก) :').lower()
    if oname == 'exit':
        break
    else:
        price = int(input('price :'))
        olist.append(oname)
        pricelist.append(price)
dicorder = {"Order's name": olist,'Price': pricelist}
print(dicorder)

'''คำนวนรายการสินค้า'''
sumprice = 0
menulist = []
prmenulist = []
while True:
    x = input('ชื่อรายการสินค้า(exitถ้าจะออก) :').lower()
    if x in olist:
        num = int(input('จำนวนสินค้า :'))
        value = pricelist[olist.index(x)]
        s = value*num
        menulist.append(x)
        prmenulist.append(s)
        print('ราคาสินค้า %.2f บาท' % s)
        sumprice = sumprice + s
    elif x == 'exit':
        showBill()
        print('ราคารวมทั้งสิ้น %.2f บาท' % sumprice)
        break
    else:
        print('ไม่มีชื่อสินค้านี้ในรายการสินค้า ลองใหม่อีกครั้ง')