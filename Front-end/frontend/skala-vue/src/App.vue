<template>
  <ChildComp>
    <template #top>
      <HongsDiet></HongsDiet>
    </template>
  </ChildComp>
</template>

<script setup>
import ChildComp from './components/slot/ChildComp.vue' ;
import HongsDiet from './components/slot/HongsDiet.vue' ;
</script>