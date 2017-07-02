import math
import numpy as np

if __name__ == '__main__':
    print math.log(3)
    x = [3, 2, 6, 5, 9, 5, 8]
    print np.array(x).shape
    for number in x[:3]:
        print number
    mh = [[1, 5, 9], [5, 8, 7]]
    print np.amax(mh)
    print '----------'
    print mh[1][2]

    abc = [1,5,6,8,4]
    # abc.append([[5, 29], [57, 45], [1,79]])
    print type(abc)

    var = np.zeros(5)
    print type(var)
    print 'var = ', var

    abc.append(var)
    print 'abc = ', abc



