from PIL import Image, ImageEnhance
img_path = "chainsaw_doge.webp"

generateImgObj = lambda filepath: Image.open(filepath)
changeBrightness = lambda image, factor: ImageEnhance.Brightness(generateImgObj(image)).enhance(factor)

inputImg = generateImgObj(img_path)
outputImg = changeBrightness(img_path, 2)
inputImg.show()
outputImg.show()