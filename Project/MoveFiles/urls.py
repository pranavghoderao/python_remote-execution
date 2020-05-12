from django.urls import path
from MoveFiles import views

urlpatterns = [
    path('upload',views.upload,name="upload"),
    path('list',views.list,name="show"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('execute/<int:id>',views.execute,name="execute"),
]

