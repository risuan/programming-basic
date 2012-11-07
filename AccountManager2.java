

public class AccountManager2 {
	public static void main(String[] args) { // create the application's
												// objects:
		BankReader reader = new BankReader();
		BankAccount primary_account = new BankAccount(0);
		BankWriter primary_writer = new BankWriter("°èÁÂ#1", primary_account,0,0);
		BankAccount secondary_account = new BankAccount(0);
		BankWriter secondary_writer = new BankWriter("°èÁÂ#2", secondary_account,0,200);
		AccountControlloer2 controller = new AccountControlloer2(reader,
				primary_account, primary_writer, secondary_account,
				secondary_writer);
		controller.processTransactions();
	}

}
