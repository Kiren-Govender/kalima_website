from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("services/", views.services, name="services"),
    # Not implemented yet
    ### LEGAL
    # path("", views.disclaimer, name="disclaimer"),
    # path("", views.emaildisclaimer, name="emaildisclaimer"),
    # path("", views.paia, name="paia"),
    # path("", views.popi, name="popi"),
    # path("", views.privacypolicy, name="privacypolicy"),
    # path("", views.termsofuse, name="termsofuse"),

    ### CORPORATE
    path("about/", views.about, name="about"),
    # path("", views.accreditation, name="accreditation"),
    # path("", views.empowerment, name="empowerment"),
    # path("", views.faircompetition, name="faircompetition"),
    # path("", views.globalpartnerships, name="globalpartnerships"),
    # path("", views.governance, name="governance"),
    # path("", views.humancapital, name="humancapital"),
    # path("", views.managementteam, name="managementteam"),
    # path("", views.socialresponsibility, name="socialresponsibility"),
    # path("", views.zerocorruption, name="zerocorruption"),
    # path("", views.zeroracismsexism, name="zeroracismsexism"),
    # path("", views.zeroslavery, name="zeroslavery"),
    # path("", views.zerotrafficking, name="zerotrafficking"),

    ### CONTACT
    # path("", views.checkorderstatus, name="checkorderstatus"),
    path("contact/", views.contact, name="contact"),
    # path("", views.logservicerequest, name="logservicerequest"),
    # path("", views.quotationrequest, name="quotationrequest"),

    ### DATACENTER
    # path("", views.cloud, name="cloud"), 
    # path("", views.datacenter, name="datacenter"),
    # path("", views.edgesecurity, name="edgesecurity"),
    # path("", views.endpointsecurity, name="endpointsecurity"), 
    # path("", views.hybrid, name="hybrid"),
    # path("", views.onpremise, name="onpremise"),
    # path("", views.securitymanagement, name="securitymanagement"),

    ### DOWNLOADPAGES
    # path("", views.downloads, name="downloads"),
    # path("", views.softwaredownloads, name="softwaredownloads"),

    ### END USER COMPUTING
    # path("", views.devices, name="devices"),
    # path("", views.endusercomputing, name="endusercomputing"),
    # path("", views.imaging, name="imaging"),
    # path("", views.software, name="software"),

    ### NEWS
    # path("", views.adobepartner, name="adobepartner"),
    # path("", views.companynews, name="companynews"),
    # path("", views.currentitem, name="currentitem"),
    # path("", views.ibmsilverpartner, name="ibmsilverpartner"),
    # path("", views.pgovenderdirector, name="pgovenderdirector"),

    ### RESOURCES
    # path("", views.articles, name="articles"),
    # path("", views.downloads, name="downloads"),
    # path("", views.pagetemplate, name="pagetemplate"),
    # path("", views.resources, name="resources"),


    ### SOLUTIONS
    # path("", views.disasterrecovery, name="disasterrecovery"),
    # path("", views.electronicsignature, name="electronicsignature"),
    # path("", views.monitoringmanagement, name="monitoringmanagement"),
    # path("", views.pamsolution, name="pamsolution"),
    # path("", views.sftp, name="sftp"),
    # path("", views.solutions, name="solutions"),

    ### FOOTERBASELINKS
    # path("", views.legal, name="legal"),
    # path("", views.sitemap, name="sitemap"),


    # path("<str:name>", views.greet, name="greet"),
]