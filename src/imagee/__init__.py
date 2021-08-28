"""
Package name: imagee
Description: Tool for optimizing image 
Github repo: https://github/dev-muhammad/imagee
Author: Muhammad (https://github/dev-muhammad)
"""

import os.path
import sys
from PIL import Image

def optimize(inputPath, outputPath, quality=85):
    """
    Optimaze method for image optimizing
    params:
    - inputPath: input image path
    - outputPath: output image path
    - quality: quality of image from 0 to 100 (default 85)
    """
    
    # validating path
    _validateImage(inputPath)
    _validateImage(outputPath)

    try:
        
        file_size_before = _checkSize(inputPath) # get image size before optimizing

        image = Image.open(inputPath) 
        image.save(outputPath, "JPEG", optimize=True, quality=quality)

        file_size_after = _checkSize(outputPath) # get image size after optimizing
        optimization_rate = round((file_size_before-file_size_after)/float(file_size_before)*100, 2)
        print(f"Image optimized {optimization_rate}%")

    except Exception:
        sys.exit("Error on optimization process!")

def _checkSize(path):
    """
    Local method for checking file size
    """
    return os.stat(path).st_size
    


def _validateImage(path):
    """
    Local method to validating image
    - path: image path
    """

    SUPPORTED_FORMATS = ['.jpg', '.png'] # other formats not tested

    if os.path.exists(path):
        _, file_extension = os.path.splitext(path)
        if file_extension in SUPPORTED_FORMATS:
            return None
        else:
            sys.exit(f'Format {file_extension} not supported! Use {SUPPORTED_FORMATS}')
    else:
        sys.exit(f'File not exist in {path}')
