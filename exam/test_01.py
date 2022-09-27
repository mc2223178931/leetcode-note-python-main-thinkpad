import numpy as np
def conv2d(image, kernel):
    print(len(image))
    result = (np.multiply(image, kernel)).sum()
    return result
# 3*3
kernel = [
    [1., 0., 1.],
    [2., 0., 2.],
    [1., 0., 1.]
]
# 4*3
image = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [1, 3, 5, 7],
    [2, 4, 6, 8]
]
out = conv2d(image, kernel)




