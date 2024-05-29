from django.shortcuts import render

def index_view(request):
    context = {'name': 'Akbar', 'family': 'Mohammadi', 'email': 'akbar.mohammadi70@gmail.com', 'phone': '0989214383005'}
    return render(request, 'blog/index.html', context)