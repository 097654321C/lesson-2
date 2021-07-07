
x=input('輸入數字!')
x=int(x)
import random
ans=random.randint(1,2)
y=str('y')
if x==ans:
 y=input('恭喜你!:),還要玩嗎?要請按0,不要請按1')
elif y==1:
  print('bye bye')
elif y==0:
 x=input('輸入數字!')
else:
 print('你錯嘞>_<,再試一次')
i=int(i)
while x != ans or i<5:
 x=input('再輸入一次數字!')
 x=float(x)
 print('你錯嘞>_<,再試一次')
 i+1
if i==ans:
 print('恭喜你!:),還要玩嗎?要請按0,不要請按1')
else:
 print('bye bye')