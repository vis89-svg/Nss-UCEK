from django.shortcuts import render, redirect
from .forms import CardForm
from .models import Card
from django.core.paginator import Paginator
from django.utils import timezone

def upload_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_cards')
    else:
        form = CardForm()
    
    return render(request, 'upload.html', {'form': form})

def view_cards(request):
    query = request.GET.get('q')
    now = timezone.now().date()

    # Filter by query
    if query:
        cards = Card.objects.filter(title_icontains=query) | Card.objects.filter(description_icontains=query)
    else:
        cards = Card.objects.all()

    # Separate past (including today) and upcoming events
    upcoming_events = cards.filter(date__gt=now).order_by('date')  # Upcoming events
    past_events = cards.filter(date__lte=now).order_by('-date')    # Past and current events

    context = {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
    }
    
    return render(request, 'view_cards.html', context)

def upcoming_events(request):
    now = timezone.now().date()

    # Fetch only future events without deleting past ones
    upcoming_events = Card.objects.filter(date__gt=now).order_by('date')
    
    paginator = Paginator(upcoming_events, 10)  # Show 10 events per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'upcoming_events.html', {'page_obj': page_obj})