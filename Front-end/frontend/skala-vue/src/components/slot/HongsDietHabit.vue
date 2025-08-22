<template>
  <h1> {{ title }}</h1>
  <button v-for="(habit, index) in habits" :key="index" @click="changeWeight(habit.weight)">
    {{ habit.name }} ({{ habit.weight > 0 ? "+" + habit.weight : habit.weight }}kg)
  </button>
</template>
<script setup>
const props = defineProps({
  title: String,
  habits: Array // { name: '햄버거' , weight: 1}
})
const emit = defineEmits(['weightChanged'])
function changeWeight(weight) {
  console.log(weight)
  emit('weightChanged', weight)
}
</script>