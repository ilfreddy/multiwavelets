import numpy
import matplotlib.pyplot as plt

def scaling(x):
    if( x >= 0.0 and x < 1.0):
        val = 1.0
    else:
        val = 0.0
    return val

def wavelet(x):
    return (scaling_nl(1,0,x) - scaling_nl(1,1,x)) / numpy.sqrt(2.0)

    
def scaling_nl(n, l, x):
    factor = 2.0**n
    return numpy.sqrt(factor) * scaling(factor*x-l)

def wavelet_nl(n, l, x):
    factor = 2.0**n
    return numpy.sqrt(factor) * wavelet(factor*x-l)

if __name__ == '__main__':
    x = numpy.arange(-0.1, 1.100001, 0.001);
    y = numpy.array([wavelet_nl(2,2,x[i]) for i in range(x.size)])
    plt.plot(x, y)
    plt.show()


    
