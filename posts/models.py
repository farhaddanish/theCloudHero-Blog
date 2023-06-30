from django.db import models
from django.db.models.deletion import SET_NULL
from PIL import Image


# Artcile Caption
class ArticleCaption (models.Model):
    caption = models.CharField(
        verbose_name="Article - Caption", default="News", blank=False, max_length=20)

    def __str__(self):
        return f"{self.caption.capitalize()}"

    class Meta:
        verbose_name_plural = "Article Captions"


# Artcile_Author
class ArticleAuthor (models.Model):
    FirstName = models.CharField(
        verbose_name="First Name", blank=False, max_length=10)
    LastName = models.CharField(
        verbose_name="Last Name", blank=False, max_length=10)

    def __str__(self):
        return f"{self.FirstName.capitalize()}  {self.LastName.capitalize()}"

    class Meta:
        verbose_name_plural = "Article Authors"


# Article_sub_catagories
class ArticleSubCatagories (models.Model):
    article_sub_catagories = models.CharField(unique=True,
                                              verbose_name="Article Sub Catagories", blank=False, max_length=50)

    slug = models.SlugField(unique=True, max_length=255,
                            db_index=True, null=True)

    def __str__(self):
        return f"{self.article_sub_catagories.capitalize()}"

    class Meta:
        verbose_name_plural = "Article Sub Catagories"


# Article_main_catagories
class ArticleMainCatagories (models.Model):
    object = (
        ('Programming', 'Programming'),
        ('Cloud', 'Cloud'),
        ('Security', 'Security'),
        ('Windows', 'Windows'),
        ('Microsoft 365', 'Microsoft 365'),
        ('Linux', 'Linux'),
    )
    article_main_catagories = models.CharField(
        verbose_name="Article Main Catagories", choices=object, null=True, blank=False, unique=True, max_length=50)

    article_sub_catagories = models.ManyToManyField(ArticleSubCatagories,
                                                    verbose_name="Article Sub Catagories", blank=True, max_length=50)

    def __str__(self):
        return f"{self.article_main_catagories}"

    class Meta:
        verbose_name_plural = "Article Main Catagories"


# Artcile_extra_content
class ArticleExtraContent (models.Model):
    extra_content_title = models.CharField(
        verbose_name="Extra - title", max_length=100, null=False, blank=False)

    extra_content_image = models.ImageField(
        verbose_name="Extra - Image", null=False, upload_to="ExtraImages")

    extra_content_article1 = models.TextField(
        verbose_name="Extra - Article-part-1", null=False, blank=False)

    extra_content_article2 = models.TextField(
        verbose_name="Extra - Article-part-2", blank=True, null=True)

    def __str__(self):
        return f"{self.extra_content_title.capitalize()}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.extra_content_image.path)
        resized_image = img.resize((872, 491))
        resized_image.save(self.extra_content_image.path)

    class Meta:
        verbose_name_plural = "Extra - Contents"


# Article_posts
class ArticlePost (models.Model):
    article_title = models.TextField(
        blank=False, null=False, verbose_name="Article - Title")
    article_caption = models.ForeignKey(
        ArticleCaption, on_delete=models.CASCADE)
    article_author = models.ForeignKey(
        ArticleAuthor, on_delete=models.SET_NULL, null=True)
    post_date = models.DateField(
        verbose_name="Post - Date", blank=False, null=False)
    article_describtion = models.TextField(
        verbose_name="Article - Describtion")
    article_image = models.ImageField(
        verbose_name="Article - Image", blank=False, null=False, upload_to="images")
    catagories = models.ForeignKey(
        ArticleMainCatagories, verbose_name="Main - Catagories", on_delete=models.CASCADE)
    sub_catagories = models.ForeignKey(
        ArticleSubCatagories, verbose_name="Sub - Catagories", on_delete=SET_NULL, null=True, blank=True)
    article_content1 = models.TextField(
        verbose_name="Article - Content-part-1", blank=False, null=False)
    article_content2 = models.TextField(
        verbose_name="Article - Content-part-2", blank=False, null=False)
    article_content3 = models.TextField(
        verbose_name="Article - Content-part-3", blank=False, null=False)
    slug = models.SlugField(db_index=True, unique=True, max_length=255)

    extra_content = models.OneToOneField(
        ArticleExtraContent, verbose_name="Extra - Content", on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.article_image.path)
        resized_image = img.resize((872, 491))
        resized_image.save(self.article_image.path)

    def __str__(self):
        return f"{self.article_title.capitalize()} "

    class Meta:
        ordering = ("-post_date",)
        verbose_name_plural = "Article"
