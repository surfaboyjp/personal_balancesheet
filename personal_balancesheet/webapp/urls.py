from django.urls import path
from . import views
from django.contrib.auth import logout

app_name = 'webapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('journals/<int:pk>/', views.JournalDetailView.as_view(), name='journal_detail'),
    path('journals/<int:pk>/records/', views.RecordView.as_view(), name='records'),
    path('journals/<int:pk>/records/<int:record_pk>', views.RecordDetailView.as_view(), name='record_detail'),
    # path('fstatement_detail/<int:pk>', views.FstatementView.as_view(), name='fstatement'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', logout, {'template_name': 'index.html'}, name='logout'),
    path('signup', views.CreateUserView.as_view(), name='signup'),
]

