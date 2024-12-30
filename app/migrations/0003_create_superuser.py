from django.utils import timezone
from django.db import migrations

def create_superuser(apps, schema_editor):
    from django.contrib.auth import get_user_model
    
    User = get_user_model()
    
    # this will end the function if a user already exists
    if not User.objects.exists():
        return

    superuser = User.objects.create_superuser(
        username = "user",
        email = "example@mail.com",
        password = "password",
        last_login = timezone.now()
    )
    
    superuser.save()

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_article_word_column'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
