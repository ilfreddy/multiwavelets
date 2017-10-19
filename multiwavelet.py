import numpy, sys, struct
from math import sin, pi
import matplotlib.pyplot as plt

nPolynomials = 4
max_scale = 5

def scaling(j,x): # j goes from 0 to nPolynomials - 1
    if ( x >= 0.0 and x < 1.0):
        coefs = [0 for i in range(j+1)]
        coefs[j] = 1
        scaling = numpy.sqrt(2*j + 1) * numpy.polynomial.legendre.Legendre(coefs,domain=[0,1])
        value = scaling(x)
    else:
        value = 0.0

    return value

def wavelet(j,np,x):
    if ( x >= 0.0 and x < 1.0):
        s0 = numpy.array([scaling_nl(i, 1, 0, x) for i in range(np)])
        s1 = numpy.array([scaling_nl(i, 1, 1, x) for i in range(np)])
        g0 = getfilter("G",0,np)
        g1 = getfilter("G",1,np)
        values = g0.dot(s0) + g1.dot(s1)
        value = values[j]
    else:
        value = 0.0
    return value
    
def scaling_nl(j, n, l, x):
    coef = 2.0 ** (float(n)/2.0)
    coef2 = 2.0 ** (float(n))
    return coef * scaling(j, coef2 * x - l)

def wavelet_nl(j, n, l, np, x):
    coef = 2.0 ** (float(n)/2.0)
    coef2 = 2.0 ** (float(n))
    return coef * wavelet(j, np, coef2 * x - l)

def getfilter(type="H",flag=0,np=4):
    order = np - 1
    name = "mwfilters/L_" + type + "0_" + str(order)
    filterFile = open(name, 'rb')
    filterData = filterFile.read()
    filterList = []
    for i in range((np)*(np)):
        rstart = i * 8
        rend = (i + 1) * 8
        filterList.append(struct.unpack_from("d",filterData[rstart:rend]))
    filterArray = numpy.array(filterList)
    filterMatrix = numpy.ndarray((np, np),buffer=filterArray)
    if (flag == 1):
        if (type == "G" and np%2 != 0 ):
            sign_np = -1
        else:
            sign_np = 1
        for i in range(np):
            for j in range(np):
                sign_ij = 1
                if (((i+j)%2) == 0):
                    sign_ij = -1
                sign = sign_ij * sign_np
                filterMatrix[i,j] *= sign
    return filterMatrix



if __name__ == '__main__':
#    print getfilter("H",0,2)
#    print getfilter("H",1,2)
#    print getfilter("G",0,2)
#    print getfilter("G",1,2)
    x = numpy.arange(0, 1.0001, 0.001);
    w0 = numpy.array([wavelet_nl(0,3,0,8,x[i]) for i in range(x.size)])
    w1 = numpy.array([wavelet_nl(1,3,1,8,x[i]) for i in range(x.size)])
    w2 = numpy.array([wavelet_nl(2,3,2,8,x[i]) for i in range(x.size)])
    w3 = numpy.array([wavelet_nl(3,3,3,8,x[i]) for i in range(x.size)])
    w4 = numpy.array([wavelet_nl(4,3,4,8,x[i]) for i in range(x.size)])
    w5 = numpy.array([wavelet_nl(5,3,5,8,x[i]) for i in range(x.size)])
    w6 = numpy.array([wavelet_nl(6,3,6,8,x[i]) for i in range(x.size)])
    w7 = numpy.array([wavelet_nl(7,3,7,8,x[i]) for i in range(x.size)])
#    s00 = numpy.array([scaling_nl(0,1,0,x[i]) for i in range(x.size)])
#    s01 = numpy.array([scaling_nl(1,1,0,x[i]) for i in range(x.size)])
#    s10 = numpy.array([scaling_nl(0,1,1,x[i]) for i in range(x.size)])
#    s11 = numpy.array([scaling_nl(1,1,1,x[i]) for i in range(x.size)])
    #    plt.plot(x, s00, '.')
    #    plt.plot(x, s01, '.')
    #    plt.plot(x, s10, '.')
    #    plt.plot(x, s11, '.')
    
    plt.plot(x, w0)
    plt.plot(x, w1)
    plt.plot(x, w2)
    plt.plot(x, w3)
    plt.plot(x, w4)
    plt.plot(x, w5)
    plt.plot(x, w6)
    plt.plot(x, w7)
    plt.show()


    
