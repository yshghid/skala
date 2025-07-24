// ✅ if-else if 문 실습
let age = 18;

if (age < 13) {
  console.log("어린이");
} else if (age < 20) {
  console.log("청소년");
} else {
  console.log("성인");
}

// 구분선
console.log("-------------");

// ✅ switch 문 실습
let day = "Monday";

switch (day) {
  case "Monday":
    console.log("월요일");
    break;
  case "Tuesday":
    console.log("화요일");
    break;
  default:
    console.log("기타");
}
