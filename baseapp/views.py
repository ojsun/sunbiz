from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'baseapp/about.html')
def portfolio_1(request):
    return render(request, 'baseapp/portfolio_1.html')
def portfolio_2(request):
    return render(request, 'baseapp/portfolio_2.html')
def portfolio_3(request):
    return render(request, 'baseapp/portfolio_3.html')
def portfolio_4(request):
    return render(request, 'baseapp/portfolio_4.html')
def portfolio_0(request):
    return render(request, 'baseapp/portfolio-item.html')
def faq(request):
    return render(request, 'baseapp/faq.html')

