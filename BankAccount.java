import java.util.Calendar;

import javax.swing.JOptionPane;

public class BankAccount {
	private double balance;
	private int accountnumber;
	private String[] record = new String[10];

	public BankAccount(int x,int initial_amount) {
		accountnumber = x; 
		if (initial_amount >= 0)
			balance = initial_amount;
		else
			balance = 0;
	}

	public double getBalance() {
		return balance;
	}
	
	public int getAccountnumber(){
		return accountnumber;
	}

	public boolean deposit(int amount) {
		boolean result = false;
		if (amount < 0)
			JOptionPane.showMessageDialog(null, "잘못된 입금액이라 무시합니다.");
		else {
			balance = balance + amount;
			result = true;
		}
		return result;
	}

	public boolean withdraw(int amount) {
		boolean result = false;
		if (amount < 0)
			JOptionPane.showMessageDialog(null, "잘못된 출금액이라 무시합니다.");
		else if (amount > balance)
			JOptionPane.showMessageDialog(null, "잔고가 부족합니다.");
		else {
			balance = balance - amount;
			result = true;
		}
		return result;
	}
	

	public double interest() {
		double temp = balance;
		balance = balance*1.01;
		
		return balance-temp;
	}

	
	public void writeRecord(String s,double amount){
		Calendar c = Calendar.getInstance();
		String now = (c.get(Calendar.MONTH)+1)+"."+c.get(Calendar.DAY_OF_MONTH)+" "+c.get(Calendar.HOUR_OF_DAY)+":"+c.get(Calendar.MINUTE);
		if(record[9] != null){
			String[] temp = new String[10];
			for(int i=0; i<9; i++){
				temp[i] = record[i+1];
			}
			temp[9] = now+" "+s+":"+amount;
			record = temp;
		}
		else{
			for(int i=0; i<10; i++){
				if(record[i] == null){
					record[i] = now+" "+s+":"+amount;
					break;
				}
			}
		}
	}
	public String resultRecord(){
		String result = "";
		for(int i=0; i<record.length; i++){
			if(record[i] != null){
				result = result+record[i]+"\n";
			}
		}
		return result;
	}
}
