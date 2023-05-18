from django.urls import path
from django.views.generic import TemplateView

from .views import blog, dashboard, studio, feed, discover, analytics, emailer, staff, signup_flow

urlpatterns = [
    path('', blog.home, name='home'),
    path('staff/review/', staff.review_flow, name='review_flow'),
    path('staff/review/approve/<pk>', staff.approve, name='review_approve'),
    path('staff/review/block/<pk>', staff.block, name='review_block'),
    path('staff/review/delete/<pk>', staff.delete, name='review_delete'),
    path('staff/dashboard/', staff.dashboard, name='staff_dashboard'),

    path('accounts/delete/', dashboard.delete_user, name='user_delete'),
    path('signup/', signup_flow.signup, name="signup_flow"),

    path('dashboard/', studio.studio, name="dashboard"),
    path('dashboard/nav/', dashboard.nav, name='nav'),
    path('dashboard/directives/', studio.directive_edit, name="directive_edit"),
    path('dashboard/styles/', dashboard.styles, name='styles'),
    path('dashboard/account/', dashboard.account, name='account'),
    path('dashboard/email-list/', emailer.email_list, name='email_list'),

    path('dashboard/analytics/', analytics.analytics, name='analytics'),
    path('dashboard/analytics-upgraded/', analytics.analytics_upgraded, name="analytics_upgraded"),

    path('dashboard/upgrade/', dashboard.upgrade, name='upgrade'),
    path('dashboard/opt-in-review/', dashboard.opt_in_review, name='opt_in_review'),

    path('dashboard/posts/', dashboard.posts_edit, name='post'),
    path('dashboard/posts/new/', studio.post, name="post_new"),
    path('dashboard/posts/<pk>/', studio.post, name="post_edit"),
    path('dashboard/posts/<pk>/delete/', dashboard.post_delete, name='post_delete'),
    path('dashboard/preview/', studio.preview, name="preview"),
    path('dashboard/upload-image/', dashboard.upload_image, name='upload_image'),

    path('dashboard/post-template/', studio.post_template, name="post_template"),


    path('discover/', discover.discover, name='discover'),
    path('discover/feed/', discover.feed, name='discover_feed'),
    path('search/', discover.search, name='search'),

    path('lemon-webhook/', blog.lemon_webhook, name='lemon_webhook'),

    path('ping/', blog.ping, name='ping'),
    path('blog/', blog.posts, name='posts'),
    path('sitemap.xml', blog.sitemap, name='sitemap'),
    path('robots.txt', blog.robots, name='robots'),
    path('public-analytics/', blog.public_analytics, name="public_analytics"),
    path('upvote/<pk>/', blog.upvote, name='upvote'),
    path('subscribe/', emailer.subscribe, name='subscribe'),
    path('email-subscribe/', emailer.email_subscribe, name='email_subscribe'),
    path('confirm-subscription/', emailer.confirm_subscription, name='confirm_subscription'),
    path('hit/<pk>/', analytics.post_hit, name='post_hit'),
    path("feed/", feed.feed, name="post_feed"),
    path('<slug>/', blog.post, name='post'),
    path('<path:resource>/', blog.post_alias, name='post_alias'),
    path('404/', TemplateView.as_view(template_name="404.html", content_type="text/html"))
]
