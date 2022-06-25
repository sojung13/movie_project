<template>
  <div>

    <h1 class="welcome ms-4">LOGIN</h1>
    <!-- 에러메시지 띄우는 란 -->

    <account-error-list v-if="authError" class="d-flex justify-content-center">
    </account-error-list>

    <!-- 사인업 폼 -->
    <div class="login-container d-flex justify-content-center ms-3" id="login-container">
      <form class="form-signin text-center" onsubmit="login(event)" 
            id="form-signin" @submit.prevent="login(credentials)">
        <fieldset id="form-fieldset">
          <div class="d-flex mb-3 justify-content-start logo-container" 
              id="logo-container">
          </div>

          <div class="login-form" id="form-container">
            <div id="form-child">
              <div class="mb-4">
                <div class="form-group form-group-1">
                  <label for="inputEmail" class="sr-only"></label>
                  <input type="text" style="background-color:black; color:white; border:solid 1px rgb(168, 168, 168); margin-bottom:5px;"
                        name="username"
                        id="username"
                        class="form-control" placeholder="USERNAME" v-model="credentials.username" required>
                </div>

                <div class="form-group form-group-2">
                  <label for="inputPassword" class="sr-only"></label>
                  <input type="password" style="background-color:black; color:white; border:solid 1px rgb(168, 168, 168); margin-bottom:5px;"
                        name="password"
                        id="password" 
                        class="form-control" placeholder="PASSWORD" v-model="credentials.password" required>
                </div>
              </div>
              <button class="btn btn-outline-light btn-lg btn-block form-group-3" style="font-weight:600" type="submit">GO!</button>
            </div>
          </div>
        </fieldset>
      </form>
    </div>
  </div>
</template>



<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>


<style scoped lang="scss">
.welcome {
  color: #ecebe8;
  font-family: 'Times New Roman', Times, serif;
}

$border-radius: 4px;
$primary-color: blue;
$primary-color-light: lighten(blue, 15%);

.login-container {
  overflow: auto;
  position: absolute;
  width: 100%;
  height: 100%;
  z-index: 4;
  
}

.form-control {
  font-family: 'Times New Roman', Times, serif;
}

.btn { 
  font-family: 'Times New Roman', Times, serif;
}

.error {
  list-style: none;
  color: white;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(4px);
  }

  to {
    opacity: 1;
    transform: translateY(0px);
  }
}

.form-group-3,
.form-group-2,
.form-group-1 {
  opacity: 0;
  animation: fadeIn ease 1;
  animation-fill-mode: forwards;
  animation-duration: 0.6s;
  animation-delay: 0.3s;
}

.form-group-2 {
  animation-delay: 0.4s;
}

.form-group-3 {
  animation-delay: 0.5s;
}

.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
}

.form-signin .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
  border-width: 0;
  box-shadow: 0 2px 6px 0 hsla(0, 0%, 0%, 0.2);
}

.form-signin .form-control:focus {
  z-index: 2;
}

.loading-spinner {
  opacity: 0;
  margin-top: 2px;
  transform: translateX(5px);
  transition: opacity 0.4s ease, transform 0.2s ease;
  transition-delay: 0.0s;
}

.logging-in .loading-spinner{
  opacity: 1;
  transform: translateX(0px);
  transition-delay: 0s;
}

.logged-in .loading-spinner {
  transition-delay: 0s;
  opacity: 0 !important;
  transform: translateX(-3px) !important;
}

.logo-container {
  position: relative;
  transition: left 0.3s ease;
  left: 0;
  transition-delay: 0.3s;
}

.logged-in .logo-container {
  left: 65px;
  transition-delay: 0.3s;
}

fieldset[disabled] {
  .btn,
  .form-control {
    opacity: 0.7;
    pointer-events: none;
  }
}

.login-form {
  //transition: height 0.3s ease-out;
  transition: all 0.3s ease-out;
  overflow: hidden;
}

.minimized {
  opacity: 0;
  height: 0 !important;
}

.adoxa-credit {
  color: #444;
  padding: 0.3rem 0.75rem;
  border-radius: $border-radius;
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
  position: fixed;
  background-color: white;
  bottom: 4px;
  right: 15px;

  transition: all ease 0.3s;

  &:hover, &:focus {
    text-decoration: none;
    opacity: 1.0;
    padding-bottom: 0.45rem;
    box-shadow: 0px -3px 4px 0 rgba(0, 0, 0, 0.1);
  }
}

@keyframes bubble-in {
  0% {
    opacity: 0;
    transform: rotate(-15deg);
  }

  40% {
    opacity: 0.8;
    transform: rotate(15deg);
  }

  100% {
    opacity: 1;
    transform: rotate(10deg);
  }
}

@keyframes bubble-out {
  0% {
    opacity: 1;
    transform: rotate(10deg);
  }

  100% {
    opacity: 0;
    transform: rotate(20deg);
  }
}
.logged-in #login-success-bubble {
  animation: bubble-in ease 1;
  animation-fill-mode: forwards;
  animation-duration: 0.6s;
}

.fadeout #login-success-bubble {
  opacity: 0;
  animation: bubble-out ease 1;
  animation-fill-mode: forwards;
  animation-duration: 0.2s;
  animation-iteration-count: 1;
}

.fadeout {
  transition: opacity 0.3s ease;
  opacity: 0;
}

.logged-in-thing{
  z-index: 0;
  position: fixed;
  left: 0;
  height: 100%;
  width: 100%;
  top: 0;
  font-size: 128px;
  animation: shake 0.01s infinite;
}
@keyframes shake {
  0% {
    transform: translateX(-5px);
  }
  30% {
    transform: translateX(5px) translateY(4px) rotate(12deg);
  }
  50% {
    transform: translateX(5px) rotate(-20deg);
  }
  60% {
    transform: translateX(5px) translateY(-4px);
  }
  100% {
    transform: translateX(-5px);
  }
}


#login-success-bubble {
  opacity: 0;
  transform-origin: 4px 40px;

  position: absolute;
  left: 132px;
  top: -47px;
  box-shadow: 0px 3px 3px 0 rgba(0, 0, 0, 0.1);
  padding: 0.25rem 0.5rem;
  background-color: white;
  border-radius: $border-radius;
  z-index: 2;

  .arrow {
    z-index: -1;
    position: absolute;
    top: 20px;
    left: 8px;
    width: 15px;
    height: 15px;
    border-radius: 4px;
    background-color: white;
    transform: rotate(45deg);
  }
}

.alert-danger {
  opacity: 0;
  height: 0;
  transition: all 0.2s ease;
  margin-bottom: 0;
  padding-bottom: 0;
  padding-top: 0;

  &.show-alert {
    height: 48px;
    opacity: 1;
    margin-bottom: 1rem;
    padding-bottom: 12px;
    padding-top: 12px;
  }
}


.alert {
  text-align:left;
  box-shadow: 0px 2px 2px 0px rgba(0, 0, 0, 0.2);
}

.alert.alert-danger {
  border-width : 0px;
  border-left: 3px solid red;
}


// Logo letter animations and stuff
.letter-container {
  position: relative;
  width: 165px;
  height: 34px;
}

@keyframes letter-slide {
  from {
    opacity: 0;
    transform: translateX(-5px) translateY(0px) rotate(9deg);
  }

  60% {
    opacity: 1;
    transform: translateX(2px) translateY(-3px) rotate(0deg);
  }

  100% {
    opacity: 1;
    transform: translateX(0px) translateY(0px);
  }
}

@keyframes elastic-up {
  0% {
    transform: translateY(0px) rotate(0deg);
  }

  15% {
    transform: translateY(-20px) rotate(3deg);
  }

  100% {
    transform: translateY(0px) rotate(0deg);
  }
}

@keyframes elastic-down {
  0% {
    transform: translateY(0px) rotate(0deg);
  }

  15% {
    transform: translateY(20px) rotate(-3deg);
  }

  100% {
    transform: translateY(0px) rotate(0deg);
  }
}

@keyframes fade-out {
  from {
    opacity: 1;
    transform: translateY(0);
  }

  20% {
    transform: translateY(-4px);
  }

  to {
    opacity: 0;
    transform: translateY(10px);
  }
}

.letter {
  position: absolute;
}

.slide-in {
  .letter {
    opacity: 0;
    animation: letter-slide 0.5s forwards;
  }

  $delay-start: 0.1s;
  $delay-increase: 0.1s;

  .letter-1 {
    animation-delay: $delay-start + $delay-increase * 1;
  }

  .letter-2 {
    animation-delay: $delay-start + $delay-increase * 2;
  }

  .letter-3 {
    animation-delay: $delay-start + $delay-increase * 3;
  }

  .letter-4 {
    animation-delay: $delay-start + $delay-increase * 4;
  }

  .letter-5 {
    animation-delay: $delay-start + $delay-increase * 5;
  }
}

.letter-1 {
  left: 0;
  top: 0px;
}

.letter-2 {
  top: -4px;
  left: 35px;
}

.letter-3 {
  top: 0px;
  left: 70px;
}

.letter-4 {
  top: 0px;
  left: 97px;
}

.letter-5 {
  top: 0px;
  left: 124px;
}

.hiddenCompletely {
  opacity: 0 !important;
  animation: none;
}

#logo.fade-out {
  $delay-start: 0s;
  $delay-increase: 0.05s;

  .letter {
    opacity: 1;
    animation: fade-out 0.4s forwards;
  }

  .letter-1 {
    animation-delay: $delay-start + $delay-increase * 1;
  }

  .letter-2 {
    animation-delay: $delay-start + $delay-increase * 2;
  }

  .letter-3 {
    animation-delay: $delay-start + $delay-increase * 3;
  }

  .letter-4 {
    animation-delay: $delay-start + $delay-increase * 4;
  }

  .letter-5 {
    animation-delay: $delay-start + $delay-increase * 5;
  }
}

.elastic-up .letter {
  animation: elastic-up 0.5s forwards;
}

.elastic-down .letter {
  animation: elastic-down 0.5s forwards;
}

.elastic-down,
.elastic-up {
  $delay-start: 0s;
  $delay-increase: 0.01s;

  .letter-1 {
    animation-delay: $delay-start + $delay-increase * 0;
  }

  .letter-2 {
    animation-delay: $delay-start + $delay-increase * 1;
  }

  .letter-3 {
    animation-delay: $delay-start + $delay-increase * 2;
  }

  .letter-4 {
    animation-delay: $delay-start + $delay-increase * 3;
  }

  .letter-5 {
    animation-delay: $delay-start + $delay-increase * 4;
  }
}


</style>
