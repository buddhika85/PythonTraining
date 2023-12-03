import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Test {
    public static void main(String[] args) {

        // 1
        ArrayList<Integer> arrayList = new ArrayList<>();
        for(int i = 0; i <= 10; i++)
        {
            arrayList.add(i);
        }
        System.out.println(arrayList);

        // 2
        Integer[] array = new Integer []{100, 200, 300, 400 };
        arrayList = new ArrayList<>(Arrays.asList(array));
        for (Integer integer : arrayList) {
            System.out.println(integer);
        }

        // 3
        HashMap<Integer, Point> pointsMap = new HashMap<>();
        pointsMap.put(1, new Point(1, 2));
        pointsMap.put(2, new Point(3, 4));
        for (Map.Entry<Integer, Point> pair : pointsMap.entrySet()) 
        {
            Integer key = pair.getKey();
            Point value = pair.getValue();
            System.out.println("Key :" + key + " , value: " + value);
        }
    }
}


class Point
{
    private int x, y;
    public Point(int x, int y)
    {
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
        
        return "x=" + x + "y=" + y;
    }
}