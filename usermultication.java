package exercice;

import java.util.Scanner;

class usermultication {
	public static void main(String[] args)
	{
		int n,c; 
		System.out.println("Entré la table de votre choix ");
		Scanner in=new Scanner(System.in);
		n=in.nextInt();
		System.out.println("Multiplication table of "+n+"is;=");
		
		for (c=1;c<=10;c++)
		{
			System.out.println(n+"*"+c+"="+(n*c));
		}
	}
}
