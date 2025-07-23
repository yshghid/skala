import java.util.*;

class Hong {
    String name;
    int age;
    String job;
    List<String> skills;
    Shadow shadow; // 진짜 홍길동만 가짐

    static class Shadow {
        String color;

        Shadow(String color) {
            this.color = color;
        }
    }

    Hong(String name, int age, String job, List<String> skills, Shadow shadow) {
        this.name = name;
        this.age = age;
        this.job = job;
        this.skills = skills;
        this.shadow = shadow;
    }

    boolean isReal() {
        return skills.contains("분신") && shadow != null;
    }

    void speak() {
        System.out.println(name + " (" + job + ")의 기술 목록: " + skills);
        if (shadow != null) {
            System.out.println("그림자 색상: " + shadow.color);
        } else {
            System.out.println("그림자가 없습니다.");
        }
        System.out.println("진짜 홍길동인가요? " + (isReal() ? "네!" : "아니요!"));
        System.out.println();
    }
}

public class Practice5 {
    public static void main(String[] args) {
        // 진짜 홍길동
        Hong realHong = new Hong(
            "홍길동",
            25,
            "의적",
            Arrays.asList("검술", "전략", "분신"),
            new Hong.Shadow("검은색")
        );

        // 가짜 홍길동
        Hong fakeHong = new Hong(
            "홍길동",
            25,
            "의적",
            Arrays.asList("검술", "전략"),
            null
        );

        // 결과 출력
        realHong.speak();
        fakeHong.speak();
    }
}
