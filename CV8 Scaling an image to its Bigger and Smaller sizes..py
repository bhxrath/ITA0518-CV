@@ -0,0 +1,7 @@
import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("C:/Users/Admin/Pictures/craiyon_084318_Cartoon_drawing_of_a_cute_panda.jpg",cv2.IMREAD_COLOR)
img = cv2.resize(img,(600,600))
cv2.imshow("image",img)
cv2.waitKey(0)
