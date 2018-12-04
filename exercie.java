package exercice;

import java.util.Scanner;

public class exercie{
	public static void main (String[]args ){
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Saisissez votre prénom :");
		String str = sc.nextLine();
		System.out.println("Salut"+ " " + str);
		sc.close();	
	}
}
