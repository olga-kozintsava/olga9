from django.shortcuts import render
from django.views.generic import ListView

from my_test_app.models import NameModel


def input_name(request):
    if request.method == 'POST':
        names = request.POST.dict()
        del names['csrfmiddlewaretoken']
        names = {k: v for k, v in names.items() if v}
        new_names = NameModel(name=names)
        new_names.save()
    return render(request, 'input.html')


class NameListView(ListView):
    template_name = 'name_list.html'
    context_object_name = 'names'

    def get_queryset(self, *args):
        names = NameModel.objects.all()
        return names
