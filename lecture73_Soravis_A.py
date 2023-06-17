systemMenu = {'ลาบ':45,'น้ำตก':50,'แกงอ่อม':65}
menulist =[]
def showBill():
    print('---order---')
    for number in range(len(menulist)):
        print(menulist[number][0],menulist[number][1])

while True:
    menuName = input('please enter your menu :')
    if menuName.lower() == 'exit':
        break
    else:
        menulist.append([menuName, systemMenu[menuName]])
total = 0
for k in range(len(menulist)):
    total = total + menulist[k][1]
showBill()
print('ราคารวมทั้งสิ้น %.2f'%total)