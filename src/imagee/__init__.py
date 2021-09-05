"""
Package name: imagee
Version: 1.0
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
    """Main class"""
    image = None
    size = None
    format = None
    path = None
    optimized_size = None
    optimization_rate = None
    quality = 85
    optimized_image = BytesIO()

    SUPPORTED_FORMATS = {'jpg':"JPEG", 'jpeg':"JPEG", 'png':"PNG"} # other formats not tested

    def read(self, path):
        """Read image from path"""
        self.format = self._validateImage(path)
        self.size = self._checkSize(path)
        self.image = Image.open(path)
        self.path = path 
        pass

    def optimaze(self, quality=85):
        """
        Optimaze method for image optimization
        """
        if self.image is None:
            sys.exit('Any image not read for optimization. Use .read() method to select file, then optimize it!')
        self.quality = quality
        self.image.save(
                        self.optimized_image, 
                        self.format, 
                        optimize=True, 
                        quality=self.quality)
        self.optimized_size = self.optimized_image.getbuffer().nbytes # get image size after optimizing
        self.optimization_rate = round((self.size-self.optimized_size)/float(self.size), 2)
        pass

    def save(self, path):
        """Save image on path"""
        if self.optimized_size is None:
            sys.exit('Any image for saving. Use .read() method to select file, then optimize it!')
        image = Image.open(BytesIO(self.optimized_image.getbuffer()))
        image.save(path)
        # self.optimized_image.save(path, self.format)
        
        pass

    def getBase64(self):
        """Return image in base64 format"""
        if self.optimized_size is None:
            sys.exit('Any image not optimized. Use .read() method to select file, then optimize it!')
        return "data:image/"+self.format+";base64," + base64.b64encode(self.optimized_image.getvalue()).decode("utf-8")
        
    def _validateImage(self, path):
        """
        Local method to validating image
        - path: image path
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

    def _checkSize(self, path):
        """
        Local method for checking file size
        """
        return os.stat(path).st_size

