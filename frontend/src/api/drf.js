// const HOST = 'https://hallofmovie.click/api/v1/'
const HOST = 'http://127.0.0.1:8000/api/v1/'


const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const REVIEWS = 'reviews/'
const VOTES ='votes/'
export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
    follow: username => HOST + ACCOUNTS + 'follow/' + username,
  },
  movies: {
    search:() => HOST + MOVIES + 'search',
    choice:movietitle => HOST + MOVIES + movietitle,
    popular:() => HOST + MOVIES + 'popular/movie',
    emotion:() => HOST + MOVIES + 'random/emotion',
    like:movieId => HOST + MOVIES + 'like/' + movieId,
    vote:payload => HOST + VOTES + payload['movieTitle'],
    reVote:payload => HOST + VOTES + 're/' + payload['movieTitle']+'/'+payload['voteId'],
    genre:() => HOST + MOVIES + 'search/genre/year',
    shuffle:() => HOST + MOVIES + 'double/shuffle'
  },
  reviews:{
    commentC:reviewId => HOST + REVIEWS + 'comment_list/' + reviewId,
    commentUd:commentPk => HOST + REVIEWS + 'comment/' + commentPk,
    reviewC:movieId => HOST + REVIEWS + 'review_list/' + movieId,
    reviewUd:reviewId =>  HOST + REVIEWS + reviewId
  }
}
