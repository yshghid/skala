import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Practice2 {
    // 한글로만 이루어진 문자열인지 판별하는 함수
    public static boolean isKoreanName(String name) {
        // 정규표현식: 시작(^), 끝($) 사이에 한글만 허용
        String regex = "^[가-힣]+$";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(name);
        return matcher.matches();
    }

    public static void main(String[] args) {
        System.out.println(isKoreanName("홍길동"));     // true
        System.out.println(isKoreanName("Tom"));       // false
        System.out.println(isKoreanName("홍길동123"));  // false
        System.out.println(isKoreanName("김영수"));     // true
    }
}