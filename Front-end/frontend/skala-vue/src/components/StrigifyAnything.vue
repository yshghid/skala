<script setup>
import { ref, reactive, isRef, isReactive, unref, toRaw } from 'vue'
function toJsonString(value) {
  let anything = value
  // ref인 경우 .value 해제
  if (isRef(value)) {
    anything = unref(value)
  }
  // reactive인 경우 원시 객체 추출
  if (isReactive(anything)) {
    anything = toRaw(anything)
  }
  try {
    return JSON.stringify(anything)
  } catch (e) {
    return `"변환 불가: ${e.message}"`
  }
}
const primitive = 123
const obj = { name: '홍길동', age: 30 }
const arr = [1, 2, 3]
const r1 = ref({ city: '서울' })
const r2 = reactive({ job: '개발자' })
console.log(
  toJsonString(primitive), // "123"
  toJsonString(obj),       // {"name":"홍길동","age":30}
  toJsonString(arr),       // [1,2,3]
  toJsonString(r1),        // {"city":"서울"}
  toJsonString(r2)         // {"job":"개발자"}
)
</script>