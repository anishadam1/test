//Anisha Dam
//Lab # 2
//Name Translater 

public class NameTranslater {

	public static void main(String[] args) {
		
		String fullname = "          pEtER           FRedEricK   stRaWSOn   ";
		
	fullname = fullname.trim();
		
	int first = fullname.indexOf(" ");
		
	String firstname = fullname.substring(0,first).toLowerCase();
		
	int last = fullname.lastIndexOf(" ");
		
	String lastname = fullname.substring(last).trim().toLowerCase();
		
	String middlename = fullname.substring(first, last).trim().toUpperCase();
		
	String lastname_ = lastname.substring(0, 1).toUpperCase() + lastname.substring(1);

	String firstname_ = firstname.substring(0,1).toUpperCase() + firstname.substring(1);

	String middlename_ = middlename.substring(0, 1) + ".";

System.out.println(lastname_ + ',' +  ' ' + firstname_ + ' ' + middlename_);
		
		
	}

}
