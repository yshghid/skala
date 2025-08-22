<template>
    <button @click="doClick">버튼</button>
    <div> {{ message }}</div>
</template>

<script setup>
import { ref } from 'vue'

const message = ref('')

function doClick(event) {
    console.log(event)
    message.value = "눌렸습니다."
}
</script>