// 서로 다른 따옴표 사용 예제
let sum1 = "합계는 '3'";
let sum2 = '합계는 "3"';
let sum3 = `합계는 "3"`;

// 동일한 따옴표를 내부에서 쓸 때 이스케이프 처리
let sameQuote1 = '그는 나에게 \'안녕\'이라고 말했다';
let sameQuote2 = "그는 나에게 \"안녕\"이라고 말했다";

// 줄 바꿈 예제 (텍스트 출력)
let lineText = "첫 번째 줄\n두 번째 줄";

// 콘솔 출력
console.log("▶ 따옴표 출력:");
console.log(sum1);
console.log(sum2);
console.log(sum3);

console.log("▶ 이스케이프 따옴표 출력:");
console.log(sameQuote1);
console.log(sameQuote2);

console.log("▶ 줄 바꿈 (\\n) 처리:");
console.log(lineText);

// HTML 페이지에 출력
let outputDiv = document.getElementById("output");

outputDiv.innerHTML += `<p>${sum1}</p>`;
outputDiv.innerHTML += `<p>${sum2}</p>`;
outputDiv.innerHTML += `<p>${sum3}</p>`;

outputDiv.innerHTML += `<p>${sameQuote1}</p>`;
outputDiv.innerHTML += `<p>${sameQuote2}</p>`;

outputDiv.innerHTML += `<p>첫 번째 줄<br>두 번째 줄</p>`;  // HTML 줄 바꿈
