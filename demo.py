from src.imagee import Imagee
image_path = "images/peach.jpg"
output_path = "images/min_peach.png"

im = Imagee()
im.read(image_path)
print(im.format)
print(im.size)

im.optimaze()
print(im.optimized_size)
print(im.optimization_rate)

r = im.getBase64()
print(r[:50])
im.save("images/min_peach.jpg")