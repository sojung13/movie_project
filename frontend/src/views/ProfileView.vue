<template>
  <div>
    <div class="d-flex justify-content-center animate__animated animate__fadeInUp page-title">
      <h2 class="p-3 eng-text">HALL OF</h2>
      <h1 class="eng-text">{{ profile.username }}</h1>
    </div>

    <div class="d-flex justify-content-center animate__animated animate__fadeInDown follow">
      <h5 class="ps-3 eng-text">FOLLOWER {{FOLLOWER_COUNT}} </h5> 
      <h5 class="px-3 eng-text">FOLLOWING {{FOLLOWING_COUNT}}</h5>
      <!-- <h4
      v-if="profile.username !== currentUser.username"
        @click="follow(profile.username), !temp"
        >🤍</h4> -->


      <div v-if="temp" id=#follow>
        <h4
      v-if="profile.username !== currentUser.username"
        @click="follow(profile.username)"
        style="cursor: pointer;"
        >❤️</h4>
      </div>
      <div v-if="!temp" id=#follow>
        <h4
      v-if="profile.username !== currentUser.username"
        @click="follow(profile.username)"
        style="cursor: pointer;"
        >🤍</h4>
      </div>

    </div>


    <div class="container" style="padding-bottom:10%;">
      <div class="row">
        <div class="user-movie animate__animated animate__fadeInDown col col-12 col-lg-4">
          <div class="card card1">
            
            <div class="snip1236 ">
              <h1>MOVIES</h1>
              <h5 class="korean-text">좋아요를 누른 영화 리스트</h5>
            </div>

            <p class="korean-text">클릭하여 해당 영화를 구경해 보세요!</p>
            <ul class="list-unstyled">
              <li v-for="(like_movie, idx) in profile.like_movies" :key="idx">
                <router-link :to="{ name: 'detailmovie', params: { movietitle: like_movie.title } }" class="korean-text list-text">
                  {{ like_movie.title }}
                </router-link>
              </li>
            </ul>
          </div>
        </div>

        <div class="user-review animate__animated animate__fadeInUp col col-12 col-lg-4">
          <div class="card card2">
            <div class="snip1236 ">
              <h1>REVIEWS</h1>
              <h5 class="korean-text">작성한 리뷰 리스트</h5>
            </div>
            <p class="korean-text">클릭하여 해당 리뷰의 영화를 구경해 보세요!</p>
            <ul class="list-unstyled">
              <li v-for="review in profile.reviews" :key="review.pk">
                <router-link :to="{ name: 'detailmovie', params: { movietitle: review.movie.title } }" 
                class="korean-text list-text" style="line-height:30px; font-size:90%;">
                {{ review.content }}
                <hr>
                </router-link>
              </li>
            </ul>
          </div>
        </div>

        <div class="user-comment animate__animated animate__fadeInDown col col-12 col-lg-4">
          <div class="card card3">
            <div class="snip1236" style="padding-bottom:4%;">
              <h1 style="padding-bottom:12px;">COMMENTS</h1>
              <h5 class="korean-text" style="padding-bottom: 10px;">작성한 댓글 리스트</h5>
            </div>
            <ul class="list-unstyled">
              <li v-for="comment in profile.comments" :key="comment.pk" class="korean-text" 
              style="line-height:20px; font-size:70%; margin-left:2%; margin-right:2%;">       
                {{ comment.content }}
                <hr>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile','currentUser']),
    FOLLOWER_COUNT(){
      return this.profile.followers.length
    },
    FOLLOWING_COUNT(){
      return this.profile.followings.length
    }

  },
  data() {
    return {
      temp: false
      }
  },
  methods: {
    ...mapActions(['fetchProfile','follow']),
    IS_FOLLOW_USER(){
      // 좋아요를 이미 눌렀으면 트루를 반환할거임
      for (let i = 0; i < this.profile.followers.length; i++){
        if (this.profile.followers[i] === this.currentUser.pk){
          this.temp = true
          return
        } 
      } this.temp = false
    }
  },
  created() {
    this.fetchProfile(this.$route.params.username)
    this.IS_FOLLOW_USER()
  },
  watch:{
    profile(){
      this.IS_FOLLOW_USER()
    }
  }

  // watch:{
  //   profile(){
  //     this.fetchProfile(this.$route.params.username)
  //   },
  // }
}

</script>

<style>
@import url(//fonts.googleapis.com/earlyaccess/jejumyeongjo.css);
.eng-text {
  font-family: 'Times New Roman', Times, serif;
}
.korean-text {
  font-family: 'Jeju Myeongjo', serif;
}




/* 팔로우 버튼 */
@import url(https://fonts.googleapis.com/css?family=Roboto);
.snip1505 {
  font-family: 'Roboto', Arial, sans-serif;
  color: #ffffff;
  cursor: pointer;
  padding: 0px 40px;
  display: inline-block;
  margin: 15px 30px;
  text-transform: uppercase;
  line-height: 2.7em;
  letter-spacing: 1.5px;
  font-size: 1em;
  outline: none;
  position: relative;
  font-size: 16px;
  border: 3px solid #fff;
  background-color: transparent;
  border-radius: 15px 15px 0;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
}
.snip1505:before {
  content: "";
  position: absolute;
  left: -3px;
  top: -3px;
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 35px 35px 0 0;
  border-color: #c87f0a transparent transparent transparent;
  z-index: 1;
}
.snip1505:hover,
.snip1505.hover {
  border-color: #c87f0a;
}






/* 클릭하면 넘어가는 영화제목 리뷰 리스트 글자 */
.list-text {
  text-decoration: none;
  color: rgb(0, 0, 0);
  transform: color(rgb(0, 0, 0));
  transition: color 0.5s, font-size 0.3s;
  font-family: 'Jeju Myeongjo', serif;
  font-size: 120%;
}
.list-text:hover {
  color: rgb(209, 118, 7);
  font-size: 140%;
  transform: rgb(209, 118, 7);
  transition: color 0.5s, font-size 0.3s;
}
.page-title {
  animation-duration: 1s; 
  color: aliceblue;
}
.follow {
  /* animation-duration: 1s;  */
  color: aliceblue;
}






/* 빅3중 1 좋아하는 영화 */
.user-movie {
  padding-top: 1%;
  line-height: 250%;
}
/* .like-movie-title {
  padding-top: 5%;
  padding-bottom: 5%;
  border-top: solid 1px black;
  border-bottom: solid 1px black;

} */
.card1 {
  background-color: #dbdbdb;
  transition: scale 0.4s, transform 0.4s;
  /* padding-top: 10%; */
  border-radius: 7px;
  padding-top: 50px;
  padding-bottom: 50px;

}
.card1:hover {
  transform: scale(1.05);
  transition: transform 0.4s;
}






/* 빅3중 2 리뷰 */
.user-review {
  padding-top: 3%;
  animation-duration: 1.7s; 
  line-height: 250%;
  padding-bottom: 2%;
}
.card2 {
  background-color: #bababa;
  transition: scale 0.4s, transform 0.4s;
  border-radius: 7px;
  padding-top: 50px;
  padding-bottom: 50px;
}

.card2:hover {
  transform: scale(1.05);
  transition: transform 0.4s;
}




/* 빅3중 3 댓글 */
.user-comment {
  padding-top: 1%;
  animation-duration: 1.3s; 
  line-height: 50%;
  font-size: 130%;
}

.card3 {
  background-color: #f1f1f1;
  transition: scale 0.4s, transform 0.4s;
  padding-top: 50px;
  padding-bottom: 50px;
  border-radius: 7px;
}

.card3:hover {
  transform: scale(1.05);
  transition: transform 0.4s;
}






/* 로고 이미지 */
@import url(https://fonts.googleapis.com/css?family=Raleway:400);
@import url(https://fonts.googleapis.com/css?family=Playfair+Display:900);
.snip1236 {
  font-family: 'Raleway', Arial, sans-serif;
  position: relative;
  float: left;
  color: #2b2b2b;
  overflow: hidden;
  /* margin: 60px 25px; */
  /* max-width: 280px; */
  width: 100%;
  text-align: center;
  font-size: 16px;
  border-top: 3px solid #616161;
  /* padding-top: 6px; */
  justify-content: center;
}
.snip1236 * {
  -webkit-box-sizing: padding-box;
  box-sizing: padding-box;
}
.snip1236 h1,
.snip1236 h5 {
  margin: 0;
  line-height: 1em;
}
.snip1236 h1 {
  font-family: 'Playfair Display', Arial, sans-serif;
  font-size: 2.8em;
  text-transform: uppercase;
}
.snip1236 h5 {
  line-height: 0.5em;
  font-weight: 400;
  display: table;
  position: relative;
  display: inline-block;
  width: auto;
  padding: 0 10px;
}
.snip1236 h5:before,
.snip1236 h5:after {
  position: absolute;
  height: 2px;
  content: '';
  background: #7f7f7f;
  width: 1000%;
  top: 50%;
}
.snip1236 h5:before {
  left: -1000%;
}
.snip1236 h5:after {
  right: -1000%;
}


</style>
