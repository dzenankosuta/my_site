from django.shortcuts import render
from datetime import date

posts = [
    {
        "slug": "mountain",
        "image": "mountain.jpg",
        "author": "DŽENAN",
        "date": date(2025, 1, 7),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains!",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio."
    },
    {
        "slug": "mountain",
        "image": "mountain.jpg",
        "author": "DŽENAN",
        "date": date(2025, 1, 7),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains!",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio."
    },
    {
        "slug": "mountain",
        "image": "mountain.jpg",
        "author": "DŽENAN",
        "date": date(2025, 1, 7),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains!",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio."
    }
]

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html", {
        "post": posts[0]
    })