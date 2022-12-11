import pytesseract
from PIL import ImageFont, Image, ImageDraw
import numpy as np


class Text_util(object):
    def write(texto, x, y, img, tamanho_texto=19):
        font = ImageFont.load_default()
        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        draw.text(
            (x, y - tamanho_texto), texto, font=font)
        return np.array(img_pil)

    def find(rgb, ipt):
        from services.ocr.utils.pred_util import Text_pred

        if len(pytesseract.image_to_string(rgb)) > 0:
            return Text_pred().predict_text(ipt, 40, rgb, "_rgb")
        else:
            return "Nada encontrado"
