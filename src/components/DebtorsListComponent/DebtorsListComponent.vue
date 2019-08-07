<template>
<div>
  <v-content>
    <h1>Debtors</h1>
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
  </v-content>
</div>
</template>

<script src="./DebtorsListComponent.js"></script>

<style src="./DebtorsListComponent.scss" lang="scss"></style>

 