import pytesseract
from pytesseract import Output
import cv2
import os
import shutil
import base64
import numpy as np
import tensorflow as tf

# pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
frase = ""


class OCR(object):
    def __init__(self, image):
        self.image = image;
    def config_input(self, img, lang="por", dict=Output.DICT):
        return pytesseract.image_to_data(img, lang=lang, output_type=dict)

    def build_phrase(self, frase, textos, img):
        for i in textos:
            if len(frase) <= 1:
                frase = i
            else:
                frase = frase + " " + i
        response = {"status": 200, "message": frase, "data":  base64.b64encode(img)}
        return response

    def start(self):
        from services.ocr.utils.text_util import Text_util
        from services.ocr.utils.img_util import Img_util
        img_raw = tf.image.decode_image(self.image, channels=3)
        cv2.imwrite(os.path.abspath(".") +  "/services/ocr/assets/data.jpg", img_raw.numpy())
        img, rgb, ipt = Img_util.config_img(self.config_input, "/services/ocr/assets/data.jpg")
        textos, img = Text_util.find(rgb, ipt)
        return self.build_phrase(frase, textos, img.tostring())


if __name__ == "__main__":
    OCR().start()
