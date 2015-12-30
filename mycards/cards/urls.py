from django.conf.urls import url, include
import views
urlpatterns = [
    url(r'^page_0/', views.page_0),
    url(r'^generator/', views.generator),
    url(r'^interface/', views.interface),
    url(r'^(?P<card_id>\d+)/', views.card),
    #url(r'^profile/', views.profile),
]

