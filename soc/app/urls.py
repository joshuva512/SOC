from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', views.home, name='home'),
    path('user_base/', views.user_base, name='user_base'),
    path('s1', views.s1, name='s1'),
    path('s2', views.s2, name='s2'),
    path('s3', views.s3, name='s3'),
    path('s4', views.s4, name='s4'),
    path('register/', views.register, name = 'register'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='home'), name = 'logout')

]

urlpatterns +=  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
