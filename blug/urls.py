from django.urls import path
from . import views

app_name = "blug"

urlpatterns = [
    path("create-post/", views.create_post, name="create-post"),
    path("edit-posts/<int:post_id>", views.edit_post, name="edit-post"),
    path("process-post/", views.process_post, name="process-post"),
    path("process-journal/", views.process_journal, name="process-journal"),
    path("posts", views.list_post, name="list-posts"),
    path("success/", views.submission_success, name="submission-success"),
    path("bad/", views.bad_submission, name="bad-submission"),
]
