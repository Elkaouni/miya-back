from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

import gpt4free
from gpt4free import Provider

# Create your views here. (request handlers)

def say_hello():
    return HttpResponse('Welcome to poc Miya v1')

@csrf_exempt
def generate_response(request):
    if request.method == 'POST':
        if request.body is not None:
            print("response body is " + str(request.body))
            body= json.loads(request.body)
            prompt = body.get('prompt', None)

            if prompt is not None:
                print("prompt is "+prompt + "\n")
                response =  gpt4free.Completion.create(Provider.You, prompt=prompt)
                return JsonResponse({ 'response' : response}, status= 200)
            else:
                return JsonResponse({'error' : 'Parameter not found'}, status=400)
        else:
            return JsonResponse({'error' : 'Request body is empty'}, status=400)
    else:
        return JsonResponse({'error' : 'invalid request method'}, status=405)

def generate_wav_response(request):
    return HttpResponse('Still empty')