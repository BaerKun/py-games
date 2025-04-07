import random

print('')
print('Let\'s play CHOOSE BEAR!')
input(
    'Game rules:There are 100 bears in total.You can take some bears away'
    '---at least one bears and the most is ten bears.'
    'If the final is taken away by you,you win.Or,zhanshen win it!Good Luck!!      ')
input(' ')
b = int(input('Choose how many bears in total'))
c = int(input('Choose how many you take away a time'))
sx = 0
zs = 0
while b > 0:
    sx = int(input('How much bear?'))
    if sx > b or sx < 1 or sx > c:
        print('                        Strong man cannot make such weak mistake!')
        continue
    else:
        b = b - sx
    print('sexiong:', ' takes away----', sx, 'bear(s),', 'total bears:----', b, 'bears')
    if b == 0:
        print('')
        print('You win the match!!!!!!!!The chicken is so weak!!!!!!!!!!!!!!!!!!')
        continue
    if b % 11 == 0:
        zs = random.randint(1, c)
        if zs >= b:
            zs = b
    else:
        zs = b % 11
    b -= zs
    print('zhanshen:', ' takes away----', zs, 'bear(s),', 'total bears:----', b, 'bears')
    if b == 0:
        print('Zhanshen win the match!!!The chicken is still strong!!!')  # CHOOSE BEAR
