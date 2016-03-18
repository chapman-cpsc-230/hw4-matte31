def H(x):
    if x < 0:
        value = 0
    else:
        value = 1
    return value

def test_H(value):
    if H(-10) != 0:
        print "Error 1"
    if H(-10**-15) != 0:
        print "Error 2"
    if H(0) != 1:
        print "Error 3"
    if H(10**-15) != 1:
        print "Error 4"
    if H(10) != 1:
        print "Error 5"
def main():
    value=0
    x = 0
    H(x)
    test_H(value)
main()
