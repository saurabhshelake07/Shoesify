from django.shortcuts import render

# Create your views here.
def first_view(request):
    temp="ShoeSApp/first.html"
    context={}
    return render(request,temp,context)