import math
import input_object

def inp():
    print("Введите режим: 0 - ввести точки 1 - выбор функции")
    while True:
        try:
            inp_mode = int(input())
            if(inp_mode==0 or inp_mode == 1):
                break
        except Exception:
            print("Введите режим: 0 - ввести точки 1 - выбор функции")

    if(inp_mode==0):
        while True:
            try:
                dots = []
                print("Введите количество точек:")
                n = int(input())
                print("Теперь вводите точки через ENTER в таком виде: X Y где Х - абсцисса Y - ордината")
                print("Attention! при вводе 2 одинаковых точек в методе будет деление на 0! (смотри теорию многочлен Лагранжа)")
                for i in range(0,n):
                    temp = input().split()
                    temp[0] = float(temp[0])
                    temp[1] = float(temp[1])
                    dots.append(temp)
                answer = input_object.InputObject(0,dots)
                return answer
            except Exception:
                print("Некорректный ввод, повторите попытку")
    elif(inp_mode==1):
        while True:
            try:
                print("Выберите функцию:")
                print("sin x - 0")
                print("x^2 - 1")
                print("ln(x) - 2")
                print("sqrt(x) - 3")
                n = int(input())
                if(n==0 or n==1 or n==2 or n==3 ):
                    temp=[]
                    temp.append(n)
                    answer = input_object.InputObject(1,temp)
                    return answer
                print("Некорректный ввод, повторите попытку")
            except Exception:
                print("Некорректный ввод, повторите попытку")

