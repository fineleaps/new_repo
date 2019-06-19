from django.contrib import admin
from .models import Result


class ResultAdmin(admin.ModelAdmin):

    list_display = ('get_prospect', 'get_campaign',
                    "result_choice", "by", "on")
    list_filter = ("result_choice", "by", "on")


admin.site.register(Result, ResultAdmin)

