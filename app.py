import streamlit as st
from PIL import Image
import numpy as np
import cv2
from embedding import svd_compress

st.title("Image Compression Using SVD")
st.write("Upload an image, choose color mode, and adjust the slider to observe the effect of compression.")

# File uploader
uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
else:
    image = Image.open("AuroraBorealis.jpg").convert("RGB")

# Convert to arrays
img_array_rgb = np.array(image)
img_array_bgr = cv2.cvtColor(img_array_rgb, cv2.COLOR_RGB2BGR)
img_array_gray = cv2.cvtColor(img_array_bgr, cv2.COLOR_BGR2GRAY)

# Choose color or grayscale
mode = st.radio("Choose mode:", ["Color", "Grayscale"])
is_color = mode == "Color"

img_array = img_array_bgr if is_color else img_array_gray

# Slider for k
k = st.slider("Select number of singular values (k)", min_value=1, max_value=min(img_array.shape[0], img_array.shape[1]), value=50)

# Compress
compressed_img = svd_compress(k, img_array)

# Display results
col1, col2 = st.columns(2)
with col1:
    st.image(img_array_rgb if is_color else img_array_gray, caption="Original Image", use_column_width=True, channels="RGB" if is_color else "L")
with col2:
    compressed_display = cv2.cvtColor(compressed_img, cv2.COLOR_BGR2RGB) if is_color else compressed_img
    st.image(compressed_display, caption=f"Compressed Image with k={k}", use_column_width=True, channels="RGB" if is_color else "L")
