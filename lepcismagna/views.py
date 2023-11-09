from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import User, Inscription, Bibliography, InscriptionBibliography, EpigraphicReference, InscriptionReference, Category, Image, Abbreviation, InscriptionAbbreviation, AgeAtDeath, DivineSacredBeing, EmperorImperialFamily, Erasure, Findspot, Fragment, Organization, Person, PersonalName, PlaceName, Symbol, Word
from .forms import InscriptionEntryForm


def index(request):
    if request.user.is_authenticated:
        # If user is logged in, redirect to profile page
        return render(request, "lepcismagna/index.html")
    else:
        return HttpResponseRedirect(reverse('login'))
    
# User account handling

def login_view(request):
    if request.method == 'POST':
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "lepcismagna/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "lepcismagna/login.html")
       
def logout_view(request):
    # Render page indicating that user has logged out
    logout(request)
    return render(request, "lepcismagna/logout.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "lepcismagna/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "lepcismagna/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "lepcismagna/register.html")
    
# Logged-in user handling

@login_required
def profile(request, username):
    # Display user's profile page
    if request.method == 'POST':
        user = get_object_or_404(User, username=username)
    return render(request, 'lepcismagna/profile.html', {'user': user})
    
@login_required
def create_entry(request):
    # Handle the creation of a new inscription entry
    if request.method == 'POST':
        form = InscriptionEntryForm(request.POST, request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.entry_creator = request.user
            new_entry.save()
            return redirect('inscription_detail', reference_id=new_entry.reference_id)
        else:
            print(form.errors)
    else:
        form = InscriptionEntryForm()
    return render(request, 'lepcismagna/create_entry.html', {'form': form})

@login_required
def dossier(request):
    # Retrieve the user's dossier and display on the dossier page
    user = request.user
    dossier_inscriptions = user.dossier.all()
    return render(request, "lepcismagna/dossier.html", {"dossier_inscriptions": dossier_inscriptions})

@login_required
def toggle_dossier(request, reference_id):
    # Add or remove inscription from dossier
    inscription = get_object_or_404(Inscription, reference_id=reference_id)
    if inscription in request.user.dossier.all():
        request.user.dossier.remove(inscription)
    else:
        request.user.dossier.add(inscription)
    return HttpResponseRedirect(reverse('inscription_detail', args=[reference_id]))

# Inscription information handling

def inscriptions(request):
    # Retrieve inscription entries and display them
    inscriptions = Inscription.objects.all()
    return render(request, "lepcismagna/inscriptions.html", {"inscriptions": inscriptions})

def inscription_detail_view(request, reference_id):
    # Display the details of an inscription
    inscription = get_object_or_404(Inscription, reference_id=reference_id)
    return render(request, 'lepcismagna/inscription_detail.html', {'inscription': inscription})

def categories(request):
    # Retrieve all categories and display on categories page
    categories = Category.objects.all()
    return render(request, "lepcismagna/categories.html", {"categories": categories})

def category_view(request, category_name):
    # Get the category object by name or handle error if not found
    category = get_object_or_404(Category, name=category_name)

    # Filter inscriptions based on the selected category and display on category page
    category_inscriptions = Inscription.objects.filter(
        category=category)

    context = {
        'category_inscriptions': category_inscriptions,
        'category_name': category_name,
    }
    return render(request, "lepcismagna/category_view.html", context)

def bibliography(request):
    bibliography_entries = Bibliography.objects.all()
    return render(request, "lepcismagna/bibliography.html", {"bibliography_entries": bibliography_entries})

# Epigraphic indices handling

def abbreviations(request):
    abbreviations = Abbreviation.objects.prefetch_related('inscription_references')
    return render(request, "lepcismagna/abbreviations.html", {"abbreviations": abbreviations})

def ages_at_death(request):
    ages_at_death = AgeAtDeath.objects.all()
    return render(request, "lepcismagna/ages_at_death.html", {"ages_at_death": ages_at_death})

def divine_sacred_beings(request):
    divine_sacred_beings = DivineSacredBeing.objects.all()
    return render(request, "lepcismagna/divine_sacred_beings.html", {"divine_sacred_beings": divine_sacred_beings})

def emperors_imperial_family(request):
    emperors_imperial_family = EmperorImperialFamily.objects.all()
    return render(request, "lepcismagna/emperors_imperial_family.html", {"emperors_imperial_family": emperors_imperial_family})

def erasures(request):
    erasures = Erasure.objects.all()
    return render(request, "lepcismagna/erasures.html", {"erasures": erasures})

def findspots(request):
    findspots = Findspot.objects.all()
    return render(request, "lepcismagna/findspots.html", {"findspots": findspots})

def fragments(request):
    fragments = Fragment.objects.all()
    return render(request, "lepcismagna/fragments.html", {"fragments": fragments})

def organizations(request):
    organizations = Organization.objects.all()
    return render(request, "lepcismagna/organizations.html", {"organizations": organizations})

def people(request):
    people = Person.objects.all()
    return render(request, "lepcismagna/people.html", {"people": people})

def personal_names(request):
    personal_names = PersonalName.objects.all()
    return render(request, "lepcismagna/personal_names.html", {"personal_names": personal_names})

def place_names(request):
    place_names = PlaceName.objects.all()
    return render(request, "lepcismagna/place_names.html", {"place_names": place_names})

def symbols(request):
    symbols = Symbol.objects.all()
    return render(request, "lepcismagna/symbols.html", {"symbols": symbols})

def words(request):
    words = Word.objects.all()
    return render(request, "lepcismagna/words.html", {"words": words})