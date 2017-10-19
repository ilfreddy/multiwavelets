import numpy
import matplotlib.pyplot as plt

nPolynomials = 4
max_scale = 5

def scaling(x):
    if( x >= 0 and x < 1):
        val = 1.0
    else:
        val = 0.0
    return val

def wavelet(x):
    return scaling(2*x) - scaling(2*x-1)

    
def scaling_nl(n, l, x):
    factor = 2.0**n
    return numpy.sqrt(factor) * scaling(factor*x-l)

def wavelet_nl(n, l, x):
    factor = 2.0**n
    return numpy.sqrt(factor) * wavelet(factor*x-l)

if __name__ == '__main__':
    x = numpy.arange(0, 1.0001, 0.001);
    w0 = numpy.array([wavelet_nl(3,0,x[i]) for i in range(x.size)])
    w1 = numpy.array([wavelet_nl(3,1,x[i]) for i in range(x.size)])
    w2 = numpy.array([wavelet_nl(3,2,x[i]) for i in range(x.size)])
    w3 = numpy.array([wavelet_nl(3,3,x[i]) for i in range(x.size)])
    w4 = numpy.array([wavelet_nl(3,4,x[i]) for i in range(x.size)])
    w5 = numpy.array([wavelet_nl(3,5,x[i]) for i in range(x.size)])
    w6 = numpy.array([wavelet_nl(3,6,x[i]) for i in range(x.size)])
    w7 = numpy.array([wavelet_nl(3,7,x[i]) for i in range(x.size)])
    plt.plot(x, w0)
    plt.plot(x, w1)
    plt.plot(x, w2)
    plt.plot(x, w3)
    plt.plot(x, w4)
    plt.plot(x, w5)
    plt.plot(x, w6)
    plt.plot(x, w7)
    plt.show()


    
