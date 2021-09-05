"""
Package name: imagee
Description: Tool for optimizing image 
Github repo: https://github/dev-muhammad/imagee
Author: Muhammad (https://github/dev-muhammad)
"""

import os.path
import sys
from PIL import Image

class Imagee():
    """Main class"""
    image = None
    size = None
    format = None
    path = None
    optimized_size = None
    optimization_rate = None
    quality = 85
    optimized_image = None

    def read(self, path):
        """Read image from path"""
        self.format = _validateImage(path)
        self.size = _checkSize(path)
        self.image = Image.open(path)
        self.path = path 
        pass

    def optimaze(self, quality=85):
        """
        Optimaze method for image optimization
        """
        self.image.save(
                        self.optimized_image, 
                        self.format, 
                        optimize=True, 
                        quality=self.quality)
        file_size_after = self.optimized_image.getbuffer().nbytes # get image size after optimizing
        self.optimization_rate = round((self.size-file_size_after)/float(self.size), 2)
        pass

    def save(self, path):
        """Save image on path"""
        # self.optimized_image.save(buffer, file_type, optimize=True, quality=quality)
        pass

    def getBase64():
        """Return image in base64 format"""
        pass

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
            return file_extension
        else:
            sys.exit(f'Format {file_extension} not supported! Use {SUPPORTED_FORMATS}')
    else:
        sys.exit(f'File not exist in {path}')
