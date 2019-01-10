# x = 25
# def my_fun():
#     x = 50
#     return x
#
# # print(x)
# # print(my_fun())
# my_fun()
# print(x)

# LOCAL
# lambda x:x*2

# Enclosing function Locals
name = 'This is a Global Name!'

def greet():
    name = 'NK'

    def hello():
        print('hello '+name)

    hello()

greet()
print(name)

x = 50

def func(x):
    print('x is: ', x)
    x = 1000
    print('local x changed to:', x)

func(x)
print(x)

y = 50

def funcNew():
    global y
    y = 100

print('Before function call, y is: ',y)
funcNew()
print('After function call, y is: ', y)

