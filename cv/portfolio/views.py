from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html', {})


def blog_detail(request, id):
    return render(request, 'portfolio/blog-detail.html', {})


def portfolio_detail(request):
    return render(request, 'portfolio/portfolio-detail.html', {})