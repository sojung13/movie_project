<template>
  <div>
    <div class="container">
      <div class="row d-flex align-items-center">
        <!-- 왼쪽 영화 검색 영역 -->
        <div class=" col-12 col-md-5 animate__animated animate__fadeInLeft">
          <input class="search__input korean-text" type="text" placeholder="Search" v-model="searchKeyword1" @input="searchMovies(searchKeyword1)" @keyup.enter="goDetail"
          style="font-size:110%;">
          <div>
            <ul class="list-unstyled">
              <li
              v-for="(searchedmovie, idx) in searchedMovies"
              :key="idx"
              class="related-movie"
              > 
              <span @click="pickMovie1(searchedmovie)">{{searchedmovie.title}}</span>
              </li>
            </ul>
          </div>
        </div>
        <br>
        <br>
        <!-- 중간 셔플 버튼 영역 -->
        <div class="col-12 col-md-2 animate__animated animate__fadeIn" style="padding-bottom:2.5%;">
          <button
            @click="goShuffle" class="snip0072 red">SHUFFLE</button>
        </div>
        <br>
        <br>
        <!-- 오른쪽 영화 검색 영역 -->
        <div class=" col-12 col-md-5 animate__animated animate__fadeInRight">
          <input class="search__input korean-text" type="text" placeholder="Search" v-model="searchKeyword2" @input="searchMovies2(searchKeyword2)" @keyup.enter="goDetail"
          style="font-size:110%;">
          <div>
            <ul class="list-unstyled">
              <li
              v-for="(searchedmovie, idx) in searchedMovies2"
              :key="idx"
              class="related-movie"
              >
              <span class="related-movie" @click="pickMovie2(searchedmovie)">{{searchedmovie.title}}</span>
              <!-- <button
              @click="pickMovie2(searchedmovie)">선택</button> -->
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- 오리지날 검색 코드 1 -->
    <!-- <input 
      type="text" placeholder="Search" 
      v-model="searchKeyword1" @input="searchMovies(searchKeyword1)"> -->
    
    <!-- 오리지날 검색 코드 2 -->
    <!-- <input 
      type="text" placeholder="Search" 
      v-model="searchKeyword2" @input="searchMovies2(searchKeyword2)"> -->
    

  </div>
</template>

<script>
import {mapActions, mapGetters, mapMutations} from 'vuex'
import axios from 'axios'
import drf from '@/api/drf'
export default {
  name:'SearchForm',
  data() { 
    return {
      searchKeyword1:'',
      searchKeyword2:'',
      pick: [],

    }
  },
  methods:{
    ...mapActions(['searchMovies','searchMovies2']),
    ...mapMutations(['SET_MOVIE_LIST','SET_DETAIL_MOVIE2','SET_DETAIL_MOVIE']),
    pickMovie1(searchedmovie){
      this.searchKeyword1 = searchedmovie.title
      this.SET_DETAIL_MOVIE([])
      for (let i = 0; i < searchedmovie.genre_ids.length; i++){
        this.pick.push(searchedmovie.genre_ids[i].pk)
      }
    },
    pickMovie2(searchedmovie){
      this.searchKeyword2 = searchedmovie.title
      this.SET_DETAIL_MOVIE2([])
      for (let i = 0; i < searchedmovie.genre_ids.length; i++){
        this.pick.push(searchedmovie.genre_ids[i].pk)
      }
    },
    goShuffle(){
      axios({ 
        url: drf.movies.shuffle(),
        method: 'get',
        headers: this.authHeader,
        params:{
          genres: this.pick.toString(),
        }
      })
        .then(res=>{
          this.SET_MOVIE_LIST(res.data)
          this.this.pick = []
          this.searchKeyword1 = ''
          this.searchKeyword2 = ''
        })
    },
  },
  computed:{
    ...mapGetters(['searchedMovies','searchedMovies2','authHeader']),
  },
  created(){
    this.SET_DETAIL_MOVIE([])
    this.SET_DETAIL_MOVIE2([])
  }
}
</script>

<style lang="scss">
// 서치바 css 템플릿
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
        
        color: #b8b8b8;
        background-color: transparent;
/*         background-image: url(http://mihaeltomic.com/codepen/input-search/ic_search_black_24px.svg); */
 
      // background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3Cpath d='M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z'/%3E%3Cpath d='M0 0h24v24H0z' fill='none'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-size: 18px 18px;
        background-position: 95% center;
        border-radius: 50px;
        border: 1px solid #b8b8b8;
        transition: all 250ms ease-in-out;
        backface-visibility: hidden;
        transform-style: preserve-3d;
        
        &::placeholder {
            color: color(#b8b8b8 a(0.8));
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }
        
        &:hover,
        &:focus {
            padding: 12px 0;
            outline: 0;
            border: 1px solid transparent;
            border-bottom: 1px solid #b8b8b8;
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


</style>

<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/jejumyeongjo.css);
.korean-text {
  font-family: 'Jeju Myeongjo', serif;
  color: rgb(220, 220, 220);
}



/* // 더하기 버튼 css 코드 */
@import url(https://fonts.googleapis.com/css?family=Raleway:400,500);
button.snip0072 {
  font-family: 'Raleway', Arial, sans-serif;
  border: none;
  background-color: #000000;
  border-radius: 5px;
  color: rgba(255, 255, 255, 0.7);
  cursor: pointer;
  padding: 10px 20px;
  display: inline-block;
  margin: 0px 35px;
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




/* 연관검색어 영화 이름 */
.related-movie {
  text-decoration: none;
  color: rgb(185, 185, 180);
  transform: color(rgb(185, 185, 180));
  transition: color 0.5s, font-size 0.3s;
  font-family: 'Jeju Myeongjo', serif;
  font-size: 120%;
  cursor: pointer;
}

.related-movie:hover {
  color: white;
  font-size: 140%;
  transform: color(white);
  transition: color 0.5s, font-size 0.3s;
}
</style>