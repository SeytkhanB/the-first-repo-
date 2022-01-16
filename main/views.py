
from django.shortcuts import render

# Create your views here.
def index(request):
    data = {'title': 'The Main page',
            'values': ['smth', 'hi', '5645'],
            'object': {
                'name': 'seyt',
                'lastName': 'balikbaev',
                'age': 26,
                'profession': 'entrepreneur',
                'goal': 'create starships',
                'wealthy': '$10000000000'
            }
            }
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

