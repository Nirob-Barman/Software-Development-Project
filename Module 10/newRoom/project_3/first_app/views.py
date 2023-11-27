from django.shortcuts import render
import datetime

# Create your views here.


def home(request):
    # return render(request, 'home.html')
    # d = {'author': 'Rahim', 'age': 25, 'List': [1, 2, 3]}
    # return render(request, 'home.html', context=d)
    # return render(request, 'home.html', d)
    return render(request, 'home.html',

                  {'author': 'Rahim', 'age': 15, 'List': [1, 2, 3], 
                   'newList': ['python', 'is', 'good'],
                   'birthday': datetime.datetime.now(),
                   'val': '',
                   'courses': 
                   [
                      {
                          'id': 1,
                          'name': "Python",
                          'fee': 5000
                      },
                      {
                          'id': 2,
                          'name': "Java",
                          'fee': 4000
                      },
                      {
                          'id': 3,
                          'name': "C++",
                          'fee': 3000
                      },
                      {
                          'id': 4,
                          'name': "C",
                          'fee': 2000
                      }
                  ]
                  }
                  )
