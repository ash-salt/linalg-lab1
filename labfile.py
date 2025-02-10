import numpy 
import math

def projection(v1, v2):
    factor = (numpy.dot(v1,v2))/numpy.dot(v2,v2)
    return [factor*v for v in v2]

def sub(v1, v2):
    i = 0
    sumvector = []
    while i < len(v1):
        sumvector.append(v1[i] - v2[i])
        i += 1
    return sumvector

def calculate_projection_normalvector(point, normalvector):
    xn = projection(point, normalvector)
    return sub(point,xn)

def calculate_projection_angular_vectors(point, u, v):
    normalvector = numpy.cross(u,v)
    return calculate_projection_normalvector(point, normalvector)

print(calculate_projection_angular_vectors([numpy.pi, numpy.e, 1], [1,1,0], [0,-1,0]))
print(calculate_projection_angular_vectors([numpy.pi, numpy.e, 1], [1,1,0], [0,1,0]))
print(calculate_projection_normalvector([numpy.pi, numpy.e, 1], [1,1,1]))
print(calculate_projection_normalvector([numpy.pi, numpy.e, 1], [3,3,3]))


# se bild för motivering
