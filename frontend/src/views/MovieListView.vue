<template>
  <div>
    <div class="container">
      <div class="row">
        <movie-list-item
          v-for="(movie, idx) in movieList"
          :key="idx"
          :movie="movie"
          class="movie-poster col-sm-6 col-md-4 col-lg-3 col-xl-2"
          ></movie-list-item>
      </div>
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'
export default {
  name: 'MovieListView',
  components:{
    MovieListItem
  },
  props: {
    movieList: Array,
  },
}
</script>

<style lang="scss">
h1{
	font-size: 3em;
}

.row {
  width: 100%;
  overflow: hidden;
}

.movie-poster {
  overflow: hidden;
}

</style>