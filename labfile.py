import numpy 

def calculate_projection_normalvector(point, normalvector):
    return numpy.dot(point, normalvector)

def calculate_projection_angular_vectors(point, u, v):
    normalvector = numpy.cross(u,v)
    return calculate_projection_normalvector(point, normalvector)

print(calculate_projection_angular_vectors([numpy.pi, numpy.e, 1], [1,1,0], [0,-1,0]))
print(calculate_projection_normalvector([numpy.pi, numpy.e, 1], [3,3,3]))