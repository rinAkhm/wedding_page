from django.shortcuts import render
from django.http import HttpResponse

from .forms import WeddingForm


def base_url(request):
    return render(request, 'wedding/wrapper.html')


def wedding_form(request):
    if request.method == 'POST':
        page_form = WeddingForm(request.POST)
        if page_form.is_valid():
            name = page_form.cleaned_data['name']
            surname = page_form.cleaned_data['surname']
            page_form.save()
            success_message = 'Форма успешно заполнена.'
            return render(request, 'wedding/wrapper.html', {"form": page_form,'success_message': success_message})
        else:
            return HttpResponse('<h3>произошла ошибка</h3>')

    else:
        page_form = WeddingForm()
        return render(request, 'wedding/wrapper.html',
                      {"form": page_form})
