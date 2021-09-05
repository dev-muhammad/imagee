"""
Package name: imagee
Description: Tool for optimizing image 
Github repo: https://github/dev-muhammad/imagee
Author: Muhammad (https://github/dev-muhammad)
"""

import os.path
import sys
from PIL import Image

def optimize_in_buffer(inputPath, buffer, quality=85):
    """
    Optimaze method for image optimizing
    params:
    - inputPath: input image path
    - buffer: BytesIO object
    - quality: quality of image from 0 to 100 (default 85)

    return:
    dict 
        original_size: (int) image size in bytes before optimazing, 
        optmized_size: (int) image size after in bytes optimazing, 
        optimization_rate: (float) optimization rate, 
        image: optimized image in buffer object
    """
    
    # validating path
    file_type = _validateImage(inputPath)

    try:
        
        file_size_before = _checkSize(inputPath) # get image size before optimizing

        image = Image.open(inputPath) 
        image.save(buffer, file_type, optimize=True, quality=quality)
        file_size_after = buffer.getbuffer().nbytes # get image size after optimizing
        optimization_rate = round((file_size_before-file_size_after)/float(file_size_before), 2)
        # print(f"Image optimized {optimization_rate}%")
        return { "original_size": file_size_before, 
                 "optimized_size": file_size_after, 
                 "optimization_rate": optimization_rate, 
                 "image": buffer
                 }
    except Exception:
        sys.exit("Error on optimization process!")


def optimize(inputPath, outputPath, quality=85):
    """
    Optimaze method for image optimizing
    params:
    - inputPath: input image path
    - outputPath: output image path
    - quality: quality of image from 0 to 100 (default 85)

    return:
    dict 
        original_size: (int) image size in bytes before optimazing, 
        optmized_size: (int) image size after in bytes optimazing, 
        optimization_rate: (float) optimization rate,  
        saved_path: saved path
    """
    
    # validating path
    file_type = _validateImage(inputPath)

    try:
        
        file_size_before = _checkSize(inputPath) # get image size before optimizing

        image = Image.open(inputPath) 
        image.save(outputPath, file_type, optimize=True, quality=quality)
        file_size_after = _checkSize(outputPath) # get image size after optimizing
        optimization_rate = round((file_size_before-file_size_after)/float(file_size_before), 2)
        # print(f"Image optimized {optimization_rate}%")
        # print(f"Image saved in {outputPath}")
        return { "original_size": file_size_before, 
                 "optimized_size": file_size_after, 
                 "optimization_rate": optimization_rate, 
                 "saved_path": outputPath
                 }
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

    SUPPORTED_FORMATS = {'.jpg':"JPEG", '.jpeg':"JPEG", '.png':"PNG"} # other formats not tested

    if os.path.exists(path):
        _, file_extension = os.path.splitext(path)
        if file_extension in SUPPORTED_FORMATS.keys():
            return SUPPORTED_FORMATS[file_extension]
        else:
            sys.exit(f'Format {file_extension} not supported! Use {list(SUPPORTED_FORMATS.values())}')
    else:
        sys.exit(f'File not exist in {path}')
