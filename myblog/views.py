from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUp, diaryEntry
from .models import Blog
from datetime import datetime


def index(request):
    return render(request, 'myblog/index.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/myblog/index')
    else:
        form = SignUp()
    return render(request, 'myblog/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'myblog/userprofiles/profile.html')


@login_required
def diary(request):
    all_entries = Blog.objects.filter(author=request.user)
    return render(request, 'myblog/userprofiles/diary.html', {'diary': all_entries})


@login_required
def add_diary(request):
    if request.method == 'POST':
        form = diaryEntry(request.POST)
        if form.is_valid():
            form.save(commit=False)
        subject = form.cleaned_data.get('subject')
        entry = form.cleaned_data.get('entry')
        x = Blog()
        x.author = request.user
        x.subject = subject
        x.entry = entry
        x.save()
        return redirect('/myblog/Diary')
    else:
        form = diaryEntry()
        button_display = "Add to diary"
        return render(request, 'myblog/userprofiles/Write.html', {'form': form, 'button':button_display})


@login_required
def edit_diary(request, id):
    if id:
        entry = get_object_or_404(Blog, id=id)
        if entry.author != request.user:
            return render(request, "403.html")
    else:
        entry = Blog(author=request.user)

    if request.method == "POST":
        form = diaryEntry(request.POST, instance=entry)
        if form.is_valid():
            entry.last_update = datetime.now()
            entry = form.save(commit=False)
            entry.save()
            # messages.add_message(request, messages.SUCCESS,
            #                      'You have succesfully updated your post')
            return redirect('/myblog/Diary')
    else:
        form = diaryEntry(instance=entry)
    button_display= "Edit entry"
    return render(request, 'myblog/userprofiles/Write.html', {'form': form, 'button': button_display})
