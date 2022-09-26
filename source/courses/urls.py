from django.urls import path

from .views import CourseCreateView, CourseListView, CourseView, my_fbv

app_name = "course"

urlpatterns = [
    # path("", my_fbv, name="course-list"),
    # path("", CourseView.as_view(), name="course-list"),
    # path("", CourseView.as_view(template_name="contact.html"), name="course-list"),
    path("", CourseListView.as_view(), name="course-list"),
    path("<int:id>/", CourseView.as_view(), name="course-detail"),
    path("create/", CourseCreateView.as_view(), name="course-create"),
]
