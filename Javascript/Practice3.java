import java.util.*;

public class Practice3 {
    public static void main(String[] args) {
        // 음식 리스트
        String[] foods = {
            "쌀", "보리", "콩", "감자", "양파",
            "마늘", "배추", "무", "고구마", "호박"
        };

        // 사람 리스트
        String[] poors = {"철수", "영희", "민수"};

        // 결과 저장할 리스트 (각 사람에 대해 Map 저장)
        List<Map<String, Object>> results = new ArrayList<>();

        // 초기화: 이름과 빈 아이템 리스트 설정
        for (String name : poors) {
            Map<String, Object> person = new HashMap<>();
            person.put("name", name);
            person.put("items", new ArrayList<String>());
            results.add(person);
        }

        // 음식 분배
        for (int i = 0; i < foods.length; i++) {
            int targetIndex = i % poors.length;
            @SuppressWarnings("unchecked")
            List<String> items = (List<String>) results.get(targetIndex).get("items");
            items.add(foods[i]);
        }

        // 결과 출력
        System.out.println("음식 분배 결과:");
        for (Map<String, Object> person : results) {
            String name = (String) person.get("name");
            @SuppressWarnings("unchecked")
            List<String> items = (List<String>) person.get("items");
            System.out.printf("%s → %s\n", name, items);
        }
    }
}
