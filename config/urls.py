"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from question_box import views
from django.contrib.auth.models import User


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.question_list, name='question-list'), 
    path('questions/<int:pk>', views.question_detail, name='question-detail'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/profile/', views.user_profile, name='user-profile'),
    path('accounts/profile/questions/', views.user_questions, name='user-questions'),
    # path('signup/', views.signup, name='signup'),
    path('newquestion/', views.new_question, name='new-question'),
    # path('question/<int:pk>/answer/', views.add_answer, name='add-answer')


]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
