// Program to showcase Control Statements in Java
// if, if-else, if-else if-else, nested if-else, switch statement

package com.sample;

class Product{
	String name;
	float cost;

	void valueOfCost(int cost){
		if(cost<100)
			System.out.println("Cost is less than 100");
		else if(cost>100&&cost<500)
			System.out.println("Cost between 100 and 500");
		else
			System.out.println("Cost more than 500");
	}
}

public class Control{
	public static void main(String[] args){
		Product p=new Product();
		p.valueOfCost(50);
		p.valueOfCost(220);
		p.valueOfCost(700);
	}
}
