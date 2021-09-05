import os
import imagee
from io import BytesIO
import base64

root = os.path.join(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_EXTENSIONS = ['.png', '.jpg', '.jpeg']

def optimize(image_name):
    buffer = BytesIO()
    image_path = root + "/temp/" + image_name
    _, file_extension = os.path.splitext(image_path)
    if file_extension not in ALLOWED_EXTENSIONS:
        return {"status": "error", "message": f'Format {file_extension} not supported! Use {ALLOWED_EXTENSIONS}'}
    try:
        res = imagee.optimize_in_buffer(image_path, buffer)
        if (
            isinstance(res, dict)
            and
            "image" in res.keys()
            ):
            res["image"] = "data:image/"+file_extension[1:]+";base64," + base64.b64encode(res["image"].getvalue()).decode("utf-8") 
            res["status"] = "success"
        else:
            res = {"status": "error", "message": "1"}
        return res
    except:
        print("imagee optimize error!")
        return {"status": "error", "message": "2"}