### Cara membaca dan Menampilkan Gambar dengan Menggunakan Opencv
import cv2

gambar_input = cv2.imread('ronaldo.jpg') #Membaca/Load Gambar

cv2.imshow("Ronaldo". gambar_input) #Menampilkan Gambar

cv2.waitKey(0) #ESC
cv2.destroyALLWindows()