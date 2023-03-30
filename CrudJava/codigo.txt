package aaa;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    static List<Livro> livros = new ArrayList<>(); //Lista que armazenará os Livros

    
    
    
    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	
    	int op = 1;

    	while(op != 0) {
    		System.out.println("-------MENU-------");
    		System.out.println("1 - Cadastrar");
    		System.out.println("2 - Visualizar");
    		System.out.println("3 - Atualizar");
    		System.out.println("4 - Deletar");
    		System.out.println("0 - FIM");
    		op = sc.nextInt();
    	
    		switch(op) {
    		case 1:
    			System.out.println("-x-x-x-x-x-");
		        //Adicionando alguns Livros
    			String titulo;
    			String autor;
    			String genero;
    			
    			sc.nextLine();
    			System.out.print("Digite o Nome do Livro: ");
    			titulo = sc.nextLine();
    			
    			System.out.print("Nome do Autor: ");
    			autor = sc.nextLine();
    			
    			System.out.print("Genero: ");
    			genero = sc.nextLine();
    			
    			Livro livro1 = new Livro(titulo, autor, genero);
		        
		        adicionarLivro(livro1);
		        System.out.println("\n");
		        break;
		        
    		case 2:
    			System.out.println("-x-App Livros-x-");
		        //Exibindo todos os Livros
		        exibirLivros();
		        break;
	
    		case 3:
    			System.out.println("-x-x-x-x-x-");
		        //Atualizando o email da Maria
    			
    	        //Exibindo todos os Livros novamente
    	        exibirLivros();
    			
    			//Nome do Livro que desejo atualizar
    			String antigoTitulo;
    			sc.nextLine();
    			System.out.print("Qual o Nome do Livro que deseja Atualizar: ");
    			antigoTitulo = sc.nextLine();
    			
    			//Passar registro para atualizar
    			String novoTitulo;
    			String novoAutor;
    			String novoGenero;
    			
    			System.out.print("Nome do Novo Titulo: ");
    			novoTitulo = sc.nextLine();
    			System.out.print("Nome do Novo Autor: ");
    			novoAutor = sc.nextLine();
    			System.out.print("Classe Genero do Livro: ");
    			novoGenero = sc.nextLine();
    			
		        Livro livroAtualizado = new Livro(novoTitulo, novoAutor, novoGenero);
		        atualizarLivro(antigoTitulo, livroAtualizado);
		        break;
	
    		case 4:
    			System.out.println("-x-x-x-x-x-");
    			
    			//Exibindo todos os Livros novamente
    	        exibirLivros();
    	        
		        //Removendo Livro
		        String n;
    			sc.nextLine();
    			System.out.print("Que Livro você deseja Apagar: ");
    			n = sc.nextLine();
    			removerLivro(n);
		        break;
		        
    		case 0:
				System.out.println("Até a próxima!");
				break;
			
			default:
				System.out.println("Nao entendi");
				break;
    		}
    	}
    	sc.close();
    }
    
    
    
    
 
		
    
/*--CRUD--*/
    
    /*CREATE*/
    //Método para adicionar um Livro
    public static void adicionarLivro(Livro livro) {
        livros.add(livro);
    }

    
    /*READ*/
    //Método para exibir todos os Livros
    public static void exibirLivros() {
        System.out.println("Livros:");
        for (Livro livro : livros) {
            System.out.println(livro);
        }
        System.out.println();
    }
    
    
    /*UPDATE*/
    //Método para atualizar um Livro
    public static void atualizarLivro(String tituloAntigo, Livro livroAtualizada) {
        for (int i = 0; i < livros.size(); i++) {
            Livro livro = livros.get(i);
            if (livro.getTitulo().equals(tituloAntigo)) {
                livros.set(i, livroAtualizada);
                break;
            }
        }
    }

    
    /*DELETE*/
    //Método para remover um Livro
    public static void removerLivro(String name){//Livro livro) {
    	for (int i = 0; i<livros.size(); i++) {
    		Livro livro = livros.get(i);
    		if (livro.getTitulo().equals(name)) {
    			livros.remove(livro);
    		}
    	} 
    }

}








class Livro {
    private String titulo;
    private String autor;
    private String genero;

    
    public Livro(String titulo, String autor, String genero) {
        this.titulo = titulo;
        this.autor = autor;
        this.genero = genero;
    }
    
    
    public String getTitulo() {
        return titulo;
    }
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }
    
    
    public String getAutor() {
        return autor;
    }
    public void setAutor(String autor) {
        this.autor = autor;
    }
    
    
    public String getGenero() {
        return genero;
    }
    public void setGenero(String genero) {
        this.genero = genero;
    }

    
    @Override
    public String toString() {
        return "Titulo -> ("+titulo+") | Autor -> ("+autor+") | Genero -> ("+genero+")";
    }
}