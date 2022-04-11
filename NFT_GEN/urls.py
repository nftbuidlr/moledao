from django.urls import path
from NFT_GEN.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',homeView,name='genhome'),
    path('layoutP/',LayerPost,name='layoutP'),
    path('layoutG/',LayerGet,name='LayerGet'),
    path('upload/<int:pkk>',uploadImage,name='uploadImage'),
    path('generate/',GenerateImg,name='GenerateImg'),
    path('download/',download,name='download'),
    path('uploadnft/',uploadnft,name='uploadnft'),
    path('setrarity/<int:k>',setrarity,name='setrarity'),
    path('addproj/',add_proj,name='add_proj')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
