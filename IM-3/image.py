from PIL import Image, ImageFilter
img = Image.open("a.jpg")

#Image_Resize
resize_image = img.resize((300,300))
resize_image.save("a4.png", "png")
resize_image.show()

#Rotate_Image
rotate_image = img.rotate(90)
rotate_image.save("a5.png", "png")
rotate_image.show()

#Crop_Image
crop_img = (100, 100, 300, 300)
crop_img = img.crop(crop_img)
crop_img.save("a6.png", "png")
crop_img.show()