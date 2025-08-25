from django.shortcuts import render

from django.http import HttpResponse

#def homeviews(request):
    #return HttpResponse("Welcome AMNA") 
#def my_view(request):
def index(request):
        id=request.GET.get("id")
        print(id,"656565")
        return render(request, 'index.html')
#def removepunc(request):
        
        djtext= request.GET.get('text','default')
        print(djtext)
        return HttpResponse("remove punc")
def analyze(request):
      djtext= request.POST.get('text','default')
      removepunc= request.POST.get('removepunc','off')
      fullcaps= request.POST.get('fullcaps','off')
      newlineremover= request.POST.get('newlineremover','off')
      extraspaceremover= request.POST.get('extraspaceremover','off')
      print(removepunc)
      print(djtext)
      if removepunc=="on":
            #analyzed=djtext
            punctuations='''!()-[]{:;'"\,<>./&?@#$%^*_~'''
            analyzed= ""
            for char in djtext:
                 if char not in punctuations:
                  analyzed= analyzed + char
            params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
            djtext=analyzed
            #return render(request,'analyze.html',params)
      if(fullcaps=="on"):
           analyzed=""
           for char in djtext:
            analyzed=analyzed + char.upper()
           params={'purpose':'Changed to Uppercase','analyzed_text':analyzed}
           djtext=analyzed
           #return render(request,'analyze.html',params)
      if(newlineremover=="on"):
           analyzed=""
           for char in djtext:
            if char !="\n"and char !="\r":
                
                analyzed= analyzed + char
           params={'purpose':'Removed NewLines','analyzed_text':analyzed}
           djtext=analyzed
           #return render(request,'analyze.html',params)
      if(extraspaceremover=="on"):
           analyzed=""
           for index, char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed= analyzed + char
           params={'purpose':'Removed ExtraLines','analyzed_text':analyzed}
           djtext=analyzed
      if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover !="on"):
          return HttpResponse("Select any operation ")
           #return render(request,'analyze.html',params)
      #else:
           #return HttpResponse("Error: No operation selected")
      
      return render(request,'analyze.html',params)
       




        
 

      
           
              









        
        
     