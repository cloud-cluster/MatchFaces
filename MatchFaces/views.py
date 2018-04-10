import json
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
import calculate_similarity as calculate
import os


def home(request):
    return render(request, 'home.html')


def upload(request):
    if request.method == "POST":
        ret = {'status': False, 'data': None, 'error': None}
        pic_file = request.FILES.get("picture")
        file_path = os.path.join("upload", pic_file.name)
        file_cut_path = str('dist/' + pic_file.name.split(".")[0] + '_cut.jpg')
        f = open(file_path, mode="wb")
        for chunk in pic_file.chunks():
            f.write(chunk)
        f.close()

        result = calculate.calculate_similarity(file_path, file_cut_path)
        if result == 1:
            ret['status'] = True
            ret['data'] = file_path
            HttpResponse(json.dumps(ret))
        else:
            ret['status'] = False
            ret['error'] = "Failed to detect the human face. Please pick another photo."
            HttpResponse(json.dumps(ret))

        return render(request, 'match.html', {'file_path': file_path})
        # return render(request, 'match.html/pic='+picture.name)
    else:
        return redirect("/home/")
