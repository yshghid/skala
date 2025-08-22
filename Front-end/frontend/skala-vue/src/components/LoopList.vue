<template>
  <ul>
    <li v-for="(fruit, index) in fruits" :key="index">{{ index }}. {{ fruit }}</li>
  </ul>
  <hr />
  <input v-model="inputFruit" placeholder="과일 입력" />
  <button @click="addFruit">추가</button>
</template>

<script setup>
import { ref } from "vue"

const fruits = ref(['바나나', '수박', '참외', '체리'])
const inputFruit = ref('')

function addFruit() {
  if (inputFruit.value.trim() !== '') {
    fruits.value.push(inputFruit.value)  
    console.log(fruits)  
  }
}
</script>
