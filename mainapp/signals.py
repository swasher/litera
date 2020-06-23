import os
import shutil
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_delete

from mainapp.models import Family


@receiver(post_delete, sender=Family)
def remove_font_dir(sender, instance, **kwargs):
    font_dir = os.path.join(settings.MEDIA_ROOT, instance.name)
    if os.path.exists(font_dir):
        # TODO self.name must be safe
        # os.rmdir(font_dir)
        shutil.rmtree(font_dir)
        print(f"shutil.rmtree({font_dir})")


# post_delete.connect(remove_font_dir, sender=Family)
