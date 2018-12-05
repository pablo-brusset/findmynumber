package exercice; // j'appel le package

import java.util.Scanner; // j'import mon scanner pour répondre
class usermultication {
	public static void main(String[] args)
	{
		int saisieutilisateur,i; 
		System.out.println("Enter your table choice");
		
		Scanner in=new Scanner(System.in);
		saisieutilisateur=in.nextInt();
		
		System.out.println("Multiplication table of "+saisieutilisateur);
		
		for(i=1;i<=10;i++) //Permet de signaler a mon opérateur de calculer que jusqu'à 10              		
		{
			System.out.println(saisieutilisateur+"*"+i+"="+(saisieutilisateur*i));
			in.close(); // Permet de fermer la saisie 
		}
	}
}
