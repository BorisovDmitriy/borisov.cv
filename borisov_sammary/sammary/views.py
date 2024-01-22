from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def base(request):
    # return render(request, 'portfolio/base.html')
    return render(request, 'portfolio/index_1.html')

# def portfolio(request):
#     return render(request, 'portfolio/index_1.html')


# def portfolio_details(request):
#     return render(request, 'portfolio/portfolio-details.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')