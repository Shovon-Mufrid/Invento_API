from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Software_Settings import views
# import notifications.urls
# import notifications_rest.urls

router = DefaultRouter()
router.register('user', views.UserProfileViewSet)
router.register('module', views.moduleViewSet)
router.register('sub_module', views.sub_moduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),
#     path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
#     path('notifications/', include(notifications_rest.urls)),
    # path('reset-session-timeout/', views.reset_session_timeout, name='reset-session-timeout'),
]
