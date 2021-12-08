from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import commentListView, commentDetailView, commentCreateView, commentUpdateView, commentDeleteView
from .import views
#from register.views import SingleClass

urlpatterns = [
    path('', views.landing, name='Landing-Page'),

    path('comment_list/', commentListView.as_view(), name='comments'),
    path('comment/<int:pk>/', commentDetailView.as_view(), name='comment-detail'),
    path('comment/new/', commentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', commentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', commentDeleteView.as_view(), name='comment-delete'),

    path('course/', views.course, name='Course-Page'),
    path('personal/', views.personal, name='Personal-Page'),

    path('complain/', views.complain, name='complains'),

    path('remove/<int:pk>', views.deletepersonal, name='delete_view'),

    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='register/logout.html'), name='logout'),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


