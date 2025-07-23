public class Practice1 {
    public static void main(String[] args) {

        // 서로 다른 따옴표 사용 예제
        String sum1 = "합계는 '3'";
        String sum2 = "합계는 \"3\"";
        // String sum3 = 합계는 "3"; // ❌ 오류: 문자열 따옴표 빠짐

        // 동일한 따옴표를 내부에서 쓸 때 이스케이프 처리
        String sameQuote1 = "그는 나에게 '안녕'이라고 말했다";
        String sameQuote2 = "그는 나에게 \"안녕\"이라고 말했다";

        // 줄 바꿈 예제
        String lineText = "첫 번째 줄\n두 번째 줄";

        // 출력
        System.out.println("▶ 따옴표 출력:");
        System.out.println(sum1);
        System.out.println(sum2);
        // System.out.println(sum3); // sum3은 오류가 있으므로 제외

        System.out.println("▶ 이스케이프 따옴표 출력:");
        System.out.println(sameQuote1);
        System.out.println(sameQuote2);

        System.out.println("▶ 줄 바꿈 (\\n) 처리:");
        System.out.println(lineText);
    }
}
