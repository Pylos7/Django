from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World!')

def about(request):
    return HttpResponse('Hello, my name is Nestor! I am woring on a Software Development Associate and learning about Django in this course!')

def hello(request, first_name):
    return HttpResponse(f"Hello {str.capitalize(first_name)}")

def age(request, first_name, age, years_past):
    return HttpResponse(f"Hello {str.capitalize(first_name)} you are {age} years old! and you where {age - years_past} years old {years_past} years ago!")