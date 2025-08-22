<template>
  <div>
    <!-- 색상, 사이즈 입력 -->
    <input v-model="inputColor" placeholder="색상 입력 (예: orange)" />
    <input v-model="inputSize" placeholder="크기 입력 (예: 150)" type="number" />
    <button @click="applyStyle">적용</button>

    <!-- 미리보기 박스 -->
    <div class="preview-box" :style="boxStyle">
      스타일 미리보기 박스
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// 입력값
const inputColor = ref('')
const inputSize = ref('')

// 적용된 스타일 상태
const boxStyle = ref({
  backgroundColor: '#f0f0f0',
  width: '150px',
  height: '150px',
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  borderRadius: '10px'
})

// 적용 버튼 클릭 시 실행
function applyStyle() {
  boxStyle.value.backgroundColor = inputColor.value || 'orange'
  boxStyle.value.width = inputSize.value ? inputSize.value + 'px' : '150px'
  boxStyle.value.height = inputSize.value ? inputSize.value + 'px' : '150px'
}
</script>

<style>
.preview-box {
  margin-top: 10px;
  color: black;
}
</style>
