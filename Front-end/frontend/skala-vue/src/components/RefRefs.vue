<template>
  <div>name : {{ user.name }}</div>
  <div>age : {{ user.age }}</div>
  <hr>
  <input v-model="user.name"></input>
  <input v-model="user.age"></input>
  </hr>
</template>

<script setup>
import { reactive, toRef } from "vue";

const user = reactive({
  name: "홍길동",
  age: 25,
})

const name = toRef(user, 'name')
const age = toRef(user, 'age')
</script>