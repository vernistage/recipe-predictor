from django.shortcuts import render

def landing_page(request):
    return render(request, 'welcome/landing_page.html', {})
