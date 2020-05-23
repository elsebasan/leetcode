import numpy

n, m = map(int,input().split())
array_numpy = numpy.eye(n, m, k=0)
print(str(array_numpy).replace('1', ' 1').replace('0', ' 0'))