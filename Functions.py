# 함수(Functions)
# 함수 이름 파라미터, 내용
def print_name(name): # name은 파라미터(매개변수)
    print(name)

print_name("LION")   #"hyun"
print_name("DJANGO") #"jin" 은 인자(인수)

def print_ex_string():
    print('예시 문자열')

print_ex_string()

def print_name_age(name, age):
    print(f'이름은 {name}이고 {age}살 입니다.')

print_name_age("jin", 26)

def order_coffee(qty, option = 'hot'):
    print(f'{qty}잔 / {option}')
order_coffee(3,'ice')
order_coffee(3)

def get_max(a, b):
    if a>b:
        max = a
    else :
        max = b
    return max

get_max(10,20)
print(get_max(10,20))
print(get_max(20,10))
