public class BankSystem
{
    public static void main(String[] args) {
        
    }
}

class SavingsAccount
{
    private String accNum;
    private String ownerNationalId;
    private double balance;

    public SavingsAccount(String accNum, String ownerNationalId) {
        this.accNum = accNum;
        this.ownerNationalId = ownerNationalId;
        this.balance = 0.0;
    }

    public void deposit(double amount)
    {
        this.balance += amount;
    }

    public boolean withdraw(double amount)
    {
        if (canWithdraw(amount))
        {
            this.balance -= amount;
            return true;
        }
        else
            return false;
    }

    private boolean canWithdraw(double amount) {
        return this.balance >= amount;
    }

    public String getAccNum()
    {
        return accNum;
    }

    public double getBalance()
    {
        return balance;
    }

    @Override
    public String toString() {
        return "Savings Account: " + this.accNum + ", owner national ID:" + this.ownerNationalId 
            + " with balance: " + this.balance;
    }
}

class Customer
{
    private String name;
    private String nationalId;
    private SavingsAccount[] savingsAccounts;

    public Customer(String name, String nationalId) {
        this.name = name;
        this.nationalId = nationalId;
        savingsAccounts = new SavingsAccount[Bank.MAX_ACCOUNTS_PER_CUSTOMER];
    }

    public void deposit(double amount, SavingsAccount account)
    {
        account.deposit(amount);
    }

    public boolean withdraw(double amount, SavingsAccount account)
    {
        return account.withdraw(amount);
    }

    public boolean hasAccount(SavingsAccount account)
    {
        for (SavingsAccount savingsAccount : savingsAccounts) {
            if (savingsAccount.getAccNum().equals(account.getAccNum()))
                return true;
        }
        return false;
    }
}

class Bank
{
    public final static int MAX_ACCOUNTS_PER_CUSTOMER = 10;
    private String name;
    private Customer[] customers = new Customer[100];
    private SavingsAccount[] savingsAccounts = new SavingsAccount[100];

    public Bank(String name)
    {
        this.name = name;
    }

    private double calcDepositBase()
    {
        double total = 0.0;
        for (SavingsAccount account : savingsAccounts) {
            total += account.getBalance();
        }
        return total;
    }

    public SavingsAccount findLargestBalanceAccount()
    {
        SavingsAccount largest = savingsAccounts[0];
        for (SavingsAccount account : savingsAccounts) {
            if (account.getBalance() > largest.getBalance())
                largest = account;
        }
        return largest;
    }

    public SavingsAccount[] findNegativeAccounts()
    {
        SavingsAccount[] negatives = new SavingsAccount[savingsAccounts.length];
        int count = 0;
        for (SavingsAccount account : savingsAccounts) {
            if (account.getBalance() < 0.0)
                negatives[count++] = account;
        }
        return negatives;
    }
}