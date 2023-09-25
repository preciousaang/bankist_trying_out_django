from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from blug.models.post import Post
from .forms import PostForm, JournalForm

# Create your views here.


def create_post(request):
    formData = request.session.pop("form_data", None)
    journalData = request.session.pop("journal_form_data", None)
    postForm = PostForm(formData)
    journalForm = JournalForm(journalData)
    return render(
        request,
        "blug/create-post.html",
        {"post_form": postForm, "journal_form": journalForm},
    )


def edit_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/bad")
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Post updated")
            return redirect("blug:edit-post", post_id)
        else:
            for field in form.errors:
                form[field].field.widget.attrs["class"] += " is-invalid"

    else:
        form = PostForm(instance=post)
    return render(request, "blug/edit-post.html", {"form": form})


def list_post(request):
    posts = Post.objects.all()
    return render(request, "blug/post-list.html", {"posts": posts})


def process_post(request):
    if request.method == "POST":
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            postForm.save()
            messages.add_message(request, messages.SUCCESS, "Post created")
            return redirect("blug:list-posts")
        else:
            request.session["form_data"] = request.POST
            return redirect("blug:create-post")

    return redirect("blug:bad-submission")


def process_journal(request):
    if request.method == "POST":
        jounalForm = JournalForm(request.POST)
        if jounalForm.is_valid():
            return redirect("blug:submission-success")
        else:
            request.session["journal_form_data"] = request.POST
            return redirect("blug:create-post")

    return redirect("blug:bad-submission")


def submission_success(request):
    return render(request, "blug/submission-success.html", {})


def bad_submission(request):
    return render(request, "blug/bad-submission.html")
