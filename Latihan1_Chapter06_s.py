# definition
def isPythagoras(a, b, c):
    if((c*c) == (a*a) + (b*b) or (a*a) == (c*c) - (b*b) or (b*b) == (c*c) - (a*a)):
        print(True)
    else:
        print(False)

# data a
isPythagoras(3, 4, 5)
# data b
isPythagoras(5, 9, 12)
# data c
isPythagoras(8, 6, 10)
# data d
isPythagoras(7, 8, 11)

