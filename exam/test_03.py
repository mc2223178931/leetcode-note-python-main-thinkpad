import numpy as np

def conv2d(image, kernel):
    # size = len(image)
    # print(size)
    # image_np = np.array(image)
    # (width, height) = image_np.shape
    # width = image_np.shape()
    result = [[0 for i in range(4)] for i in range(4)]
    img_pad = np.pad(image, (1, 1))
    # print(img_pad)
    for i in range(4):
        for j in range(4):
            image_tmp = img_pad[i:i+3, j:j+3]
            # print(image_tmp)
            result_kernel = (np.multiply(image_tmp, kernel)).sum()
            # print(result_kernel)
            # print(kernel)
            result[i][j] = result_kernel

    # for i

    return result

if __name__ == "__main__":
    # 3*3
    kernel = [
        [1., 0., 1.],
        [2., 0., 2.],
        [1., 0., 1.]
    ]
    # 4*4
    image = [
        [1, 3, 5, 7],
        [2, 4, 6, 8],
        [1, 3, 5, 7],
        [2, 4, 6, 8]
    ]
    out = conv2d(image, kernel)
    print(out)
    out = np.array(out)
    print(out.shape)





