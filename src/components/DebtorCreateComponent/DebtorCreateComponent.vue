<template>
    <v-content>

      <v-snackbar v-model="snackbarCreateFailed" :timeout="3000" top color="red">
        <span>Ooops, Creating Debtor Failed!</span>
        <v-btn flat color="white" @click="snackbarGetListFailed = false">Close</v-btn>
      </v-snackbar>

      <v-snackbar v-model="snackbarCreated" :timeout="3000" top color="green">
        <span>Debtor Added Successfully!</span>
        <v-btn flat color="white" @click="snackbarCreated = false">Close</v-btn>
      </v-snackbar>

      <v-container fluid fill-height>
        <v-layout mt-5 justify-center>
          <v-flex xs12 sm8 md6>
            <h1>Create Debtor</h1>

              <v-layout row wrap justify-center align-center>
              <v-flex xs12 md6 class="mt-5 mb-1">
                <v-form ref="form" lazy-validation>
                  <v-text-field label="First Name" autocomplete="on" :rules="nameRules" required type="text" v-model="firstName"></v-text-field>
                  <v-text-field label="Last Name" autocomplete="on" :rules="nameRules" required type="text" v-model="lastName"></v-text-field>
                  <v-text-field label="E-mail" autocomplete="on" :rules="emailRules" required type="email" v-model="email"></v-text-field>
                  <v-text-field label="IBAN" autocomplete="on" :rules="ibanRules" required type="text" v-model="iban"></v-text-field>
                </v-form>
              </v-flex>
              </v-layout>

              <v-layout justify-center>
                <v-flex xs12 md6 class="text-xs-right">
                  <v-btn color="#feae25" :disabled="!valid" large class="elevation-0" @click="submit">Submit</v-btn>
                </v-flex>
              </v-layout>
              
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
</template>

<script src="./DebtorCreateComponent.js"></script>

<style src="./DebtorCreateComponent.scss" lang="scss"></style>

 