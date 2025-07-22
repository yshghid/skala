// 한글로만 이루어진 문자열인지 판별하는 함수
function isKoreanName(name) {
    const regex = /^[가-힣]+$/;
    return regex.test(name);
  }
  
  // 테스트
  console.log(isKoreanName("홍길동")); // true
  console.log(isKoreanName("Tom"));   // false
  console.log(isKoreanName("홍길동123")); // false
  console.log(isKoreanName("김영수"));    // true