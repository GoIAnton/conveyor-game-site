from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Theme, User
from .forms import ThemeForm, CommentForm


def create_page_obj(request, theme_list):
    paginator = Paginator(theme_list, 10)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def index(request):
    return render(request, 'themes/index.html')


def themes(request):
    theme_list = (
        Theme.objects.
        order_by('-pub_date')
    )
    page_obj = create_page_obj(request, theme_list)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'themes/themes.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    theme_list = (
        author.themes.
        order_by('-pub_date')
    )
    page_obj = create_page_obj(request, theme_list)
    context = {
        'author': author,
        'page_obj': page_obj,
    }
    return render(request, 'themes/profile.html', context)


def theme_detail(request, theme_id):
    theme = get_object_or_404(Theme, pk=theme_id)
    form = CommentForm(request.POST or None)
    comments = (
        theme.comments.order_by('-created')
    )
    context = {
        'theme': theme,
        'form': form,
        'comments': comments,
    }
    return render(request, 'themes/theme_detail.html', context)


@login_required
def theme_create(request):
    form = ThemeForm(request.POST or None, files=request.FILES or None,)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            username = request.user
            instance.author = username
            instance.save()
            return redirect('themes:profile', username)
        return render(
            request,
            'themes/create_theme.html',
            {'form': form, 'is_edit': False}
        )
    return render(
        request,
        'themes/create_theme.html',
        {'form': form, 'is_edit': False}
    )


@login_required
def theme_edit(request, theme_id):
    theme = get_object_or_404(Theme, id=theme_id)
    if request.user != theme.author:
        return redirect(f'/themes/{theme_id}/')
    form = ThemeForm(
        request.POST or None,
        instance=theme
    )
    if form.is_valid():
        form.save()
        return redirect('themes:theme_detail', theme_id=theme_id)
    context = {
        'theme': theme,
        'form': form,
        'is_edit': True,
    }
    return render(request, 'themes/create_theme.html', context)


@login_required
def add_comment(request, theme_id):
    form = CommentForm(request.POST or None)
    theme = get_object_or_404(Theme, id=theme_id)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.theme = theme
        comment.save()
    return redirect('themes:theme_detail', theme_id=theme_id)


@login_required
def delete_theme(request, theme_id):
    theme = get_object_or_404(Theme, id=theme_id)
    theme.delete()
    return redirect('themes:themes')