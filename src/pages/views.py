from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
     #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs): 
    return render(request, "contact.html", {})
    
def about_view(request, *args, **kwargs): 
    my_context = {
        "title": "abc this is about us",
        "This is true": True,
        "my_number": 123,
        "my_list": [156, 7865, 9958, "Abc"],
        "my_code": "<h1>Maulana Imran Ganteng</h1>" 
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs): 
    return render("<h1>social.html</h1>")


def escape_view(request, *args, **kwargs): 
    my_codee = {
        "my_escape": "<p>Web Developer</p>"
    }
    return render(request, "escape.html", my_codee)