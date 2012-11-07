import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.border.Border;

public class Bankframe extends JFrame {
	Database db = new Database(4);
	JFrame f = new JFrame();
	JPanel main = new JPanel();
	JPanel Bankwriter = new JPanel();
	TextArea t1 = new TextArea("�ȳ��ϼ���");
	TextArea t2;

	
	JButton cbutton = new JButton("��ȸ");
	JButton dbutton = new JButton("�Ա�");
	JButton wbutton = new JButton("���");
	JButton tbutton = new JButton("��ü");
	JButton abutton = new JButton("���°���");

	public Bankframe() {
		f.setLayout(new BorderLayout());
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		main.setSize(100, 200);
		main.setBackground(Color.white);
		Bankwriter.setBackground(Color.white);
		main.setLayout(new GridLayout(5,1));
		main.add(cbutton);
		cbutton.addActionListener(new cbuttonListener());
		main.add(dbutton);
		dbutton.addActionListener(new dbuttonListener());
		main.add(wbutton);
		wbutton.addActionListener(new wbuttonListener());
		main.add(tbutton);
		tbutton.addActionListener(new tbuttonListener());
		main.add(abutton);
		abutton.addActionListener(new abuttonListener());
		
		f.getContentPane().add(BorderLayout.CENTER,t1);
		f.getContentPane().add(BorderLayout.EAST,main);
		f.setSize(250, 200);
		f.setVisible(true);
	}

	class cbuttonListener implements ActionListener {
		
		public cbuttonListener(){
			
		}
		public void actionPerformed(ActionEvent e) {
			JPanel Checkface = new JPanel();
			//JLabel Lbankwriter = new JLabel("��ȸ");
			//Lbankwriter.setSize(100,100);
			t2 = new TextArea("��ȸ");
			
			Checkface.setBackground(Color.white);
			//Checkface.setLayout(new BoxLayout(Checkface, BoxLayout.Y_AXIS));
			f.setLayout(new BorderLayout());
			Checkface.setLayout(new GridLayout(5,1));
			
			for(int i=0 ; i<db.getBaseLength(); i++){
				if(db.getAccount(i) != null){
					Checkface.add(new aButton(""+db.getAccount(i).getAccountnumber(), -1, db.getAccount(i)));
				}
			}
			JButton Backbutton = new JButton("�ڷ�");

			Checkface.add(Backbutton);
			
			main.setVisible(false);
			t1.setVisible(false);
			f.getContentPane().add(BorderLayout.CENTER,t2);
			f.getContentPane().add(BorderLayout.EAST,Checkface);
			
			Backbutton.addActionListener(new BackbuttonListener(Checkface,t2));

		}
	}

	class dbuttonListener implements ActionListener {
		public void actionPerformed(ActionEvent e){
			JPanel depositface = new JPanel();
			t2 = new TextArea("�Ա�");			
			
			depositface.setBackground(Color.white);
			f.setLayout(new BorderLayout());
			depositface.setLayout(new GridLayout(5, 1));
			for(int i=0 ; i<db.getBaseLength(); i++){
				if(db.getAccount(i) != null){
					depositface.add(new aButton(""+db.getAccount(i).getAccountnumber(), 0, db.getAccount(i)));
				}
			}

			JButton Backbutton = new JButton("�ڷ�");
			
			depositface.add(Backbutton);
			
			
			main.setVisible(false);
			t1.setVisible(false);
			f.getContentPane().add(BorderLayout.CENTER, t2);
			f.getContentPane().add(BorderLayout.EAST, depositface);
			
			Backbutton.addActionListener(new BackbuttonListener(depositface,t2));
		}	
		

	}

	class wbuttonListener implements ActionListener {
		public void actionPerformed(ActionEvent e) {
			JPanel withdrawface = new JPanel();
			TextArea t2 = new TextArea("���");
			
			withdrawface.setBackground(Color.white);
			f.setLayout(new BorderLayout());

			withdrawface.setLayout(new GridLayout(5,1));

			for(int i=0 ; i<db.getBaseLength(); i++){
				if(db.getAccount(i) != null){
					withdrawface.add(new aButton(""+db.getAccount(i).getAccountnumber(), 1, db.getAccount(i)));
				}
			}
			JButton Backbutton = new JButton("�ڷ�");

			withdrawface.add(Backbutton);

			main.setVisible(false);
			t1.setVisible(false);
			f.getContentPane().add(BorderLayout.CENTER, t2);
			f.getContentPane().add(BorderLayout.EAST, withdrawface);

			Backbutton.addActionListener(new BackbuttonListener(withdrawface,t2));
		}
	}



	class tbuttonListener implements ActionListener {
		public void actionPerformed(ActionEvent e) {
			JPanel transferface = new JPanel();
			TextArea t2 = new TextArea("��ü");
			
			transferface.setBackground(Color.white);
			f.setLayout(new BorderLayout());

			transferface.setLayout(new GridLayout(5,1));

			for(int i=0 ; i<db.getBaseLength(); i++){
				if(db.getAccount(i) != null){
					transferface.add(new aButton(""+db.getAccount(i).getAccountnumber(), 2, db.getAccount(i)));
				}
			}
			JButton Backbutton = new JButton("�ڷ�");

			transferface.add(Backbutton);

			main.setVisible(false);
			t1.setVisible(false);
			f.getContentPane().add(BorderLayout.CENTER, t2);
			f.getContentPane().add(BorderLayout.EAST, transferface);

			Backbutton.addActionListener(new BackbuttonListener(transferface,t2));
		}

	}

	class abuttonListener implements ActionListener {
		public void actionPerformed(ActionEvent e) {
			JPanel manageface = new JPanel();
			TextArea t2 =  new TextArea("����");
			
			manageface.setBackground(Color.white);
			f.setLayout(new BorderLayout());
			manageface.setLayout(new GridLayout(3, 1));
			
			mbutton button1 = new mbutton("���� ����",0);
			mbutton button2 = new mbutton("���� ����",1);
			JButton Backbutton = new JButton("�ڷ�");
			
			manageface.add(button1);
			manageface.add(button2);
			manageface.add(Backbutton);
			
			main.setVisible(false);
			t1.setVisible(false);
			f.getContentPane().add(BorderLayout.CENTER, t2);
			f.getContentPane().add(BorderLayout.EAST, manageface);
			
			Backbutton.addActionListener(new BackbuttonListener(manageface,t2));
		}

	}
	
	class mbutton extends JButton implements ActionListener{
		int flag;
		public mbutton(String s,int f){
			super(s);
			flag = f;
			addActionListener(this);
		}
		public void actionPerformed(ActionEvent e) {
			if(flag == 0){
				int input = new Integer(JOptionPane.showInputDialog(null,"���� ��ȣ")).intValue();
				if(db.insert(new BankAccount(input , 0)));
					JOptionPane.showMessageDialog(null, "�Ϸ�");
			}
			else if(flag == 1){
				int input = new Integer(JOptionPane.showInputDialog(null,"���� ��ȣ")).intValue();
				if(db.delete(input));
					JOptionPane.showMessageDialog(null, "�Ϸ�");
			}
		}
	}
	
	class aButton extends JButton implements ActionListener{
		int flag;
		BankAccount account;
		public aButton(String s, int f, BankAccount a){
			super(s);
			flag = f;
			account = a;
			addActionListener(this);
		}
		public void actionPerformed(ActionEvent e){
			if(flag == -1){
				JOptionPane.showMessageDialog(null, account.resultRecord());
			}
			else if(flag == 0){
				int input = new Integer(JOptionPane.showInputDialog(null,"�ݾ�"));
				if(account.deposit(input)){
					JOptionPane.showMessageDialog(null, "�Ϸ�\n"+"���¹�ȣ:"+account.getAccountnumber()+"\n�ܾ�:"+account.getBalance());
					account.writeRecord("�Ա�", input);
					account.writeRecord("����", account.interest());
				}
			}
			else if(flag == 1){
				int input = new Integer(JOptionPane.showInputDialog(null,"�ݾ�"));
				if(account.withdraw(input)){
					JOptionPane.showMessageDialog(null, "�Ϸ�\n"+"���¹�ȣ:"+account.getAccountnumber()+"\n�ܾ�:"+account.getBalance());
					account.writeRecord("���", input);
					account.writeRecord("����", account.interest());
				}
			}
			else if(flag == 2){
				int input = new Integer(JOptionPane.showInputDialog(null,"�����ôº� ����"));
				int input1 = new Integer(JOptionPane.showInputDialog(null,"�ݾ�"));
				if(account.withdraw(input1) && db.find(input).deposit(input1)){
					JOptionPane.showMessageDialog(null, "�Ϸ�\n"+"���¹�ȣ:"+account.getAccountnumber()+"\n�ܾ�:"+account.getBalance());
					account.writeRecord("��ü", -input1);
					account.writeRecord("����", account.interest());
					db.find(input).writeRecord("��ü", input1);
					db.find(input).writeRecord("����", db.find(input).interest());
				}
			}
		}
	}
	
	class BackbuttonListener implements ActionListener {
		JPanel panel;
		TextArea text;

		public BackbuttonListener(JPanel j, TextArea t) {
			text = t;
			panel = j;
		}
		public void actionPerformed(ActionEvent arg0) {
			
			panel.setVisible(false);
			text.setVisible(false);
			main.setVisible(true);
			t1.setVisible(true);
		}
	}
}
