<template>
  <div>
    <div class="accordion" id="accordionExample" style="outline: none; border:none; color:black; background-color:black;">
      <div class="accordion-item" style="outline: none; border:none; color:black; background-color:black;">
        <h2 class="accordion-header" id="headingOne" style="outline: none; border:none; color:black; background-color:black;">
          <button class="accordion-button radio-background position-relative" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne" style="outline: none; color:black; background-color:black;">
            <h3 class="korean-text position-absolute search-title col-12 d-flex justify-content-center">DETAIL SEARCH</h3> 
          </button>
        </h2>
        <div id="collapseOne" class="accordion-collapse collapse radio-background" aria-labelledby="headingOne" data-bs-parent="#accordionExample" style="outline: none; color:black; background-color:black;">
          <div class="accordion-body" style="outline: none;">
            <form 
            @submit.prevent=""
            action="">
            <div class="conrtainer">
              <div class="row d-flex justify-content-center ms-3 ">
                <div class="d-flex flex-column col col-4 p-2 col-md-3 col-xl-1 animate__animated animate__fadeInLeft colorgroup-1">
                  <div class="d-flex">
                    <input type="radio" name="color" id="action" value="28" v-model="genre"/>
                    <label for="action"><span class="action"></span></label>
                    <p class="radio-text">액션</p> 
                  </div>

                  <div class="d-flex">
                    <input type="radio" name="color" id="adventure" value="12" v-model="genre"/>
                    <label for="adventure"><span class="adventure"></span></label>
                    <p class="radio-text">모험</p>
                  </div>
                </div>

                <div class="d-flex flex-column col col-4 p-2 col-md-3 col-xl-1 animate__animated animate__fadeInRight colorgroup-2">
                  <div class="d-flex">
                    <input type="radio" name="color" id="animation" value="16" v-model="genre"/>
                    <label for="animation"><span class="animation"></span></label>
                    <p class="radio-text" style="font-size:90%;">애니메이션</p>
                  </div>
                  <div class="d-flex">
                    <input type="radio" name="color" id="comedy" value="35" v-model="genre"/>
                    <label for="comedy"><span class="comedy"></span></label>
                    <p class="radio-text">코미디</p>
                  </div>
                </div>

                <div class="d-flex flex-column col col-4 p-2 col-md-3 col-xl-1 animate__animated animate__fadeInLeft colorgroup-3">
                  <div class="d-flex">
                    <input type="radio" name="color" id="crime" value="80" v-model="genre"/>
                    <label for="crime"><span class="crime"></span></label>
                    <p class="radio-text">범죄</p>
                  </div>

                  <div class="d-flex">
                    <input type="radio" name="color" id="documentary" value="99" v-model="genre"/>
                    <label for="documentary"><span class="documentary"></span></label>
                    <p class="radio-text" style="font-size:90%;">다큐멘터리</p>
                  </div>
                </div>

                <div class="d-flex flex-column col col-4 p-2 col-md-3 col-xl-1 animate__animated animate__fadeInRight colorgroup-4">
                  <div class="d-flex">
                    <input type="radio" name="color" id="drama" value="18" v-model="genre"/>
                    <label for="drama"><span class="drama"></span></label>
                    <p class="radio-text">드라마</p>
                  </div>

                  <div class="d-flex">
                    <input type="radio" name="color" id=" family" value="10751" v-model="genre"/>
                    <label for=" family"><span class="family"></span></label>
                    <p class="radio-text">가족</p>
                  </div>
                </div>

                <div class="d-flex flex-column col col-4 p-2 col-md-3 col-xl-1 animate__animated animate__fadeInLeft colorgroup-5">
                  <div class="d-flex">
                    <input type="radio" name="color" id="fantasy" value="14" v-model="genre"/>
                    <label for="fantasy"><span class="fantasy"></span></label>
                    <p class="radio-text">판타지</p>
                  </div>

                  
                  <div class="d-flex">
                    <input type="radio" name="color" id="horror" value="27" v-model="genre"/>
                    <label for="horror"><span class="horror"></span></label>
                    <p class="radio-text">공포</p>
                  </div>

                </div>

                <div class="d-flex flex-column col col-4 p-2 col-md-3 col-xl-1 animate__animated animate__fadeInRight colorgroup-6">
                  <div class="d-flex">
                    <input type="radio" name="color" id="music" value="10402" v-model="genre"/>
                    <label for="music"><span class="music"></span></label>
                    <p class="radio-text">음악</p>
                  </div>

                  <div class="d-flex">
                    <input type="radio" name="color" id="mystery" value="9648" v-model="genre"/>
                    <label for="mystery"><span class="mystery"></span></label>
                    <p class="radio-text" style="font-size:90%;">미스터리</p>
                  </div>
                </div>

                <div class="d-flex flex-column col col-4 p-2 col-md-3 col-xl-1 animate__animated animate__fadeInLeft colorgroup-7">
                  <div class="d-flex">
                    <input type="radio" name="color" id="romance" value="10749" v-model="genre"/>
                    <label for="romance"><span class="romance"></span></label>
                    <p class="radio-text">로맨스</p>
                  </div>

                  <div class="d-flex">
                    <input type="radio" name="color" id="SF" value="878" v-model="genre"/>
                    <label for="SF"><span class="SF"></span></label>
                    <p class="radio-text">SF</p>
                  </div>
                </div>

                <div class="d-flex flex-column col col-4 p-2 col-md-3 col-xl-1 animate__animated animate__fadeInRight colorgroup-8">
                  <div class="d-flex">
                    <input type="radio" name="color" id="TV" value="10770" v-model="genre"/>
                    <label for="TV"><span class="TV"></span></label>
                    <p class="radio-text" style="font-size:90%;">TV 영화</p>
                  </div>

                  <div class="d-flex">
                    <input type="radio" name="color" id="thriller" value="53" v-model="genre"/>
                    <label for="thriller"><span class="thriller"></span></label>
                    <p class="radio-text">스릴러</p>
                  </div>
                </div>

                <div class="d-flex flex-column col col-4 p-2 col-md-3 col-xl-1 animate__animated animate__fadeInLeft colorgroup-9">
                  <div class="d-flex">
                    <input type="radio" name="color" id="war" value="10752" v-model="genre"/>
                    <label for="war"><span class="war"></span></label>
                    <p class="radio-text">전쟁</p>
                  </div>

                  <div class="d-flex">
                    <input type="radio" name="color" id="west" value="37" v-model="genre"/>
                    <label for="west"><span class="west"></span></label>
                    <p class="radio-text">서부</p>
                  </div>

                  <div class="d-flex">
                    <input type="radio" name="color" id="history"  value="36" v-model="genre"/>
                    <label for="history"><span class="history"></span></label>
                    <p class="radio-text">역사</p>
                  </div>

                </div>
              </div>
            </div>

            <p class="radio-text" style="">1980~2022년 사이 개봉된 영화를 검색해보세요</p>  
            <div class="d-flex justify-content-center">
              <div>
                <input type="number" min="1980" max="2022" step="1" value="2022" v-model="year" class="year-input">
                <button @click="searchMovie" class="snip0072 red">SEARCH</button>

              </div>
            </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import drf from '@/api/drf'
import {mapGetters,mapMutations} from 'vuex'
export default {
  name:'GenreYearForm',
  data(){
    return {
      genre: '',
      year: 0
    }
  },
  computed:{
    ...mapGetters(['authHeader'])
  },
  methods:{
    ...mapMutations(['SET_MOVIE_LIST']),
    searchMovie(){
      axios({ 
      url: drf.movies.genre(),
      method: 'get',
      headers: this.authHeader,
      params:{
        genres: this.genre,
        year: this.year
      },
      })
        .then(res => {
          this.SET_MOVIE_LIST(res.data)
        })
    },
  }
}
</script>

<style scoped lang="scss">
.radio-background {
  background-color: black;
}

.korean-text {
    font-family: 'Jeju Myeongjo', serif;
}

.search-title {
  color: white;
  transform: scale(1);
  transition: transform 0.4s;
}

.search-title:hover {
  transform: scale(1.2);
  transition: transform 0.4s;
}





@import url(//fonts.googleapis.com/earlyaccess/jejumyeongjo.css);

.radio-text {
  color: rgb(218, 218, 218);
  font-family: 'Jeju Myeongjo', serif;
}

@import url(https://fonts.googleapis.com/css?family=Lato:400,300);

$colors: (
  action: #fda57f,
  adventure: #f98e6e,
  animation: #f98e6e,
  comedy: #e7725b,
  crime: #e7725b,
  documentary: #c8655c,
  drama: #c8655c,
  family: #bb5b5b,
  fantasy: #bb5b5b,
  horror: #9c4053,
  music: #9c4053,
  mystery: #7d3451,
  romance: #7d3451,
  SF: #6e2e53,
  TV: #6e2e53,
  thriller: #672a4f,
  war: #672a4f,
  west: #4f2246,
  history: #4f2246,
);

* {
  box-sizing: border-box;
}

body {
  // position: absolute;
  position: relative;
  top: 35%;
  left: 35%;
  transform: translate(-35%, -35%);
  font-family: 'lato';
  color: #333;
}

input[type="radio"] {
  display: none;
  
  position: absolute;

  &:checked + label {
    span { transform: scale(1.25); }
    @each $name, $value in $colors {
      .#{$name} {
        border: 2px solid white;
      }
    } // !@each
  } // !&:checked + label
}

label {
  // display: inline-block;
  width: 25px;
  height: 25px;
  margin-right: 10px;
  cursor: pointer;
  &:hover {
    span { 
      transform: scale(1.25); 
    }
  }
  span {
    display: block;
    width: 100%;
    height: 100%;
    border-radius: 5px;
    transition: transform .2s ease-in-out;
    @each $name, $value in $colors {
      &.#{$name} {
        background: $value;
      }
    }
  }
}





// 색깔 나타나는 모션 시간 조정
.colorgroup-1 {
  animation-duration: 1.1s;
}

.colorgroup-2 {
  animation-duration: 1.2s;
}

.colorgroup-3 {
  animation-duration: 1.3s;
}

.colorgroup-4 {
  animation-duration: 1.4s;
}

.colorgroup-5 {
  animation-duration: 1.5s;
}

.colorgroup-6 {
  animation-duration: 1.6s;
}

.colorgroup7  {
  animation-duration: 1.7s;
}

.colorgroup-8 {
  animation-duration: 1.8s;
}

.colorgroup-9 {
  animation-duration: 1.9s;
}





// 서치 버튼 css
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






input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
}


.year-input {
  position: relative;
  width: 140px;
  height: 40px;
  border-radius: 5px;
  border: 2px solid rgba(255,255,255,.2);
  transition: 0.5s;
  background-color: black;
  color: white;
}

.year-input:hover {
  width: 120px;
  border: 2px solid rgba(255,255,255,1);
  background-color: black;
}


</style>