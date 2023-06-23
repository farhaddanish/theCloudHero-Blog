from django.contrib import admin
from .models import ArticlePost, ArticleCaption, ArticleAuthor, ArticleMainCatagories, ArticleExtraContent, ArticleSubCatagories


class ArticlePost_Admin (admin.ModelAdmin):

    list_display = ['article_title',
                    'article_author', 'catagories', 'post_date']
    list_filter = ['post_date', 'catagories']

    prepopulated_fields = {
        'slug': ['article_title']
    }
    # readonly_fields =["post_date"]
    fieldsets = (
        ('Main Content', {'fields': ('article_title', 'article_caption',
                                     'article_author', 'post_date', 'article_describtion', 'article_image',
                                     'catagories', 'sub_catagories', 'article_content1', 'article_content2', 'article_content3', 'slug',)}),
        ('Extra Content', {'fields': ('extra_content',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'first_Name', 'password', 'password_2',), }
    #      ),
    # )

    search_fields = ['article_title']
    ordering = ['-post_date']
    
    filter_horizontal = ()


class ArticleSubCatagoriesAdmin (admin.ModelAdmin):
    list_display = ["article_sub_catagories", ]

    prepopulated_fields = {
        "slug": ["article_sub_catagories"]
    }


class ArticleCaptionAdmin (admin.ModelAdmin):
    list_filter = ["caption"]


class ArticleAuthorAdmin (admin.ModelAdmin):
    list_display = ["FirstName", "LastName"]
    list_filter = ["FirstName"]


class ArticleExtraAdmin (admin.ModelAdmin):
    list_display = ["extra_content_title"]


admin.site.register(ArticlePost, ArticlePost_Admin)
admin.site.register(ArticleCaption, ArticleCaptionAdmin)
admin.site.register(ArticleAuthor, ArticleAuthorAdmin)
admin.site.register(ArticleMainCatagories)
admin.site.register(ArticleSubCatagories, ArticleSubCatagoriesAdmin)
admin.site.register(ArticleExtraContent, ArticleExtraAdmin)
