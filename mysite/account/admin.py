from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account


class AccountAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        new_fields = Account.get_admin_fields()
        self.list_display += new_fields
        self.fieldsets[1][1]["fields"] += new_fields
        return UserAdmin.__init__(self, *args, **kwargs)


admin.site.register(Account, AccountAdmin)
