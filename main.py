import input_object
import input_settings
import laGranzh
import methodNewton
import sys

what = input_settings.inp()
# print(f"mode = {what.mode} datalist = {what.dataList}")


while True:
    print(
        "Введите точки, значение которых хотите узнать: PS промежуток от наим. Х до наиб Х, не забывайте об области определения(для ф-ии)")
    print("Для окончания ввода напишите \"end\" без кавычек")
    try:
        temp=[]
        while True:
            x = input()
            if (x == "end"):
                break
            x = float(x)
            temp.append(x)
            # print(methodNewton.countY(x,what.getDataList()))
        laGranzh.draw(what.getDataList(),"Лагранж",temp,what)
        methodNewton.draw(what,temp)

    # begEnd = [0,len(what.getDataList())-1]
    # print(methodNewton.razdelRaznost(begEnd,what.getDataList()))


    except Exception:
    #     e = sys.exc_info()[1]
    #     print(e.args[0])
        print("ошибка ввода, повторите")
# print(laGranzh.countY(0.35,what.dataList))


# 0.1 1.25
# 0.2 2.38
# 0.3 3.79
# 0.4 5.44
# 0.5 7.14

# 2 10
# -1 5
# 100 4
# 200 5