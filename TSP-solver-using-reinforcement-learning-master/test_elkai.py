import elkai
import numpy as np

CONST = 100000.0
def calc_dist(p, q):
    return np.sqrt(((p[1] - q[1])**2)+((p[0] - q[0]) **2)) * CONST

if __name__ =='__main__':
    data = np.random.uniform(0, 1, size=(10, 2))
    #print(data)
    num_points = len(data)
    ret_matrix = np.zeros((num_points, num_points))
    for i in range(num_points):
        for j in range(i+1, num_points):
            ret_matrix[i,j] = ret_matrix[j,i] = calc_dist(data[i], data[j])
    q = elkai.solve_float_matrix(ret_matrix) # Output: [0, 2, 1]

    print(q)
    dist = 0
    for i in range(num_points):
        dist += ret_matrix[q[i], q[(i+1) % num_points]]
    print(dist / CONST)