from django.conf.urls.defaults import *

# your_app = name of your root djang app.
urlpatterns = patterns('music.views',
    # First leg of the authentication journey...
    url(r'^music/$', "index", name="index_player"),
    url(r'^venndoo/$', "venn"),
    url(r'^ven2/$', "venn2"),
    url(r'^hadoop/$', "hadoop"),
    url(r'^hadoop2/$', "hadoop2"),
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
