from django.contrib import admin
from .models import Outline, Background, Drives, Natures, Connections, Stats, WeaponSkills, RoguishFeats, Moves

# Register your models here.
admin.site.register(Drives)
admin.site.register(Outline)
admin.site.register(Background)
admin.site.register(Natures)
admin.site.register(Connections)
admin.site.register(Stats)
admin.site.register(WeaponSkills)
admin.site.register(RoguishFeats)
admin.site.register(Moves)