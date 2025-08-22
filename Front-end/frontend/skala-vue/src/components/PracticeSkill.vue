<template>
  <div>
    <h2>🏃 기술 연습</h2>
    <button @click="emit('practice', 1)">걷기 (-1kg)</button>
    <button @click="emit('practice', 2)">달리기 (-2kg)</button>
  </div>
</template>

<script setup>
const emit = defineEmits(['practice'])
</script>
