<template>
  <div> 

    <div class="wrapper container">
      <div class="typing-demo row">
        <div class="col-12">HALL OF MOVIE</div>
      </div>
    </div>
		<br>
		<div>
			<input class="search__input search-movie-input" type="text" placeholder="Search" v-model="searchKeyword" @input="searchMovies(searchKeyword)" @keyup.enter="goDetail"
      >
		</div>
		<br>

    <div class="related-movie-area">
      <ul class="list-unstyled list-group" >
          <li
          v-for="(searchedmovie, idx) in searchedMovies"
          :key="idx"
          class="related-movie-title "
          > 
          <router-link 
          :to="{name:'detailmovie',
                params: {movietitle:searchedmovie.title} }" class="related-movie " >
            {{searchedmovie.title}}</router-link>
          </li>
      </ul>
    </div>
    <br>
    <br>
    <genre-year-form></genre-year-form>

		
		<movie-list-view
		:movieList="movieList"></movie-list-view>
    <br>
    <br>
    <br>
    <br>
  </div>
</template>




<script>
import {mapActions, mapGetters} from 'vuex'
import router from '@/router'
import MovieListView from '@/views/MovieListView.vue'
import GenreYearForm from '@/components/GenreYearForm'



export default {
	components:{
		MovieListView,
    GenreYearForm
	},
  data() { 
    return {
      searchKeyword:'',
    }
  },
  computed:{
    ...mapGetters(['searchedMovies','authHeader','movieList'])
  },
  methods:{
    ...mapActions(['searchMovies','getPopular']),
    goDetail(){
      router.push({ name: 'detailmovie', params: {movietitle:this.searchedMovies[0].title}})
    },
  },
	// 홈에 오면 인기영화 띄워 줘야함
	created(){
		this.getPopular()
	}
}
</script>

<style scoped lang="scss">
@import url(//fonts.googleapis.com/earlyaccess/jejumyeongjo.css);

// .related-movie-area {
//   height: 100px;
// }

.related-movie {
  text-decoration: none;
  color: rgb(185, 185, 180);
  transform: color(rgb(185, 185, 180));
  transition: color 0.5s, font-size 0.3s;
  font-family: 'Jeju Myeongjo', serif;
  font-size: 140%;
}

.related-movie:hover {
  color: white;
  font-size: 160%;
  transform: color(white);
  transition: color 0.5s, font-size 0.3s;
}

.related-movie-title {
  width: 100%;
  height: 20px;
}





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
        
        color: #575756;
        background-color: transparent;
/*         background-image: url(http://mihaeltomic.com/codepen/input-search/ic_search_black_24px.svg); */
 
      background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3Cpath d='M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z'/%3E%3Cpath d='M0 0h24v24H0z' fill='none'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-size: 18px 18px;
        background-position: 95% center;
        border-radius: 50px;
        border: 1px solid #575756;
        transition: all 250ms ease-in-out;
        backface-visibility: hidden;
        transform-style: preserve-3d;
        
        &::placeholder {
            color: color(#575756 a(0.8));
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }
        
        &:hover,
        &:focus {
            padding: 12px 0;
            outline: 0;
            border: 1px solid transparent;
            border-bottom: 1px solid #575756;
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





// 상단 타이핑 타이틀 효과
.wrapper {
  /*This part is important for centering*/
  display: grid;
  place-items: center;
}

.typing-demo {
  width: 16ch;
  animation: typing 2s steps(22), blink .5s step-end infinite alternate;
  white-space: nowrap;
  overflow: hidden;
  border-right: 3px solid;
  font-size: 3em;
  color: #ecebe8;
  font-family: 'Times New Roman', Times, serif;
}

@keyframes typing {
  from {
    width: 0
  }
}
    
@keyframes blink {
  50% {
    border-color: transparent
  }
}



.search-movie-input {
  font-family: 'Jeju Myeongjo', serif;
  color:white;
  font-size: 150%;
}
  </style>

