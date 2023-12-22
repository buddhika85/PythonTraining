class Division {

    static int divide(int x, int y) {
        return x / y;
    }

    static void divide_ad_infinitum() {
        while (true) {
            try {
                int numOne = readNumber("Number 1 :");
                int numTwo = readNumber("Number 2 :");
                System.out.println(divide(numOne, numTwo));
            } catch (ArithmeticException e) {
                System.out.println(e.getMessage());
            }
        }
    }

    private static int readNumber(String question)
    {
        System.out.println(question);
        return In.nextInt();
    }

    public static void main(String[] args) {
        Division.divide_ad_infinitum();
    }
}