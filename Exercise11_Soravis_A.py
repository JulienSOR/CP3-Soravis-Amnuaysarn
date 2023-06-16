'''
5
    *      4
   ***     3
  *****   เคาะ2ที
 *******   1
*********  0
'''
x = int(input())
h=1
for i in range(x-1,-1,-1):
    print(' '*i,end='')
    print('*'*h)
    h += 2