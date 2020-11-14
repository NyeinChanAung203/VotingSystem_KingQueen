from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name="index"),
    path('first_king/',views.FirstKingListView.as_view(),name="firstking"),
    path('first_queen/',views.FirstQueenListView.as_view(),name="firstqueen"),
    path('first_king/<int:pk>/',views.FirstKingDetailView.as_view(),name="firstkingdetail"),
    path('first_queen/<int:pk>/',views.FirstQueenDetailView.as_view(),name="firstqueendetail"),
    path('first_king/<int:pk>/vote',views.FirstKingVote,name="firstkingvote"),
    path('first_queen/<int:pk>/vote',views.FirstQueenVote,name="firstqueenvote"),

    path('thewhole_king/',views.TheWholeKingListView.as_view(),name="thewholeking"),
    path('thewhole_queen/',views.TheWholeQueenListView.as_view(),name="thewholequeen"),
    path('thewhole_king/<int:pk>/',views.TheWholeKingDetailView.as_view(),name="thewholekingdetail"),
    path('thewhole_queen/<int:pk>/',views.TheWholeQueenDetailView.as_view(),name="thewholequeendetail"),
    path('thewhole_king/<int:pk>/vote',views.TheWholeKingVote,name="thewholekingvote"),
    path('thewhole_queen/<int:pk>/vote',views.TheWholeQueenVote,name="thewholequeenvote"),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
