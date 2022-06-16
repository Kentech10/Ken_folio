from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from.models import Destination


def index(request):
    dest1 = Destination()
    dest1.name = 'Computer Engineer'
    dest1.text = 'Designs, and manages computer hardware and software systems issues, Kentech can work on any type of computer system, desktop, laptop, pads e.t.c'
    dest1.about_me = 'I have just over a year of expirence as a  software Engineer with Netexcel systems and  technology. In this short time there i have already contributed to over a dozen of projects and assisted in managing one project for one of the firm in long-time client'
    dest1.about_me2 = 'Prior to this role, I completed a two-year internship with Netexcel Systems and Technology, where I honor my web app development skills. Ideally, I would like to continue to specialize in mobile software engineering, an area where I know your firm excels'
    dest1.about_me3 ="Also an expirenced computer Engineer with 3years working expirence with purechem industrial limited in which am able to use my engineering skills to impact and impriove the organization growth."
    dest1.blog = 'Blog'
    dest1.blog2 = 'Get the latest news around the globe here.'
    dest1.folio ="Kentech completed jobs listed below"
    dest1.folio2 ="Online coffee ordering system"
    dest1.folio3 ="Facial recognition for student attendance"
    dest1.folio4 ="Kentech Developers blog"
    dest1.folio5 ="E-commerce system"
    dest1.folio6 = "Online Studio management system"
    dest1.folio7 ="School management system"
    dest1.blog3 ="David Degea on the verge of signing a new man utd deal worth 350k a week"
    dest1.blog4 ="Real Madrid Complete the signing of Anthony Rudiger from chelsea on a free transfer"
    dest1.blog5 ="Names of 13 presidential Aspirant cleared by APC committee [LIST]"
    dest1.service ="We offer web designing skills by providing you with a good looking websites, we offer this project on school management system, online book shopping and many more.Feel free to reach out to Kentech today."
    dest1.service3 ="Kentech also offer service  in Networking both wired and wireless networking, and also offer a network maintenance service with general supply of networking equipment."
    dest1.service4 ="Kentech also offer service on CCTV camera installations, both indoors, outdoor, and PTZ cameras including network camera, we also offer maintenance service on CCTV camera"
    dest1.service5 ="We provide a good and a well looking graphics works, such as mukup designs, 3D's, 2D's and also we design a bussiness logo's and wedding cards "
    dest1.service2 ="Kentech provide service on web Applications, both creating and maintentaning a web applications, we work on project such as Facial Recognition, Paypal, E-commerce and many more. "
    dest1.get_in_touch ='Want to get in touch? Fill out the form below to send a messange to Kentech and i will get back to you as soon as possible!'
    return render(request, 'index.html', {'dest1': dest1})