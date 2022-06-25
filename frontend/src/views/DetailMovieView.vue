<template>
<div>
  <div class="container">
    <div class="row">
      <!-- 1-1) 왼쪽 섹션 포스터 / 큰 화면에선 오른쪽 영화 정보 영역과 같이 / 작은 화면에선 영화 포스터부터 보여주기 -->
      <div class="up-left-poster col-sm-12 col-lg-6">
        <!-- 1-1-1) 영화 포스터 -->
        <div class="poster-box">
          <img :src="POSTER_URL" alt="" class="poster-image">
        </div>
      </div>
      <!-- 1-2) 영화 정보 / 큰 화면에서 왼쪽 포스터와 같이 / 작은 화면에선 영화 포스터 밑에 붙여서-->
      <div class="up-right-information col-sm-12 col-lg-6">
        <h1 class="movie-title">{{choicedMovie.title}}</h1>
        <div class="d-flex justify-content-end">
          <p class="korean-text">{{LIKE_COUNT}} LIKES</p>

          <p 
          v-if="!temp"
          @click="likeMovie(choicedMovie.id)" class="mx-3 emoji">🤍</p>
          <p
          v-if="temp"
          @click="likeMovie(choicedMovie.id)" class="mx-3 emoji">❤️</p>
        </div>

        <!-- 일요일 저녁 구현 밑에 두버튼 눌렀을때 평점 수정,삭제 기능 구현해야함 새벽 ㅅㄱ -->

          <div class="d-flex justify-content-between">
              <div class="d-flex">
                <h4 class="korean-text" style="padding-left:3px;">유저 평균 평점 ⭐️</h4>
                <p class="korean-text">{{scoreAvg}}</p>
              </div>
            <div class="d-flex px-3">
              <input type="number" min="0" max="5" step="0.5" value="5" v-model="score" class="star-input">
              <button
              v-if="!scoreUser"
              @click="vote({movieTitle:choicedMovie.title, score:score, movie:choicedMovie.id})" class="star-button">SCORE</button>
              <h4
              v-if="scoreUser"
              @click="reVote({movieTitle:choicedMovie.title, score:score, movie:choicedMovie.id, voteId:VOTE_PK()})"
              style="cursor: pointer; padding-top:4%;"
              >
              ↩️</h4>
              <h4
              @click="deVote({movieTitle:choicedMovie.title, score:score, movie:choicedMovie.id, voteId:VOTE_PK()})"
              v-if="scoreUser" style="cursor: pointer; padding-top:4%;">❌</h4>
            </div>
          </div>


        <!-- 영화 정보 -->
        <div>
          <p class="d-flex justify-content-start m-2 korean-text">개봉일자 : {{choicedMovie.release_date}}</p>
          <p class="d-flex justify-content-start m-2 korean-text">역대 평점 : {{choicedMovie.vote_average}}</p>
          <p class="d-flex justify-content-start m-1 korean-text ">줄거리 : {{ choicedMovie.overview }}</p>
          <div class="poster-box">
            <img :src="BACKDROP_URL" alt="" class="backdrop_image">
          </div>
        </div>
      </div>
    </div>
  </div>

    <!-- 2) 아래 리뷰폼과 리뷰 확인란 -->
  <div class="container" style="width:100%;">
    <div class="row">
      <!-- 2-1)왼쪽 하단 리뷰다는 폼 -->
      <div class="down-left-review-form col-12">
        <!-- 리뷰작성 폼 -->
        <div>
          <h3 class="korean-text">한 줄 리뷰</h3>
          <br>
          <div class="search__container">
            <input class="search__input korean-text" style="font-size:110%;" type="text" placeholder="write your review!" v-model="review" @keyup.enter="reviewCreate">
            <button @click="reviewCreate" class="snip1319">SUBMIT</button>
          </div>
        </div>
        <br>
        <br>
      </div>


      <!-- 2-2-1) 리뷰란 -->
      <div class="down-right-review col-12">
        <h3 class="korean-text">리뷰 보기</h3>
        <div class="accordion">
          <div v-for="review in choicedMovie.reviews"
            :key="review.pk" 
            class="accordion-item">
            <!-- 리뷰 헤더 = 눈에 보이는 영역 -->
            <div class="accordion-header" id="headingOne">
              <button class="accordion-button collapsed row" type="button" data-bs-toggle="collapse" :data-bs-target="`#collapse${review.pk.toString()}`" aria-expanded="false" :aria-controls="`collapse${review.pk.toString()}`"
              style=" background-color: #d2d2d2; margin-left:1px;">
                <div class="col-12 d-flex">
                  <router-link :to="{ name: 'profile', params: { username:review.user.username } } " class="text-decoration-none text-black eng-text" style="font-size:120%;">
                    <p class="user-name col-1"> &nbsp;{{review.user.username}}</p>
                  </router-link>
                  <p class="korean-text card" style="background-color: #d2d2d2; border:none; col-11">&nbsp; : {{review.content}}</p>
                </div>
                <div class="d-flex col-12 justify-content-end">
                  <div v-if="isClicked">
                    <input v-if="currentUser.username === review.user.username"
                    class="search__input" type="text" placeholder="update your review!" v-model="updatereview" @keyup.enter="reviewUpdate(review.pk)" value="review(review.pk)">
                  </div>
                  <h3
                  @click="reviewUpdate(review.pk), isClicked=true"
                  v-if="currentUser.username === review.user.username" style="height:26px; color:green; margin-right:1%;"><i class="fa fa-arrow-left"></i></h3>
                  <h3
                    v-if="currentUser.username === review.user.username"
                    @click="deleteReview(review.pk)"  style="height:70%;">
                    <i class="fa fa-trash" style="color:black;"></i></h3>
                </div>
                <div style="font-size:75%; " class="col-12 d-flex justify-content-end">
                  <div class="d-flex flex-column">
                    <p class="korean-text">생성 시각 : {{ review.created_at}}</p>
                    <p class="korean-text">수정 시각 : {{ review.updated_at}}</p>
                  </div>
                </div>
              </button>
            </div>

            <!-- 리뷰 내용 = 눈에 안보이는 영역 -->
            <div :id="`collapse${review.pk.toString()}`" class="accordion-collapse collapse" aria-labelledby="headingOne" >
              <div class="accordion-body">
                <!-- 리뷰 댓글달기 -->
                <div class="d-flex">
                  <input class="search__input korean-text" style="width:100%; font-size:110%;" type="text" placeholder="write your comment!" v-model="wrightComment" @keyup.enter="commentCreate(review.pk)">
                  <button @click="commentCreate(review.pk)" class="snip1319">SUBMIT</button>
                </div>
                <!-- 리뷰에 대한 댓글 -->
                <div class="accordion" id="accordionExample">
                  <div
                    class="korean-text accordion-item"
                    v-for="(comment, idx) in review.comments"
                    :key="idx" >
                    <!-- 댓글 내용 -->
                    <div class="accordion-header" id="headingOne">
                      <button class="accordion-button" type="button" data-bs-toggle="collapse" :data-bs-target="`#comment${comment.pk.toString()}`" aria-expanded="false" :aria-controls="`comment${comment.pk.toString()}`"
                      style="background-color: #e0e0e0;">
                        <p class="card col-10" style="background-color: #e0e0e0; border:none;">{{comment.content}}</p>
                        <p v-if="currentUser.username === comment.user.username"
                          class="col-2 d-flex justify-content-end" style="color:grey"
                        >CLICK TO EDIT</p>
                      </button>
                    </div>
                    <!-- 댓글 수정 폼 -->
                    <div class="accordion-collapse collapse" :id="`comment${comment.pk.toString()}`" aria-labelledby="headingOne" data-bs-parent="#accordionExample"
                    v-if="currentUser.username === comment.user.username"
                    >
                      <div class="accordion-body d-flex justify-content-end">
                        <div v-if="isClicked">
                          <input 
                          v-model="updateComment"
                          @keyup.enter="commentUpdate(comment.pk)"
                          v-if="currentUser.username === comment.user.username"
                          type="text" class="search__input korean-text" style="width:100%; font-size:110%;" placeholder="UPDATE YOUR COMMENT!">
                        </div>
                        <h2
                        @click="commentUpdate(comment.pk), isClicked=true"
                        v-if="currentUser.username === comment.user.username" style="height:26px; margin-right:1%; color:green;">
                          <i class="fa fa-arrow-left"></i></h2>
                        <h2
                          v-if="currentUser.username === comment.user.username"
                          @click="deleteComment(comment.pk)" style="height:70%;">
                          <i class="fa fa-trash" style="color:black;"></i></h2>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <router-link to="/"><button class="snip0072 m-3 ">HOME</button></router-link>
      </div>
    </div>
    <br>
    <br>
  </div>
</div>
</template>




<script>
import axios from 'axios'
import drf from '@/api/drf'
import {mapActions, mapGetters, mapMutations} from 'vuex'
// import CommentForm from '@/components/CommentForm.vue'
// import router from '@/router'


export default {
  name:'DetailMovieView',


  data() { 
    return {
      review:'',
      reviewPk:'',
      wrightComment:'',
      isClicked : false,
      score: 0,
      scoreAvg: 0,
      scoreUser: false,
      updatereview: '',
      updateComment:'',
      temp: false,
    }
  },
  computed: {
    ...mapGetters(['choicedMovie','authHeader','currentUser']),
    POSTER_URL() {
    return "https://image.tmdb.org/t/p/original" + this.choicedMovie.poster_path
    },
    BACKDROP_URL() {
      return "https://image.tmdb.org/t/p/original" + this.choicedMovie.backdrop_path
    },
    LIKE_COUNT(){
      return this.choicedMovie.like_users.length
      },
    CHECK_POINT(){
      return this.choicedMovie.reviews.length
    },
    // LIKE_USER() {
    //   return this.choicedMovie.like_users
    // }
  },

  methods:{
    ...mapActions(['choiceMovie','likeMovie','vote','reVote','deVote']),
    ...mapMutations(['CHOICE_MOVIE']),
    reviewCreate() {
      axios({ 
        url: drf.reviews.reviewC(this.choicedMovie.id),
        method: 'post',
        headers: this.authHeader,
        data:{
          content: this.review,
        },
      })
        .then(res=>{
          this.CHOICE_MOVIE(res.data)
        })
        // .then(router.go({ name: 'detailmovie', params:{movietitle:this.choicedMovie.title} }))
      this.review = ''
    },
    deleteReview(reviewId) {
      axios({ 
        url: drf.reviews.reviewUd(reviewId),
        method: 'delete',
        headers: this.authHeader,
        data:{
          movie: this.choicedMovie.id
        },
      })
        .then(res=>{
          this.CHOICE_MOVIE(res.data)
        })
    },
    reviewUpdate(reviewId){
      axios({ 
        url: drf.reviews.reviewUd(reviewId),
        method: 'put',
        headers: this.authHeader,
        data:{
          content: this.updatereview,
          movie: this.choicedMovie.id
        },
      })
        .then(res=>{
          this.CHOICE_MOVIE(res.data)
        })
      this.updatereview = ''
    },
    commentCreate(reviewId) {
      axios({ 
        url: drf.reviews.commentC(reviewId),
        method: 'post',
        headers: this.authHeader,
        data:{
          content: this.wrightComment,
          movie: this.choicedMovie.id
        }
      })
        .then(res=>{
          this.CHOICE_MOVIE(res.data)
        })
      // router.go({ name: 'detailmovie', params:{movietitle:this.choicedMovie.title} })
      this.wrightComment = ''
    },
    deleteComment(commentPk) {
      axios({ 
        url: drf.reviews.commentUd(commentPk),
        method: 'delete',
        headers: this.authHeader,
        data:{
          movie: this.choicedMovie.id
        },
      })
        .then(res=>{
          this.CHOICE_MOVIE(res.data)
        })
    },
    commentUpdate(commentPk){
      axios({ 
        url: drf.reviews.commentUd(commentPk),
        method: 'put',
        headers: this.authHeader,
        data:{
          content: this.updateComment,
          movie: this.choicedMovie.id
        }
      })
        .then(res=>{
          this.CHOICE_MOVIE(res.data)
        })
      this.updateComment = ''
    },
    getData(data) {
      this.wrightComment = data
    },
    // choicedMovie.votes 돌면서 rate값의 평균 구해야한다.
    getAvgScore(){
      const votes = this.choicedMovie.votes
      let sum = 0
      let temp = 0
      for (let i = 0; i < votes.length; i++){
        sum +=votes[i].rate   // 배열의 요소들을 하나씩 더한다.
        if (votes[i].user === this.currentUser.pk){
          this.scoreUser = true
          temp = 1
        }
      }
      if (temp === 0){
        this.scoreUser = false
      }
      if (isNaN((sum / votes.length).toFixed(1))){
        return this.scoreAvg = '첫 평가하기'
      }
      else {return this.scoreAvg = (sum / votes.length).toFixed(1)}
      

      
    },
    VOTE_PK(){
      const votes = this.choicedMovie.votes
      for (let i = 0; i < votes.length; i++){
        if (votes[i].user === this.currentUser.pk){
          return votes[i].id
        }
      }
    },
    IS_LIKE_USER(){
      // 좋아요를 이미 눌렀으면 트루를 반환할거임
      for (let i = 0; i < this.choicedMovie.like_users.length; i++){
        if (this.choicedMovie.like_users[i] === this.currentUser.pk){
          this.temp = true
          return
        } 
      } this.temp = false
    }
  },
  created(){
      const payload = this.$route.params.movietitle
      this.choiceMovie(payload)
      this.getAvgScore()
      this.IS_LIKE_USER()
    },
  
  watch:{
    choicedMovie(){
      this.getAvgScore()
      this.IS_LIKE_USER()
      
      // this.choiceMovie(this.choicedMovie.title)
    },
    // CHECK_POINT() {
    //   this.IS_LIKE_USER()
    // }


    }

}
</script>

<style scoped lang="scss">
@import url(//fonts.googleapis.com/earlyaccess/nanumpenscript.css);
@import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);
@import url(//fonts.googleapis.com/earlyaccess/jejumyeongjo.css);
/* 한글 영어 폰트 지명하기 */
.korean-text {
  font-family: 'Jeju Myeongjo', serif;
}

.eng-text {
  font-family: 'Times New Roman', Times, serif;
}

.emoji {
  cursor: pointer;
}

/* 큰 섹션 구분 */

.up-left-poster {
  background-color: #e8e8e8;
}

.up-right-information {
  background-color: #e8e8e8;
  padding-right: 3%;
}

.down-left-review-form {
  background-color: #e8e8e8;
}

.down-right-review {
  background-color: #e8e8e8;
}





/* 영화 이미지들 */
.poster-box {
  overflow: hidden;
}

.poster-image {
  width: 90%;
  padding-top: 7%;
  padding-bottom: 7%;
  transition: transform 1s;
  transform: scale(1);
}

.poster-image:hover {
  transform: scale(1.07);
  transition: scale 1s, transform 1s;
}

.backdrop_image {
  width: 98%;
  transition: transform 1s;
  transform: scale(1);
  overflow: hidden;
  padding-bottom: 7%;
}

.backdrop_image:hover {
  transform: scale(1.2);
  transition: scale 1s, transform 1s;
}


/* 내부 글자들  */

.movie-title {
  padding-top: 20%;
  padding-bottom: 2%;
  font-size: 250%;
  font-family: 'Jeju Myeongjo', serif;
}


/* 리뷰란 */

.user-name {
  font-size: 100%;
  transition: font-size 0.5s;
}

.user-name:hover {
  font-size: 130%;
  transition: font-size 0.5s;
}

.review-input-form {
  width: 10%;
  height: 100%;
  border-top: none;
  border-left: none;
  border-right:none;
  border-bottom: 3px solid black;
  background-color: #e8e8e8;
}

.accordion-button {
  // background-color: #d2d2d2;
  color: black;
}

.accordion-item {
  border: none;
  background-color: #e8e8e8;
  // border: 2px solid rgb(194, 188, 180);
}





// 제출 버튼 디자인
.snip1319 {
  font-family: 'Times New Roman', Times, serif;
  border: none;
  background-color: #838383;
  border-radius: 5px;
  color: rgb(255, 255, 255);
  cursor: pointer;
  padding: 0px 20px;
  display: inline-block;
  // margin: 15px 30px;
  text-transform: uppercase;
  line-height: 3.6em;
  // font-weight: 700;
  font-size: 2em;
  outline: none;
  position: relative;
  font-size: 12px;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
}
.snip1319:after {
  content: "";
  position: absolute;
  height: 100%;
  left: 0;
  right: 100%;
  border-radius: inherit;
  background-color: rgba(255, 255, 255, 0.15);
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
}
.snip1319:before {
  content: "";
  position: absolute;
  height: 100%;
  width: 100%;
  left: 0;
  top: 0;
  -webkit-transform: translateY(5px);
  transform: translateY(5px);
  background-color: inherit;
  border-radius: 10px;
  z-index: -1;
  box-shadow: inset 0 -6px 10px rgba(111, 109, 105, 0.75);
}
.snip1319:hover:after,
.snip1319.hover:after {
  right: 0;
}







// 인풋창 디자인 
@use postcss-color-function;
@use postcss-nested;
@import url('https://fonts.googleapis.com/css?family=Raleway:400,700,900');

/* Base styling */


.search {

    &__input {
        width: 80%;
        padding: 12px 24px;

        background-color: transparent;
        transition: transform 250ms ease-in-out;
        font-size: 14px;
        line-height: 18px;
        
        color: #464646;
        background-color: transparent;
/*         background-image: url(http://mihaeltomic.com/codepen/input-search/ic_search_black_24px.svg); */
 
      // background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3Cpath d='M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z'/%3E%3Cpath d='M0 0h24v24H0z' fill='none'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-size: 18px 18px;
        background-position: 95% center;
        border-radius: 5px;
        border: 1px solid #464646;
        transition: all 250ms ease-in-out;
        backface-visibility: hidden;
        transform-style: preserve-3d;
        
        &::placeholder {
            color: color(#464646 a(0.8));
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }
        
        &:hover,
        &:focus {
            padding: 12px 0;
            outline: 0;
            border: 1px solid transparent;
            border-bottom: 1px solid #464646;
            border-radius: 0;
            background-position: 100% center;
        }
    }
}

.credits {
    &__container {
        margin-top: 24px;
    }
    
    &__text {
        text-align: center;
        font-size: 13px;
        line-height: 18px;
    }
    
}






// 웬만한 버튼 모음
.star-button {
  border: none;
  background-color: #888888;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  cursor: pointer;
  color: rgb(255, 255, 255);
  margin-left: 5px;
  border-radius: 5px;
}

.star-button:hover {
  background-color: #6e6e6e;
  color: rgb(216, 200, 55);
}

.restar-button {
  border: none;
  background-color: #b3b3b3;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  cursor: pointer;
  color: rgb(3, 99, 183);
  margin-left: 5px;
  border-radius: 5px;
}

.cancel-button {
  border: none;
  background-color: #b3b3b3;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  cursor: pointer;
  color: rgb(183, 3, 3);
  margin-left: 5px;
  border-radius: 5px;
}

.delete-button {
  border: none;
  background-color: #b3b3b3;
  font-family: 'Times New Roman', Times, serif;
  cursor: pointer;
  color: rgb(179, 0, 0);
  margin-left: 5px;
}


.modi-button {
  border: none;
  background-color: #b3b3b3;
  font-family: 'Times New Roman', Times, serif;
  cursor: pointer;
  color: rgb(1, 101, 1);
}




// 인풋 넘버창
// input[type="number"]::-webkit-outer-spin-button,
// input[type="number"]::-webkit-inner-spin-button {
//     -webkit-appearance: none;
//     -moz-appearance: none;
//     appearance: none;
// }


.star-input {
  position: relative;
  width: 50px;
  height: 40px;
  border-radius: 5px;
  border: 2px solid rgba(0, 0, 0, 0.2);
  transition: 0.5s;
  background-color: #e8e8e8;
}

.star-input:hover {
  width: 60px;
  border: 2px solid rgb(0, 0, 0);
  background-color: #e8e8e8;
}






// 홈 버튼
@import url(https://fonts.googleapis.com/css?family=Raleway:400,500);
button.snip0072 {
  font-family: 'Raleway', Arial, sans-serif;
  border: none;
  background-color: #000000;
  border-radius: 5px;
  color: rgba(255, 255, 255, 0.7);
  cursor: pointer;
  // padding: 10px 20px;
  display: inline-block;
  // margin: 0px 35px;
  width: 100px;
  height: 40px;

  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 500;
  font-size: 1em;
  outline: none;
  position: relative;
  overflow: hidden;
}

button.snip0072:before {
  border-radius: 3px;
  content: '';
  display: block;
  position: absolute;
  left: 10px;
  right: 10px;
  top: 50%;
  bottom: 50%;
  background-color: #ffffff;
  border-top: 2px solid rgba(255, 255, 255, 0.8);
  border-bottom: 2px solid rgba(255, 255, 255, 0.8);
  opacity: 0;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  -webkit-transition-delay: 0.3s;
  transition-delay: 0.3s;
}

button.snip0072:hover,
button.snip0072.hover {
  color: #e5d2d2;
  -webkit-animation: flashText 0.3s;
  animation: flashText 0.3s;
}

button.snip0072:hover:before,
button.snip0072.hover:before {
  top: 15%;
  bottom: 15%;
  background-color: rgba(255, 255, 255, 0.1);
  opacity: 0.8;
}

button.snip0072:active:before {
  background-color: rgba(255, 255, 255, 0.3);
  opacity: 1;
  -webkit-transition-delay: 0s;
  transition-delay: 0s;
}

button.snip0072.blue {
  background-color: #1e5d87;
}

button.snip0072.red {
  background-color: #8e2a20;
}

button.snip0072.yellow {
  background-color: #b66015;
}

@-webkit-keyframes flashText {
  0% {
    color: rgba(255, 255, 255, 0.5);
  }
  50% {
    color: transparent;
  }
  100% {
    color: #fff;
  }
}

@keyframes flashText {
  0% {
    color: rgba(255, 255, 255, 0.5);
  }
  50% {
    color: transparent;
  }
  100% {
    color: #fff;
  }
}
</style>