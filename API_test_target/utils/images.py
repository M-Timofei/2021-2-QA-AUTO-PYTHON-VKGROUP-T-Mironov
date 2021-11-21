import os
import numpy
from PIL import Image

class CreateImg:

    @staticmethod
    def create_img(image_path, company_name):
        img_name = company_name + '.png'
        imarray = numpy.random.rand(400, 240, 3) * 255
        im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
        im.save(os.path.join(image_path, img_name))
        return img_name