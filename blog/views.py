from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "mountain",
        "image": "mountain.jpg", 
        "author": "DŽENAN",
        "date": date(2025, 1, 7),
        "title": "Mountain Hiking",
        "excerpt": "Join me on an epic adventure scaling one of Europe's most challenging peaks!",
        "content": "Last week I embarked on my most ambitious climb yet - tackling the treacherous north face of Mount Triglav. The weather conditions were harsh with strong winds and snow, but the breathtaking views from the summit made it all worthwhile. In this post, I'll share my preparation, the challenges faced, and tips for fellow adventurers looking to conquer this majestic peak."
    },
    {
        "slug": "hiking", 
        "image": "hiking.jpg",
        "author": "DŽENAN",
        "date": date(2025, 1, 1),
        "title": "Hiking",
        "excerpt": "Discovering hidden alpine lakes and meadows on a peaceful day hike",
        "content": "Sometimes the best hiking experiences are the peaceful, solitary ones. Today I explored some lesser-known trails that led to pristine alpine lakes and meadows bursting with wildflowers. The silence was broken only by birdsong and gentle mountain breezes. I'll guide you through this serene route that's perfect for hikers seeking tranquility in nature."
    },
    {
        "slug": "gear",
        "image": "gear.jpg",
        "author": "DŽENAN", 
        "date": date(2024, 10, 20),
        "title": "Gear",
        "excerpt": "Essential gear guide: What you really need for mountain hiking",
        "content": "After years of mountain hiking, I've learned what gear is truly essential and what's just extra weight in your pack. In this comprehensive guide, I break down the must-have equipment for different types of mountain terrain and weather conditions. From choosing the right boots to selecting appropriate layers, I'll help you prepare for your next mountain adventure with confidence."
    }
]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })