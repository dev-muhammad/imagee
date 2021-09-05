# Imagee
## Simple image optimization tool
Install with pip
```
pip install imagee
```
Optimaze image with simple way

```
from imagee import Imagee
image_path = "images/peach.jpg"
output_path = "images/min_peach.png"
im = Imagee()
im.read(image_path)
print(im.format)
print(im.size)
im.optimaze()
print(im.optimized_size)
print(im.optimization_rate)
im.save(output_path)
```