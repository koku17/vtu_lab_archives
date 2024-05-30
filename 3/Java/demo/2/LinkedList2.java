//Linked List implementation in java

package com.sample;

import java.util.LinkedList;

public class LinkedList2{
	public static void main(String[] args){
		// TODO Auto-generated method stub
		// Creating object of the
		// class linked list
		LinkedList<String> ll=new LinkedList<String>();

		// Adding elements to the linked list
		ll.add("B");
		ll.add("C");
		ll.addFirst("A");
		ll.addLast("D");
		//ll.add(1, "F");
		System.out.println(ll);

		// Remove options
		ll.remove("B");
		ll.remove(2);
		// ll.removeFirst();
		// ll.removeLast();

		System.out.println(ll);
	}
}

