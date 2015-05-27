import itertools


def valid(option):
    a,b,c,d,e,f,g,h,i = map(lambda x: float(x), option)
    
    return a + (13 * b / c) + d + (12 * e) - f - 11 + (g * h / i) - 10 == 66

correct = []

def print_option(option):
    a,b,c,d,e,f,g,h,i = option

    print "%i + (13 * %i : %i) + %i + (12 * %i) - %i - 11 + (%i * %i / %i) - 10 = 66" % (a,b,c,d,e,f,g,h,i)

for option in itertools.permutations(range(1, 10)):
    if valid(option):
        correct.append(option)
        print_option(option)
    
