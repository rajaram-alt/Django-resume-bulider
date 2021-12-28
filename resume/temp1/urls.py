from django.urls import path
from temp1 import views

urlpatterns = [
    path('index1/',views.show,name='index1'),
    path('post1/',views.temp1post,name='post1'),
    path('get1/',views.temp1get,name='get1'),
    path('update1/<int:pk>/',views.temp1update,name='update1'),
    path('pdf_download1/<pk>',views.pdf_download,name='pdf_download1'),
]