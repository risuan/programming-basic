

public class AccountControlloer2 {
	private BankReader reader; // input view
	private BankAccount primary_account, secondary_account, nowaccount, oldaccount;
	private BankWriter primary_writer, secondary_writer, writer, oldwriter;

	public AccountControlloer2(BankReader r, BankAccount a1, BankWriter w1,
			BankAccount a2, BankWriter w2) {
		reader = r;
		primary_account = a1;
		primary_writer = w1;
		secondary_account = a2;
		secondary_writer = w2;
		writer = primary_writer;
	}
	public void resetAccount(BankAccount new_account, BankWriter new_writer, BankAccount old_account, BankWriter old_writer) {
		writer.showTransaction("��Ȱ��");
		nowaccount = new_account;
		oldaccount = old_account;
		writer = new_writer;
		oldwriter = old_writer;
		writer.showTransaction("Ȱ��");
	}

	public void processTransactions() {
		char command = reader.readCommand("��� P/S/D/W/Q/I/T�� �ݾ��� �Է��ϼ���.");
		switch (command) {
		case 'P':
			resetAccount(primary_account, primary_writer, secondary_account, secondary_writer);
			break;
		case 'S':
			resetAccount(secondary_account, secondary_writer, primary_account, primary_writer);
			break;
		case 'Q':
			return;
		case 'D': {
			int amount = reader.readAmount();
			if (nowaccount.deposit(amount))
				writer.showTransaction("�Ա� $", amount);
			else
				writer.showTransaction("�Ա� ���� ", amount);
			break;
		}
		case 'W': {
			int amount = reader.readAmount();
			if (nowaccount.withdraw(amount))
				writer.showTransaction("��� $", amount);
			else
				writer.showTransaction("��� ���� ", amount);
			break;
		}
		case 'I':{
			double interest = reader.readInterest();
			if (nowaccount.interest(interest))
				writer.showTransaction("���� $");
			else
				writer.showTransaction("����");
			break;
		}
		case 'T': {
			int amount = reader.readAmount();
			if(nowaccount.trasfer(amount, 0) && oldaccount.trasfer(amount, 1)){
				writer.showTransaction("��ü����");
				oldwriter.showTransaction("����");
			}
			else{
				//����
				writer.showTransaction("����");
			}
			}
		break;
		default:
			writer.showTransaction("�߸��� ��� " + command);
		}
		this.processTransactions();

	}
}
