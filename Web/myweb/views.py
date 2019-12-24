from django.shortcuts import render


# Create your views here.
def index(request):
    contexts = {
        'title': '庆余年2019',
        'url': 'http://gif-china.cc//uploads/allimg/201911/9a23fb545c9ad26f.jpg?h=190',
    }
    return render(request, 'index.html', context=contexts)