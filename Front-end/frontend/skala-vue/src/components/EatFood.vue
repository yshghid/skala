<template>
  <div>
    <h1>홍길동의 BMI</h1>
    <p>현재 체중: {{ weight }}kg</p>
    <p>현재 키: {{ height }}cm</p>
    <p>BMI: {{ bmi }} ({{ bmiStatus }})</p>

    <h2>🍔 음식 먹기</h2>
    <button @click="gainWeight(1)">햄버거 (+1kg)</button>
    <button @click="gainWeight(2)">피자 (+2kg)</button>

    <PracticeSkill @practice="loseWeight" />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import PracticeSkill from './PracticeSkill.vue'

const height = 170
const weight = ref(60)

const bmi = computed(() => {
  const h = height / 100
  return Math.floor(weight.value / (h * h))
})

const bmiStatus = computed(() => {
  if (bmi.value < 18.5) return '저체중'
  if (bmi.value < 23) return '정상'
  if (bmi.value < 25) return '과체중'
  return '비만'
})

function gainWeight(amount) {
  weight.value += amount
}
function loseWeight(amount) {
  weight.value -= amount
}
</script>
