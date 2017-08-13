from django.shortcuts import render
from django.http import JsonResponse
import requests

def text_search(request):
	api_key = "AIzaSyBx6lJJvCFx69Bf5-Gkv7QG2Uk-CsGO_8w"
	query = request.GET.get("query", '')

	url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=%s&key=%s'%(query, api_key)
	# url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?query='+query+'&key='+api_key
	# ^ another method to type up the url (connoctation)

	next_page_token = request.GET.get("next_page_token")
	if next_page_token is not None:
		url+="&pagetoken=%s"%(next_page_token)

	response = requests.get(url)

	# return JsonResponse(response.json(), safe=False) #in raw json format
	return render(request, 'google.html',{'response': response.json()})

def text_detail(request):
	api_key = "AIzaSyBx6lJJvCFx69Bf5-Gkv7QG2Uk-CsGO_8w"
	query = request.GET.get("reference")

	url = 'https://maps.googleapis.com/maps/api/place/details/json?reference=%s&key=%s'%(query, api_key)

	response = requests.get(url)

	return JsonResponse(response.json(), safe=False) #in raw json format
	# return render(request, 'google.html',{'response': response.json()})

def place_detail(request):
	api_key = "AIzaSyBx6lJJvCFx69Bf5-Gkv7QG2Uk-CsGO_8w"
	query = request.GET.get("reference", "")
	map_key = "AIzaSyCZZMBmno9mAq_ulyyouknzhHGmsIodZUQ"

	PLACE_ID_URL = "https://maps.googleapis.com/maps/api/place/details/json?reference="+query+"&key="+api_key
	response = requests.get(PLACE_ID_URL)

	context = {
		"response": response.json(),
		"api_key": map_key,
	}

	return render(request, 'googleplace.html', context)