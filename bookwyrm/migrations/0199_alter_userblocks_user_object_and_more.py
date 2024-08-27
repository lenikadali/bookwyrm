# Generated by Django 4.2.11 on 2024-03-29 19:25

import bookwyrm.models.fields
from django.conf import settings
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0198_book_search_vector_author_aliases"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userblocks",
            name="user_object",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)s_user_object",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="userblocks",
            name="user_subject",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)s_user_subject",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="userfollowrequest",
            name="user_object",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)s_user_object",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="userfollowrequest",
            name="user_subject",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)s_user_subject",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="userfollows",
            name="user_object",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)s_user_object",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="userfollows",
            name="user_subject",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)s_user_subject",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]