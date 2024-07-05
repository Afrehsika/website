from django.contrib import admin
from .models import (Carousel,News,Announcement,Principal_Desk,Spotlight,lecturerImage,main_department_page,
                     Press_Release,Department,Spotlight_staff,Spotlight_students,Program,programBrief,
                     ResearchDocument,Calender,Campus,CampusImage,Principal,PrincipalImage,Purpose,
                     History,Emblem,Anthem,SrcCarousel,SrcAbout,SrcBody,SrcExecutive,Accomodation,
                     AccomodationInfo
                     )

# department.

class lecturerImageAdmin(admin.StackedInline):
    model = lecturerImage

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    inlines = [lecturerImageAdmin]

    class Meta:
        model=Department

@admin.register(lecturerImage)
class lecturerImageAdmin(admin.ModelAdmin):
    jazzmin_section_order = ("")


#campus
class CampusImageAdmin(admin.StackedInline):
    model = CampusImage

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    inlines = [CampusImageAdmin]

    class Meta:
        model=Campus

@admin.register(CampusImage)
class CampusImageAdmin(admin.ModelAdmin):
    jazzmin_section_order = ("")


#principal
class PrincipalImageAdmin(admin.StackedInline):
    model = PrincipalImage

@admin.register(Principal)
class PrincipalAdmin(admin.ModelAdmin):
    inlines = [PrincipalImageAdmin]

    class Meta:
        model=Principal

@admin.register(PrincipalImage)
class CampusImageAdmin(admin.ModelAdmin):
    jazzmin_section_order = ("")




admin.site.register(AccomodationInfo)
admin.site.register(Accomodation)
admin.site.register(SrcExecutive)
admin.site.register(SrcBody)
admin.site.register(SrcAbout)
admin.site.register(SrcCarousel)
admin.site.register(Anthem)
admin.site.register(Purpose)
admin.site.register(main_department_page)
admin.site.register(Carousel)
admin.site.register(News)
admin.site.register(Announcement)
admin.site.register(Principal_Desk)
admin.site.register(Press_Release)
admin.site.register(History)
admin.site.register(Emblem)
admin.site.register(Spotlight_staff)
admin.site.register(Spotlight_students)
admin.site.register(Spotlight)
admin.site.register(Program)
admin.site.register(programBrief)
admin.site.register(ResearchDocument)
admin.site.register(Calender)