import input_object
import matplotlib.pyplot as plt
import math

def draw(x_y,name,uncknownXs,what_input): # what_input - object of class input_object
    min = 1000000
    max = -1000000
    if (what_input.getMode() == 0):
        for i in range(0, len(x_y)):
            x = x_y[i][0]
            if (min > x):
                min = x
            if (max < x):
                max = x

        count_y = countY


            # if(what_input.getMode() == 1 and what_input.getDataList()[0] == 4 and this_x==0):
            #     print("1/x x!=0 Не забывай!")

    elif (what_input.getMode() == 1):
        funcType = what_input.getDataList()[0]
        if (funcType == 0):
            count_y = countSinX
            min = 100000
            max = -100000

        elif (funcType == 1):
            count_y = countX2
            min = 100000
            max = -100000


        elif (funcType == 2):
            count_y = countLogX
            min = 0.1
            max = -100000

        elif (funcType == 3):
            count_y = countSqrtX
            min = 0
            max = -100000

        # elif (funcType == 4):
        #     count_y = countGip
        #     min = 100000
        #     max = -100000
        #     for i in range(0, len(uncknownXs)):
        #         x = uncknownXs[i]
        #         if (min > x):
        #             min = x
        #     min = min - 2
        for i in range(0, len(uncknownXs)):
            x = uncknownXs[i]
            if (max < x):
                max = x
            if(funcType==0 or funcType==1):
                if (min > x):
                    min = x
        if (funcType ==0 or funcType==1):
            min = min - 2


        max = max+1

    for j in range(0,len(uncknownXs)):
        this_x = uncknownXs[j]
        if (this_x < min or this_x > max):
            print("промежуток от наим. заданного Х до наиб заданного Х, не выходите за область определения ф-ии!")
            return 1

    fig = plt.figure()
    axes = fig.add_subplot(111)

    axes.grid()
    a = []
    b = []
    # if (what_input.getMode() == 1 and what_input.getDataList()[0] == 4): # гипербола
    #     for i in range(int(min * 10), 0):
    #         x = i / 10
    #         if (what_input.getMode() == 1 and what_input.getDataList()[0] == 4 and x == 0):
    #             continue
    #         a.append(x)
    #         b.append(count_y(x, x_y))
    #     axes.plot(a, b)
    #     a = []
    #     b = []
    #     for i in range(1, int(max + 1) * 10):
    #         x = i / 10
    #         if (what_input.getMode() == 1 and what_input.getDataList()[0] == 4 and x == 0):
    #             continue
    #         a.append(x)
    #         b.append(count_y(x, x_y))
    #
    #     axes.plot(a, b)
    # else:

    #
    #





    plt.title(name)


    if(what_input.getMode() == 0): # если точки
        knownDots = what_input.getDataList()
        for i in range(0,len(knownDots)):
            axes.scatter(knownDots[i][0],knownDots[i][1],c="black") # это по которым строим

        print("для метода Лагранжа:")
        for i in range(0,len(uncknownXs)):
            this_x = uncknownXs[i]
            axes.scatter(this_x, countY(uncknownXs[i],x_y),c="deeppink") # это которые хотим узнать

            print(f" x = {this_x} y = {countY(this_x, knownDots)}")

        for i in range(int(min * 10), int(max + 1) * 10):
            x = i / 10
            if (what_input.getMode() == 1 and what_input.getDataList()[0] == 4 and x == 0):
                continue
            a.append(x)
            b.append(count_y(x, x_y))

            axes.plot(a, b, c='#05aff5')





    else: # если функции

        print("для метода Лагранжа:")
        for i in range(0, len(uncknownXs)):
            finaldots = []
            this_x = uncknownXs[i]

            if(this_x-2 > min ):
                x = this_x-2
                beginning = this_x-2
            else:
                x = min
                beginning = min

            # if (what_input.getMode() == 1 and what_input.getDataList()[0] == 4 and x == 0):
            #     x = x+0.001
            #     beginning = 0.001

            for j in range(0, 5):
                temp = []
                step = (this_x + 2 - beginning) / 5
                temp.append(x)
                temp.append(count_y(x, x_y))
                finaldots.append(temp)
                # if (what_input.getMode() == 1 and what_input.getDataList()[0] == 4 and x == 0):
                #     x = x + 0.001
                x = x + step



            axes.scatter(this_x, countY(this_x,finaldots),c="deeppink")
            print(f" x ={this_x} y = {countY(this_x, finaldots)}")

        a = []
        b = []
        for i in range(int(min * 10), int(max + 1) * 10):
            # print(f"x = {x}")
            finaldots = []
            x = i / 10
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
                temp.append(count_y(this_x, x_y))
                finaldots.append(temp)
                this_x = this_x + step
            b.append(countY(x, finaldots))

        axes.plot(a, b, c='#05aff5')





    plt.show()

def countY(x,dots): # это подсчет значения ф-ии ГАУССА в точке х
    # dots must be a list of dots x and y like that [[x1,y1],[x2,y2],...]
    n = len(dots)
    answer = 0
    for i in range(0,n):
        numerator = 1.0
        denumerator = 1.0
        for j in range(0,n):
            if(j==i):
                continue
            numerator = numerator*(x - dots[j][0])# числитель
            denumerator = denumerator*(dots[i][0] - dots[j][0]) # знаменатель
        answer = answer + numerator*dots[i][1]/denumerator
    return answer


def countSinX(x,dots):
    return math.sin(x)

def countX2(x,dots):
    return x*x

def countLogX(x,dots):
    return math.log(x)

def countSqrtX(x,dots):
    return math.sqrt(x)

# def countGip(x,dots):
#     return 1/x