const foods = [
    "쌀", "보리", "콩", "감자", "양파",
    "마늘", "배추", "무", "고구마", "호박"
  ];
  
  const poors = ["철수", "영희", "민수"];
  
  // 빈 결과 배열 생성
  const results = poors.map(name => ({
    name,
    items: []
  }));
  
  // 순환하면서 음식 분배
  foods.forEach((food, index) => {
    const targetIndex = index % poors.length;
    results[targetIndex].items.push(food);
  });
  
  // 결과 출력
  console.table(results);
  