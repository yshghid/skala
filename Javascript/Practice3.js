// 음식 배열
const foods = [
    "쌀", "보리", "콩", "감자", "양파",
    "마늘", "배추", "무", "고구마", "호박"
  ];
  
  // 사람 배열
  const poors = ["철수", "영희", "민수"];
  
  // 결과를 담을 배열
  const results = poors.map(name => ({
    name: name,
    items: []
  }));
  
  // 음식 분배
  for (let i = 0; i < foods.length; i++) {
    const targetIndex = i % poors.length;
    results[targetIndex].items.push(foods[i]);
  }
  
  // 결과 출력 (표 형태)
  console.table(results);
  