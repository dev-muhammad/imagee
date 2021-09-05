"""
Package name: imagee
Version: 1.1
Description: Tool for optimizing image 
Github repo: https://github/dev-muhammad/imagee
Author: Muhammad (https://github/dev-muhammad)
"""

import os.path
import sys
from PIL import Image
from io import BytesIO
import base64

class Imagee():
    """
    Main Imagee class

    Attribute:
    - image (PIL.Image): current image 
    - size (int): current image size
    - format (str): current image format
    - path (str): current image path
    - optimized_size (int): optimized image size in bytes
    - optimization_rate (float): optimization rate
    - quality (int): quality of optimized image | default = 85
    - optimized (io.BytesIO): optimized image in buffer

    Methods:
    - read(path: str) -> none: select/read image from path
    - optimaze(quality: int) -> none: optimize selected image (0<quality<100)
    - save(path: str) -> none: save optimized image to path
    - getBase64() -> str: get optimized image in string with base64 decoded format
    """
    
    image = None
    size = None
    format = None
    path = None
    optimized_size = None
    optimization_rate = None
    quality = 85
    optimized = BytesIO()

    SUPPORTED_FORMATS = {'jpg':"JPEG", 'jpeg':"JPEG", 'png':"PNG"} # other formats not tested

    def __init__(self) -> None:
        self.image = None
        self.size = None
        self.format = None
        self.path = None
        self.optimized_size = None
        self.optimization_rate = None
        self.quality = 85
        self.optimized = BytesIO()

    def read(self, path: str) -> None:
        """Read image from path"""
        self.format = self._validateImage(path)
        self.size = self._checkSize(path)
        self.image = Image.open(path)
        self.path = path 
    

    def optimaze(self, quality=85) -> None:
        """
        Optimaze method for image optimization
        """
        if self.image is None:
            sys.exit('Any image not read for optimization. Use .read() method to select file, then optimize it!')
        self.quality = quality
        self.image.save(
                        self.optimized, 
                        self.format, 
                        optimize=True, 
                        quality=self.quality)
        self.optimized_size = self.optimized.getbuffer().nbytes # get image size after optimizing
        self.optimization_rate = round((self.size-self.optimized_size)/float(self.size), 2)

    def save(self, path: str) -> None:
        """Save image on path"""
        if self.optimized_size is None:
            sys.exit('Any image for saving. Use .read() method to select file, then optimize it!')
        image = Image.open(BytesIO(self.optimized.getbuffer()))
        image.save(path)

    def getBase64(self) -> str:
        """Return image in base64 format in string"""
        if self.optimized_size is None:
            sys.exit('Any image not optimized. Use .read() method to select file, then optimize it!')
        return "data:image/"+self.format+";base64," + base64.b64encode(self.optimized.getvalue()).decode("utf-8")
        
    def _validateImage(self, path: str) -> str:
        """
        Local method to validating image
        - path: image path (str)
        returns file extensions (str)
        """

        if os.path.exists(path):
            _, file_extension = os.path.splitext(path)
            file_extension = file_extension[1:]
            if file_extension in self.SUPPORTED_FORMATS.keys():
                return self.SUPPORTED_FORMATS[file_extension]
            else:
                sys.exit(f'Format {file_extension} not supported! Use {self.SUPPORTED_FORMATS}')
        else:
            sys.exit(f'File not exist in {path}')

    def _checkSize(self, path: str) -> int:
        """
        Local method for checking file size
        - path: image path (str)
        returns file size (int)
        """
        return os.stat(path).st_size
