/*						Program 3
 * Make a class called Employee, which models an employee with an id, name and salary designed as shown in the
 * following class diagram.
 * The method raiseSalary(percent) increase the salary given by the percentage.
 * Develop the Employee class and suitable method of demonstration.
 */

package raisesalary;

import java.util.Scanner;

class Employee{
	int empID;
	String empName;
	float empSalary;

	public void getDetailes(){
		Scanner sc=new Scanner(System.in);
		System.out.print("\nEnter the ID : ");
		empID=sc.nextInt();
		System.out.print("Enter the Name : ");
		empName=sc.next();
		System.out.print("Enter the Salary : ");
		empSalary=sc.nextInt();
	}
	
	public void raiseSalary(double percentage){
		double increaseAmount=(percentage/100)*empSalary;
		empSalary+=increaseAmount;
		System.out.println(empName+"'s Salary increased by "+percentage+"%");
		System.out.println("New Salary "+empSalary);
	}
}

public class RaiseSalary{
	public static void main(String[] args){
		Employee e1=new Employee();
		Employee e2=new Employee();
		Employee e3=new Employee();

		e1.getDetailes();
		e1.raiseSalary(100);
		e2.getDetailes();
		e2.raiseSalary(100);
		e3.getDetailes();
		e3.raiseSalary(200);
	}
}
