/**
 * Tutorial-1: https://www.youtube.com/watch?v=bLtm94mvfjE&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=75
 * Tutorial-2: https://youtu.be/O7BtCGkkPBY?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 * Tutorial-3: https://youtu.be/TQ1LlaRHaow?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 * Tutorial-4: https://www.youtube.com/watch?v=75JAn8ejI_I&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=79
 * 
 * Graph Data Structure
 *
 * A graph is a non-linear data structure that consists of a finite number of vertices (also called nodes) connected by edges.
 * Trees are a specific type of graph data structure.
 * A graph has a set of vertices (nodes) represented as circles and a set of edges represented as lines connecting the vertices.
 * There is no hierarchy in a graph, and there is no fixed way to represent a graph.
 *
 * Example Graph:
 *          B
 *        /  \
 *       A    C
 *
 * Components of a Graph:
 * - Vertices (Nodes): The fundamental units of the graph.
 * - Edges: The connections between the vertices.
 *
 * Types of Graphs:
 * 1. Directed Graph: A graph in which the edges have a direction. Edges are usually represented by arrows pointing in the direction the graph can be traversed.
 *    Example: A -> B -> C (We can traverse from A to B to C, but not from C to B to A)
 *
 * 2. Undirected Graph: A graph in which the edges are bidirectional. The graph can be traversed in either direction.
 *    Example: A - B - C (We can traverse from A to B to C and vice versa)
 *
 * Graph Properties:
 * - A graph can have one or more vertices with no edges.
 * - Multiple edges can exist from one node to another.
 * - A graph can contain cycles (a path where a node is revisited).
 * - A graph can have self-loops (an edge that connects a vertex to itself).
 * - A graph may be disconnected (some vertices are not connected to others).
 * - A graph may contain weights on edges representing the cost of traversing that edge.
 *
 * Graph Usage:
 * - Google Maps: Cities as vertices and roads as edges to help build a navigation system.
 * - Social Media: Users as vertices and connections (friendships, follows) as edges.
 *
 * Ways to Represent Graphs:
 * 1. Adjacency Matrix: 
 *    - An adjacency matrix is a 2D array of size V x V where V is the number of vertices in the graph.
 *    - Each row and column represent a vertex.
 *    - If the value of any element, say matrix[i][j], is 1, it represents that there is an edge connecting vertex i and vertex j.
 *
 * Example of Adjacency Matrix Representation:
 *          A  B  C
 *        A[0, 1, 0]
 *        B[1, 0, 1]
 *        C[0, 1, 0]
 *
 * Adjacency Matrix for the example graph:
 *          A  B  C
 *    A -> [0, 1, 0]
 *    B -> [1, 0, 1]
 *    C -> [0, 1, 0]
 */

// Example of an adjacency matrix for a simple graph
const adjacencyMatrix = [
    [0, 1, 0], // Connections for vertex A
    [1, 0, 1], // Connections for vertex B
    [0, 1, 0]  // Connections for vertex C
];

/**
 * Adjacency List:
 * - An adjacency list represents a graph as a collection of linked lists or arrays.
 * - Each vertex has a list of the vertices to which it is connected.
 * - This is more space-efficient for sparse graphs.
 *
 * Example of Adjacency List Representation:
 *    A -> B
 *    B -> A, C
 *    C -> B
 */

// Example of an adjacency list for a simple graph
const adjacencyList = {
    A: ['B'], // Connections for vertex A
    B: ['A', 'C'], // Connections for vertex B
    C: ['B'] // Connections for vertex C
};

/**
 * Big O Notation for Graph Operations:
 * - Adding an edge: O(1) for adjacency list, O(1) for adjacency matrix
 * - Removing an edge: O(E) for adjacency list, O(1) for adjacency matrix
 * - Checking if there is an edge between two vertices: O(V) for adjacency list, O(1) for adjacency matrix
 * - Space complexity: O(V + E) for adjacency list, O(V^2) for adjacency matrix
 */

/**
 * Graph Traversal Algorithms:
 * 1. Depth-First Search (DFS): Traverses as far as possible along a branch before backtracking.
 * 2. Breadth-First Search (BFS): Traverses level by level, exploring all neighbors of a vertex before moving to the next level.
 */

/*
// Example of Depth-First Search (DFS)
function dfs(graph, start) {
    const visited = new Set();
    function visit(vertex) {
        if (!visited.has(vertex)) {
            visited.add(vertex);
            console.log(vertex);
            graph[vertex].forEach(neighbor => visit(neighbor));
        }
    }
    visit(start);
}

// Example of Breadth-First Search (BFS)
function bfs(graph, start) {
    const visited = new Set();
    const queue = [start];
    visited.add(start);
    while (queue.length > 0) {
        const vertex = queue.shift();
        console.log(vertex);
        graph[vertex].forEach(neighbor => {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor);
            }
        });
    }
}

// Example usage of DFS and BFS
console.log("DFS Traversal:");
dfs(adjacencyList, 'A'); // Output: A B C

console.log("BFS Traversal:");
bfs(adjacencyList, 'A'); // Output: A B C
*/


class Graph{
    constructor(){
        this.adjacencyList = {};

    }

    addVertex(vertex){
        if(!this.adjacencyList[vertex]){
            this.adjacencyList[vertex] = new Set();
        }
    }

    addEdge(vertex1, vertex2){
        if(!this.adjacencyList[vertex1]){
            this.addVertex(vertex1);
        }

        if(!this.adjacencyList[vertex2]){
            this.addVertex(vertex2);
        }

        this.adjacencyList[vertex1].add(vertex2);
        this.adjacencyList[vertex2].add(vertex1);
    }

    removeEdge(vertex1, vertex2){
        this.adjacencyList[vertex1].delete(vertex2);
        this.adjacencyList[vertex2].delete(vertex1);
    }

    removeVertex(vertex){
        if(!this.adjacencyList[vertex])return;
        
        for (const adjacencyVertex of this.adjacencyList[vertex]) {
            this.removeEdge(vertex, adjacencyVertex);
        }

        delete this.adjacencyList[vertex];
    }

    hasEdge(vertex1, vertex2){
        return (
            this.adjacencyList[vertex1].has(vertex2) && 
            this.adjacencyList[vertex2].has(vertex1)
        )
    }

    display(){
        for (let vertex in this.adjacencyList) {
            console.log(vertex + " -> " + [...this.adjacencyList[vertex]]);
        }
    }
}

const graph = new Graph();
graph.addVertex("A");
graph.addVertex("B");
graph.addVertex("C");

graph.addEdge("A", "B");
graph.addEdge("B", "C");



graph.display();
console.log(graph.hasEdge("A", "B"));
console.log(graph.hasEdge("A", "C"));
// graph.removeEdge("A", "B");
graph.removeVertex("B");

graph.display();








