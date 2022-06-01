from PIL import Image
img = Image.open("a.jpg")

#Image_Resize
resize_img = img.resize((300, 300))
img.thumbnail((300, 300))
img.save("a7.png", "png")
img.show()


