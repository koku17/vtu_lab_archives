#!/bin/python

import math
import heapq

class Cell:
	def __init__(self):
		self.parent_i=0
		self.parent_j=0
		self.f=float('inf')
		self.g=float('inf')
		self.h=0
ROW=9
COL=10

def is_valid(row,col):
	return row>=0 and row<ROW and col>=0 and col<COL

def is_unblocked(grid,row,col):
	return grid[row][col]==1

def is_destination(row,col,dest):
	return row==dest[0] and col==dest[1]

def calculate_h_value(row,col,dest):
	return ((row-dest[0])**2+(col-dest[1])**2)**0.5

def trace_path(cell_details,dest):
	print("The Path is ")
	path=[]
	row=dest[0]
	col=dest[1]
	while not (cell_details[row][col].parent_i==row and cell_details[row][col].parent_j==col):
		path.append((row,col))
		temp_row=cell_details[row][col].parent_i
		temp_col=cell_details[row][col].parent_j
		row=temp_row
		col=temp_col
	path.append((row,col))
	path.reverse()
	for i in path:
		print("-> ",i)
	print()

def a_star_search(grid,src,dest):
	if not is_valid(src[0],src[1]) or not is_valid(dest[0],dest[1]):
		print("Source or destination is invalid")
		return
	if not is_unblocked(grid,src[0],src[1]) or not is_unblocked(grid,dest[0],dest[1]):
		print("Source or the destination is blocked")
		return
	if is_destination(src[0],src[1],dest):
		print("We are already at the destination")
		return
	closed_list=[[False for _ in range(COL)] for _ in range(ROW)]
	cell_details=[[Cell() for _ in range(COL)] for _ in range(ROW)]
	i=src[0]
	j=src[1]
	cell_details[i][j].f=0
	cell_details[i][j].g=0
	cell_details[i][j].h=0
	cell_details[i][j].parent_i=i
	cell_details[i][j].parent_j=j
	open_list=[]
	heapq.heappush(open_list,(0.0,i,j))
	found_dest=False
	while len(open_list)>0:
		p=heapq.heappop(open_list)
		i=p[1]
		j=p[2]
		closed_list[i][j]=True
		directions=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
		for dir in directions:
			new_i=i+dir[0]
			new_j=j+dir[1]
			if is_valid(new_i,new_j) and is_unblocked(grid,new_i,new_j) and not \
				closed_list[new_i][new_j]:
				if is_destination(new_i,new_j,dest):
					cell_details[new_i][new_j].parent_i=i
					cell_details[new_i][new_j].parent_j=j
					print("The destination cell is found")
					trace_path(cell_details,dest)
					found_dest=True
					return
				else:
					g_new=cell_details[i][j].g+1.0
					h_new=calculate_h_value(new_i,new_j,dest)
					f_new=g_new+h_new
					if cell_details[new_i][new_j].f==float('inf') or \
						cell_details[new_i][new_j].f>f_new:
						heapq.heappush(open_list,(f_new,new_i,new_j))
						cell_details[new_i][new_j].f=f_new
						cell_details[new_i][new_j].g=g_new
						cell_details[new_i][new_j].h=h_new
						cell_details[new_i][new_j].parent_i=i
						cell_details[new_i][new_j].parent_j=j
	if not found_dest:
		print("Failed to find the destination cell")

def main():
	grid=[
		[1,0,1,1,1,1,0,1,1,1],
		[1,1,1,0,1,1,1,0,1,1],
		[1,1,1,0,1,1,0,1,0,1],
		[0,0,1,0,1,0,0,0,0,1],
		[1,1,1,0,1,1,1,0,1,0],
		[1,0,1,1,1,1,0,1,0,0],
		[1,0,0,0,0,1,0,0,0,1],
		[1,0,1,1,1,1,0,1,1,1],
		[1,1,1,0,0,0,1,0,0,1]
	]
	src=[8,0]
	dest=[0,0]
	a_star_search(grid,src,dest)

if __name__=="__main__":
	main()
