from multiprocessing.util import DEFAULT_LOGGING_FORMAT
from django import template
import random

register = template.Library()


@register.filter
def ranges(i,j):
    return range(i,j)

@register.filter
def mul(i,j):
    return i * j

# 기본운임 가격에서 랜덤으로 가격 지정
@register.filter
def ran_money(org_money):
    num = random.randint(1, 100)
    m1 = 10000
    m2 = 30000
    m3 = 50000
    m4 = 80000

    if num <= 25:
        org_money += m1
    elif 25 < num and num <= 50:
        org_money += m2
    elif 50 < num and num <= 75:
        org_money += m3
    elif 75 < num and num <=100:
        org_money += m4

    return org_money

@register.filter
def i_int(num):
    return int(num)

# 특가운임 정하는 함수
@register.filter
def special_price(money, d_time):
    tt = d_time.hour

    special_price = money   # 특가


    if 0 < tt and tt <= 6:
        percen = 0.5
        special_price *= percen

        
    elif 6 < tt and tt <= 12:
        percen = 0.6
        special_price *= percen

      
    elif 12 < tt and tt <= 18:
        percen = 0.75
        special_price *= percen

        
    elif 18 < tt and tt <= 24:
        percen = 0.7
        special_price  *= percen

    return round(special_price)


# 할인운임 정하는 함수
@register.filter
def discount_price(money, d_time):
    tt = d_time.hour

    discount_price = money   # 할인


    if 0 < tt and tt <= 6:
        percen = 0.76
        discount_price *= percen

        
    elif 6 < tt and tt <= 12:
        percen = 0.79
        discount_price *= percen

     
    elif 12 < tt and tt <= 18:
        percen = 0.9
        discount_price *= percen


    elif 18 < tt and tt <= 24:
        percen = 0.85
        discount_price *= percen

    return round(discount_price)

@register.filter
def indexing(ls:list, i):
    return ls[i]

@register.filter
def typeof(a):
    return type(a)


@register.filter
def list(a):
    return list(a)

@register.filter
def split(a):
    return a.split('_')

# 문자'1', '2', '3'으로 받은 운입 타입 단어로 바꿔주기 
@register.filter
def convert_amount(type):
    if type == '1':
        str_type = '특별운임'

    elif type == '2':
        str_type = '할인운임'

    else:
        str_type = '정상운임'

    return str_type

# 더하는 함수
@register.filter
def plus(num1, num2):
    num3 = num1 + num2

    return num3


@register.filter
def str_plus(i,j):
    return str(i)+str(j)


