<template>
  <v-content>

    <v-container fluid fill-height>
      <v-layout mt-5 justify-center>
        <v-flex xs12 sm8 md6>

          <h1 v-if="isEmpty(user) && !this.$store.getters.isLoggedIn">Hi There!</h1>
          <h1 v-else>Welcome {{ this.$store.getters.name }}!</h1>

          <g-signin-button
                v-if="isEmpty(user) && !this.$store.getters.isLoggedIn"
                :params="googleSignInParams"
                @success="onGoogleSignInSuccess"
                @error="onGoogleSignInError">
                <v-btn class="btn btn-block btn-success">Sign in with Google</v-btn>
          </g-signin-button>
          <v-btn v-else color="#feae25" @click="$router.push('debtors')">Manage Deptors</v-btn>

        </v-flex>
      </v-layout>
    </v-container>

  </v-content>

  
</template>

<script src="./HelloComponent.js"></script>

<style src="./HelloComponent.scss" lang="scss"></style>

 