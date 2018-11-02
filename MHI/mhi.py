import cv2
import numpy as np


def abs_diff_threshold(im1, im2, th):
    """
    im1 - Grayscale image
    im2 - Grayscale image
    """
    assert len(im1.shape) == 2
    assert len(im2.shape) == 2
    assert im1.shape == im2.shape
    assert th is not 0

    im3 = np.zeros(im1.shape, dtype=np.uint8)
    rows, cols = im1.shape[0], im1.shape[1]
    for i in range(0, rows):
        for j in range(0, cols):
            if abs(im1[i, j]-im2[i, j]) > th:
                im3[i, j] = 1
            else:
                im3[i, j] = 0
    return im3

def mhi():
    """
    mhi
    =====

    Find mhi of given two images
    """
    im1 = np.array([[1, 2], [1, 2], [1, 2]])
    im2 = np.array([[1, 2], [1, 2], [1, 2]])
    th = 1
    im3 = abs_diff_threshold(im1, im2, th)


if __name__ == '__main__':
    
    mhi()
