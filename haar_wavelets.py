import numpy
import matplotlib.pyplot as plt

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
    w00 = numpy.array([wavelet_nl(0,0,x[i]) for i in range(x.size)])
    w10 = numpy.array([wavelet_nl(1,0,x[i]) for i in range(x.size)])
    w11 = numpy.array([wavelet_nl(1,1,x[i]) for i in range(x.size)])
    w20 = numpy.array([wavelet_nl(2,0,x[i]) for i in range(x.size)])
    w21 = numpy.array([wavelet_nl(2,1,x[i]) for i in range(x.size)])
    w22 = numpy.array([wavelet_nl(2,2,x[i]) for i in range(x.size)])
    w23 = numpy.array([wavelet_nl(2,3,x[i]) for i in range(x.size)])
    w30 = numpy.array([wavelet_nl(3,0,x[i]) for i in range(x.size)])
    w31 = numpy.array([wavelet_nl(3,1,x[i]) for i in range(x.size)])
    w32 = numpy.array([wavelet_nl(3,2,x[i]) for i in range(x.size)])
    w33 = numpy.array([wavelet_nl(3,3,x[i]) for i in range(x.size)])
    w34 = numpy.array([wavelet_nl(3,4,x[i]) for i in range(x.size)])
    w35 = numpy.array([wavelet_nl(3,5,x[i]) for i in range(x.size)])
    w36 = numpy.array([wavelet_nl(3,6,x[i]) for i in range(x.size)])
    w37 = numpy.array([wavelet_nl(3,7,x[i]) for i in range(x.size)])
    plt.plot(x, w10)
    plt.plot(x, w22)
    plt.plot(x, w36)
    plt.show()


    
