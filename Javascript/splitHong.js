// 진짜 홍길동 객체
const realHong = {
    name: "홍길동",
    age: 25,
    job: "의적",
    skills: ["검술", "전략", "분신"],
    shadow: {
      color: "검은색"
    }
  };
  
  // 가짜 홍길동 생성: "분신" 제거 + shadow 속성 제거
  const fakeHong = {
    ...realHong, // 얕은 복사
    skills: realHong.skills.filter(skill => skill !== "분신")
  };
  
  delete fakeHong.shadow;
  
  // 결과 출력
  console.log("realHong:");
  console.log(realHong);
  
  console.log("\nfakeHong:");
  console.log(fakeHong);
  