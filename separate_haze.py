from PIL import Image
import os,sys
from torchvision.transforms.functional import crop


PATH = "./train/haze_images"
OUTPUT_PATH = "./train/Separate"

haze_imgs_dir = os.listdir(PATH)
haze_imgs = [(os.path.join(PATH,img),img) for img in haze_imgs_dir]

n = len(haze_imgs)
cnt = 0
for haze_img,name in haze_imgs:
    if cnt < int(n*0.7):
        img = Image.open(haze_img)
        haze_img = crop(img, 0, 0, int(img.size[1] / 2), img.size[0])
        clear_img = crop(img, int(img.size[1] / 2) + 1, 0, int(img.size[1] / 2), img.size[0])
        haze_img.save(os.path.join(OUTPUT_PATH,"train","hazy",name))
        clear_img.save(os.path.join(OUTPUT_PATH,"train","clear",name))
    else:
        img = Image.open(haze_img)
        haze_img = crop(img, 0, 0, int(img.size[1] / 2), img.size[0])
        clear_img = crop(img, int(img.size[1] / 2) + 1, 0, int(img.size[1] / 2), img.size[0])
        haze_img.save(os.path.join(OUTPUT_PATH,"test","hazy", name))
        clear_img.save(os.path.join(OUTPUT_PATH, "test","clear", name))

    cnt += 1
