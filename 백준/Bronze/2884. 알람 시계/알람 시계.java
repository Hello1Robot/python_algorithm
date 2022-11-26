import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String n;
        Scanner sc = new Scanner(System.in);
        n = sc.nextLine();
        String[] times = n.split(" ");
        int bun = Integer.parseInt(times[1]);
        int see = Integer.parseInt(times[0]);

        if(bun>=45){
            bun -= 45;
        }else{
            bun += 15;
            see -= 1;
        }

        if(see<0){
            see = 23;
        }

        System.out.print(see);
        System.out.print(' ');
        System.out.print(bun);


    }
}
