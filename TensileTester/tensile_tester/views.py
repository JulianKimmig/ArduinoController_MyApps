# Create your views here.
import logging

from django.shortcuts import render
from django.views import View

mpl_logger = logging.getLogger('matplotlib')
mpl_logger.setLevel(logging.WARNING)

def index(request):
    #tensile_tests = TensileTestInstance.objects.all()
    return render(request, "tensile_tester_index.html"
                  #,{'tensile_tests':tensile_tests}
    )


BOARDDATASTREAMRECEIVER = None


class NewRoutine(View):
    def get(self,request):
        return render(request, "tensile_tester_routine.html")