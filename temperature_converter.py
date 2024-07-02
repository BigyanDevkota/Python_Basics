def temperature():
    print("temperature calculator")
    temp = float(input('enter temperature '))
    unit = input('which temperature did you enter ?\ntype c for celsius and type f for farenheit ').lower()

    if(unit == 'c'):
        fahrenheit = float((9*temp + 160)/5)
        print (round(fahrenheit,2))

    elif (unit == 'f'):
        celsius = float(5/9 * (temp - 32))
        print (round(celsius,2))

    else:
        print('invalid input')
        temperature()

temperature()
