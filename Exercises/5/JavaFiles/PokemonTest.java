public class PokemonTest {
    public static void main(String[] args) {
        Pokemon pokemonOne = new Pokemon("Pikachu", 1, "electric");
        Pokemon pokemonTwo = new Pokemon("Black", 2, "dragon");

        System.out.println(pokemonOne);
        System.out.println(pokemonTwo);

        pokemonOne.attack(pokemonTwo);
        pokemonTwo.attack(pokemonOne);
        System.out.println("\nAfter one round of attacking: ");
        System.out.println(pokemonOne);
        System.out.println(pokemonTwo);

    }
}
