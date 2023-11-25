import java.util.Random;

public class Week6Challenge {
    public static void main(String[] args) {
        Tournament tourney = new Tournament();
        Player player = new Player("Joe");
        SimulatedPlayer simulatedPlayer = new SimulatedPlayer("Simulated Player");

        int numGames = 5;
        int i = 0;

        while (i < numGames) {
            GameResult result = tourney.runFullySimulatedGame(player, simulatedPlayer);
            System.out.println(result);
            System.out.println();
            i++;
        }

    }
}

class Tournament {
    Random random = new Random();
    final static int ROCK = 0;
    final static int PAPER = 1;
    final static int SCISSORS = 2;

    final static int PLAYER_ONE_WINS = 0;
    final static int PLAYER_TWO_WINS = 1;
    final static int DRAW = 2;

    GameResult runFullySimulatedGame(Player player, SimulatedPlayer simulatedPlayer) {
        int playerOneMove = player.selectMove();
        int playerTwoMove = simulatedPlayer.selectMove();

        GameResult result = new GameResult(player.getName(), playerOneMove, simulatedPlayer.getName(), playerTwoMove);

        if (playerOneMove == ROCK) {
            if (playerTwoMove == ROCK) {
                result.outcome = DRAW;
            } else if (playerTwoMove == PAPER) {
                result.outcome = PLAYER_TWO_WINS;
            } else {
                // player two made scissors
                result.outcome = PLAYER_ONE_WINS;
            }
        } else if (playerOneMove == PAPER) {
            if (playerTwoMove == ROCK) {
                result.outcome = PLAYER_ONE_WINS;
            } else if (playerTwoMove == PAPER) {
                result.outcome = DRAW;
            } else {
                // player two made scissors
                result.outcome = PLAYER_TWO_WINS;
            }
        } else {
            // player one made scissors
            if (playerTwoMove == ROCK) {
                result.outcome = PLAYER_TWO_WINS;
            } else if (playerTwoMove == PAPER) {
                result.outcome = PLAYER_ONE_WINS;
            } else {
                // player two made scissors
                result.outcome = DRAW;
            }
        }

        return result;
    }
}

class GameResult {
    public String playerOneName;
    public String playerTwoName;
    public int playerOneMove;
    public int playerTwoMove;
    public int outcome;

    GameResult(String playerOneName, int playerOneMove, String playerTwoName, int playerTwoMove) {
        this.playerOneName = playerOneName;
        this.playerTwoName = playerTwoName;
        this.playerOneMove = playerOneMove;
        this.playerTwoMove = playerTwoMove;
    }

    public String toString() {
        String player1Description = " - " + this.playerOneName + " made " +
                moveToString(this.playerOneMove) + "\n";
        String player2Description = " - " + this.playerTwoName + " made " +
                moveToString(this.playerTwoMove) + "\n";
        String outcomeDescription = outcomeToString(outcome, playerOneName, playerTwoName);

        return "OUTCOME OF GAME--------------------\n" +
                player1Description +
                player2Description +
                outcomeDescription;
    }

    String moveToString(int move) {
        if (move == Tournament.ROCK) {
            return "Rock";
        } else if (move == Tournament.PAPER) {
            return "Paper";
        } else {
            return "Scissors";
        }
    }

    String outcomeToString(int outcome, String playerOneName, String playerTwoName) {
        if (outcome == Tournament.PLAYER_ONE_WINS) {
            return playerOneName + " wins.";
        } else if (outcome == Tournament.PLAYER_TWO_WINS) {
            return playerTwoName + " wins.";
        } else {
            return "Draw";
        }
    }
}

class Player{
    private String name;
    
    public Player(String name) {
        this.name = name;
    }

    public int selectMove()
    {
        System.out.println(name + " Enter 0 for Rock, 1 for Paper and 2 for Scissors:");
        return In.nextInt();
    }

    public String getName()
    {
        return name;
    }
}

class SimulatedPlayer{
    private String name;
   
    public SimulatedPlayer(String name) {
        this.name = name;
    }

    public int selectMove()
    {
        System.out.println("Simulated Player " + name + " - Enter 0 for Rock, 1 for Paper and 2 for Scissors:");
        // nextInt(3) generates a random int with value of 0, 1 or 2.
        int result = new Random().nextInt(3);
        System.out.println(name + " selects " + result);
        return result;
    }

    public String getName()
    {
        return name;
    }
}