# Generated by Django 4.2.5 on 2024-02-14 07:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0005_reviews_review_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="watchlist",
            name="avg_rating",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="watchlist",
            name="number_rating",
            field=models.IntegerField(default=0),
        ),
    ]
