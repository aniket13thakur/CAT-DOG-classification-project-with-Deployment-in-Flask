from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
# import os
# import uuid
# import flask
# import urllib
# from PIL import Image
# from tensorflow.keras.models import load_model
# from flask import Flask , render_template  , request , send_file
# from tensorflow.keras.preprocessing.image import load_img , img_to_array

app = Flask(__name__)

dic = {0 : 'Cat', 1 : 'Dog'}

model = load_model('Trained_Model.h5')

model.make_predict_function()

def predict_label(img_path):
	i = image.load_img(img_path, target_size=(100,100))
	i = image.img_to_array(i)/255.0
	i = i.reshape(1, 100,100,3)
	p = model.predict(i)
	print(p[0])
	if p[0][0]>0.5:
		return 'CAT'
	elif p[0][1]>0.5:
		return 'DOG'
	else:
		return 'Unknown'
	


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "Designed and Developed by Aniket Thakur"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = predict_label(img_path)

	return render_template("index.html", prediction = p, img_path = img_path)




if __name__ =='__main__':
	app.run(debug = True)






# 





# @app.route("/submit", methods = ['GET', 'POST'])
# def get_output():
# 	img_path=''
# 	if request.method == 'POST':
# 		if(request.form):
# 			link = request.form.get('link')
# 			resource = urllib.request.urlopen(link)
# 			unique_filename = str(uuid.uuid4())
# 			filename = unique_filename+".jpg"
# 			img_path = os.path.join(img_path, filename)
# 			print(img_path)
# 			output = open(img_path , "wb")
# 			output.write(resource.read())
# 			output.close()
#             # img = filename
# 		else:
# 	   		img = request.files['my_image']
# 	   		img_path = "static/" + img.filename
# 	   		img.save(img_path)

# 		p = predict_label(img_path)

# 	return render_template("index.html", prediction = p, img_path = img_path)