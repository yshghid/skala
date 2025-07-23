import java.util.Scanner;

public class Practice4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("홍길동이 무엇으로 변신할까요? : ");
        String input = scanner.nextLine().trim();

        if (!input.isEmpty()) {
            System.out.println("홍길동 변신 – " + input + "!");
        } else {
            System.out.println("연기처럼 사라졌습니다.");
        }

        scanner.close();
    }
}
