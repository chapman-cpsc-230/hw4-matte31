print "Histogram"
x = [4,9,13,5]
def histogram():

    for n in x:
        for y in range(n):
            st = ""
            for col in range(n):
                st += "*"

        print st
histogram()
