function transform() {
    const input = prompt("홍길동이 무엇으로 변신할까요?");
  
    if (input && input.trim() !== "") {
      alert("홍길동 변신 – " + input.trim() + "!");
    } else {
      alert("연기처럼 사라졌습니다.");
    }
  }
  
  // 페이지 열리자마자 실행
  transform();