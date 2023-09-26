from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,signup
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('sign-up/',signup,name='signup'),
    path('login/',LoginView.as_view(template_name='app/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('',TaskList.as_view(),name='tasks'),
    path('detail-task/<int:pk',TaskDetail.as_view(),name='task'),
    path('create-task/',TaskCreate.as_view(),name='task-create'),
    path('update-task/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('delete-task/<int:pk>/',TaskDelete.as_view(),name='task-delete')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
