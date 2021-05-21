import matplotlib.pyplot as plt
import input_object
import laGranzh

def razdelRaznost(begEnd,x_y): # рекурсивный подсчет разделенной разности n-го порядка, например 2 или 5-го
    # begEnd - лист из 2 чисел x0 и xn где x0-первый номер xn - номер эл-та, до которого нужно сосчитать
    # Напрмимер begEnd=[0,2] то же самое что f(x0,x1,x2)
    # x_y - лист точек [[x0,y0],[x1,y1]]
    if(begEnd[1]-begEnd[0]==1):
        return (x_y[begEnd[1]][1] - x_y[begEnd[0]][1])/(x_y[begEnd[1]][0] - x_y[begEnd[0]][0])
    else:
        # left is like when we use f(x0,x1,x2) left is f(x0,x1) right is f(x1,x2)
        temp = begEnd.copy()
        temp[1] = temp[1] - 1
        left = razdelRaznost(temp,x_y)
        temp = begEnd.copy()
        temp[0]= temp[0] + 1
        right = razdelRaznost(temp,x_y)
        return (right-left)/(x_y[begEnd[1]][0]-x_y[begEnd[0]][0])

# 0.15 1.25
# 0.2 2.38
# 0.33 3.79
# 0.47 5.44
# 0.62 7.14

# проверил на примере из презы - работает на f(x0,x1,x2) f(x0..x3) f(x0...x4)
# f(x0...x3) = 214.9    f(x0...x4) = -482.85

def countY(x,x_y): # подсчет значения ф-ии Ньютона в точке
    # x_y - массив начальных точек
    answer = x_y[0][1] # this is f(0)
    for i in range(1,len(x_y)):
        begEnd = [0,i]
        composition = 1 # произведение
        for j in range(0,i):
            composition = composition*(x-x_y[j][0])
        answer = answer + razdelRaznost(begEnd,x_y)*composition

    return answer

def minX(x_y):
    min=1000000
    for i in range(0,len(x_y)):
        if(min>x_y[i][0]):
            min = x_y[i][0]
    return min

def maxX(x_y):
    max=-1000000
    for i in range(0,len(x_y)):
        if(max<x_y[i][0]):
            max = x_y[i][0]
    return max

def draw(what,uncknownXs): #uncknownXs - те что вводим в конце в цикле while с end
    mode = what.getMode()
    fig = plt.figure()
    axes = fig.add_subplot(111)
    plt.title("Метод Ньютона")
    axes.grid()

    if(mode==0): # по точкам
        knownDots = what.getDataList()

        min = 1000000
        max = -1000000

        for i in range(0, len(knownDots)):
            x = knownDots[i][0]
            if (min > x):
                min = x
            if (max < x):
                max = x

        for j in range(0, len(uncknownXs)):
            this_x = uncknownXs[j]
            if (this_x < min or this_x > max):
                print("промежуток от наим. заданного Х до наиб заданного Х, не выходите за область определения ф-ии!")
                return 1


        for i in range(0, len(knownDots)):
            axes.scatter(knownDots[i][0], knownDots[i][1], c="black")  # это по которым строим

        print("для метода Ньютона:")
        for i in range(0, len(uncknownXs)):
            this_x = uncknownXs[i]
            axes.scatter(this_x, countY(uncknownXs[i], knownDots), c="deeppink")  # это которые хотим узнать
            print(f" x = {this_x} y = {countY(this_x, knownDots)}")


        count_y = countY



    else: # выбираем функцию
        funcType = what.getDataList()[0]
        if (funcType == 0):
            count_y = laGranzh.countSinX
            min = 100000
            max = -100000

        elif (funcType == 1):
            count_y = laGranzh.countX2
            min = 100000
            max = -100000


        elif (funcType == 2):
            count_y = laGranzh.countLogX
            min = 0.1
            max = -100000

        elif (funcType == 3):
            count_y = laGranzh.countSqrtX
            min = 0
            max = -100000

        for i in range(0, len(uncknownXs)):
            x = uncknownXs[i]
            if (max < x):
                max = x
            if (funcType == 0 or funcType == 1):
                if (min > x):
                    min = x
        if (funcType == 0 or funcType == 1):
            min = min - 2

        max = max + 1

        for j in range(0, len(uncknownXs)):
            this_x = uncknownXs[j]
            if (this_x < min or this_x > max):
                print("промежуток от наим. заданного Х до наиб заданного Х, не выходите за область определения ф-ии!")
                return 1

        print("для метода Ньютона:")
        for i in range(0, len(uncknownXs)):
            finaldots = []
            this_x = uncknownXs[i]

            if (this_x - 2 > min):
                x = this_x - 2
                beginning = this_x - 2
            else:
                x = min
                beginning = min


            for j in range(0, 5):
                temp = []
                step = (this_x + 2 - beginning) / 5
                temp.append(x)
                temp.append(count_y(x, what.getDataList()))
                finaldots.append(temp)
                x = x + step

            axes.scatter(this_x, countY(this_x, finaldots), c="deeppink")
            print(f" x ={this_x} y = {countY(this_x, finaldots)}")


###


#
    # a = []
    # b = []
    # for i in range(int(min * 10), int(max + 1) * 10):
    #     x = i / 10
    #     a.append(x)
    #     b.append(count_y(x, what.getDataList()))
    #
    #     axes.plot(a, b, c='#05aff5')
    #
    #
#
    a=[]
    b=[]
    for i in range(int(min*10),int(max+1)*10):
        # print(f"x = {x}")
        finaldots=[]
        x = i/10
        a.append(x)
        if (x - 2 > min):
            this_x = x - 2
            beginning = this_x - 2
        else:
            this_x = min
            beginning = min
        for j in range(0, 5):
            # print(f"Thisx = {this_x}")
            temp = []
            step = (x + 2 - beginning) / 5
            temp.append(this_x)
            temp.append(count_y(this_x, what.getDataList()))
            finaldots.append(temp)
            this_x = this_x + step
        b.append(countY(x,finaldots))

    axes.plot(a, b, c='#05aff5')
    plt.show()

# 0
# 2.2
# 4.4
# 6.6
# 8.8
# 11.1
# 13.3
# 15.5
# 17.7
# 21
# end