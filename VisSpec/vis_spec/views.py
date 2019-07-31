import threading
import time

from django.apps import apps
from django.http import JsonResponse, HttpResponseBadRequest, StreamingHttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
from django.views import View

from arduino_controller.serialport import SerialPortDataTarget


def index(request):
    return render(request,'vis_spec_index.html')


BOARDDATASTREAMRECEIVER = None