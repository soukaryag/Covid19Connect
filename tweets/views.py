from django.shortcuts import render

def index(request):
    return render(request, 'tweets/index.html', {})

def graph(request):
    return render(request, 'tweets/graph.html', {})

def table(request):
    return render(request, 'tweets/table.html', {})