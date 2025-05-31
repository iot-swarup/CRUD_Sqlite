from django.urls import path
from . import views

urlpatterns=[
    path('', views.main_menu, name='main_menu'),
    path('create/', views.add_student, name='create_student'),
    path('retrieve/', views.retrieve_student, name='retrieve_student'),
    path('update/<int:student_id>/', views.update_student, name='update_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),

    # Search URLs
    path('search/id/', views.search_student_by_id, name='search_student_by_id'),
    path('search/name/', views.search_student_by_name, name='search_student_by_name'),

    # Additional URLs
    path('highest/', views.highest_score_student, name='highest_score_student'),
]