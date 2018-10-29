from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .forms import UploadFileForm


from keras.models import load_model
from tensorflow.keras.preprocessing.image import array_to_img, img_to_array, load_img
from sklearn.externals import joblib

import numpy as np

#load model
clf = joblib.load('model.pkl') 
#Dict bird_species_Id: Species name
birds_classes = {1:"Black footed Albatross", 2:"Yellow breasted Chat", 3:"Red legged Kittiwake",4:"Horned Lark"}

# Create your views here.
def homePageView(request):
    #return HttpResponse('Hello, World!')
	return render(request, 'index.html')

#views get the uploaded image
def simple_upload(request):
	if request.method == 'POST' and request.FILES['myfile']:	#myfile name in forms.html
		myfile = request.FILES['myfile']
		
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)					#get saved file name
		#uploaded_file_url = fs.url(filename)
		
		image_data = load_img(filename, target_size=(150,150))	#load the saved file
		img_array = img_to_array(image_data).flatten()			#flatten in 1XD vector
		img_reshaped=img_array.reshape(1,-1)					#reshape fo fit predict
		prediction_results = clf.predict(img_reshaped)
		prediction_results = birds_classes[prediction_results[0]]

		filename = fs.delete(myfile)	
		
		return render(request, 'forms.html', {'results':prediction_results})
		#return HttpResponse(birds_classes[prediction_results[0]])
		
		
	return render(request, 'forms.html')
	#return HttpResponse('is it reall done')




