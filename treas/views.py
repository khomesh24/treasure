from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Treasurelist
from .forms import TreasureForm

# Create your views here.
def index(request):
    treasures = Treasurelist.objects.all()
    form = TreasureForm()
    return render(request,'index.html',{"treasure":treasures,"form":form})

def detail(request,treasure_id):
    treasure = Treasurelist.objects.get(id=treasure_id)
    return render(request,'detail.html',{"treasure":treasure})

def post_treasure(request):
    form = TreasureForm(request.POST)
    if form.is_valid():
        treasure = Treasurelist(
            name=form.cleaned_data['name'],
            value=form.cleaned_data['value'],
            location=form.cleaned_data['location'],
            img_url=form.cleaned_data['img_url']
        )
        treasure.save()
    return HttpResponseRedirect('/')