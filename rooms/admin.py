from django.contrib import admin
from . import models


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
        "count_amenities",
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

    search_fields = ("=city", "^host__username")
    filter_horizontal = ("amenity", "facility", "house_rules")

    # self = admin class , obj = row
    def count_amenities(self, obj):
        return obj.amenity.count()

    count_amenities.short_description = "hello "


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition"""

    pass
