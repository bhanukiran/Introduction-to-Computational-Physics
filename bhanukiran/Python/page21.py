
def lagrange():
    xi = [0, 0.5, 1, 1.5, 2]
    fi = [1, 0.938470, 0.765198, 0.511828, 0.223891]

    x = 0.9; f = aitken(x, xi, fi)

    print("intepreted value = ", f)
    return f

def aitken(x, xi, fi):
    n = len(xi) - 1
    ft = [i for i in fi]

    for i in xrange(0, n):
        for j in xrange(0, n - i):
            ft[j] = (x-xi[j])/(xi[i+j+1]-xi[j])*ft[j+1] +(x-xi[i+j+1])/(xi[j]-xi[i+j+1])*ft[j]
    return ft[0]
    
