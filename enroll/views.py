from django.shortcuts import render
from .forms import Studentform


def sforms(request):
    # if request.method == 'POST':
    #     fm=Studentform(request.POST)
    #     print(fm)
    #     print('Dawar khan is a web developer')
    #     print(fm.cleaned_data)
    #     print(fm.cleaned_data['name'])
    #     print(fm.cleaned_data['email'])
      if request.method == 'POST':
          fm=Studentform(request.POST)
          if fm.is_valid():
              name=fm.cleaned_data['name']
              print('Name:',name)
              print('Email',fm.cleaned_data['email'])
              print('Email',fm.cleaned_data['password'])
              '''for input field should be empty after every sumbmission'''
            #   fm=Studentform()  
              '''render the page to another page'''
              return render(request,'page.html',{'nm':name})






      else:
        fm=Studentform()
      return render(request,'loops.html',{'form':fm})

