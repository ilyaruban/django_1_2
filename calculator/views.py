from django.shortcuts import render
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
}

def home_view(request):
    template_name = 'calculator/index.html'
    pages = {
        'Omlet': reverse('omlet'),
        'Pasta': reverse('pasta'),
        'Buter': reverse('buter')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def omlet(request):
    recipe_omlet = DATA['omlet']
    servings = float(request.GET.get('servings', 1))
    context = {
        'recipe': recipe_omlet,
        'servings': servings
    }
    return render(request, 'calculator/omlet.html', context)


def pasta(request):
    recipe_pasta = DATA['pasta']
    servings = float(request.GET.get('servings', 1))
    context = {
        'recipe': recipe_pasta,
        'servings': servings
    }
    return render(request, 'calculator/pasta.html', context)


def buter(request):
    recipe_buter = DATA['buter']
    servings = float(request.GET.get('servings', 1))
    context = {
        'recipe': recipe_buter,
        'servings': servings
    }
    return render(request, 'calculator/buter.html', context)