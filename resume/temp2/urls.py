from django.urls import path
from temp2 import views

urlpatterns = [
    path('index2/',views.show,name='index2'),
    path('post2/',views.temp2post,name='post2'),
    path('get2/',views.temp2get,name='get2'),
    path('update2/<int:pk>/',views.temp2update,name='update2'),
    path('pdf_download2/<pk>',views.pdf_download2,name='pdf_download2'),
]