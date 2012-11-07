

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
		writer.showTransaction("비활성");
		nowaccount = new_account;
		oldaccount = old_account;
		writer = new_writer;
		oldwriter = old_writer;
		writer.showTransaction("활성");
	}

	public void processTransactions() {
		char command = reader.readCommand("명령 P/S/D/W/Q/I/T와 금액을 입력하세요.");
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
				writer.showTransaction("입금 $", amount);
			else
				writer.showTransaction("입금 오류 ", amount);
			break;
		}
		case 'W': {
			int amount = reader.readAmount();
			if (nowaccount.withdraw(amount))
				writer.showTransaction("출금 $", amount);
			else
				writer.showTransaction("출금 오류 ", amount);
			break;
		}
		case 'I':{
			double interest = reader.readInterest();
			if (nowaccount.interest(interest))
				writer.showTransaction("이자 $");
			else
				writer.showTransaction("실패");
			break;
		}
		case 'T': {
			int amount = reader.readAmount();
			if(nowaccount.trasfer(amount, 0) && oldaccount.trasfer(amount, 1)){
				writer.showTransaction("이체성공");
				oldwriter.showTransaction("성공");
			}
			else{
				//오류
				writer.showTransaction("실패");
			}
			}
		break;
		default:
			writer.showTransaction("잘못된 명령 " + command);
		}
		this.processTransactions();

	}
}
