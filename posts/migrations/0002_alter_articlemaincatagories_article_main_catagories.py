# Generated by Django 4.1.7 on 2023-06-30 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemaincatagories',
            name='article_main_catagories',
            field=models.CharField(choices=[('Programming', 'Programming'), ('Cloud', 'Cloud'), ('Security', 'Security'), ('Windows', 'Windows'), ('Microsoft 365', 'Microsoft 365'), ('Linux', 'Linux')], max_length=50, null=True, unique=True, verbose_name='Article Main Catagories'),
        ),
    ]
