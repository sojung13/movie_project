from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<username>', views.profile),
    path('follow/<username>', views.follow),
]



# df39a2ed37b299695c2df1170364e142fbc5c11c (test계정)
# 48e9fe9ebb18da87ee7e68a36a714884e97b714c  (admin)