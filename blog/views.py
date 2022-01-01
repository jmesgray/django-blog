from django.shortcuts import render  # already here


# Create your views here.

def starting_page(request):  # this view will be for the starting page
    return render(request,
                  "blog/index.html")  # instructs django to render this index.html template and return it for this view.


def posts(request):  # this view will be for the posts page
    pass


def post_detail(request):  # this will be for individual posts
    pass
