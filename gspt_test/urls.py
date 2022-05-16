from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'gspt_test'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('students', views.students, name = 'students'),
    path('students/<int:person_id>/', views.study_plan, name = 'study_plan'),
    path('students/<int:pk>/add_course', login_required(views.EnrollmentCreateView.as_view()), name = 'enrollment_add'),
    path('students/<int:pk>/<int:course_id>/edit_course', login_required(views.EnrollmentUpdateView.as_view()), name = 'enrollment_edit'),
    path('students/<int:pk>/<int:course_id>/delete_course', login_required(views.EnrollmentDeleteView.as_view()), name = 'enrollment_delete'),
    path('checklist', views.checklist, name = 'checklist'),
    path('login', views.loginUser, name = 'login'),
    path('logout', views.logoutUser, name = 'logout'),
    path('home', views.home, name = 'home'),
]

urlpatterns += staticfiles_urlpatterns()