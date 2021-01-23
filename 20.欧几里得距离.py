import numpy
def calEuclideanDistance(vec1,vec2):
    dist = numpy.sqrt(numpy.sum(numpy.square(vec1 - vec2)))
    return dist
v1 = [1,2]
v2 = [2,3]
v1 = numpy.array(v1)
v2 = numpy.array(v2)
print(calEuclideanDistance(v1,v2))