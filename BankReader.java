

import java.text.DecimalFormat;

import javax.swing.*;

public class BankReader {
	private String input_line = "";

	public char readCommand(String message) {
		input_line = JOptionPane.showInputDialog(message).toUpperCase();
		return input_line.charAt(0);
	}

	public int readAmount() {
		int answer = 0;
		String s = input_line.substring(1, input_line.length());
		if (s.length() > 0) {
			double dollars_cents = new Double(s).doubleValue();
			answer = (int) (dollars_cents * 100);
		} else
			JOptionPane.showMessageDialog(null, "금액을 입력하지 않아 0으로 처리합니다.");
		return answer;
	}
	public int readTransfer(){
		int answer = 0;
		String s = input_line.substring(1, input_line.length());
		if (s.length() > 0){
			double dollars_cents = new Double(s).doubleValue();
			answer = (int) (dollars_cents * 100);
		}else
			JOptionPane.showMessageDialog(null,"금액을 입력하지 않아 0으로 처리합니다.");
		return answer;
		}
	
	public double readInterest(){
		double answer = 1.0;
		String s = input_line.substring(1, input_line.length());
		if (s.length() > 0) {
			double temp = new Double(s).doubleValue();//0.555555  double
			String inter = new DecimalFormat("0.00").format(temp);//0.55     string
			double interest = new Double(inter).doubleValue();// 0.55 double
			//double interest = new Double(temp).doubleValue();
			answer = answer + interest;
		} else
			JOptionPane.showMessageDialog(null, "금액을 입력하지 않아 0으로 처리합니다.");
		return answer;
		
	}
	
}
