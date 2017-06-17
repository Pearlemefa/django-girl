from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        'title': 'Emefa',
    }
    template = 'post/home.html'
    return render(request, template, context)
