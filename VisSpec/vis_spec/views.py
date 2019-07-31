from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, "vis_spec_index.html")


BOARDDATASTREAMRECEIVER = None
