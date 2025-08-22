<template>
  <h1 class="bgOrange" :class="color">스타일 클래스 바인딩</h1>
  <div>
    <button @click="changeColor('blue')">파랑</button>
    <button @click="changeColor('red')">빨강</button>
  </div>
</template>

<script setup>
import {ref} from "vue"

const color = ref('');

function changeColor(param) {
    color.value = param
    console.log(color)
    color = "c"
}
</script>

<style>
.red {
    color: red
}

.blue {
    color: blue
}

.bgOrange {
    background-color: orange
}
</style>