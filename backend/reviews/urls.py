from django.urls import path
from . import views
 
app_name = ''
urlpatterns = [
    # 리뷰작성, 영화의 리뷰목록 반환
    path('review_list/<int:movie_pk>', views.review_cr),
    # 리뷰수정과 리뷰삭제
    path('<int:review_pk>', views.review_ud),
    #리뷰 좋아요 누르기
    path('like/<int:review_pk>', views.review_like),
    # 리뷰댓글작성과 리뷰댓글목록 받기
    path('comment_list/<int:review_pk>', views.comment_cr),
    path('comment/<int:comment_pk>', views.comment_ud),
    path('like/comment/<int:comment_pk>', views.comment_like)
]
