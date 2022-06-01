from PIL import Image, ImageFilter
img = Image.open("a.jpg")

#Blur_Image
blur_img = img.filter(ImageFilter.BLUR)
blur_img.save("a1.png", "png")

#Sharpen_Image
sharp_img = img.filter(ImageFilter.SHARPEN)
sharp_img.save("a2.png", "png")

#Smooth_Image
smooth_img = img.filter(ImageFilter.SMOOTH)
smooth_img.save("a3.png", "png")
