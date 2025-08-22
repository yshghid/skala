<template>
  <h1> XSS 예제 </h1>
  <input v-model="inputMessage"></input> 
  <button @click="showMessage">눌러</button>
  <div> TEXT 출력 : {{ outputMessage }} <b> {{ }}님</b> </div>
  <div> HTML 출력 : <p v-html="outputMessage"></p>
  </div>
  <a :href="url">Google</a>
</template>

<script setup>
import { ref } from 'vue'

const inputMessage = ref()
const outputMessage = ref()

function showMessage() {
    outputMessage.value = inputMessage.value
}

const url = "https://naver.com"
</script>