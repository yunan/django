from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from search.models import SearchKeyword

class SearchKeywordInline(admin.StackedInline):
    model=SearchKeyword

class FlatPageAdminWithKeywords(FlatPageAdmin):
    inlines = [SearchKeywordInline]

#class SearchKeyworkdAdmin(admin.ModelAdmin):
#    pass

#admin.site.register(SearchKeyword,SearchKeyworkdAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminWithKeywords)
