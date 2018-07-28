from django.shortcuts import render, redirect

from .forms import WelcomeForm


def landing_page(request):
    context = {}
    if request.method == "POST":
        form = WelcomeForm(request.POST)
        if form.is_valid():
            context['form'] = form
            context['name'] = form.cleaned_data['your_name']
            return render(request, 'welcome/landing_page.html', context)
    else:
        form = WelcomeForm()
        context['form'] = form
        return render(request, 'welcome/landing_page.html', context)
