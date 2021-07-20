import random
def auto_add(x):
    num1 = random.randint(0, x)
    num2 = random.randint(0, x)
    ans = num1 + num2
    print(num1, '+', num2, )
    f_ans = int(input('Answer: '))
    if f_ans == ans:
        print('Correct')
    else:
        print('Wrong')
    auto_add(x)

def auto_sub(x):
    num1 = random.randint(0,x)
    num2 = random.randint(num1,x)
    ans = num2-num1
    print(num2, '-', num1, )
    f_ans = int(input('Answer: '))
    if f_ans == ans:
        print('Correct')
    else:
        print('Wrong')
    auto_sub(x)




