import requests
import json
from rauth import OAuth2Service
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse

def login(request):
    uber_api = OAuth2Service(
        client_id=settings.UBER_CLIENT_ID,
        client_secret=settings.UBER_CLIENT_SECRET,
        name=settings.UBER_APP_NAME,
        authorize_url='https://login.uber.com/oauth/authorize',
        access_token_url='https://login.uber.com/oauth/token',
        base_url='https://api.uber.com/v1/',
    )

    parameters = {
        'response_type': 'code',
        'redirect_uri': settings.UBER_REDIRECT_URI,
        'scope': 'profile history',
    }

    login_url = uber_api.get_authorize_url(**parameters)

    return redirect(login_url)


def login_return(request):

    parameters = {
        'redirect_uri': settings.UBER_REDIRECT_URI,
        'code': request.GET.get('code'),
        'grant_type': 'authorization_code',
    }

    response = requests.post(
        'https://login.uber.com/oauth/token',
        auth=(
            settings.UBER_CLIENT_ID,
            settings.UBER_CLIENT_SECRET,
        ),
        data=parameters,
    )

    request.session['access_token'] = response.json().get('access_token')

    return redirect('/')


def trips_feed(request):

    if not request.session.get('access_token'):
        return HttpResponse('Unauthorized', status=401)

    url = 'https://api.uber.com/v1/history?limit=50'
    response = requests.get(
        url,
        headers={
            'Authorization': 'Bearer %s' % request.session['access_token']
        }
    )

    data = response


    return HttpResponse(data, content_type="application/json")

def home(request):

    return render(request, 'home.html', {'logged_in':request.session.get('access_token')})