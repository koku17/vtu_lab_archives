// Program 11 : Multidimensional Array in Java

/* Syntax
 * data_type[1st dimension][2nd dimension][]..[n_th dimension];
 * array_name=new data_type[size1][size2].[sizen];
 */

public class NDimArray{
	public static void main(String[] args){
		// Array [0][0] contains 1 ; [0][1] contains 2
		// [1][0] contains 3 ; [1][1] contains 4
		int[][] arr={{1,2},{3,4}};

		for(int i=0;i<2;i++)
			for(int j=0;j<2;j++)
				System.out.println("arr["+i+"]["+j+"]="+arr[i][j]);
	}
}
