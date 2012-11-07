
public class Database {
	private BankAccount[] base;
	private int NOT_FOUND = -1;

	public Database(int initial_size) {
		if (initial_size <= 0)
			initial_size = 1;
		base = new BankAccount[initial_size];
	}
	public int getBaseLength(){
		return base.length;
	}
	public BankAccount getAccount(int i){
		return base[i];
	}
	private int findLocation(int k) {
		for (int i = 0; i < base.length; i++)
			if (base[i] != null && base[i].getAccountnumber() == k)
				return i;
		return NOT_FOUND;
	}

	private int findEmpty() {
		for (int i = 0; i < base.length; i++)
			if (base[i] == null)
				return i;
		return NOT_FOUND;
	}

	public BankAccount find(int k) {
		int index = findLocation(k);
		if (index != NOT_FOUND)
			return base[index];
		else
			return null;
	}

	public boolean delete(int k) {
		int index = findLocation(k);
		if (index != NOT_FOUND) {
			base[index] = null;
			return true;
		} else
			return false;
	}

	public boolean insert(BankAccount r) {
		if (findLocation(r.getAccountnumber()) != NOT_FOUND)
			return false;
		int index = findEmpty();
		if (index != NOT_FOUND)
			base[index] = r;
		else {
			BankAccount[] temp = new BankAccount[base.length * 2];
			for (int i = 0; i < base.length; i++)
				temp[i] = base[i];
			temp[base.length] = r;
			base = temp;
		}
		return true;
	}
}