import math as m

def H_eps(x,eps=float(0.01)):
    if x < -eps:
        value = 0
    elif x <= eps:
        value = (1/2)+(x/(2*eps))+(1/(2*m.pi))*m.sin((m.pi*x)/eps)
    else:
        value = 1
    return value
eps=float(0.01)
def test_H_eps(value):
    x = -10
    if H_eps(x) != 0:
        print "Error 1"
    x = -eps
    if H_eps(x) != (1/2)+(x/(2*eps))+(1/(2*m.pi))*m.sin((m.pi*x)/eps):
        print "Error 2"
    x = 0
    if H_eps(x) != (1/2)+(x/(2*eps))+(1/(2*m.pi))*m.sin((m.pi*x)/eps):
        print "Error 3"
    x = eps
    if H_eps(x) != (1/2)+(x/(2*eps))+(1/(2*m.pi))*m.sin((m.pi*x)/eps):
        print "Error 4"
    x = 10
    if H_eps(x) != 1:
        print "Error 5"
def main():
    x = 0
    eps=float(0.01)
    value = 0
    H_eps(x,eps=float(0.01))
    test_H_eps(value)

main()
