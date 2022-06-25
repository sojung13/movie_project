<template>
  <div>
    <br>


<figure class="snip1577 movie-poster-box poster" @click="goDetail">
  <img :src="POSTER_URL" alt=""
       class="poster">
  <figcaption>
    <h3 class="korean-text">{{ movie.title}}</h3>
    <h4>view detail</h4>
  </figcaption>
  <a href="#"></a>
</figure>


    <!-- <div class="movie-poster-box ">
      <img :src="POSTER_URL" alt=""
      @click="goDetail" class="poster">
      <h1 class="poster-title">{{ movie.title}}</h1> 
    </div> -->

  </div>
</template>

<script>
import router from '@/router'
export default {
  name:'MovieListItem',
  props: {
    movie: Object,
  },
  computed:{
    POSTER_URL() {
    return "https://image.tmdb.org/t/p/original" + this.movie.poster_path
    },
  },
  methods:{
    goDetail(){
      router.push({ name: 'detailmovie', params: {movietitle:this.movie.title}})
    }
  }
}
</script>

<style>
@import url(//fonts.googleapis.com/earlyaccess/jejumyeongjo.css);
img {
  cursor: pointer;;
}

.movie-poster-box {
  position: relative;
}
.poster {
  transition: scale 0.4s, transform 0.4s, filter 0.3s;
  width: 100%;
  /* opacity: 80%; */
  /* filter: grayscale(100%); */
}
.poster:hover {
  /* opacity: 100%; */
  transform: scale(1.08);
  /* filter: grayscale(0%); */
  transition: filter 0.4s, transform 0.4s;
}

.korean-text{
  font-family: 'Jeju Myeongjo', serif;
}





/* 무비 포스터카드 css */
@import url(https://fonts.googleapis.com/css?family=Montserrat:200);
.snip1577 {
  font-family: 'Montserrat', Arial, sans-serif;
  position: relative;
  display: inline-block;
  overflow: hidden;
  margin: 10px;
  /* min-width: 230px;
  max-width: 315px; */
  width: 100%;
  color: #fff;
  text-align: left;
  font-size: 16px;
  background: #000;
}

.snip1577 *,
.snip1577:before,
.snip1577:after {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}

.snip1577 img {
  max-width: 100%;
  backface-visibility: hidden;
  vertical-align: top;
}

.snip1577:before,
.snip1577:after {
  position: absolute;
  top: 20px;
  right: 20px;
  content: '';
  background-color: #fff;
  z-index: 1;
  opacity: 0;
}

.snip1577:before {
  width: 0;
  height: 1px;
}

.snip1577:after {
  height: 0;
  width: 1px;
}

.snip1577 figcaption {
  position: absolute;
  left: 0;
  bottom: 0;
  padding: 15px 20px;
}

.snip1577 h3,
.snip1577 h4 {
  margin: 0;
  font-size: 1.1em;
  font-weight: normal;
  opacity: 0;
}

.snip1577 h4 {
  font-size: .8em;
  text-transform: uppercase;
}

.snip1577 a {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 1;
}

.snip1577:hover img,
.snip1577.hover img {
  zoom: 1;
  filter: alpha(opacity=20);
  -webkit-opacity: 0.1;
  opacity: 0.2;
}

.snip1577:hover:before,
.snip1577.hover:before,
.snip1577:hover:after,
.snip1577.hover:after {
  opacity: 1;
  -webkit-transition-delay: 0.25s;
  transition-delay: 0.25s;
}

.snip1577:hover:before,
.snip1577.hover:before {
  width: 40px;
}

.snip1577:hover:after,
.snip1577.hover:after {
  height: 40px;
}

.snip1577:hover h3,
.snip1577.hover h3,
.snip1577:hover h4,
.snip1577.hover h4 {
  opacity: 1;
}

.snip1577:hover h3,
.snip1577.hover h3 {
  -webkit-transition-delay: 0.3s;
  transition-delay: 0.2s;
}

.snip1577:hover h4,
.snip1577.hover h4 {
  -webkit-transition-delay: 0.2s;
  transition-delay: 0.25s;
}

</style>