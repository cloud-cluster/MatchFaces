import json
from django.shortcuts import render, redirect
from django.http import HttpResponse

import calculate_similarity as calculate
import os


def home(request):
    return render(request, 'home.html')


def upload(request):
    if request.method == "POST":
        ret = {'status': 'fail', 'data': None, 'error': None}
        pic_file = request.FILES.get("photo")
        file_path = os.path.join("upload", pic_file.name)
        file_cut_path = str('dist/' + pic_file.name.split(".")[0] + '_cut.jpg')
        f = open(file_path, mode="wb")
        for chunk in pic_file.chunks():
            f.write(chunk)
        f.close()

        result = calculate.calculate_similarity(file_path, file_cut_path)
        if result == 1:
            ret['status'] = 'success'
            ret['data'] = file_path
        else:
            ret['status'] = 'fail'
            ret['error'] = "Failed to detect the human face."

        return HttpResponse(json.dumps(ret), content_type='application/json')
    # else:
    #     return redirect("/home/")
