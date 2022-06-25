import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'
// import Vue from 'vue'
 
export default {
  state:{
    // 연관검색어
    searchedMovies:[],
    searchedMovies2:[],

    // 디테일무비
    choicedMovie:{},
    // 무비리스트
    movieList:[],
  },
  
  getters:{
    searchedMovies: state => state.searchedMovies,
    searchedMovies2: state => state.searchedMovies2,
    choicedMovie: state => state.choicedMovie,
    movieList: state => state.movieList
  },
  mutations:{
    SET_DETAIL_MOVIE(state, results){
      const searchedMovies = []
      for (const movie of results){
        searchedMovies.push(movie)
      }
      state.searchedMovies = searchedMovies
    },
    SET_DETAIL_MOVIE2(state, results){
      const searchedMovies = []
      for (const movie of results){
        searchedMovies.push(movie)
      }
      state.searchedMovies2 = searchedMovies
    },
    CHOICE_MOVIE(state, movie){
      state.choicedMovie = movie
    },
    SET_MOVIE_LIST(state, movieList){
      state.movieList = movieList
    },
  },
  actions:{
    searchMovies({commit, getters}, keyword) {
      axios({
        url: drf.movies.search(),
        method: 'get',
        headers: getters.authHeader,
        data:{},
        params:{
          search_keyword:keyword
        }
      })
        .then(res => {
          if (res.status === 200){
            commit('SET_DETAIL_MOVIE', res.data)
          }
        })
    },
    searchMovies2({commit, getters}, keyword) {
      axios({
        url: drf.movies.search(),
        method: 'get',
        headers: getters.authHeader,
        data:{},
        params:{
          search_keyword:keyword
        }
      })
        .then(res => {
          if (res.status === 200){
            commit('SET_DETAIL_MOVIE2', res.data)
          }
        })
    },
    choiceMovie({getters,commit}, movieTile){
      axios({
        url: drf.movies.choice(movieTile),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res=>{
          commit('CHOICE_MOVIE',res.data)
          router.go({ name: 'detailmovie', params:{movietitle:this.choicedMovie.title} })
        })
    },
    getPopular({getters,commit}){
			axios({
				url:drf.movies.popular(),
				method:'get',
				headers: getters.authHeader,
			})
        .then(res =>{
          commit('SET_MOVIE_LIST', res.data)
        })
    },
    getEmotion({getters,commit},emo){
      axios({
				url:drf.movies.emotion(),
				method:'get',
				headers: getters.authHeader,
        params:{
          emotion: emo
        }
			})
        .then(res =>{
          commit('SET_MOVIE_LIST', res.data)
        })
    },
    likeMovie({getters,commit},movieId){
      axios({
				url:drf.movies.like(movieId),
				method:'post',
				headers: getters.authHeader,
			})
        .then(res=>{
          commit('CHOICE_MOVIE',res.data)
        })
    },
    vote({getters,commit},payload){
      
      axios({
				url:drf.movies.vote(payload),
				method:'post',
				headers: getters.authHeader,
        data: {
          user: getters.currentUser.pk,
          rate:payload['score'],
          movie:payload['movie']
        }
			})
        .then(res=>{
          commit('CHOICE_MOVIE',res.data)
        })
    },
    reVote({getters,commit},payload){
      
      axios({
				url:drf.movies.reVote(payload),
				method:'put',
				headers: getters.authHeader,
        data: {
          user: getters.currentUser.pk,
          rate:payload['score'],
          movie:payload['movie'],
        }
			})
        .then(res=>{
          commit('CHOICE_MOVIE',res.data)
        })
    },
    deVote({getters,commit},payload){
      console.log(payload)
      
      axios({
				url:drf.movies.reVote(payload),
				method:'delete',
				headers: getters.authHeader,
        data: {
          user: getters.currentUser.pk,
          rate:payload['score'],
          movie:payload['movie'],
        }
			})
        .then(res=>{
          commit('CHOICE_MOVIE',res.data)
        })
    },

  }
}
