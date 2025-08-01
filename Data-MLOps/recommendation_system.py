from dataclasses import dataclass
from typing import List

# 1. 음료 클래스 정의
@dataclass
class Beverage:
    name: str
    price: float
    tags: List[str]

# 2. 주문 클래스 정의
class Order:
    __slots__ = ('beverage', 'quantity')

    def __init__(self, beverage: Beverage, quantity: int):
        self.beverage = beverage
        self.quantity = quantity

    @property
    def total_price(self) -> float:
        return self.beverage.price * self.quantity

# 3. 사용자 클래스 정의
class User:
    def __init__(self, name: str):
        self.name = name
        self.orders: List[Order] = []

    def add_order(self, order: Order):
        self.orders.append(order)

    def get_total_spent(self) -> float:
        return sum(order.total_price for order in self.orders)

    def get_recent_tags(self, n: int = 3) -> List[str]:
        tags = []
        for order in self.orders[-n:]:
            tags.extend(order.beverage.tags)
        return list(set(tags))  # 중복 제거

# 4. 추천 시스템 클래스 정의
class RecommendationEngine:
    def __init__(self, menu: List[Beverage]):
        self.menu = menu

    def recommend(self, user: User) -> List[Beverage]:
        recent_tags = user.get_recent_tags()
        recommendations = []
        for beverage in self.menu:
            if any(tag in beverage.tags for tag in recent_tags):
                recommendations.append(beverage)
        return recommendations

# 5. 테스트 실행
if __name__ == "__main__":
    # 메뉴 정의
    menu = [
        Beverage("아이스 아메리카노", 3000, ["커피", "콜드"]),
        Beverage("카페라떼", 3500, ["커피", "밀크"]),
        Beverage("녹차", 2800, ["차", "뜨거운"]),
        Beverage("허브티", 3000, ["차", "차가운"]),
    ]

    # 사용자 생성 및 주문
    user = User("철수")
    user.add_order(Order(menu[0], 1))  # 아이스 아메리카노
    user.add_order(Order(menu[1], 2))  # 카페라떼

    # 추천 시스템
    recommender = RecommendationEngine(menu)
    recommended = recommender.recommend(user)

    # 출력
    print("📌 추천 음료:")
    for b in recommended:
        print(f"- {b.name} ({b.tags})")

    print(f"\n💰 총 주문 금액: {user.get_total_spent()}원")