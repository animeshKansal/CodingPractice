package LibraryCatalogue;

public class Book {

	// properties
	String title;
	int pages;
	int ISBN;
	boolean isCheckedOut; // whether checked out or not
	int dayCheckOut = -1;

	// Constructor
	public Book(String bookTitle, int bookPageCount, int bookISBN) {
		this.title = bookTitle;
		this.pages = bookPageCount;
		this.ISBN = bookISBN;
		isCheckedOut = false;

	}

	// Getters - Instance Methods
	public String getTitle() {
		return this.title;
	}

	public int getPageCount() {
		return this.pages;
	}

	public int getISBN() {
		return this.ISBN;
	}

	public boolean getIsCheckedOut() {
		return this.isCheckedOut;
	}

	public int getDayCheckedOut() {
		return this.dayCheckOut;
	}

	// Setters
	public void setIsCheckedOut(boolean newIsCheckedOut, int currentDayCheckOut) {
		this.isCheckedOut = newIsCheckedOut;
		setDayCheckedOut(currentDayCheckOut);
	}

	private void setDayCheckedOut(int day) {
		this.dayCheckOut = day;
	}

}
