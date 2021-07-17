from django.http import HttpResponse

def index(request, network_data):
    return HttpResponse("Current data is %s", network_data)
