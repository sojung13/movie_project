<template>
  <div>
    <br>
    <nav class="navbar navbar-expand-lg navbar-dark ">
      <div class="container-fluid">

        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse justify-content-between" id="navbarNavDropdown">
          <ul class="navbar-nav">
            <li class="nav-item">
              <div @click="getPopular()"  class="snip1241">
                <router-link to="/">HOME</router-link>
              </div>
            </li>
            <li class="nav-item">
              <div class="snip1241" @click="SET_MOVIE_LIST([])">
              <router-link to="/emotion">EMOTION</router-link> 
              </div>
            </li>
            <li class="nav-item">
              <div @click="SET_MOVIE_LIST([])"  class="snip1241">
                  <router-link to="/shuffle">SHUFFLE</router-link> 
              </div>
            </li>
          </ul>


         <ul class="navbar-nav" v-if="!isLoggedIn">
            <li class="nav-item snip1241">
              <router-link to="/login">LOGIN</router-link>
            </li>
            <li class="nav-item snip1241">
              <router-link to="/signup">SIGNUP</router-link>
            </li>
         </ul>

         <ul class="navbar-nav" v-if="isLoggedIn">
          <li
          @click="fetchProfile(currentUser.username)" class="nav-item snip1241">
            <router-link 
            :to="{ name: 'profile', params: { username:currentUser.username } }">PROFILE</router-link>
          </li>
          <li class="nav-item snip1241">
            <router-link to="/logout">LOGOUT</router-link>
          </li>
        </ul>


        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import { mapGetters, mapActions,mapMutations } from 'vuex'
import router from '@/router'
  export default {
    name: 'NavBarView',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
    methods:{
       ...mapActions(['fetchProfile','getPopular']),
       ...mapMutations(['SET_MOVIE_LIST']),
       goProfile(){
         //  console.log(this.currentUser.username)
          router.go({ name: 'profile', params: { username:this.currentUser.username } })
       }
    }
  }
</script>

<style scoped>
.menu-white {
  color: white;
}



@import url(https://fonts.googleapis.com/css?family=Raleway:400,500);
.snip1241 {
  font-family: 'Raleway', Arial, sans-serif;
  text-align: center;
  text-transform: uppercase;
  font-weight: 500;
  letter-spacing: 1px;
}
.snip1241 * {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: all 0.35s ease;
  transition: all 0.35s ease;
}
.snip1241 li {
  display: inline-block;
  list-style: outside none none;
  margin: 0.5em 1em;
  padding: 0;
}
.snip1241 a {
  padding: 0.5em 0.8em;
  color: rgba(255, 255, 255, 0.5);
  position: relative;
  text-decoration: none;
}
.snip1241 a:before,
.snip1241 a:after {
  height: 14px;
  width: 14px;
  position: absolute;
  content: '';
  -webkit-transition: all 0.35s ease;
  transition: all 0.35s ease;
  opacity: 0;
}
.snip1241 a:before {
  right: 0;
  top: 0;
  border-right: 3px solid #ffffff;
  border-top: 3px solid #ffffff;
  -webkit-transform: translate(-100%, 50%);
  transform: translate(-100%, 50%);
}
.snip1241 a:after {
  left: 0;
  bottom: 0;
  border-left: 3px solid #ffffff;
  border-bottom: 3px solid #ffffff;
  -webkit-transform: translate(100%, -50%);
  transform: translate(100%, -50%);
}
.snip1241 a:hover,
.snip1241 .current a {
  color: #ffffff;
}
.snip1241 a:hover:before,
.snip1241 .current a:before,
.snip1241 a:hover:after,
.snip1241 .current a:after {
  -webkit-transform: translate(0%, 0%);
  transform: translate(0%, 0%);
  opacity: 1;
}


/* 여기서부터 다른 css */




</style>