# function definition is used by keywork def

# n = int(input("Enter the value of n: "))


# def get_fibonacci_numbers(n):
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result


# print(get_fibonacci_numbers(n))

# default arguments

# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y','ye','yes'):
#             return True
#         if ok in ('n','no','nop','nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)


# ask_ok(str)

# default is a mutable objects such as list, dictionary or instances

# def f(a, L=[]):
#     L.append(a)
#     return L


# print(f(1))  # [1]
# print(f(2))  # [1,2]
# print(f(3))  # [1,2,3]


# if we don't want the default to be shared between subsequent calls, use None

# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L


# print(f(1))  # [1]
# print(f(2))  # [2]
# print(f(3))  # [3]

# keyword arguments

# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     for kw in keywords:
#         print(f"{kw} : {keywords[kw]}")


# cheeseshop("Limburder", "It's very runny sir.", "It's really very, VERY runny sir.",
#            shopkeeper='Michael Palin', client="john cleese", sketch='Cheese Shop Sketch')

# Special parameters

# positional only arguments = the arguments which are before the /

# def pos_only_args(args, /):
#     print(args)


# pos_only_args(1)

# # keyword only argumetns = the arguments which are after the *


# def keyword_only_arguments(*, kwargs):
#     print(kwargs)


# keyword_only_arguments(kwargs=1)

# combination of all 

# def combinated_example(pos_only,/,standard,*,kwd_only):
#     print(pos_only,standard,kwd_only)

# combinated_example(1,2,kwd_only=3)




