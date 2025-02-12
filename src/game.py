import cv2
import numpy as np

window_width = 480
window_height = 360

window = np.zeros((window_height, window_width, 3), dtype=np.uint8)
window_name = "Game"

cv2.namedWindow(window_name)
cv2.imshow(window_name, window)

png_image_path = "assets/enemigo.png"
png_image = cv2.imread(png_image_path, cv2.IMREAD_UNCHANGED)

if png_image is None:
    print("Error: No se pudo cargar la imagen")
    exit()

height, width = png_image.shape[:2]

if png_image.shape[2] == 4:
    b, g, r, a = cv2.split(png_image)
    alpha = a / 255.0
    
x = 100
y = 200

for c in range(3):
    window[y:y+height, x:x+width, c] = (alpha* png_image[:, :, c] + (1-alpha) * window[y:y+height, x:x+width, c])

while cv2.waitKey(1) != ord('q'):
    cv2.imshow(window_name, window)

cv2.destroyAllWindows()