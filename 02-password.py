print('\n-----cutitng line-------')
import random
for i in range(1,3):
    password = random.randint(0,9999)
    print('Password is:%04d' % (password))
#-------------
print('\n-----cutitng line-------')
nums = ('0','1','2','3','4','5','6','7','8','9')
password = []
for i in range(1,5):
    password.append(random.choice(nums))
    print('debag-Password list changing : %s' % (password))
print('debug-list of password = %s' % (password))
#-------------
print('\n-----cutitng line-------')
print('Password is : ',end = '')
for item in password:
    print('%s' % (item),end = '')
#-------------
char1 = ['0','1','2','3','4','5','6','7','8','9']
char2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
char3 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
char4 = ['~','!','@','#','$','%','^','&','*','(',')','_','+','-','=','{','}','[',']',':','"',';','<','>','?',',','.','/']
charAll = char1 + char2 + char3 + char4
print('debug-All usable chars : %s' % (charAll))
pwdLen = 8
password = []
for i in range(1,pwdLen):
    password.append(random.choice(charAll))
    print('debag-Password list changing : %s' % (password))

print('debug-list of password = %s' % (password))
print('Password is : ',end = '')
for item in password:
    print('%s' % (item),end = '')
