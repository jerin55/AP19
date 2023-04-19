
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import article_list_by_tag


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pageindex", views.pageindex, name="pageindex"),
    path("intrest_page", views.intrest_page, name="intrest_page"),
    path("intrest_create", views.intrest_create, name="intrest_create"),
    path("login", views.login_view, name="login"),
    path("n/logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:username>", views.profile, name='profile'),
    path("buyprofile/<int:username>", views.buyprofile, name='buyprofile'),
    path('tag/<str:tag>/', article_list_by_tag, name='article_list_by_tag'),
    
    path("n/saved", views.saved, name="saved"),
    path("n/user_create_post/<int:pk>", views.user_create_post, name="user_create_post"),
    path("n/create_pagepost/<int:pageid>", views.create_pagepost, name="create_pagepost"),
    path("n/intrest_create_post/<int:pk>", views.intrest_create_post, name="intrest_create_post"),
    path("n/sub_intrest_create_post/<int:pk>", views.sub_intrest_create_post, name="sub_intrest_create_post"),
    path("n/post/<int:id>/like", views.like_post, name="likepost"),
    path("n/post/<int:id>/unlike", views.unlike_post, name="unlikepost"),
    path("n/post/<int:id>/save", views.save_post, name="savepost"),
    path("n/post/<int:id>/unsave", views.unsave_post, name="unsavepost"),
    path("n/post/<int:userid>/commentz", views.commentz, name="commentz"),
   
    path("n/post/<int:post_id>/delete", views.delete_post, name="deletepost"),
    path("<str:username>/follow", views.follow, name="followuser"),
    path("<str:username>/unfollow", views.unfollow, name="unfollowuser"),
    path("n/post/<int:post_id>/edit", views.edit_post, name="editpost"),
    path('n/page_registration/<int:pk>',views.page_registration,name="page_registration"),
    path('n/page_creation/<int:pk>',views.page_creation,name="page_creation"),
    path('n/pag/<int:pk>',views.pag,name="pag"),
    path('pageprofile/<int:pageid>',views.pageprofile,name="pageprofile"),
    path('n/cart',views.cart,name="cart"),
    path('n/checkout',views.checkout,name="checkout"),
    path('n/product_detail/<int:id>/<int:userid>',views.product_detail,name="product_detail"),
    path('topicpage/<int:pk>',views.topicpage,name='topicpage'),
    path('subtopicpage/<int:pk>',views.subtopicpage,name='subtopicpage'),
    path('intrest_follow/<int:pk>', views.intrest_follow, name='intrest_follow'),
    path('intrest_unfollow/<int:pk>', views.intrest_unfollow, name='intrest_unfollow'),
    path('intrest_follow_topicpage/<int:pk>', views.intrest_follow_topicpage, name='intrest_follow_topicpage'),
    path('intrest_unfollow_topicpage/<int:pk>', views.intrest_unfollow_topicpage, name='intrest_unfollow_topicpage'),
    path('filter_intrest_follow/<int:pk>', views.filter_intrest_follow, name='filter_intrest_follow'),
    path('filter_intrest_unfollow/<int:pk>', views.filter_intrest_unfollow, name='filter_intrest_unfollow'),
    path("new_post",views.new_post,name="new_post"),
    path("user_posts",views.user_posts,name="user_posts"),
    path("best_post",views.best_post,name="best_post"),
    path("top_post",views.top_post,name="top_post"),
    path("sales_post",views.sales_post,name="sales_post"),
    path("intrst_followers/<int:id>",views.intrst_followers,name="intrst_followers"),
    path("page_follow/<int:userid>",views.page_follow,name="page_follow"),
    path("page_unfollow/<int:pk>",views.page_unfollow,name="page_unfollow"),
    path('download_item/<int:pk>/<int:userid>',views.download_item,name='download_item'),
    path('delete_frd_download/<int:pid>/<int:pk>',views.delete_frd_download,name='delete_frd_download'),
    path('sent_friend_request_download/<int:pk>/<int:userid>',views.sent_friend_request_download,name='sent_friend_request_download'), 
    path('create_post/<int:pk>',views.create_post,name='create_post'),
    path('topic_createpost/<int:pk>',views.topic_createpost,name='topic_createpost'),
    path('page_createpost/<int:pk>',views.page_createpost,name='page_createpost'),

  
    path('article_list',views.article_list_by_tag,name='article_list'),

    path('add_cart/<int:id>',views.add_cart,name='add_cart'),

    path('zip',views.zip,name='zip'),

    path('remove_cart/<int:id>',views.remove_cart,name='remove_cart'),

    path('remove_cart_all',views.remove_cart_all,name='remove_cart_all'),

    
    path('shipping_address',views.shipping_address,name='shipping_address'),
    

    path('place_order/<int:id>',views.place_order,name='place_order'),

    path('n/dashboard',views.dashboard,name='dashboard'),

    path('dashboard_profile',views.dashboard_profile,name='dashboard_profile'),

    path('dash_edit_profile',views.dash_edit_profile,name='dash_edit_profile'),

    path('edit',views.edit,name='edit'),

    path('dash_address_book',views.dash_address_book,name='dash_address_book'),

    path('track_order',views.track_order,name='track_order'),

    path('n/my_order',views.my_order,name='my_order'),

    path('manage_order/<int:id>',views.manage_order,name='manage_order'),
    path('n/pagepost/<int:pk>',views.pagepost,name='pagepost'),
    path('n/mypage/<int:pk>',views.mypage,name='mypage'),
  
    path('n/edit_profile/<int:pk>',views.edit_profile,name='edit_profile'),
    path('n/edit_pr/<int:pk>',views.edit_pr,name='edit_pr'),
    path('n/edit_page/<int:pk>',views.edit_page,name='edit_page'),
    path('n/edit_pages/<int:pk>',views.edit_pages,name='edit_pages'),
    path('search/', views.search, name='search'),
    path('sent_friend_request/<int:userid>',views.sent_friend_request,name='sent_friend_request'),
    path('accept_friend_request/<int:requestid>',views.accept_friend_request,name='accept_friend_request'),
    path('notification/<int:nid>',views.notification,name='notification'),
    path('invitation_request/<int:nid>',views.invitation_request,name='invitation_request'),
    path('userfriends/<int:id>',views.userfriends,name='userfriends'),
    path('following/<int:id>',views.following,name='following'),
    path('followers/<int:id>',views.followers,name='followers'),
    path('sent_invite_request/<int:userid>/<int:id>',views.sent_invite_request,name='sent_invite_request'),
    path('accept_invite_request/<int:requestid>',views.accept_invite_request,name='accept_invite_request'),
    path('userinviters/<int:id>',views.userinviters,name='userinviters'),
    path('delete_inv/<int:pk>',views.delete_inv,name='delete_inv'),
    path('delete_frd/<int:pk>',views.delete_frd,name='delete_frd'),
    path('delete_post/<int:pk>',views.delete_post,name='delete_post'),
    path('pages_accept_invites/<int:pk>',views.pages_accept_invites,name='pages_accept_invites'),
    path('post_comment/<int:pk>',views.post_comment,name='post_comment'),
    path('nsale_post_share/<int:pk>',views.nsale_post_share,name='nsale_post_share'),
    path('sale_post_share/<int:pk>',views.sale_post_share,name='sale_post_share'),
    path('wishlis/<int:pk>',views.wishlis,name='wishlis'),
    path('add_to_wish/<int:pk>',views.add_to_wish,name='add_to_wish'),
    path('delete_wishlist/<int:pk>',views.delete_wishlist,name='delete_wishlist'),
    path('reviews/<int:userid>/<int:id>',views.reviews,name='reviews'),
    path('subtopic_createpost/<int:pk>',views.subtopic_createpost,name='subtopic_createpost'),

    path('Invite_Page/<int:pk>',views.Invite_Page,name='Invite_Page'),

    path('Leave_Join/<int:pk>',views.Leave_Join,name='Leave_Join'),

    path('Invite_Joined/<int:pk>/<int:id>',views.Invite_Joined,name='Invite_Joined'),

    path('Invite_Removed/<int:pk>/<int:id>',views.Invite_Removed,name='Invite_Removed'),


    path('Join_friends/<int:id>',views.Join_friends,name='Join_friends'),

    path('Join_friends_reqest/<int:id>',views.Join_friends_reqest,name='Join_friends_reqest'),
    path('review_reply/<int:pk>',views.review_reply,name='review_reply'),
    path("reply/<int:userid>", views.reply, name="reply"),
    path("reply_delete/<int:pk>/<int:id>", views.reply_delete, name="reply_delete"),
    path("review_delete/<int:pk>/<int:id>", views.review_delete, name="review_delete"),






]
