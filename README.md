# Image_Compression_Using_SVD

This project demonstrates **image compression using Singular Value Decomposition (SVD)**. By breaking down each color channel of an image into its singular values and vectors, we can reconstruct the image using fewer components, effectively compressing it with minimal quality loss.

The project includes a **Streamlit web app** that allows interactive control of the compression parameter \(k\) to observe how it affects image quality.

---

## 📁 Project Structure


| File                | Purpose                                                           |
|---------------------|-------------------------------------------------------------------|
| `embedding.py`      | Contains the core compression logic                               |
| `app.py`            | Streamlit app for UI and user interaction                         |
| `hacker.jpeg`       | Example image used in the app                                     |
| `AuroraBorealis.jpg`| Another sample image                                              |
| `Report.pdf`        | Project report describing the design, implementation, and results |
| `README.md`         | This README file                                                  |
| `.gitignore`        | Git ignore rules (excludes pycache)                               |

---

## 🧠 How It Works

1. The image is loaded and converted into a NumPy array.
2. Each color channel (Blue, Green, Red) is separated.
3. SVD is applied to each channel.
4. Only the top `k` singular values are retained to reconstruct each channel.
5. Channels are merged back to form the final compressed image.
6. The result is visualized in a Streamlit interface that lets the user change `k` and view the effect.

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Image_Compression_SVD.git
   cd Image_Compression_SVD
   ```

2. **Install dependencies**
    ```bash
    pip install streamlit numpy opencv-python pillow
    ```
---

## 🚀 Running the App

1. **Simply Run:**
    ```bash
    streamlit run app.py
    ```

2. **Then go to http://localhost:8501 in your browser.**

---

## 🖼 What You’ll See

**An interface with:**

1. A slider to change k (number of singular values retained)

2. Side-by-side view of:

    a. The original image

    b. The compressed image

3. You can adjust k and immediately observe how compression quality changes.

---

## ✍️ Author

Roshan Y Singh


