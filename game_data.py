question_data = [

    {"text": "Binary search is always faster than linear search",
     "answer": "False",
     "explanation": "Binary search is not always faster than linear search. For small number of elements (small N), say for example 20 elements, linear search is fast."},

    {"text": "An objective way to compare two algorithms is by comparing their execution time irrespective of the machines",
     "answer": "False",
     "explanation": "The correct way to compare two algorithms is to use big-O (asymptotic analysis)."},

    {"text": "The maximum number of nodes in a binary tree that has N levels is 2^N - 1",
     "answer": "True",
     "explanation": "The maximum number of nodes will be 2N-1."},

    {"text": "Traversing a tree in order of left, right and then root is called: Postorder traversal",
     "answer": "True",
     "explanation": "Post Order - left, right, root"},

    {"text": "An O(log N) algorithm is slower than an O(N) algorithm",
     "answer": "False",
     "explanation": "An algorithm with O(log N) time complexity is faster than O(N) algorithm. The first one is logarithmic time and the second is linear time."},

    {"text": "Most appropriate data structure to print a list of elements in reverse order is Queue data structure",
     "answer": "False",
     "explanation": "Queue uses First In First Out (FIFO), so the elements will be printed in the order they were inserted. Therefore, a stack would be more appropraite"},

    {"text": "The largest value in a binary search tree is always stored at the right most node of the tree",
     "answer": "True",
     "explanation": "The key of any node is greater than all keys occurring in its left subtree and less than all keys occurring in its right subtree."},

    {"text": "In a binary tree, every node has exactly two children.",
     "answer": "False",
     "explanation": "Not exactly two children. In a binary tree, a node can have zero, one or two children."},

    {"text": "O(1), O(n), O(nlog n), O(n^2) is the correct ascending order of time complexities (low to high time complexities)",
     "answer": "True",
     "explanation": "O(1) is constant time, O(n) denotes linear time, O(n log n) denotes linearithmic time, O(n^2) is quadratic time"},

    {"text": "Queue and Stack are the linear data structures",
     "answer": "True",
     "explanation": "The data structure where data items are organized sequentially or linearly where data elements attached one after another is called linear data structure. In linear data structure, each element can be traversed one after the other."},

    {"text": "Average case running time of Bubble sort is O(n log n)",
     "answer": "False",
     "explanation": "Average case running time of bubble sort is O(n2)."},

    {"text": "A tree having larger data than root in right sub tree and smaller data in left sub tree is called a Search Tree ",
     "answer": "False",
     "explanation": "It is called an AVL Tree"},

    {"text": "Recursive function calls use Tree data structure",
     "answer": "False",
     "explanation": "Recursive Function Calls uses Stacks."},

    {"text": "Queue is the suitable data structure for the application that tracks the customer orders in an ice cream parlor.",
     "answer": "True",
     "explanation": "Customers orders should be handled in a First In First Out (FIFO) manner."},

    {"text": "The running time of inserting an item into an unsorted list is O(n)",
     "answer": "False",
     "explanation": "The running time is O(1) for inserting an item into an unsorted list as the item can be added to the end of the list."},

    {"text": "Stack follows First In First Out (FIFO) rule",
     "answer": "False",
     "explanation": "Stack is Last In First Out (LIFO), where the last element inserted will be accessed first then the next last and so on."},

    {"text": "In a circular doubly linked list with 10 nodes, we will need to change 4 links if we want to delete a node other than the head node.",
     "answer": "False",
     "explanation": "TWe can change the link fields of the nodes that precede and follow the node we want to delete. So we just need to change 2 links if we want to delete a node other than the head node."},

    {"text": "The time complexity of adding 5 to each element of a array of N numbers is O(N).",
     "answer": "True",
     "explanation": "The time complexity will be O(N) because each element will be accessed only once to add number 5."},

    {"text": "Binary search in a sorted array is worst case O(n).",
     "answer": "True",
     "explanation": "The worst case runtime for binary search in a sorted array takes log(n) time, which is a function in O(n)"},

    {"text": "The number of collisions in a hash table is solely dependent on the table capacity and the hash function.",
     "answer": "False",
     "explanation": " The keys and collision resolution strategies also affect how many collisions there are."},

    {"text": "To find the shortest path from one vertex to another in an unweighted graph, you should use Dijkstra’s algorithm as it is the most efficient solution.",
     "answer": "False",
     "explanation": " BFS is more efficient and Dijkstra’s cannot run on an unweighted graph."},

    {"text": "A Tree data structure is used to manage printer buffer",
     "answer": "False",
     "explanation": "A queue is more appropriate is it follows the first in first out principles"},

    {"text": "Stack data structure is used in evaluating mathematical expressions with parentheses",
     "answer": "True",
     "explanation": "A stack is suitable to match the beginning and end parentheses"},

    {"text": " The following are all examples of Linear Data Structures: Polynomial, Graph, Trees",
     "answer": "False",
     "explanation": "None of the above data structures are linear data structures"},

    {"text": "A collection of one or more tree is a forest",
     "answer": "True",
     "explanation": "A forest refers to one or more trees"},

    {"text": "Quick sort runs fastest for a file that is already sorted",
     "answer": "False",
     "explanation": "Insertion sort is the fasted for already sorted files"},

    {"text": "The basic operations on the stack are Insert and Delete",
     "answer": "False",
     "explanation": " Push and Pop are the terminologies used in use of the stack"},

    {"text": "Stacks are only implemented using arrays",
     "answer": "False",
     "explanation": "Stack are implemented using arrays as well as linked list."},


    {"text": "A queue in which we can insert or delete elements from both ends is called a deque",
     "answer": "Deque",
     "explanation": "A deque allows for insertion and deletion at both ends"},

    {"text": "The time complexity of adding an element to a queue of n elements is O(n)",
     "answer": "False",
     "explanation": "The time complexity is O(1)"},

    {"text": "The time complexity of Deleting an element from a queue of n elements is O(log n)",
     "answer": "False",
     "explanation": "The time complexity is O(n)"},

    {"text": "Pre Order traversal of non empty binary tree is called Depth-First Order",
     "answer": "True",
     "explanation": "Pre Order traversal of non empty binary tree is called Depth-First Order"},

    {"text": " A node that does not have any child nodes is called a root",
     "answer": "False",
     "explanation": "A node that does not have a child is called a leaf"},

]