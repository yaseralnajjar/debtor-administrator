<template>
  <v-content>
    <h1>Debtors</h1>

      <v-snackbar v-model="snackbarNotAllowed" :timeout="3000" top color="red" @notAllowed="snackbarNotAllowed = true">
        <span>Mmm, you don't have the permissions to edit this one!</span>
        <v-btn flat color="white" @click="snackbarNotAllowed = false">Close</v-btn>
      </v-snackbar>

      <v-container fluid fill-height>
        <v-layout mt-8 justify-center>
          <v-flex xs12 sm8 md8>
            <v-card>

              <v-data-table :headers="headers" :items="debtors" :items-per-page="10">
                <template slot="items" slot-scope="props">
                  <tr>
                    <td class="text-xs-left">{{ props.item.email }}</td>
                    <td class="text-xs-left">{{ props.item.open_invoices_count }}</td>
                    <td class="text-xs-left">{{ props.item.overdue_invoices_count }}</td>
                    <td class="text-xs-left">{{ props.item.paid_invoices_count }}</td>
                    <td class="text-xs-left">
                      <router-link :to="'/debtors/update/'+ props.item.id">edit</router-link>
                    </td>
                    <td class="text-xs-left">
                      <div @click="deleteDebtor(props.item.id)">delete</div>
                    </td>
                  </tr>
                </template>
              </v-data-table>

            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
      
  </v-content>
  
</template>

<script src="./DebtorsListComponent.js"></script>

<style src="./DebtorsListComponent.scss" lang="scss"></style>

 