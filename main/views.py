from django.shortcuts import render


# Create your views here.
def index(request):
    # TODO get weather from request on weather site with parser
    weather = 0
    return render(request, 'index.html', {'weather': weather})
