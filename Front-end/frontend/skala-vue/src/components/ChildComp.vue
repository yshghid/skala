<template>
  <h1>아들</h1>
  <div>용돈: {{ money }}</div>
</template>

<script setup>
import { ref } from "vue"

const props = defineProps({
  moneyFromParent: Number
})

const emit = defineEmits(["thanks"])

const money = ref(1000)

function takeMoney(moneyFromParent) {
  money.value += moneyFromParent
  emit("thanks", money.value)
}

defineExpose({
  takeMoney
})
</script>
