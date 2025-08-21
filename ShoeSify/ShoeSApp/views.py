
from django.shortcuts import render, redirect
from .forms import ShoeModelForm
from .models import ShoeModel

# Create your views here.
def first_view(request):
    temp="ShoeSApp/first.html"
    context={}
    return render(request,temp,context)


def addShoeView(request):
    form = ShoeModelForm()
    if request.method == "POST":
        form = ShoeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show-shoes")
            #return HttpResponse("Shoe Added")
    template_name = "ShoeSApp/form.html"
    context = {"form":form}
    return render(request,template_name, context)



def updateShoeView(request,i):
    shoes_obj = ShoeModel.objects.get(id=i)
    form = ShoeModelForm(instance=shoes_obj)
    if request.method == "POST":
        form = ShoeModelForm(request.POST,instance=shoes_obj)
        if form.is_valid():
            form.save()
            return redirect("show-shoes")
            #return HttpResponse("Shoe Updated")
    template_name = "ShoeSApp/form.html"
    context = {"form":form}
    return render(request,template_name, context)


def deleteShoeView(request,i):
    shoes_obj = ShoeModel.objects.get(id=i)
    shoes_obj.delete()
    return redirect("show-shoes")
    #return HttpResponse("Shoe Deleted")

def showShoeView(request):
    shoes_obj_qs = ShoeModel.objects.all()
    template_name = "ShoeSApp/show.html"
    context = {"shoes_obj_qs":shoes_obj_qs}
    return render(request,template_name, context)
