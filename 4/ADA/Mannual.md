
# ADA Lab Manual (BCSL404)

## Program 1: Kruskal's Algorithm - Minimum Spanning Tree
**Logic**: Greedily select the smallest edges ensuring no cycles using union-find.  
**Time Complexity**: O(E log E)

```c
#include<stdio.h>
void kruskals();
int c[10][10], n;

int main() {
    int i, j;
    printf("Enter the number of vertices:\n");
    scanf("%d", &n);
    printf("Enter the cost matrix:\n");
    for(i = 1; i <= n; i++)
        for(j = 1; j <= n; j++)
            scanf("%d", &c[i][j]);
    kruskals();
    return 0;
}

void kruskals() {
    int i, j, u, v, a, b, min;
    int ne = 0, mincost = 0;
    int parent[10];
    for(i = 1; i <= n; i++) parent[i] = 0;

    while(ne != n-1) {
        min = 9999;
        for(i = 1; i <= n; i++)
            for(j = 1; j <= n; j++)
                if(c[i][j] < min) {
                    min = c[i][j];
                    u = a = i;
                    v = b = j;
                }
        while(parent[u]) u = parent[u];
        while(parent[v]) v = parent[v];
        if(u != v) {
            printf("\n %d ----- >%d=%d\n", a, b, min);
            parent[v] = u;
            ne++;
            mincost += min;
        }
        c[a][b] = c[b][a] = 9999;
    }
    printf("\n Mincost = %d\n", mincost);
}
```

**Sample Output**:
```
1 ----- >4=9
1 ----- >2=10
1 ----- >3=15
2 ----- >5=15
Mincost = 49
```

## Program 2: Prim's Algorithm - Minimum Spanning Tree
**Logic**: Greedy edge selection from connected component.  
**Time Complexity**: O(V^2)

```c
#include<stdio.h>
void prims();
int c[10][10],n;

void main() {
    int i,j;
    printf("Enter the number of vertices:\n");
    scanf("%d",&n);
    printf("Enter the cost matrix:\n");
    for(i = 1; i <= n; i++)
        for(j = 1; j <= n; j++)
            scanf("%d", &c[i][j]);
    prims();
}

void prims() {
    int i,j,u,v,min;
    int ne=0,mincost=0;
    int elec[10];
    for(i=1;i<=n;i++) elec[i]=0;
    elec[1]=1;

    while(ne != n-1) {
        min = 9999;
        for(i = 1; i <= n; i++) {
            for(j = 1; j <= n; j++) {
                if(elec[i]==1 && c[i][j] < min) {
                    min=c[i][j]; u=i; v=j;
                }
            }
        }
        if(elec[v]!=1) {
            printf("\n %d ----- >%d=%d\n", u, v, min);
            elec[v] = u;
            ne++;
            mincost += min;
        }
        c[u][v] = c[v][u] = 9999;
    }
    printf("\n Mincost = %d\n", mincost);
}
```

**Sample Output**:
```
1 ----- >4=9
1 ----- >2=10
1 ----- >3=15
2 ----- >5=15
Mincost = 49
```
## Program 3a: Floyd's Algorithm - All Pairs Shortest Paths

**Logic**:  
Floyd’s algorithm is a Dynamic Programming technique that finds the shortest distances between every pair of vertices in a weighted graph (including negative weights but no negative cycles).

**Time Complexity**: `O(n^3)`

```c
#include<stdio.h>
#define INF 999

int min(int a,int b) {
    return(a<b)?a:b;
}

void floyd(int p[ ][10],int n) {
    int i,j,k;
    for(k=1;k<=n;k++)
        for(i=1;i<=n;i++)
            for(j=1;j<=n;j++)
                p[i][j]=min(p[i][j],p[i][k]+p[k][j]);
}

void main() {
    int a[10][10],n,i,j;
    printf("\nEnter the n value:");
    scanf("%d",&n);
    printf("\nEnter the graph data:\n");
    for(i=1;i<=n;i++)
        for(j=1;j<=n;j++)
            scanf("%d",&a[i][j]);

    floyd(a,n);

    printf("\nShortest path matrix:\n");
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            if (a[i][j] == INF)
                printf("%4s", "INF");
            else
                printf("%4d", a[i][j]);
        }
        printf("\n");
    }
}

## Program 3b: Warshall's Algorithm - Transitive Closure

**Logic**:  
Warshall’s algorithm determines the transitive closure of a graph by checking for reachability between every pair of vertices.  
If there is a path from vertex `i` to vertex `j`, then `p[i][j]` becomes 1.  

**Time Complexity**: `O(n^3)`

```c
#include<stdio.h>

void warsh(int p[ ][10],int n) {
    int i,j,k;
    for(k=1;k<=n;k++)
        for(i=1;i<=n;i++)
            for(j=1;j<=n;j++)
                p[i][j]=p[i][j] || (p[i][k] && p[k][j]);
}

void main() {
    int a[10][10],n,i,j;
    printf("\\nEnter the n value:");
    scanf("%d",&n);
    printf("\\nEnter the graph data:\\n");
    for(i=1;i<=n;i++)
        for(j=1;j<=n;j++)
            scanf("%d",&a[i][j]);

    warsh(a,n);

    printf("\\nResultant path matrix\\n");
    for(i=1;i<=n;i++) {
        for(j=1;j<=n;j++)
            printf("%d ",a[i][j]);
        printf("\\n");
    }
}
```

**Sample Output**:
```
Enter the n value: 4
Enter the graph data:
0 1 0 0
0 0 0 1
0 0 0 0
1 0 1 0

Resultant path matrix
1 1 1 1
1 1 1 1
0 0 0 0
1 1 1 1
```
## Program 3b: Warshall's Algorithm - Transitive Closure

**Logic**:  
Warshall’s algorithm determines the transitive closure of a graph by checking for reachability between every pair of vertices.  
If there is a path from vertex `i` to vertex `j`, then `p[i][j]` becomes 1.  

**Time Complexity**: `O(n^3)`

```c
#include<stdio.h>

void warsh(int p[ ][10],int n) {
    int i,j,k;
    for(k=1;k<=n;k++)
        for(i=1;i<=n;i++)
            for(j=1;j<=n;j++)
                p[i][j]=p[i][j] || (p[i][k] && p[k][j]);
}

void main() {
    int a[10][10],n,i,j;
    printf("\\nEnter the n value:");
    scanf("%d",&n);
    printf("\\nEnter the graph data:\\n");
    for(i=1;i<=n;i++)
        for(j=1;j<=n;j++)
            scanf("%d",&a[i][j]);

    warsh(a,n);

    printf("\\nResultant path matrix\\n");
    for(i=1;i<=n;i++) {
        for(j=1;j<=n;j++)
            printf("%d ",a[i][j]);
        printf("\\n");
    }
}
```

**Sample Output**:
```
Enter the n value: 4
Enter the graph data:
0 1 0 0
0 0 0 1
0 0 0 0
1 0 1 0

Resultant path matrix
1 1 1 1
1 1 1 1
0 0 0 0
1 1 1 1
```
## Program 4: Dijkstra's Algorithm - Single Source Shortest Path

**Logic**:  
Dijkstra’s algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative edge weights. It uses a greedy approach to pick the nearest unvisited vertex.

**Time Complexity**:  
- O(V²) with adjacency matrix  
- O(E log V) with priority queue and adjacency list

```c
#include<stdio.h>
#define INF 999

void dijkstra(int c[10][10], int n, int s, int d[10]) {
    int v[10], min, u, i, j;
    for(i = 1; i <= n; i++) {
        d[i] = c[s][i];
        v[i] = 0;
    }
    v[s] = 1;

    for(i = 1; i <= n; i++) {
        min = INF;
        for(j = 1; j <= n; j++) {
            if(v[j] == 0 && d[j] < min) {
                min = d[j];
                u = j;
            }
        }
        v[u] = 1;
        for(j = 1; j <= n; j++) {
            if(v[j] == 0 && (d[u] + c[u][j]) < d[j]) {
                d[j] = d[u] + c[u][j];
            }
        }
    }
}

int main() {
    int c[10][10], d[10], i, j, s, n;
    printf("\\nEnter n value:");
    scanf("%d", &n);
    printf("\\nEnter the graph data:\\n");
    for(i = 1; i <= n; i++)
        for(j = 1; j <= n; j++)
            scanf("%d", &c[i][j]);
    printf("\\nEnter the source node:");
    scanf("%d", &s);
    dijkstra(c, n, s, d);
    for(i = 1; i <= n; i++)
        printf("\\nShortest distance from %d to %d is %d", s, i, d[i]);
    return 0;
}
```

**Sample Output**:
```
Enter n value: 6
Enter the graph data:
0 15 10 999 45 999
999 0 15 999 20 999
20 999 0 20 999 999
999 10 999 0 35 999
999 999 999 30 0 999
999 999 999 4 999 0

Enter the source node: 2

Shortest distance from 2 to 1 is 35
Shortest distance from 2 to 2 is 0
Shortest distance from 2 to 3 is 15
Shortest distance from 2 to 4 is 35
Shortest distance from 2 to 5 is 20
Shortest distance from 2 to 6 is 999
```

## Program 5: Topological Sort - Source Removal Method

**Logic**:  
Topological sorting of a Directed Acyclic Graph (DAG) gives a linear ordering of vertices such that for every directed edge `u → v`, vertex `u` comes before `v`.  
This implementation uses the **source removal** technique where we repeatedly remove nodes with in-degree 0.

**Time Complexity**: `O(V + E)`

```c
#include<stdio.h>
#include<stdlib.h>

int a[10][10], n, indegree[10];

void find_degree() {
    int i, j, sum;
    for(j = 0; j < n; j++) {
        sum = 0;
        for(i = 0; i < n; i++)
            sum += a[i][j];
        indegree[j] = sum;
    }
}

void topo() {
    int i, u, v, t[10], s[10], top = -1, k = 0;

    find_degree();

    for(i = 0; i < n; i++) {
        if(indegree[i] == 0)
            s[++top] = i;
    }

    while(top != -1) {
        u = s[top--];
        t[k++] = u;
        for(v = 0; v < n; v++) {
            if(a[u][v] == 1) {
                indegree[v]--;
                if(indegree[v] == 0)
                    s[++top] = v;
            }
        }
    }

    printf("Topological Ordering:\\n");
    for(i = 0; i < k; i++)
        printf("%d\\t", t[i]);
}

void main() {
    int i, j;
    printf("Enter the number of nodes:\\n");
    scanf("%d", &n);
    printf("Enter the adjacency matrix:\\n");
    for(i = 0; i < n; i++)
        for(j = 0; j < n; j++)
            scanf("%d", &a[i][j]);

    topo();
}
```

**Sample Output**:
```
Enter the number of nodes: 5
Enter the adjacency matrix:
0 1 0 0 0
0 0 0 1 0
0 1 0 0 0
0 0 0 0 1
0 0 0 0 0

Topological Ordering:
2 0 1 3 4
```
## Program 6: 0/1 Knapsack Problem - Dynamic Programming

**Logic**:  
In the 0/1 Knapsack problem, each item must either be included or excluded from the knapsack to maximize total profit without exceeding the weight capacity.  
This implementation uses recursion and includes memoization-like logic.

**Time Complexity**: `O(n × W)`  
Where `n` = number of items, `W` = knapsack capacity.

```c
#include<stdio.h>

int w[10], p[10], n;

int max(int a, int b) {
    return a > b ? a : b;
}

int knap(int i, int m) {
    if (i == n) 
        return w[i] > m ? 0 : p[i];
    if (w[i] > m) 
        return knap(i + 1, m);
    return max(knap(i + 1, m), knap(i + 1, m - w[i]) + p[i]);
}

void main() {
    int m, i, max_profit;
    printf("\\nEnter the number of objects:");
    scanf("%d", &n);
    printf("\\nEnter the knapsack capacity:");
    scanf("%d", &m);
    printf("\\nEnter profit followed by weight:\\n");
    for (i = 1; i <= n; i++)
        scanf("%d %d", &p[i], &w[i]);
    max_profit = knap(1, m);
    printf("\\nMax profit = %d\\n", max_profit);
}
```

**Sample Output**:
```
Enter the number of objects: 7
Enter the knapsack capacity: 15
Enter profit followed by weight:
10 2
5 3
15 5
7 7
6 1
18 4
3 1

Max profit = 54
```
