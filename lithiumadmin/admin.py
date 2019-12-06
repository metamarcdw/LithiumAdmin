from django.contrib import admin
from django.db.models.fields.mixins import NOT_PROVIDED
from django.utils.encoding import force_text

from .models import Customer, Case


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "prod_version", "prod_hosting")
    list_filter = ("prod_hosting",)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions


class OpenCasesFilter(admin.SimpleListFilter):
    not_closed = "QUE,INP,NOT"
    title = "status"
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return (
            (OpenCasesFilter.not_closed, "Not closed"),
            ("QUE", "Queued"),
            ("INP", "In Progress"),
            ("NOT", "Waiting on another Team"),
            ("CLO", "Closed / Resolved")
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value in ("QUE", "INP", "NOT", "CLO"):
            return queryset.filter(status__exact=value)
        return queryset.filter(status__in=OpenCasesFilter.not_closed.split(","))

    def choices(self, changelist):
        for lookup, title in self.lookup_choices:
            yield {
                "selected": self.value() == force_text(lookup),
                "query_string": changelist.get_query_string(
                    {self.parameter_name: lookup}, []
                ),
                "display": title,
            }


class CaseAdmin(admin.ModelAdmin):
    list_display = (
        "salesforce_case",
        "customer",
        "title",
        "priority",
        "severity",
        "date_requested",
        "status",
        "report_me",
    )
    list_filter = (OpenCasesFilter, "priority", "severity", "report_me")
    list_editable = ("report_me",)
    search_fields = ("salesforce_case", "title", "customer__name")
    ordering = ("severity", "priority", "date_requested")

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Case, CaseAdmin)
