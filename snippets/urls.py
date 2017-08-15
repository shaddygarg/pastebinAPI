from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet,UserViewSet
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

"""
snippet_list=SnippetViewSet.as_view({
    'get':'list',
    'post':'create',
    })
snippet_detail=SnippetViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy',
    })
snippet_highlight=SnippetViewSet.as_view({
    'get':'highlight'},renderer_classes=[renderers.StaticHTMLRenderer]
    )
user_list=UserViewSet.as_view(
        { 'get':'list'}
        )
user_detail=UserViewSet.as_view({'get':'retrieve'})
"""
schema_view=get_schema_view(title='PastebinAPI')

router=DefaultRouter()
router.include_format_suffixes = False
router.register(r'users',UserViewSet)
router.register(r'snippets',SnippetViewSet)

urlpatterns =format_suffix_patterns([
        url(r'^',include(router.urls)),
        url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
        url(r'^schema/$',schema_view),
    ])
