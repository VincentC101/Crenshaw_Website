from django.shortcuts import get_object_or_404, render
from .models import Album
import feedparser
# Create your views here.

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'music/album_list.html', {'albums': albums})

from django.shortcuts import redirect
from .forms import AlbumForm

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'music/add_album.html', {'form': form})

def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'music/edit_album.html', {'form': form, 'album': album})

def to_index(request):
    return render(request, 'clothing/index.html')

def collections(request):
    return render(request, 'clothing/collections.html')

def about(request):
    return render(request, 'clothing/about.html')

def show_collection(request, name):
    return render(request, f'clothing/{name}.html')

def news(request):
    feed = feedparser.parse("https://theatlantic.com/feed/category/one-story-read-today/")
    entries_atlantic = [(entry.title, entry.link, entry.published[:10], entry.summary) for entry in feed.entries[:5]]
    feed = feedparser.parse("https://www.sbnation.com/rss/index.xml")
    entries_sbnation = [(entry.title, entry.link, entry.published[:10], entry.summary) for entry in feed.entries[:5]]
    feed = feedparser.parse("https://www.nytimes.com/athletic/rss/cleveland/")
    entries_athletic_cle = [(entry.title, entry.link, entry.published[:11], entry.summary) for entry in feed.entries[:5]]
    feed = feedparser.parse("https://www.nytimes.com/athletic/rss/chicago/")
    entries_athletic_chi = [(entry.title, entry.link, entry.published[:11], entry.summary) for entry in feed.entries[:5]]
    feed = feedparser.parse("https://www.bonappetit.com/feed/recipes-rss-feed/rss")
    entries_bon = [(entry.title, entry.link, entry.published[:11], entry.summary) for entry in feed.entries[:5]]
    feed = feedparser.parse("https://pitchfork.com/feed/reviews/best/albums/rss")
    entries_pfrv = [(entry.title, entry.link, entry.published[:11], entry.summary, entry.media_thumbnail[0]) for entry in feed.entries[:8]]
    feed = feedparser.parse("https://pitchfork.com/feed/reviews/best/reissues/rss")
    entries_pfri = [(entry.title, entry.link, entry.published[:11], entry.summary, entry.media_thumbnail[0]) for entry in feed.entries[:4]]

    
    return render(request, 'other/news.html', {'entries_atlantic': entries_atlantic, 'entries_sbnation': entries_sbnation, 
                                               'entries_athletic_cle': entries_athletic_cle, 'entries_athletic_chi': entries_athletic_chi, 'entries_bon': entries_bon,
                                                'entries_pfrv': entries_pfrv, 'entries_pfri': entries_pfri})