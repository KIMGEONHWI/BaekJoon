def double(x):
    r"""
    함수 공간
    """
    return x*2

def apply_to_one(f):
    r"""
    인자가 1인 함수 f를 호출
    """
    return f(1)

my_double = double
x = apply_to_one(my_double)
print(x)
