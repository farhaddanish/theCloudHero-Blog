# Generated by Django 4.1.7 on 2023-06-23 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=10, verbose_name='First Name')),
                ('LastName', models.CharField(max_length=10, verbose_name='Last Name')),
            ],
            options={
                'verbose_name_plural': 'Article Authors',
            },
        ),
        migrations.CreateModel(
            name='ArticleCaption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(default='News', max_length=20, verbose_name='Article - Caption')),
            ],
            options={
                'verbose_name_plural': 'Article Captions',
            },
        ),
        migrations.CreateModel(
            name='ArticleExtraContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_content_title', models.CharField(max_length=100, verbose_name='Extra - title')),
                ('extra_content_image', models.ImageField(upload_to='ExtraImages', verbose_name='Extra - Image')),
                ('extra_content_article1', models.TextField(verbose_name='Extra - Article-part-1')),
                ('extra_content_article2', models.TextField(blank=True, null=True, verbose_name='Extra - Article-part-2')),
            ],
            options={
                'verbose_name_plural': 'Extra - Contents',
            },
        ),
        migrations.CreateModel(
            name='ArticleMainCatagories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_main_catagories', models.CharField(choices=[('Windows', 'Windows'), ('Cloud', 'Cloud'), ('Server', 'Server'), ('Office', 'Office'), ('Storage', 'Storage'), ('SharePoint', 'SharePoint')], max_length=50, null=True, unique=True, verbose_name='Article Main Catagories')),
            ],
            options={
                'verbose_name_plural': 'Article Main Catagories',
            },
        ),
        migrations.CreateModel(
            name='ArticleSubCatagories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_sub_catagories', models.CharField(max_length=50, unique=True, verbose_name='Article Sub Catagories')),
                ('slug', models.SlugField(max_length=255, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Article Sub Catagories',
            },
        ),
        migrations.CreateModel(
            name='ArticlePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.TextField(verbose_name='Article - Title')),
                ('post_date', models.DateField(verbose_name='Post - Date')),
                ('article_describtion', models.TextField(verbose_name='Article - Describtion')),
                ('article_image', models.ImageField(upload_to='images', verbose_name='Article - Image')),
                ('article_content1', models.TextField(verbose_name='Article - Content-part-1')),
                ('article_content2', models.TextField(verbose_name='Article - Content-part-2')),
                ('article_content3', models.TextField(verbose_name='Article - Content-part-3')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('article_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.articleauthor')),
                ('article_caption', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.articlecaption')),
                ('catagories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.articlemaincatagories', verbose_name='Main - Catagories')),
                ('extra_content', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.articleextracontent', verbose_name='Extra - Content')),
                ('sub_catagories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.articlesubcatagories', verbose_name='Sub - Catagories')),
            ],
            options={
                'verbose_name_plural': 'Article',
                'ordering': ('-post_date',),
            },
        ),
        migrations.AddField(
            model_name='articlemaincatagories',
            name='article_sub_catagories',
            field=models.ManyToManyField(blank=True, max_length=50, to='posts.articlesubcatagories', verbose_name='Article Sub Catagories'),
        ),
    ]
