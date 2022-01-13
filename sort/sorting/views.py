from django.shortcuts import render
from .SortAlgo import SelectionSort

# Create your views here.


def index(request):
    SortArr = {}
    color = "#7BF600"
    # length = 100
    if request.method == 'POST':
        array = request.POST['list']
        SelectSort, length = SelectionSort(array)
        print(length)
        SortArr = {'SortArr': SelectSort, 'len': length}
        return render(request, 'sorting/index.html', SortArr)
    return render(request, 'sorting/index.html')
