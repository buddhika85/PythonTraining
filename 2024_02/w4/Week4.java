public class Week4 {
    public static void main(String[] args) {
        int[] a = { 1, 2, 3 };
        System.out.println(Week4.findMinimum(a));
    }

    public static int findMinimum(int[] array) {
        int min = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i] < min) {
                min = array[i];
            }
        }

        return min;
    }
}