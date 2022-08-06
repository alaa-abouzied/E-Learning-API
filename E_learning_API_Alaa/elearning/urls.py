from django.urls import include, path
from elearning import views 
from elearning.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('guests',views.viewsets_guest)
urlpatterns = [
   
    # path('api-auth/', include('rest_framework.urls')),
    # path('django/jsonresponsenomodel/', views.no_rest_no_model),
    # path('django/jsonresponsefrommodel/', views.no_rest_from_model),
    # path('rest/fbv/', FBV_List),
    # path('rest/fbv/<int:pk>', FBV_pk),
    # path('rest/cbv/', CBV_List.as_view()),
    # path('rest/cbv/<int:pk>', CBV_pk.as_view()),
    # path('rest/mixins/', mixins_list.as_view()),
    # path('rest/mixins/<int:pk>', mixins_pk.as_view()),
    # path('rest/generics/', generics_list.as_view()),
    # path('rest/generics/<int:pk>', generics_pk.as_view()),
    path('rest/viewsets/', include(router.urls)),
    # path('fbv/findmovie',find_course),
    

]

