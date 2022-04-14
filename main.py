counter = 0
counter2 = 0
lib = []
lib2 = []
accuracy_gradient = 1
set = [-1,-2,-3,-5,-5,-6,-7,-8,-9]
positive_or_negative = 0
positive_or_negative2 = 0
a,a2,b,c,d,d2 = False,False,False,False,False,False
positive = False
negative = False

while 1:
    main = input('>>> ')

    for m in range(len(set)):
        if main == 'run d':
            a = True
        if main == 'run d last '+str(m):
            a2 = True
            number3 = m
        elif main  == 'run last '+str(m):
            b = True
            number1 = m
        elif main == 'run average':
            d = True
        elif main == 'run average last '+str(m):
            d2 = True
            number2 = m
        elif main == 'run exit':
            exit()

    if a == True:
        a = False
        for i in range(len(set)-1):
            part1 = set[counter]
            counter += 1
            part2 = set[counter]
            difference = ((((part1 - part2) * -1)) / accuracy_gradient)
            lib.append(difference)
        print(sum(lib))
        lib.clear()
        counter = 0
    if a2 == True:
        a2 = False
        for k in range(number3):
            part3 = set[(len(set)-k)-1]
            counter2 +=1
            if counter2 >= 1:
                print('aye')
                part4 = set[(len(set)-k)-1]
                difference = ((((part3 - part4) * -1)) / accuracy_gradient)
                lib2.append(difference)
        print(lib2)
        lib2.clear()

    if b == True:
        b = False
        for p in range(number1):
            print(set[(len(set)-p)-1])

    if d == True:
        d = False
        for n in range(len(set)):
            if set[n] > 0:
                positive_or_negative +=1
                positive = True
            if set[n] < 0:
                positive_or_negative +=1

        if positive == True:
            print(str(positive_or_negative),'+')
        elif positive == False:
            print(str(positive_or_negative),'-')
        positive_or_negative = 0
        positive = False

    if d2 == True:
        for counter3 in range(number2):
            if set[(len(set) - counter3) - 1] < 0:
                positive_or_negative2 += 1
                negative = True
        if negative == True:
            print(positive_or_negative2,'-')
        elif negative == False:
            print(positive_or_negative2,'+')
        positive_or_negative2 = 0
        negative = False
