<template>
  <div>
    <h3>댓글 달기</h3>
    <input v-model="newComment" placeholder="댓글을 입력하세요" />
    <button @click="addComment">등록</button>

    <ul>
      <li v-for="(comment, index) in comments" :key="index">
        {{ comment }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from "vue"

// 댓글 목록
const comments = ref(["가가멜", "스머프"])

// 새 댓글 입력 값
const newComment = ref("")

// 댓글 추가 함수
function addComment() {
  if (newComment.value.trim() !== "") {   // 빈 문자열 방지
    comments.value.push(newComment.value) // 뒤에 추가
    newComment.value = ""                 // 입력창 초기화
  }
}
</script>
