from django.shortcuts import render
import datetime

# Create your views here.
def built_in_filter(request):
    data='We aRe DevELopErs'
    dt=datetime.datetime.now()
    d={'data':data,'dt':dt,'c':11}

    return render(request,'built_in_filter.html',d)





# def custom_filter(request):
#    data='We aRe A FuTuRE DeveLoPEr'    
#     d={'data':data}
#     return render(request,'custom_filter.html',d)
