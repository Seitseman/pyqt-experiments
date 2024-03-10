import os
import cv2

import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image

def download_and_unzip(url, save_path):
    print(f"Downloading and extracting assets...", end="")
    
    urlretrieve(url, save_path)
    
    try:
        with ZipFile(save_path) as z:
            z.extractall(os.path.split(save_path)[0])
        
        print("Done")
    
    except Exception as e:
        print("\nInvalid file.", e)
        
URL = r"https://www.dropbox.com/s/qhhlqcica1nvtaw/opencv_bootcamp_assets_NB1.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), f"opencv_bootcamp_assets_NB1.zip")

if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)
    
image = cv2.imread(filename="checkerboard_18x18.png")
# cv2.imshow("Image", image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(image)

cb_img = cv2.imread("checkerboard_18x18.png", 0)
print(f"Image size: {cb_img.shape}   Data type: {cb_img.dtype}")

# plt.imshow(cb_img, cmap="gray")
# plt.show()

cb_img_fuzzy = cv2.imread("checkerboard_fuzzy_18x18.jpg", 0)
# cv2.imshow("Image", cb_img_fuzzy)
print(cb_img_fuzzy)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(cb_img_fuzzy, cmap="gray")
# plt.show()

coke_img = cv2.imread("coca-cola-logo.png", 1)
# cv2.imshow("Image", coke_img)

print(f"Image size: {coke_img.shape}   data type: {coke_img.dtype}")

coke_img_channels_reversed = cv2.cvtColor(coke_img, cv2.COLOR_BGR2RGB)

# plt.imshow(coke_img_channels_reversed)
# plt.show()

img_NZ_bgr = cv2.imread("New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)
b, g, r = cv2.split(img_NZ_bgr)

plt.figure(figsize=[20, 5])

plt.subplot(241)
plt.imshow(r, cmap='gray')
plt.title("Red Channel")

plt.subplot(242)
plt.imshow(g, cmap="gray")
plt.title("Green Channel")

plt.subplot(243)
plt.imshow(b, cmap="gray")
plt.title("Blue Channel")

imgMerged = cv2.merge((b, g, r))
plt.subplot(244)
plt.imshow(cv2.cvtColor(imgMerged, cv2.COLOR_BGR2RGB))
plt.title("Merged Output")

img_hsv = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2HSV)

h,s,v = cv2.split(img_hsv)

plt.subplot(245)
plt.imshow(h, cmap="gray")
plt.title("H Channel")

plt.subplot(246)
plt.imshow(s, cmap="gray")
plt.title("S Channel")

plt.subplot(247)
plt.imshow(v, cmap="gray")
plt.title("V Channel")

h_new = h + 10
img_NZ_merged = cv2.merge((h_new, s, v))
img_NZ_rgb = cv2.cvtColor(img_NZ_merged, cv2.COLOR_HSV2RGB)

plt.subplot(248)
plt.imshow(img_NZ_rgb)
plt.title("Original H + 10")

plt.show()

cv2.imwrite("New_Zealand_Lake_SAVED.png", img_NZ_bgr)
