/*
 *				Program 1
 * Develop a java program to add two matrices of suitable order N
 */

package matrixaddition;

import java.util.Scanner;

public class MatrixAddition{
	public static void main(String[] args){
		Scanner scanner=new Scanner(System.in);

		// Input the order of the matrix
		System.out.print("Enter the number of rows (N) : ");
		int N=scanner.nextInt();

		// Initialize the two matrices
		int[][] matrix1=new int[N][N];
		int[][] matrix2=new int[N][N];

		// Input the elements of the matrices
		System.out.println("Enter the elements of the first matrix :");
		for(int i=0;i<N;i++)
			for(int j=0;j<N;j++)
				matrix1[i][j]=scanner.nextInt();

		System.out.println("Enter the elements of the second matrix :");
		for(int i=0;i<N;i++)
			for(int j=0;j<N;j++)
				matrix2[i][j]=scanner.nextInt();

		// Add the matrices then store the results in new matrix and display them
		int[][] resultMatrix=new int[N][N];
		System.out.println("Resultant matrix after addition :");	
		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++){
				resultMatrix[i][j]=matrix1[i][j]+matrix2[i][j];
				System.out.print(resultMatrix[i][j]+" ");
			}
			System.out.println("");
		}
		scanner.close();
	}
}
