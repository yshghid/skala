function isKoreanName(name) {
    const regex = /^[가-힣]+$/;
    return regex.test(name);
  }
  
  console.log(isKoreanName("홍길동"));     // true
  console.log(isKoreanName("Tom"));       // false
  console.log(isKoreanName("홍길동123"));  // false
  console.log(isKoreanName("김영수"));     // true