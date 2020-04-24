# I have created this file- Divya
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")


def analyze(request):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newline = request.POST.get('newline', 'off')
    extraspace = request.POST.get('extraspace', 'off')
    org = djtext

    def removepun(djtext):
        analyzed = ""
        if (removepunc == "on"):
            for char in djtext:
                if (char not in punctuations):
                    analyzed += char
            return analyzed
        else:
            return djtext

    org = removepun(org)

    def capital(djtext):
        analyzed = djtext
        if (capitalize == "on"):
            analyzed = analyzed.upper()
            return analyzed
        else:
            return djtext

    org = capital(org)



    def new(djtext):
        analyzed=""
        if(newline=="on"):
            for char in djtext:
                if char !="\n" and char!="\r":
                    analyzed=analyzed+char
            return analyzed
        else:
            return djtext

    org=new(org)

    def extra(djtext):
        analyzed=""
        if(extraspace=="on"):
            for index,char in enumerate(djtext):
                if not(djtext[index]==" " and djtext[index+1]==" "):
                    analyzed=analyzed+char
            return analyzed
        else:
            return djtext

    org=extra(org)




    dict1 = {'purpose': 'pani pata leka', 'analyzed_text': org}

    print("hii")
    print(removepunc)
    print(djtext)
    return render(request, 'analyze.html', dict1)


def ex1(request):
    sites = ['''<h1>For entertainment</h1><a href="https://www.youtube.com">Youtube video</a>''',
             '''<h1>For Interaction</h1><a href="https://www.facebook.com">Facebook</a>''',
             '''<h1>For Insights</h1><a href="https://www.ted.com/talks">Ted talk</a>''',
             '''<h1> For Internship </h1> <a href = "https://www.internshala.com">Internship</a>'''
             ]
    return HttpResponse((sites))
