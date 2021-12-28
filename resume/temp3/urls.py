from django.urls import path
from temp3 import views

urlpatterns = [
    path('index3/',views.show,name='index3'),
    path('post3/',views.temp3post,name='post3'),
    path('get3/',views.temp3get,name='get3'),
    path('update3/<int:pk>/',views.temp3update,name='update3'),
    path('pdf_download3/<pk>',views.pdf_download3,name='pdf_download3'),
]