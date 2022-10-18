import cv2
import os
from utils.text_util import Text_util
from utils.img_util import Img_util
fonte = 'Fontes/calibri.ttf'

class Text_pred(object):
	def format_img(self, tipo,img, textos, n):
		cv2.imwrite(os.path.abspath('.') + f'/assets/preds/{tipo}{n}.jpg', img)
		return textos, f'{tipo}{n}.jpg'

	def predict_text(self, resultado, min_conf, img,n):
		img_copia = img.copy()
		textos = []
		for i in range(0, len(resultado['text'])):
			confianca = float(resultado['conf'][i])
			if int(confianca) > min_conf:
				texto = resultado['text'][i]
				if not texto.isspace() and len(texto) > 0:
				    x, y, img_copia = Img_util.bounding_box(resultado, img_copia, i)
				    textos.append(texto)
				    texto = resultado['text'][i] + ' - ' + str(int(float(resultado['conf'][i]))) + '%'
				    img_copia = Text_util.write(texto, x, y, img_copia, fonte)
		if(len(img.shape) == 3):
			textos, img = self.format_img("predicted",img_copia,textos, n)
			return textos,img
		else:
			textos, img = self.format_img("thresholded",img_copia,textos, n)
			return textos,img


