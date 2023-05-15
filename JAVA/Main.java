import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        System.out.println("hello world");
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();

        boolean b = sc.hasNextInt();
        System.out.println(b);
    }
}
