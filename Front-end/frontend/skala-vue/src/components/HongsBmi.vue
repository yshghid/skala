<template>
  <div>
    <h2>홍길동의 BMI 계산</h2>
    
    <div>
      <label>키(cm): </label>
      <input type="number" v-model.number="height" />
    </div>
    <div>
      <label>체중(kg): </label>
      <input type="number" v-model.number="weight" />
    </div>

    <hr />

    <div v-if="bmi > 0">
      <p>BMI: {{ bmi.toFixed(2) }}</p>
      <p>판정: {{ message }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'

const height = ref(0)   // cm 단위
const weight = ref(0)   // kg 단위
const message = ref('')

// BMI 계산 (computed)
const bmi = computed(() => {
  if (height.value > 0) {
    return weight.value / ((height.value / 100) ** 2)
  }
  return 0
})

// BMI에 따른 판정 메시지
function getJudgement(bmiValue) {
  if (bmiValue === 0) return ''
  if (bmiValue < 18.5) return '저체중'
  if (bmiValue < 23) return '정상'
  if (bmiValue < 25) return '과체중'
  return '비만'
}

// watch로 BMI 값이 변할 때 판정 업데이트
watch(bmi, (newBmi) => {
  let judgement = getJudgement(newBmi)
  if (judgement === '과체중' || judgement === '비만') {
    judgement += ' - 다이어트 하세요!'
  }
  message.value = judgement
})

// onMounted 훅 추가
onMounted(() => {
  console.log("HongsBmi is mounted")
})
</script>
