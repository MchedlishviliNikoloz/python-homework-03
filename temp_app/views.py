from django.shortcuts import render

# Create your views here.

def info(request):
    context = {
        "first_name": "Nikoloz",
        "last_name": "Mchedlishvili",
        "age": 17,
        "height": 180,
    }

    return render(request, 'info.html', context)

def hobbies(request):
    context = {
        "hobbies": ["Watching Sports", "Coding"],
        "grade": 12
    }
    return render(request, 'hobbies.html', context)