import scipy as sp
import pylab as p
#motion of a particle under the influence of a force F = -kx; k = 1

def shm():
    n = 1000
    dt = 2*sp.pi/n

    X = [0]*n
    V = [1]*n
    T = [0]*n
    for i in xrange(0, n-1):
        X[i+1] = V[i]*dt + X[i]
        V[i+1] = -X[i]*dt + V[i]
        T[i+1] = T[i] + dt

    p.plot(T,X) + p.plot(T,V)
    p.show()


