class Pokemon {
    private String name;
    private int level;
    private String pokemonType;
    private int health;

    public Pokemon(String name, int level, String pokemonType) {
        this.name = name;
        this.level = level;
        this.pokemonType = pokemonType;
        this.health = 10 * this.level;
    }

    public void takeDamage(int damage)
    {
        health -= damage;
    }

    public void attack(Pokemon target)
    {
        target.takeDamage(level);
    }

    public String toString()
    {
        return name + " type " + pokemonType + " of level " + level + " has health " + health;
    }
}