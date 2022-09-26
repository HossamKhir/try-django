from django.urls import path

from .views import my_fbv, CourseView

app_name = "course"

urlpatterns = [
    # path("", my_fbv, name="course-list"),
    # path("", CourseView.as_view(), name="course-list"),
    path("", CourseView.as_view(template_name="contact.html"), name="course-list"),
]
