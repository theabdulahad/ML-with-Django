from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,'home.html')

def result(request):
    cls = joblib.load('Model.h5')
    lis = []
    lis.append(int(request.POST['cylinder']))
    lis.append(int(request.POST['displacement']))
    lis.append(int(request.POST['horsepower']))
    lis.append(int(request.POST['weight']))
    lis.append(int(request.POST['acc']))
    lis.append(int(request.POST['model_year']))
    lis.append(int(request.POST['origin']))
    # print(lis)

    ans = cls.predict([lis])


    return render(request,'result.html',{'ans':ans})
