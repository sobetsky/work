from django.conf.urls import url, include
import views
urlpatterns = [
    url(r'^0/', views.page_0),
    url(r'^generator/', views.generator),
    url(r'^interface/', views.interface),
]

