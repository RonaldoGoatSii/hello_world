
def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return not is_even(n)

num = float(input("Digite um número: "))

if is_even(num):
    print("O número é par!")
else:
    print("O número é ímpar!")
