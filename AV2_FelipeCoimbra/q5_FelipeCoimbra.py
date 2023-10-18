from flask import Flask, render_template, request, redirect
from PIL import Image, ImageEnhance
# USANDO A QUESTÃO 3 PARA UTILIZAR FLASK

generateImgObj = lambda filepath: Image.open(filepath)
changeBrightness = lambda image, factor: ImageEnhance.Brightness(generateImgObj(image)).enhance(factor).save(fp= "static/images/resultado.png") or redirect("/resposta")


# inputImg = generateImgObj(img_path)
# outputImg = changeBrightness(img_path, 2)
# inputImg.show()
# outputImg.show()



app = Flask(__name__)

index = lambda : render_template("index.html") if request.method == "GET" else changeBrightness(request.form["arquivo"], int(request.form["brilho"]))
resposta = lambda : render_template("resposta.html") if request.method == "GET" else "ERRO"

app.add_url_rule("/", view_func= index, methods= ["GET", "POST"], endpoint="index")
app.add_url_rule("/resposta", view_func=resposta, methods= ["GET", "POST"], endpoint="resultado")
app.run(debug= True)

