import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.concurrent.atomic.AtomicInteger;

public class day4 {
    void main() throws IOException {
        var s = Files.readString(Path.of(System.getProperty("user.dir"), "day_4", "input"));
        var x = Arrays.stream(s.split("\n")).map(s1 -> Arrays.stream(s1.replaceFirst("Card +[0-9]+:", "").split(" ")).filter(s2 -> !s2.isEmpty()).toList()).toList();
        AtomicInteger f = new AtomicInteger();
        x.forEach(strings -> {
            var storing = true;
            var result = 0;
            var nums = new ArrayList<Integer>();
            for (var num : strings) {
                if (num.equals("|")) {
                    storing = false;
                    continue;
                }
                if (storing) nums.add(Integer.parseInt(num));
                else if (nums.contains(Integer.parseInt(num))) result = result == 0 ? 1 : result * 2;
            }
            System.out.println(result);
            f.addAndGet(result);
        });
        System.out.println(f.get());

    }
}