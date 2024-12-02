# Generated by Django 4.2 on 2024-11-28 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_managementdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tab_title', models.CharField(max_length=200)),
                ('icon_class', models.CharField(help_text="Font Awesome or Bootstrap icon class, e.g., 'bi bi-binoculars'.", max_length=50)),
                ('heading', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('italic_description', models.TextField(blank=True, null=True)),
                ('points', models.TextField(help_text="Enter points separated by '|'.")),
                ('image', models.ImageField(blank=True, null=True, upload_to='features/')),
                ('tab_id', models.CharField(help_text="Unique ID for the tab, e.g., 'features-tab-1'.", max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the service', max_length=200)),
                ('description', models.TextField(help_text='Description of the service')),
                ('icon_class', models.CharField(help_text="CSS class for the icon (e.g., 'bi bi-cash-stack')", max_length=50)),
                ('icon_color', models.CharField(default='#000000', help_text="Color code for the icon (e.g., '#0dcaf0')", max_length=20)),
                ('details_url', models.URLField(default='#', help_text='URL for the service details page')),
                ('order', models.PositiveIntegerField(default=0, help_text='Order in which the services appear')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='StudentLeadershipSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Students Leadership', max_length=200)),
                ('description_1', models.TextField()),
                ('description_2', models.TextField()),
                ('read_more_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
