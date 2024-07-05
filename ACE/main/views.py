from django.shortcuts import render,get_object_or_404
from .models import (Carousel,News,Announcement,Principal_Desk,Spotlight,lecturerImage,main_department_page,
                     Press_Release,Department,Spotlight_staff,Spotlight_students,Program,programBrief,
                     ResearchDocument,Calender,History,Emblem,Purpose,Campus,CampusImage,Principal,
                     PrincipalImage,Anthem,SrcCarousel,SrcAbout,SrcBody,SrcExecutive,Accomodation,
                     AccomodationInfo
                     )

from django.core.paginator import Paginator

# hompage

def home_page(request, *args, **kwargs):
    carousel_others = Carousel.objects.filter(Active_carousel=False)
    main_carousel = Carousel.objects.filter(Active_carousel=True)
    news = News.objects.filter(On_homepage=True)
    announcement = Announcement.objects.filter(Available=True)
    principal = Principal_Desk.objects.filter(Front=True)
    press = Press_Release.objects.filter(headlines=True)
    department = Department.objects.all()
    sstaff = Spotlight_staff.objects.filter(homepage=True)
    sstudent = Spotlight_students.objects.filter(homepage=True)
    spotlight = Spotlight.objects.filter(homepage=True)


    context ={
        "carousel_others":carousel_others,
        "main_carousel" : main_carousel,
        "news" : news,
        "announcement" : announcement,
        "principal" : principal,
        "press" : press,
        "department" : department,
        "sstaff" : sstaff,
        "sstudents" : sstudent,
        "sportlight": spotlight
        }

    return render(request,'home/index.html', context)


# All detailed pages
 
def DetailedNews(request,news_id,*args, **kwargs):
    detailednews = News.objects.get(id=news_id)
    context ={
        "dnews":detailednews
    }
    return render(request,'news/detailedPage.html',context)

def detailedPrincipal(request, principal_id, *args, **kwargs):
    detailprincipaldesk = Principal_Desk.objects.get(id=principal_id)
    context ={
        "detailprincipaldesk":detailprincipaldesk
    }
    return render(request,'desk/principal.html',context)

def detailedAnnouncement(request, announce_id,*args, **kwargs):
    detailedannouncement = Announcement.objects.get(id=announce_id)
    context ={
        "detailedannouncement": detailedannouncement
    }
    return render(request, 'desk/announcement.html',context)

def detailedPress(request, press_id, *args, **kwargs):
    detailedpress = Press_Release.objects.get(id=press_id)
    context ={
        "detailedpress" : detailedpress 
    }
    return render(request, 'desk/press.html', context)


def detailedDepartment(request, department_id, *args, **kwargs):
    detaileddepartment = get_object_or_404(Department, id=department_id)
    lectImages = lecturerImage.objects.filter(department=detaileddepartment)
    context ={
        "detaileddepartment" : detaileddepartment,
        "photo": lectImages
    }
    return render(request, 'academic/department.html', context)

def detailedSportlight(request, sportlight_id, *args, **kwargs):
    detailedsportlight = Spotlight.objects.get(id=sportlight_id)
    context ={
        "detailedsportlight" : detailedsportlight 
    }
    return render(request, 'academic/sportlight.html', context)


# individual components

def maindepartment(request, *args, **kwargs):
    main = Department.objects.all()
    info = main_department_page.objects.all()

    context = {
        'main':main,
        'info' : info
    }

    return render( request,"academic/main.html",context )

def acemedia(request,*args, **kwargs):
    news = News.objects.all()
    press =Press_Release.objects.all()
    page = Paginator(news, 3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    news = News.objects.filter(On_homepage=True)

    context = {
        'page':page,
        'press':press,
        'news':news 
    }
    return render(request, "news/acemedia.html",context)

def mainannouncement(request,*args, **kwargs):
    announcement = Announcement.objects.all()
    desk = Principal_Desk.objects.all()

    context = {
        'announcement':announcement,
        'desk':desk
    }
    return render(request, "desk/maindeck.html",context)

#academic
def program(request, *args, **kwargs):
    brief = programBrief.objects.all()
    programme = Program.objects.all()
    context = {
        'programme':programme,
        'header': brief

    }
    return render(request, 'academic/program.html',context)

def research(request, *args, **kwargs):
    res = ResearchDocument.objects.all().order_by("-created_on")
    context ={
        'research':res
    }
    return render(request, 'academic/research.html',context)

#students

def calender(request, *args, **kwargs):
    cal = Calender.objects.all()
    context = {
        'calender':cal
    }
    return render(request, 'academic/calender.html',context)

def SRC(request, *args, **kwargs):
    silderdata = SrcCarousel.objects.all()
    aboutdata = SrcAbout.objects.all()
    exedata = SrcExecutive.objects.all()
    pageinfo =SrcBody.objects.all()[0]
    context ={
        'slider': silderdata,
        'about': aboutdata,
        'executive': exedata,
        'detail': pageinfo
    }
    return render(request, 'students/src.html', context)

def accomodation(request, *args, **kwargs):
    hall = Accomodation.objects.all()
    info = AccomodationInfo.objects.all()[0]
    context={
        'hall':hall,
        'info': info
    }
    return render(request, 'students/hall.html',context)

def dean(request, *args, **kwargs):
    return render(request, 'students/dean.html')

def STS(request, *args, **kwargs):
    return render(request, 'students/sts.html')

def Guideline(request, *args, **kwargs):
    return render(request, 'students/freshmen.html')


#Group
def church(request, *args, **kwargs):
    return render(request, 'group/churches.html')

def music(request, *args, **kwargs):
    return render(request, 'group/music.html')

def cultural(request, *args, **kwargs):
    return render(request, 'group/cultural.html')

#About

def history(request, *args, **kwargs):
    his = History.objects.all()
    context ={
        "history": his 
    }
    return render(request, 'about/history.html', context)

def vision(request, *args, **kwargs):
    Pur = Purpose.objects.all()

    context = {
        "purpose": Pur,
    }
    return render(request, 'about/vision.html',context)

def facilities(request, *args, **kwargs):
    campus = Campus.objects.filter(header='CAMPUS IMAGES')[:1].get()
    campusIma =CampusImage.objects.filter(part=campus)

    context = {
        "campus":campus,
        "campusImage":campusIma
    }
    return render(request, 'about/facilities.html',context)

def anthem(request, *args, **kwargs):
    college_anthem = Anthem.objects.filter(pk=1)[:1].get()
    context = {
        "anthem":college_anthem
    }
    return render(request, 'about/anthem.html',context)

def emblem(request, *args, **kwargs):
    emb = Emblem.objects.filter(pk=1)[:1].get()
    context ={
        "emblem":emb
    }
    return render(request, 'header/emblem.html',context)

def principal(request, *args, **kwargs):
    principal = Principal.objects.filter(pk=1)[:1].get()
    principalImage =PrincipalImage.objects.filter(principal_for=principal)

    context = {
        "principal":principal,
        "principalImage":principalImage
    }
    return render(request, 'about/principal.html',context)


#header-part

def staff(request, *args, **kwargs):
    return render(request, 'staff/staff.html')

def student(request, *args, **kwargs):
    return render(request, 'students/mainstudents.html')

def about(request, *args, **kwargs):
    return render(request, 'about/about.html')

def alumni(request, *args, **kwargs):
    return render(request, 'header/alumni.html')

def contact(request, *args, **kwargs):
    return render(request, 'header/contact.html')

def libraries(request, *args, **kwargs):
    return render(request, 'header/libraries.html')

def ict(request, *args, **kwargs):
    return render(request, 'header/ict.html')

def management(request, *args, **kwargs):
    return render(request, 'header/management.html')






