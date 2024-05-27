from.import views
from django.urls import path


urlpatterns = [
    path('',views.add,name='add'),
    path("delete/<int:taskid>/",views.delete,name="delete"),
    path("update/<int:id>/",views.update,name="edit"),
    path("classhome/",views.Tasklistview.as_view(),name="classhome"),
    path("classdetails/<int:pk>/",views.Taskdetailview.as_view(),name="classdetails"),
    path("classdelete/<int:pk>/",views.Taskdeleteview.as_view(),name="classdelete"),

    ]