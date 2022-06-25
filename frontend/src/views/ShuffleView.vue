<template> 
  <div>
    <br>
    <br>
    <div class="container">
      <div class="row">
        <div class="col-12 col-md-7 animate__animated animate__fadeInDown">
          <div class="wrapper">
            <div class="typing-demo">
              <h2 class="title">HALL OF MERGE</h2>
            </div>
          </div>
          <p class="information">취향이 달라도 너무 다른 너와 나,<br>
          서로의 색깔을 합친 영화를 추천해드립니다</p>
        </div>

        <div class="col-12 col-md-5 animate__animated animate__fadeInDown">
        </div>

      </div>
    </div>
    <br>
    <br>
    <search-form></search-form>
    <movie-list-view
    :movieList="movieList"></movie-list-view>
  </div>
</template>

<script>
import MovieListView from '@/views/MovieListView.vue'
import SearchForm from '@/components/SearchForm'
import {mapGetters} from 'vuex'
export default {
  name:'ShuffleView',
  components:{
		MovieListView,
    SearchForm
    },
  computed:{
    ...mapGetters(['movieList'])
    },
}
</script>

<style>
.title {
  font-family: 'Jeju Myeongjo', serif;
  color: #e5e2d7;
}

.information {
  font-family: 'Jeju Myeongjo', serif;
  color: #e5e2d7;
  font-size: 100%;
}






/* 상단 타이핑 타이틀 효과 */
.wrapper {
  /*This part is important for centering*/
  display: grid;
  place-items: center;
}

.typing-demo {
  width: 9ch;
  animation: typing 2s steps(22), blink .5s step-end infinite alternate;
  white-space: nowrap;
  overflow: hidden;
  border-right: 3px solid;
  font-size: 4em;
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

</style>