function processOrder(itemStock, membership, orderAmount, shippingOption) {
    // 1. 재고 확인
    if (itemStock < 1) {
      console.log("❌ 죄송합니다. 해당 상품은 품절입니다.");
      return;
    }
  
    // 2. 회원 등급 할인
    let discountRate = 0;
    if (membership === "VIP") {
      discountRate = 0.10;
    } else if (membership === "Gold") {
      discountRate = 0.05;
    }
  
    // 3. 기본 할인 적용
    let discountedAmount = orderAmount * (1 - discountRate);
  
    // 4. 추가 할인 조건
    if (discountedAmount >= 200000) {
      discountedAmount -= 15000;
    } else if (discountedAmount >= 100000) {
      discountedAmount -= 5000;
    }
  
    // 5. 배송 옵션 처리
    let shippingFee = 0;
    if (shippingOption === "fast") {
      shippingFee = 3000;
    }
  
    // 6. 최종 결제 금액 계산
    const finalAmount = discountedAmount + shippingFee;
  
    // 7. 결과 출력
    console.log("✅ 주문이 정상적으로 완료되었습니다.");
    console.log(`💳 최종 결제 금액: ${finalAmount.toLocaleString("ko-KR")}원`);
  }
  
// 1. 재고 0일 경우
processOrder(0, "VIP", 120000, "fast");
console.log("----------");

// 2. VIP 회원, 120,000원 주문, 빠른 배송
processOrder(3, "VIP", 120000, "fast");
console.log("----------");

// 3. Gold 회원, 90,000원 주문, 일반 배송
processOrder(2, "Gold", 90000, "standard");
console.log("----------");

// 4. 일반회원, 250,000원 주문, 배송 옵션 없음
processOrder(5, "Basic", 250000);