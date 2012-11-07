import javax.swing.JOptionPane;

public class BankAccount {
	private double balance;

	public BankAccount(int initial_amount) {
		if (initial_amount >= 0)
			balance = initial_amount;
		else
			balance = 0;
	}

	public double getBalance() {
		return balance;
	}

	public boolean deposit(int amount) {
		boolean result = false;
		if (amount < 0)
			JOptionPane.showMessageDialog(null, "�߸��� �Աݾ��̶� �����մϴ�.");
		else {
			balance = balance + amount;
			result = true;
		}
		return result;
	}

	public boolean withdraw(int amount) {
		boolean result = false;
		if (amount < 0)
			JOptionPane.showMessageDialog(null, "�߸��� ��ݾ��̶� �����մϴ�.");
		else if (amount > balance)
			JOptionPane.showMessageDialog(null, "�ܰ� �����մϴ�.");
		else {
			balance = balance - amount;
			result = true;
		}
		return result;
	}

	public boolean interest(double interest) {
		boolean result = false;
		if (interest < 1 && interest > 2) {
			JOptionPane.showMessageDialog(null, "�߸��� �������Դϴ�.");
		} else {
			balance = balance * interest;
			result = true;
		}
		return result;

	}

	public boolean trasfer(int amount, int flag) {
		boolean result = false;
		if (flag == 0) {
			if (balance < amount) {
				JOptionPane.showMessageDialog(null, "�ܰ� �����մϴ�");
			} else if (amount < 0) {
				JOptionPane.showMessageDialog(null, "�߸��� ��ü��");
			} else {
				balance = balance - amount;
				result = true;
			}
		}
		if (flag == 1) {
			if(amount < 0){
				
			}
			else{
				balance = balance + amount;
				result = true;
			}
		}
		return result;
	}
}
