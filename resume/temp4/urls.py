from django.urls import path
from temp4 import views

urlpatterns = [
    path('index4/',views.show,name='index4'),
    path('post4/',views.temp4post,name='post4'),
    path('get4/',views.temp4get,name='get4'),
    path('update4/<int:pk>/',views.temp4update,name='update4'),
    path('pdf_download4/<pk>',views.pdf_download4,name='pdf_download4'),
]