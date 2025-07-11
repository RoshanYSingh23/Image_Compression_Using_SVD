import numpy as np
import cv2


"""
Compress a grayscale or BGR color image using SVD.

Args:
    k (int): Number of singular values to retain.
    img_array (np.ndarray): 2D grayscale or 3D BGR image.

Returns:
    np.ndarray: Compressed image.
"""
def svd_compress(k, img_array):
    if len(img_array.shape) == 2:
        # Grayscale
        U, S, VT = np.linalg.svd(img_array)
        S_k = np.diagflat(S[:k])
        U_k = U[:, :k]
        VT_k = VT[:k, :]
        compressed = np.matmul(np.matmul(U_k, S_k), VT_k)
        compressed = (compressed - np.min(compressed)) / (np.max(compressed) - np.min(compressed)) * 255
        return compressed.astype(np.uint8)

    elif len(img_array.shape) == 3 and img_array.shape[2] == 3:
        # Color (BGR)
        blue_channel, green_channel, red_channel = cv2.split(img_array)
        compressed_channels = []
        for channel in [blue_channel, green_channel, red_channel]:
            U, S, VT = np.linalg.svd(channel)
            S_k = np.diagflat(S[:k])
            U_k = U[:, :k]
            VT_k = VT[:k, :]
            compressed_channel = np.matmul(np.matmul(U_k, S_k), VT_k)
            compressed_channel = (compressed_channel - np.min(compressed_channel)) / (np.max(compressed_channel) - np.min(compressed_channel)) * 255
            compressed_channels.append(compressed_channel.astype(np.uint8))
        return cv2.merge(compressed_channels)

    else:
        raise ValueError("Input must be either a 2D grayscale or 3D BGR image.")
