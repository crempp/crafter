from django.contrib import admin
from crafter.models import (
    GameConfiguration,
    Server,
    GameVersion,
    Player,
    Game,
)


class ConfigInline(admin.StackedInline):
    model = GameConfiguration


class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'host')


class GameVersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'link')
    search_fields = ['name', 'version']
    fieldsets = [
        ('Information', {'fields': ['name', 'description', 'version', 'link']}),
        ('Technical',   {'fields': ['jar_name']}),
    ]
    ordering = ('-version',)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'uuid', 'get_username')

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'
    get_username.admin_order_field = 'player__username'


class GameAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'server', 'version']
    inlines = [ConfigInline]


# admin.site.register(GameConfiguration)
admin.site.register(Server, ServerAdmin)
admin.site.register(GameVersion, GameVersionAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
