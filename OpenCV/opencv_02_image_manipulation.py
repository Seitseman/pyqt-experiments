import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

def download_and_unzip(url, save_path):
    print(f"Downloading and unzipping assets... ", end="")
    
    urlretrieve(url, save_path)
    
    try:
        with ZipFile(save_path) as z:
            z.extractall(f"{os.path.split(save_path)[0]}")
        print("Done")
    
    except Exception as e:
        print("\nInvalid file: ", e)
        
URL = r'https://www.dropbox.com/s/rys6f1vprily2bg/opencv_bootcamp_assets_NB2.zip?dl=1'


data_path = os.path.join(os.getcwd(), f"02_data")

if not os.path.exists(data_path):
    os.makedirs(data_path)
    
asset_zip_path = os.path.join(data_path, f"opencv_bootcamp_assets_NB2.zip")
print(f"getcwd: {os.getcwd()}   asset path: {asset_zip_path}")

if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)
    
cb_img = cv2.imread(f"{data_path}/checkerboard_18x18.png", 0)

# cv2.imshow("Image", cb_img)

plt.imshow(cb_img, cmap="gray")
# plt.show()

# print(cb_img)
print(cb_img[0, 0])
print(cb_img[0, 6])

cb_img_copy = cb_img.copy()
cb_img_copy[2, 2] = 200
cb_img_copy[2, 3] = 200
cb_img_copy[3, 2] = 200
cb_img_copy[3, 3] = 200

plt.imshow(cb_img_copy, cmap="gray")
# plt.show()

img_NZ_bgr = cv2.imread(f"{data_path}/New_Zealand_Boat.jpg", cv2.IMREAD_COLOR)
img_NZ_rgb = img_NZ_bgr[:, :, ::-1]

plt.imshow(img_NZ_rgb)
# plt.show()

cropped_region = img_NZ_rgb[200:400, 300:600]
plt.imshow(cropped_region)
# plt.show()

resized_cropped_region_2x = cv2.resize(cropped_region, None, fx=2, fy=2)
plt.imshow(resized_cropped_region_2x)
# plt.show()

desired_width = 100
aspect_ratio = desired_width / cropped_region.shape[1]
desired_height = int(cropped_region.shape[0]*aspect_ratio)
dim = (desired_width, desired_height)

resized_cropped_region = cv2.resize(cropped_region, dsize=dim, interpolation=cv2.INTER_AREA)
# plt.imshow(resized_cropped_region)
# plt.show()

resized_cropped_region_2x = resized_cropped_region_2x[:, :, ::-1]
cv2.imwrite(f"{data_path}/resized_cropped_region_2x.png", resized_cropped_region_2x)
cv2.imshow("2x cropped", cv2.imread(f"{data_path}/resized_cropped_region_2x.png"))

cropped_region = cropped_region[:, :, ::-1]
cv2.imwrite(f"{data_path}/cropped_region.png", cropped_region)
cv2.imshow("Cropped region", cv2.imread(f"{data_path}/cropped_region.png"))


img_NZ_rgb_flipped_horz = cv2.flip(img_NZ_rgb, 1)
img_NZ_rgb_flipped_vert = cv2.flip(img_NZ_rgb, 0)
img_NZ_rgb_flipped_both = cv2.flip(img_NZ_rgb, -1)

plt.figure(figsize=(18, 5))
plt.subplot(231);plt.imshow(img_NZ_rgb_flipped_horz);plt.title("Horizontal Flip");
plt.subplot(234);plt.imshow(img_NZ_rgb);plt.title("Original");

plt.subplot(232);plt.imshow(img_NZ_rgb_flipped_vert);plt.title("Vertical Flip")
plt.subplot(235);plt.imshow(img_NZ_rgb);plt.title("Original");

plt.subplot(233);plt.imshow(img_NZ_rgb_flipped_both);plt.title("Both Flipped")
plt.subplot(236);plt.imshow(img_NZ_rgb);plt.title("Original");

plt.show()

cv2.waitKey(5000)
cv2.destroyAllWindows()