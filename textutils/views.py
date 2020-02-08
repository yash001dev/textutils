from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    charcount=request.POST.get('charcount','off')
    exstraspaceremover=request.POST.get('extraspaceremover','off')
    count=0
    purpose=""
    # print(djtext)
    # print(removepunc)
    # analyzed=djtext
    if removepunc=="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        purpose+=" |Removed Punctuations|"
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed To Uppercase','analyzed_text':analyzed}
        djtext=analyzed
        purpose+=" |Changed To Uppercase|"
        # return render(request,'analyze.html',params)
    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n":
                analyzed=analyzed+char
        params={'purpose':'Changed Without WhiteSpace','analyzed_text':analyzed}
        djtext=analyzed
        purpose+=" |Changed Without WhiteSpace|"
        # return render(request,'analyze.html',params)
    if(exstraspaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and  djtext[index+1]=="\r":
                pass
            else:
                analyzed=analyzed+char
        params={'purpose':'Removed NewLines','analyzed_text':analyzed}
        djtext=analyzed
        purpose+=" |Removed NewLines|"
        # return render(request,'analyze.html',params)

    if(charcount=="on"):
        analyzed=0
        analyzed=len(djtext)
        params={'purpose':'Length Of Character','analyzed_text':analyzed}
        count=analyzed
        purpose+=" |Length Of Character|"
    if(charcount!="on" and exstraspaceremover!="on" and newLinerRemover!="on" and fullcaps!="on" and removepunc!="on"):
        djtext="Please Select Appropriate Options..."

    if(count==0):
        return render(request,'analyze.html',{'purpose':purpose,'analyzed_text':djtext})
    else:
        djtext=djtext+"\nLength Of Word Count:"+str(count)
        return render(request,'analyze.html',{'purpose':purpose,'analyzed_text':djtext})
    

def removepunc(request):
    djtext=request.GET.get('text','default')
    print(djtext)
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newLinerRemover(request):
    return HttpResponse("newline remove first")

def spaceremove(request):
    return HttpResponse("space remover <a href='/'>back</a>")

def charcount(request):
    return HttpResponse("charcount")
