from django.db import migrations


def create_initial_data(apps, schema_editor):
    Category = apps.get_model('blog', 'Category')
    Tag = apps.get_model('blog', 'Tag')

    categories = [
        'Technology', 'Science', 'Travel', 'Food', 'Lifestyle',
        'Health', 'Business', 'Entertainment', 'Sports', 'Education',
    ]

    tags = [
        'Tutorial', 'News',
        'Opinion', 'Review', 'Tips', 'Beginner', 'Advanced',
    ]

    for name in categories:
        Category.objects.get_or_create(name=name)

    for name in tags:
        Tag.objects.get_or_create(name=name)


def reverse_initial_data(apps, schema_editor):
    pass  # Don't delete on rollback


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_category'),  # adjust to your last migration
    ]

    operations = [
        migrations.RunPython(create_initial_data, reverse_initial_data),
    ]