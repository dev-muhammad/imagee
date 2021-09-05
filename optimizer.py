import os
from imagee import Imagee

root = os.path.join(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_EXTENSIONS = ['.png', '.jpg', '.jpeg']

def optimize(image_name):
    image_path = root + "/temp/" + image_name
    _, file_extension = os.path.splitext(image_path)
    if file_extension not in ALLOWED_EXTENSIONS:
        return {"status": "error", "message": f'Format {file_extension} not supported! Use {ALLOWED_EXTENSIONS}'}
    try:
        im = Imagee()
        im.read(image_path)
        im.optimaze()
        base64 = im.getBase64()
        if (len(base64)>0):
            res = {
                "image": base64,
                "original_size": im.size,
                "optimized_size": im.optimized_size,
                "optimization_rate": im.optimization_rate,
                "status": "success"
            }
        else:
            res = {"status": "error", "message": "imagee result error"}
        return res
    except:
        print("imagee optimize error!")
        return {"status": "error", "message": "imagee optimize error"}