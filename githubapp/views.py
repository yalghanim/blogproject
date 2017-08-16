from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
import requests

def org_members(request):
	person = request.user
	social_account = person.socialaccount_set.get(user=person.id)
	application_token = social_account.socialtoken_set.get(account=social_account.id)
	token = application_token.token

	url = 'https://api.github.com/orgs/joinCODED/members'

	response = requests.get(url, headers={'Authorization': 'token '+token})

	# return JsonResponse(response.json(), safe=False)
	return render(request, 'github.html',{'response': response.json()})


def list_branch(request):
	person = request.user
	social_account = person.socialaccount_set.get(user=person.id)
	application_token = social_account.socialtoken_set.get(account=social_account.id)
	token = application_token.token

	url = 'https://api.github.com/repos/yalghanim/blogproject/branches'

	response = requests.get(url, headers={'Authorization': 'token '+token})

	# return JsonResponse(response.json(), safe=False)
	return render(request, 'branch.html',{'response': response.json()})

def theme(request):
	return render(request, 'index.html',{})


