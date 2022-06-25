import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'


import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import LogoutView from '@/views/LogoutView.vue'
import ProfileView from '@/views/ProfileView.vue'
import EmotionView from '@/views/EmotionView.vue'
import DetailMovieView from '@/views/DetailMovieView.vue'
import ShuffleView from '@/views/ShuffleView.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
{
  path: '/login',
  name: 'login',
  component: LoginView,
  props: true
},
{
  path: '/signup',
  name: 'signup',
  component: SignupView,
  props: true
},
{
  path: '/logout',
  name: 'logout',
  component: LogoutView
},
{
  path: '/profile/:username',   // profile/sojung 이렇게 나와야함
  name: 'profile',
  component: ProfileView
},
{
  path: '/detailmovie/:movietitle',   
  name: 'detailmovie',
  component: DetailMovieView,
  props: true,
},
{
  path: '/emotion',
  name: 'emotion',
  component: EmotionView
},
{
  path: '/shuffle',
  name: 'shuffle',
  component: ShuffleView
},

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

router.beforeEach((to, from, next) => {
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.getters

  const AuthPages = ['home','logout','profile','detailmovie','emotion','shuffle']

  const isAuthRequired = AuthPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {

    next({ name: 'login' })
  } else {
    next()
  }
})

export default router
