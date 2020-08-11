from django.contrib import admin
from . import models
from django.utils.html import mark_safe


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        ("Basic Info", {"fields": ("name", "description", "country", "address")},),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")},),
        ("More About the Space", {"fields": ("beds", "bedrooms", "baths", "guests",)}),
        (
            "Spaces",
            {
                "classes": ("collapse",),
                "fields": ("amenity", "facility", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    ordering = ("name", "price", "bedrooms")

    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "beds",
        "bedrooms",
        "baths",
        "guests",
        "check_in",
        "check_out",
        "instant_book",
        "count_photo",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "room_type",
        "amenity",
        "facility",
        "house_rules",
        "city",
        "country",
    )

    inlines = [
        PhotoInline,
    ]

    search_fields = ("=city", "^host__username")
    filter_horizontal = ("amenity", "facility", "house_rules")

    # self = admin class , obj = row
    def count_photo(self, obj):
        return obj.photos.count()

    count_photo.short_description = "photo count"


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition"""

    list_display = ("__str__", "get_thumnail")

    def get_thumnail(self, obj):
        return mark_safe(f"<img width='50' src='{obj.file.url}' />")

    get_thumnail.short_description = "Thumnail"

