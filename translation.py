import cv2
import matplotlib.pyplot as plt

# Membaca gambar seperti biasa
img = cv2.imread("meng.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Horizontal flip (dibalik kiri-kanan)
hasil_horizontal = cv2.flip(img, 1)

# Vertical flip (dibalik atas-bawah)
hasil_vertikal = cv2.flip(img, 0)

# Menampilkan hasil
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title("Citra Asli")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(hasil_horizontal)
plt.title("Horizontal Flip")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(hasil_vertikal)
plt.title("Vertical Flip")
plt.axis("off")

plt.tight_layout()
plt.show()