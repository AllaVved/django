from django.shortcuts import render


def main(request):
    context = {'user' : {'name' : 'Алла'}}
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {'prod' : [
        {'name' : 'Щенок пуделя', 'img' : 'img/poodle_puppy.jpg'},
        {'name' : 'Утка с утенком', 'img' : 'img/duck_with_duckling.jpg'},
        {'name' : 'Лама Белая', 'img' : 'img/white_llama.jpg'}
    ]}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')
