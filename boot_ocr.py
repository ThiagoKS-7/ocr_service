import pytesseract
from pytesseract import Output


pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
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
        response = {"status": 200, "data": {"frase": frase, "img": img}}
        return response

    def start(self):
        from services.ocr.utils.text_util import Text_util
        from services.ocr.utils.img_util import Img_util
        print(self.image.filename)
        # TODO: SALVAR EM ASSETS E DAI ACESSAR O PATH
        img, rgb, ipt = Img_util.config_img(self.config_input, "/assets/data.jpg")
        textos, img = Text_util.find(rgb, ipt)
        print(self.build_phrase(frase, textos, img))


if __name__ == "__main__":
    OCR().start()
