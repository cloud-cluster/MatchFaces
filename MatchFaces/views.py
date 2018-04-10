import json
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
import calculate_similarity as calculate


def home(request):
    return render(request, 'home.html')


def upload(request):
    if request.method == "POST":
        ret = {'status': False, 'data': None, 'error': None}
        print "111------------------"
        print request.FILES
        picture = request.FILES.get("picture")

        import os
        file_path = os.path.join("upload", picture.name)
        f = open(file_path, mode="wb")
        for chunk in picture.chunks():
            f.write(chunk)
        f.close()

        calculate.calculate_similarity(file_path, str('dist/' + picture.name.split(".")[0] + '_cut.jpg'))

        ret['status'] = True
        ret['data'] = file_path
        HttpResponse(json.dumps(ret))

        return render(request, 'match.html', {'file_path': file_path})
        # return render(request, 'match.html/pic='+picture.name)
    else:
        return redirect("/home/")