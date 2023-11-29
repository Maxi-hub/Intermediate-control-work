import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class ToyStore {

    static Toys constructor = new Toys(1, "constructor", 2, 20);
    static Toys robot = new Toys(2, "robot", 2, 20);
    static Toys doll = new Toys(3, "doll", 6, 60);

    public ToyStore() throws InputSexException {
    }

    public static Queue<String> getRandomToy() {
        Queue<String> ar = new LinkedList<>();
        for (int i = 0; i < 10; i++) {
            int num = (int) (Math.random() * 100);
            if (num >= 0 && num < 20)
                ar.add(constructor.getName());
            if (num >= 20 && num < 40)
                ar.add(robot.getName());
            if (num >= 40 && num < 100)
                ar.add(doll.getName());
        }
        return ar;
    }

    Queue<String> toy = getRandomToy();

    static String yourSex() throws InputSexException {
        String name = null;
        try {
            Scanner scanner = new Scanner(System.in);
            System.out.print("Input your sex (m -man or f -female): ");
            name = scanner.nextLine();
            if (!name.isEmpty()) {
                if (name.length() > 1 | (!name.equals("m") & !name.equals("f"))) {
                    throw new InputSexException("The gender was entered incorrectly!");
                }
            } else {
                throw new InputSexException("The string 'sex' is empty");
            }
        } catch (InputSexException e) {
            System.out.println("Error: " + e.getMessage());
        }
        return name;
    }



    String sex = yourSex();

    public static void getYourToy(Queue<String> toys, String sex) {
        String fileName = "Winner toy";
        try (FileWriter fileWriter = new FileWriter(Paths.get(fileName).toFile(), true)) {
            BufferedReader br = new BufferedReader(new FileReader(fileName));
            br.readLine();
            String s = System.lineSeparator();
            fileWriter.write(s);
            fileWriter.append("\n");
            fileWriter.write("List of dropped toys " + toys + "\n");
            String x = toys.remove();
            fileWriter.write("List of toys without first one " + toys + ", ");
            int size = toys.size();
            fileWriter.write("Size of the list - " + size + "\n");
            if (sex.isEmpty() | sex.length() > 1){
                fileWriter.write("You win - " + x);
            }
            else if (sex.equals("f") && (x.equals(doll.getName()) | x.equals(constructor.getName()))){
                fileWriter.write("Congratulations! You win - " + x);
            }
            else if (sex.equals("m") && (x.equals(robot.getName()) | x.equals(constructor.getName()))){
                fileWriter.write("Congratulations! You win - " + x);
            }
            else {
                fileWriter.write("Maybe next time, you win - " + x);
            }
            System.out.println("Take a look at the file \"Winner toy\"");
        } catch (IOException e) {
            System.err.println("File doesn't exist, there are errors in the entered data");
            e.printStackTrace();
        }
    }

}





