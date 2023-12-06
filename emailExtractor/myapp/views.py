from django.shortcuts import render
import re



def home(request):
    if request.method == 'POST':
        paragraph = request.POST.get('yourtext')
        print('This is para :',paragraph)
        print('This is para :',type(paragraph))
        matches = re.findall(r"\s\w*@\w*.(?:com|in|me|co)",paragraph)
        result = []
        for x in matches:
            print('This is x :',x)
            result.append(x)

        return render(request,'home.html',{'result':result})
    return render(request,'home.html')