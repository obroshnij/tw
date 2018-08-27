from django.shortcuts import render
from .forms import AbiForm
import gui.services.abi.formatter as abi_formatter

def index(request):
    abi_object = None
    if request.method == 'POST':
        form = AbiForm(request.POST, request.FILES)
        if form.is_valid():
            abi_object = abi_formatter.wrap(request.FILES['file'])
    else:
        form = AbiForm()

    return render(request, 'gui/index.html', { 'form': form, 'abi': abi_object })
