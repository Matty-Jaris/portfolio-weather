from django.shortcuts import render


def home(request):
    context = {
        'cv_link': 'odkaz_na_cv',
        'leetcode_link': 'odkaz_na_leetcode',
        'github_link': 'https://github.com/tvoje-jmeno',
    }
    return render(request, 'main/index.html', context)
