import cv2

class Img_util(object):
	def config_img(src):
		img = cv2.imread(os.path.abspath('.') + src)
		rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		ipt = self.config_input(rgb)
		return img,rgb,ipt

	def bounding_box(inp, img, i, cor=(0, 255, 0), tam_fonte=2):
		x = inp['left'][i]
		y = inp['top'][i]
		w = inp['width'][i]
		h = inp['height'][i]

		cv2.rectangle(img, (x, y), (x + w, y + h), cor, tam_fonte)
		return x, y, img