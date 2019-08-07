<template>
  <v-content>
    <h1>Hi There!</h1>
    <div>
      <g-signin-button
            v-if="isEmpty(user) && !this.$store.getters.isLoggedIn"
            :params="googleSignInParams"
            @success="onGoogleSignInSuccess"
            @error="onGoogleSignInError">
            <v-btn class="btn btn-block btn-success">
              Sign in with Google
            </v-btn>
          </g-signin-button>
          <div v-else>
              <v-btn @click="$router.push('debtors')">Manage Deptors</v-btn>
          </div>
    </div>
  </v-content>

  
</template>

<script src="./HelloComponent.js"></script>

<style src="./HelloComponent.scss" lang="scss"></style>

 