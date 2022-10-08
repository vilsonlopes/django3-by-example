from .forms import EmailPostForm
from django.shortcuts import render, get_object_or_404
from .models import Post


def enviar_email(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
