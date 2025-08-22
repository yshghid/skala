<template>
  <h1>부모</h1>
  <div>자산: {{ parentMoney }}</div>

  <label>
    자식에게 줄 용돈:
    <input v-model="moneyToChild" type="number" />
  </label>
  <button @click="sendMoney">용돈주기</button>

  <ChildComponent
    ref="childRef"
    :moneyFromParent="childMoney"
    @thanks="onThanks"
  />
</template>

<script setup>
import { ref } from "vue"
import ChildComponent from "./ChildComp.vue"

const moneyToChild = ref(0)
const childMoney = ref(0)
const parentMoney = ref(10000)
const childRef = ref(null)

function sendMoney() {
  childMoney.value = Number(moneyToChild.value)
  parentMoney.value -= moneyToChild.value

  childRef.value?.takeMoney(childMoney.value)
}

function onThanks(amount) {
  console.log("onThanks", amount)
}
</script>
