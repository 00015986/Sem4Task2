# def countdown(n):
#    if n <= 0:
#        print('Blastoff!')
#    else:
#        print(n)
#        countdown(n - 1)


def countUp_Down(number_input):  # initial point

    if number_input >= 0:

        print(f">>>> countup({number_input})")  # countup system

        while number_input > 0:
            print(number_input)
            number_input -= 1
        print("Blastoff!")
    else:
        print(f">>>> countdown({number_input})")  # countdown system

        while number_input < 0:
            print(number_input)
            number_input += 1
        print("Blastoff!")


countUp_Down(-3)  # by entering minus or plus numbers, we can see How it works.


