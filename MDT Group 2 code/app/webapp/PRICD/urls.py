from django.conf.urls.defaults import *

# your_app = name of your root djang app.
urlpatterns = patterns('PRICD.views',
    # First leg of the authentication journey...
    #url(r'^music/$', "index", name="index_player"),
    #url(r'^$', "home"),
    url(r'^$', "test"),
    url(r'^conected/c$', "conected"),
    url(r'^fitbit/$', "fitbit"),
    url(r'^check/$', "checkSess"),
    url(r'^mydata/$', "someData"),
    url(r'^about/$', "about"),
    url(r'^success/$', "success"),
    url(r'^team/$', "team"),
    url(r'^p/(?P<someid>\w+)/$', "pTest"),
    url(r'^devices/$',"devices"),
    url(r'^login/$', "loginme"),
    url(r'^login/logsucess', "logsucess"),
    url(r'^signup/$', "signup"),
    url(r'^adduser/$', "adduser"),
    url(r'^failedlogin/$', "failedlogin"),
    # Logout, if need be
    #url(r'^logout/?$', "logout", name="twitter_logout"),  # Calling logout and what not

    # This is where they're redirected to after authorizing - we'll
    # further (silently) redirect them again here after storing tokens and such.
    #url(r'^thanks/?$', "thanks", name="twitter_callback"),

    # An example view using a Twython method with proper OAuth credentials. Clone
    # this view and url definition to get the rest of your desired pages/functionality.
    #url(r'^user_timeline/?$', "user_timeline", name="twitter_timeline"),
    #url(r'^user_followers/?$', "user_followers", name="twitter_followers"),
)
