"""
Centralized Question Bank for all 6 subjects in LearnGap.
Each subject contains exactly 10 questions across 5 topics (2 questions per topic).
"""

SUBJECTS = {
    "python": {
        "id": "python",
        "name": "Python Programming",
        "badge_num": "01",
        "description": "Evaluate your understanding of Python syntax, data types, control flow, functions, and data structures.",
        "topics": [
            "Python Basics",
            "Variables and Data Types",
            "Control Statements",
            "Functions",
            "Lists, Tuples and Dictionaries"
        ],
        "questions": [
            {
                "id": 1,
                "topic": "Python Basics",
                "question": "What is the output of print(2 ** 3) in Python?",
                "options": ["6", "8", "9", "5"],
                "answer": "8",
                "explanation": "** is Python's exponentiation operator, so 2 ** 3 = 8."
            },
            {
                "id": 2,
                "topic": "Python Basics",
                "question": "Which of the following is an invalid identifier in Python?",
                "options": ["_my_var", "my_var2", "2my_var", "myVar"],
                "answer": "2my_var",
                "explanation": "Python variable names cannot begin with a number."
            },
            {
                "id": 3,
                "topic": "Variables and Data Types",
                "question": "What is the data type of the expression: type((4,))?",
                "options": ["int", "list", "tuple", "set"],
                "answer": "tuple",
                "explanation": "A comma inside parentheses defines a single-element tuple."
            },
            {
                "id": 4,
                "topic": "Variables and Data Types",
                "question": "Which data type in Python is immutable?",
                "options": ["list", "dict", "set", "str"],
                "answer": "str",
                "explanation": "Strings, tuples, and numbers are immutable in Python."
            },
            {
                "id": 5,
                "topic": "Control Statements",
                "question": "What does the 'break' statement do inside a loop?",
                "options": [
                    "Skips the current iteration",
                    "Terminates the loop completely",
                    "Restarts the loop from beginning",
                    "Causes a syntax error"
                ],
                "answer": "Terminates the loop completely",
                "explanation": "The break statement terminates the enclosing loop immediately."
            },
            {
                "id": 6,
                "topic": "Control Statements",
                "question": "What is the output of: for i in range(1, 5, 2): print(i, end=' ')?",
                "options": ["1 2 3 4 5", "1 3 5", "1 3", "2 4"],
                "answer": "1 3",
                "explanation": "range(1, 5, 2) starts at 1, stops before 5, stepping by 2, yielding 1 and 3."
            },
            {
                "id": 7,
                "topic": "Functions",
                "question": "Which keyword is used to create an anonymous inline function in Python?",
                "options": ["def", "lambda", "func", "inline"],
                "answer": "lambda",
                "explanation": "Lambda expressions create small anonymous functions."
            },
            {
                "id": 8,
                "topic": "Functions",
                "question": "What does *args indicate in a Python function definition?",
                "options": [
                    "Keyword arguments as a dictionary",
                    "Arbitrary number of positional arguments as a tuple",
                    "A mandatory single argument",
                    "A pointer to memory"
                ],
                "answer": "Arbitrary number of positional arguments as a tuple",
                "explanation": "*args packs arbitrary positional arguments into a tuple."
            },
            {
                "id": 9,
                "topic": "Lists, Tuples and Dictionaries",
                "question": "What method is used to remove and return an item from a list at a given index?",
                "options": ["pop()", "remove()", "delete()", "discard()"],
                "answer": "pop()",
                "explanation": "list.pop([i]) removes and returns the item at the specified index."
            },
            {
                "id": 10,
                "topic": "Lists, Tuples and Dictionaries",
                "question": "Which statement correctly retrieves a value from dictionary 'd' without throwing KeyError if key 'k' is missing?",
                "options": ["d[k]", "d.get(k)", "d.fetch(k)", "d.search(k)"],
                "answer": "d.get(k)",
                "explanation": "d.get(k) returns None or a default value instead of raising KeyError."
            }
        ]
    },

    "ml": {
        "id": "ml",
        "name": "Machine Learning",
        "badge_num": "02",
        "description": "Assess your knowledge of core machine learning concepts, algorithms, and evaluation metrics.",
        "topics": [
            "Linear Regression",
            "Logistic Regression",
            "Decision Tree",
            "K-Means",
            "PCA"
        ],
        "questions": [
            {
                "id": 1,
                "topic": "Linear Regression",
                "question": "What is the main purpose of Linear Regression?",
                "options": [
                    "Classification",
                    "Predicting continuous values",
                    "Clustering data",
                    "Dimensionality reduction"
                ],
                "answer": "Predicting continuous values",
                "explanation": "Linear regression models continuous numerical outcomes."
            },
            {
                "id": 2,
                "topic": "Linear Regression",
                "question": "Which metric is commonly used to measure error in Linear Regression?",
                "options": [
                    "Mean Squared Error",
                    "Accuracy",
                    "Precision",
                    "Recall"
                ],
                "answer": "Mean Squared Error",
                "explanation": "MSE calculates the average squared difference between predictions and actual values."
            },
            {
                "id": 3,
                "topic": "Logistic Regression",
                "question": "Logistic Regression is mainly used for:",
                "options": [
                    "Classification",
                    "Clustering",
                    "Sorting",
                    "Dimensionality reduction"
                ],
                "answer": "Classification",
                "explanation": "Logistic regression predicts categorical outcomes and probabilities."
            },
            {
                "id": 4,
                "topic": "Logistic Regression",
                "question": "Which function is commonly used in Logistic Regression?",
                "options": [
                    "ReLU",
                    "Sigmoid",
                    "Softmax only",
                    "Linear"
                ],
                "answer": "Sigmoid",
                "explanation": "Sigmoid squashes linear combination scores into [0, 1] probability."
            },
            {
                "id": 5,
                "topic": "Decision Tree",
                "question": "What is a Decision Tree used for?",
                "options": [
                    "Classification and Regression",
                    "Only clustering",
                    "Only dimensionality reduction",
                    "Only data visualization"
                ],
                "answer": "Classification and Regression",
                "explanation": "Decision trees can perform both classification and regression tasks."
            },
            {
                "id": 6,
                "topic": "Decision Tree",
                "question": "Which of these can be used to split nodes in a Decision Tree?",
                "options": [
                    "Gini Impurity",
                    "Mean Squared Error only",
                    "Cosine Similarity",
                    "Euclidean Distance only"
                ],
                "answer": "Gini Impurity",
                "explanation": "Gini Impurity and Information Gain measure node split purity."
            },
            {
                "id": 7,
                "topic": "K-Means",
                "question": "K-Means is an example of which type of learning?",
                "options": [
                    "Supervised Learning",
                    "Unsupervised Learning",
                    "Reinforcement Learning",
                    "Deep Learning only"
                ],
                "answer": "Unsupervised Learning",
                "explanation": "K-Means groups unlabeled data without target labels."
            },
            {
                "id": 8,
                "topic": "K-Means",
                "question": "What does K represent in K-Means?",
                "options": [
                    "Number of features",
                    "Number of clusters",
                    "Number of datasets",
                    "Number of iterations only"
                ],
                "answer": "Number of clusters",
                "explanation": "K specifies the predetermined number of cluster centroids."
            },
            {
                "id": 9,
                "topic": "PCA",
                "question": "What is the main purpose of PCA?",
                "options": [
                    "Classification",
                    "Dimensionality reduction",
                    "Data labeling",
                    "Clustering only"
                ],
                "answer": "Dimensionality reduction",
                "explanation": "PCA projects high-dimensional data onto orthogonal components of max variance."
            },
            {
                "id": 10,
                "topic": "PCA",
                "question": "PCA stands for:",
                "options": [
                    "Principal Component Analysis",
                    "Primary Classification Algorithm",
                    "Predictive Component Algorithm",
                    "Principal Classification Analysis"
                ],
                "answer": "Principal Component Analysis",
                "explanation": "PCA stands for Principal Component Analysis."
            }
        ]
    },

    "dsa": {
        "id": "dsa",
        "name": "Data Structures",
        "badge_num": "03",
        "description": "Test your mastery of fundamental data structures including arrays, linked lists, stacks, queues, and trees.",
        "topics": [
            "Arrays",
            "Linked Lists",
            "Stacks",
            "Queues",
            "Trees"
        ],
        "questions": [
            {
                "id": 1,
                "topic": "Arrays",
                "question": "What is the time complexity to access an element by index in a contiguous array?",
                "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
                "answer": "O(1)",
                "explanation": "Array indexing uses direct memory offset arithmetic for constant time O(1) access."
            },
            {
                "id": 2,
                "topic": "Arrays",
                "question": "What happens when you insert an element at the beginning of a dynamic array of size N?",
                "options": [
                    "All N existing elements must be shifted right",
                    "No elements need to be shifted",
                    "The array automatically shrinks",
                    "Only the last element is moved"
                ],
                "answer": "All N existing elements must be shifted right",
                "explanation": "Inserting at index 0 requires shifting all existing N elements to index i+1 (O(N) time)."
            },
            {
                "id": 3,
                "topic": "Linked Lists",
                "question": "What is a primary advantage of a Singly Linked List over a standard Array?",
                "options": [
                    "Random access in O(1) time",
                    "Dynamic size and efficient O(1) insertion/deletion at head",
                    "Better cache locality and memory contiguity",
                    "No memory overhead for pointers"
                ],
                "answer": "Dynamic size and efficient O(1) insertion/deletion at head",
                "explanation": "Linked lists can easily insert or delete nodes without shifting or pre-allocating contiguous memory."
            },
            {
                "id": 4,
                "topic": "Linked Lists",
                "question": "In a Doubly Linked List, what does each node store besides data?",
                "options": [
                    "Two data values",
                    "Pointers to both the Next and Previous nodes",
                    "Only a pointer to the Next node",
                    "The size of the whole list"
                ],
                "answer": "Pointers to both the Next and Previous nodes",
                "explanation": "Doubly linked list nodes store pointers to both predecessor and successor nodes."
            },
            {
                "id": 5,
                "topic": "Stacks",
                "question": "Which principle governs the order of insertion and removal in a Stack?",
                "options": [
                    "FIFO (First In First Out)",
                    "LIFO (Last In First Out)",
                    "Random Order",
                    "Priority Order"
                ],
                "answer": "LIFO (Last In First Out)",
                "explanation": "Stacks operate on Last-In, First-Out (LIFO) semantics."
            },
            {
                "id": 6,
                "topic": "Stacks",
                "question": "Which of the following applications typically relies on a Stack data structure?",
                "options": [
                    "Function call recursion and call stack",
                    "Printer spooling queue",
                    "Round-robin CPU scheduling",
                    "Breadth-First Search"
                ],
                "answer": "Function call recursion and call stack",
                "explanation": "Function calls, undo operations, and syntax parsing naturally utilize stacks."
            },
            {
                "id": 7,
                "topic": "Queues",
                "question": "A standard Queue data structure operates on which principle?",
                "options": [
                    "LIFO (Last In First Out)",
                    "FIFO (First In First Out)",
                    "FILO (First In Last Out)",
                    "Hierarchical Ordering"
                ],
                "answer": "FIFO (First In First Out)",
                "explanation": "Queues operate on First-In, First-Out (FIFO) semantics."
            },
            {
                "id": 8,
                "topic": "Queues",
                "question": "What is the primary benefit of a Circular Queue over a standard linear array queue?",
                "options": [
                    "Eliminates memory waste from false overflow",
                    "Allows searching in O(1) time",
                    "Sorts elements automatically",
                    "Supports LIFO ordering"
                ],
                "answer": "Eliminates memory waste from false overflow",
                "explanation": "Circular queues reuse previously vacated front slots as rear wraps around."
            },
            {
                "id": 9,
                "topic": "Trees",
                "question": "In a Binary Search Tree (BST), which property holds true for every node?",
                "options": [
                    "Left child < Root < Right child",
                    "Left child > Root > Right child",
                    "All leaf nodes have depth 0",
                    "All nodes must have exactly two children"
                ],
                "answer": "Left child < Root < Right child",
                "explanation": "BST property requires left subtree keys < node key < right subtree keys."
            },
            {
                "id": 10,
                "topic": "Trees",
                "question": "Which tree traversal visits nodes in the order: Left Subtree, Root, Right Subtree?",
                "options": [
                    "Pre-order Traversal",
                    "In-order Traversal",
                    "Post-order Traversal",
                    "Level-order Traversal"
                ],
                "answer": "In-order Traversal",
                "explanation": "In-order traversal visits Left, Root, Right (producing sorted keys in a BST)."
            }
        ]
    },

    "cn": {
        "id": "cn",
        "name": "Computer Networks",
        "badge_num": "04",
        "description": "Evaluate your understanding of network models, IP addressing, routing protocols, and transport layer behavior.",
        "topics": [
            "OSI Model",
            "TCP/IP",
            "IP Addressing",
            "Routing",
            "TCP and UDP"
        ],
        "questions": [
            {
                "id": 1,
                "topic": "OSI Model",
                "question": "How many layers are in the ISO/OSI Reference Model?",
                "options": ["4", "5", "7", "8"],
                "answer": "7",
                "explanation": "OSI has 7 layers: Physical, Data Link, Network, Transport, Session, Presentation, Application."
            },
            {
                "id": 2,
                "topic": "OSI Model",
                "question": "Which OSI layer is responsible for end-to-end communication, error recovery, and flow control?",
                "options": [
                    "Network Layer",
                    "Transport Layer",
                    "Data Link Layer",
                    "Physical Layer"
                ],
                "answer": "Transport Layer",
                "explanation": "Layer 4 (Transport Layer) ensures reliable end-to-end communication."
            },
            {
                "id": 3,
                "topic": "TCP/IP",
                "question": "Which layer of the TCP/IP model corresponds to the OSI Application, Presentation, and Session layers?",
                "options": [
                    "Application Layer",
                    "Transport Layer",
                    "Internet Layer",
                    "Network Access Layer"
                ],
                "answer": "Application Layer",
                "explanation": "In TCP/IP, the Application layer combines OSI layers 5, 6, and 7."
            },
            {
                "id": 4,
                "topic": "TCP/IP",
                "question": "Which protocol in the TCP/IP suite resolves an IP address into a physical MAC address?",
                "options": ["DNS", "DHCP", "ARP", "ICMP"],
                "answer": "ARP",
                "explanation": "Address Resolution Protocol (ARP) maps an IPv4 address to its physical MAC address."
            },
            {
                "id": 5,
                "topic": "IP Addressing",
                "question": "How many bits are used in an IPv4 address versus an IPv6 address?",
                "options": [
                    "32 bits for IPv4 and 128 bits for IPv6",
                    "16 bits for IPv4 and 64 bits for IPv6",
                    "32 bits for IPv4 and 64 bits for IPv6",
                    "64 bits for IPv4 and 128 bits for IPv6"
                ],
                "answer": "32 bits for IPv4 and 128 bits for IPv6",
                "explanation": "IPv4 uses 32 bits (4 octets), whereas IPv6 uses 128 bits (hexadecimal)."
            },
            {
                "id": 6,
                "topic": "IP Addressing",
                "question": "What is the default subnet mask for a Class C IPv4 network?",
                "options": [
                    "255.0.0.0",
                    "255.255.0.0",
                    "255.255.255.0",
                    "255.255.255.255"
                ],
                "answer": "255.255.255.0",
                "explanation": "Class C networks reserve the first 24 bits for the network (/24 mask: 255.255.255.0)."
            },
            {
                "id": 7,
                "topic": "Routing",
                "question": "At which OSI layer does an IP Router operate?",
                "options": [
                    "Data Link Layer (Layer 2)",
                    "Network Layer (Layer 3)",
                    "Transport Layer (Layer 4)",
                    "Application Layer (Layer 7)"
                ],
                "answer": "Network Layer (Layer 3)",
                "explanation": "Routers forward packets based on logical IP addresses at Layer 3 (Network Layer)."
            },
            {
                "id": 8,
                "topic": "Routing",
                "question": "Which metric does RIP (Routing Information Protocol) use to calculate the best path?",
                "options": [
                    "Bandwidth",
                    "Hop Count",
                    "Latency",
                    "Link Reliability"
                ],
                "answer": "Hop Count",
                "explanation": "RIP uses hop count as its sole metric (maximum 15 hops)."
            },
            {
                "id": 9,
                "topic": "TCP and UDP",
                "question": "How does TCP establish a reliable connection before transmitting data?",
                "options": [
                    "Two-way handshake",
                    "Three-way handshake (SYN, SYN-ACK, ACK)",
                    "Four-way handshake",
                    "UDP broadcast"
                ],
                "answer": "Three-way handshake (SYN, SYN-ACK, ACK)",
                "explanation": "TCP establishes state via SYN, SYN-ACK, and ACK packet exchange."
            },
            {
                "id": 10,
                "topic": "TCP and UDP",
                "question": "Which protocol is connectionless and prioritizes low latency over guaranteed delivery?",
                "options": ["TCP", "UDP", "FTP", "HTTP"],
                "answer": "UDP",
                "explanation": "UDP does not provide acknowledgments or retransmission, making it ideal for streaming and gaming."
            }
        ]
    },

    "dbms": {
        "id": "dbms",
        "name": "Database Management Systems",
        "badge_num": "05",
        "description": "Assess your understanding of relational databases, SQL queries, keys, normalization, transactions, and joins.",
        "topics": [
            "SQL",
            "Keys",
            "Normalization",
            "Transactions",
            "Joins"
        ],
        "questions": [
            {
                "id": 1,
                "topic": "SQL",
                "question": "Which SQL clause is used to filter rows after an aggregation function has been applied?",
                "options": ["WHERE", "HAVING", "ORDER BY", "GROUP BY"],
                "answer": "HAVING",
                "explanation": "HAVING filters aggregated grouped results; WHERE filters rows prior to aggregation."
            },
            {
                "id": 2,
                "topic": "SQL",
                "question": "Which SQL command is classified as Data Definition Language (DDL)?",
                "options": ["SELECT", "INSERT", "CREATE", "UPDATE"],
                "answer": "CREATE",
                "explanation": "CREATE, ALTER, and DROP modify schema structure and are DDL commands."
            },
            {
                "id": 3,
                "topic": "Keys",
                "question": "What is a Foreign Key in a relational database?",
                "options": [
                    "A key that uniquely identifies a row in the same table",
                    "A column that references the primary key of another table",
                    "A key that cannot contain integer values",
                    "An optional index for full-text search"
                ],
                "answer": "A column that references the primary key of another table",
                "explanation": "Foreign keys enforce referential integrity by pointing to primary keys in related tables."
            },
            {
                "id": 4,
                "topic": "Keys",
                "question": "What is the difference between a Primary Key and a Unique Key?",
                "options": [
                    "Primary Key cannot contain NULL, while Unique Key can accept one NULL value",
                    "Unique Key cannot contain duplicate values while Primary Key can",
                    "A table can have multiple Primary Keys but only one Unique Key",
                    "There is no difference"
                ],
                "answer": "Primary Key cannot contain NULL, while Unique Key can accept one NULL value",
                "explanation": "Primary keys strictly prohibit NULLs and uniquely identify tuples."
            },
            {
                "id": 5,
                "topic": "Normalization",
                "question": "A relational table is in First Normal Form (1NF) if and only if:",
                "options": [
                    "All column values are atomic and there are no repeating groups",
                    "It has no transitive dependencies",
                    "All non-key attributes are fully functionally dependent on the primary key",
                    "It contains foreign keys"
                ],
                "answer": "All column values are atomic and there are no repeating groups",
                "explanation": "1NF mandates atomic (indivisible) attribute values without repeating sets."
            },
            {
                "id": 6,
                "topic": "Normalization",
                "question": "Third Normal Form (3NF) eliminates which kind of dependency?",
                "options": [
                    "Partial Dependency",
                    "Transitive Dependency",
                    "Multi-valued Dependency",
                    "Join Dependency"
                ],
                "answer": "Transitive Dependency",
                "explanation": "2NF eliminates partial dependencies; 3NF eliminates transitive dependencies (X -> Y and Y -> Z)."
            },
            {
                "id": 7,
                "topic": "Transactions",
                "question": "What do the letters in ACID properties of database transactions stand for?",
                "options": [
                    "Atomicity, Consistency, Isolation, Durability",
                    "Accuracy, Consistency, Integrity, Durability",
                    "Availability, Concurrency, Isolation, Distribution",
                    "Atomicity, Concurrency, Indexing, Durability"
                ],
                "answer": "Atomicity, Consistency, Isolation, Durability",
                "explanation": "ACID ensures reliable transaction processing in database engines."
            },
            {
                "id": 8,
                "topic": "Transactions",
                "question": "Which ACID property guarantees that all operations of a transaction succeed or all fail together?",
                "options": ["Atomicity", "Consistency", "Isolation", "Durability"],
                "answer": "Atomicity",
                "explanation": "Atomicity ensures 'all-or-nothing' execution of transaction steps."
            },
            {
                "id": 9,
                "topic": "Joins",
                "question": "What does an INNER JOIN return?",
                "options": [
                    "Only the rows that have matching values in both tables",
                    "All rows from the left table and matched rows from the right table",
                    "All rows from both tables whether matched or not",
                    "Only rows that do NOT match"
                ],
                "answer": "Only the rows that have matching values in both tables",
                "explanation": "INNER JOIN combines rows from two tables where the join condition evaluates to true."
            },
            {
                "id": 10,
                "topic": "Joins",
                "question": "If you perform a LEFT JOIN and a row in the left table has no matching row in the right table, what values appear for the right table columns?",
                "options": ["0", "NULL", "An empty string", "The row is omitted"],
                "answer": "NULL",
                "explanation": "LEFT JOIN keeps all left rows and populates non-matching right columns with NULL."
            }
        ]
    },

    "os": {
        "id": "os",
        "name": "Operating Systems",
        "badge_num": "06",
        "description": "Test your grasp of operating system fundamentals including process management, scheduling, memory, and deadlocks.",
        "topics": [
            "Processes",
            "Threads",
            "CPU Scheduling",
            "Memory Management",
            "Deadlocks"
        ],
        "questions": [
            {
                "id": 1,
                "topic": "Processes",
                "question": "What is the primary difference between a program and a process?",
                "options": [
                    "A program is passive code on disk, while a process is an active program in execution",
                    "A program is stored in RAM, while a process is stored on disk",
                    "A program can have threads, but a process cannot",
                    "There is no difference"
                ],
                "answer": "A program is passive code on disk, while a process is an active program in execution",
                "explanation": "A process is a program in execution with associated resources, registers, and memory."
            },
            {
                "id": 2,
                "topic": "Processes",
                "question": "Which data structure does the OS kernel maintain to store process state, registers, and metadata?",
                "options": [
                    "Process Control Block (PCB)",
                    "File Allocation Table (FAT)",
                    "Page Replacement Table (PRT)",
                    "Inode Table"
                ],
                "answer": "Process Control Block (PCB)",
                "explanation": "The PCB holds process identifier, state, program counter, and scheduling info."
            },
            {
                "id": 3,
                "topic": "Threads",
                "question": "What resources do multiple threads of the same process share?",
                "options": [
                    "Code, data, and open files, but each has its own stack and registers",
                    "Each thread has its own isolated address space",
                    "Stack and program counter are shared, but data segment is private",
                    "Threads do not share any process memory"
                ],
                "answer": "Code, data, and open files, but each has its own stack and registers",
                "explanation": "Threads share process code, data, and file descriptors, but maintain separate stacks and registers."
            },
            {
                "id": 4,
                "topic": "Threads",
                "question": "Why is context switching between threads faster than between processes?",
                "options": [
                    "Threads share the same virtual address space, so page tables don't need to be flushed",
                    "Threads do not use CPU registers",
                    "Processes do not use cache memory",
                    "Threads are handled directly by hardware without OS intervention"
                ],
                "answer": "Threads share the same virtual address space, so page tables don't need to be flushed",
                "explanation": "Thread switching avoids costly virtual memory page table and TLB cache invalidation."
            },
            {
                "id": 5,
                "topic": "CPU Scheduling",
                "question": "Which scheduling algorithm assigns a fixed time quantum to each ready process in cyclic order?",
                "options": [
                    "First-Come, First-Served (FCFS)",
                    "Shortest Job First (SJF)",
                    "Round Robin (RR)",
                    "Priority Scheduling"
                ],
                "answer": "Round Robin (RR)",
                "explanation": "Round Robin uses time slices (quanta) to provide fair, pre-emptive time sharing."
            },
            {
                "id": 6,
                "topic": "CPU Scheduling",
                "question": "What severe drawback can occur in Shortest Job First (SJF) or Priority Scheduling?",
                "options": [
                    "Starvation of long or low-priority processes",
                    "Belady's Anomaly",
                    "Thrashing",
                    "Cache poisoning"
                ],
                "answer": "Starvation of long or low-priority processes",
                "explanation": "Indefinite blocking (starvation) occurs when incoming short jobs starve longer jobs."
            },
            {
                "id": 7,
                "topic": "Memory Management",
                "question": "In paging, what divides physical memory versus logical memory?",
                "options": [
                    "Physical memory is divided into Frames; logical memory into Pages",
                    "Physical memory is divided into Pages; logical memory into Frames",
                    "Both are divided into Segments only",
                    "Physical memory is divided into Blocks; logical memory into Clusters"
                ],
                "answer": "Physical memory is divided into Frames; logical memory into Pages",
                "explanation": "Logical memory is partitioned into fixed-size Pages; physical RAM into matching Frames."
            },
            {
                "id": 8,
                "topic": "Memory Management",
                "question": "What is 'Thrashing' in an operating system?",
                "options": [
                    "When the OS spends more time swapping pages in/out than executing processes",
                    "When a hard disk suffers physical sector failure",
                    "When the CPU frequency overheats and throttles",
                    "When multiple threads access shared memory without a lock"
                ],
                "answer": "When the OS spends more time swapping pages in/out than executing processes",
                "explanation": "Thrashing occurs when high page fault frequency causes continuous disk I/O swapping."
            },
            {
                "id": 9,
                "topic": "Deadlocks",
                "question": "Which of the following is NOT one of the four Coffman conditions necessary for a deadlock?",
                "options": [
                    "Mutual Exclusion",
                    "Hold and Wait",
                    "Preemption Allowed",
                    "Circular Wait"
                ],
                "answer": "Preemption Allowed",
                "explanation": "The condition is 'No Preemption'. If preemption is allowed, deadlocks cannot persist."
            },
            {
                "id": 10,
                "topic": "Deadlocks",
                "question": "Which classic algorithm is used by the OS to safely avoid deadlocks by testing safe resource allocations?",
                "options": [
                    "Banker's Algorithm",
                    "Dijkstra's Shortest Path",
                    "Peterson's Algorithm",
                    "Kruskal's Algorithm"
                ],
                "answer": "Banker's Algorithm",
                "explanation": "Dijkstra's Banker's algorithm tests whether resource allocation leaves the system in a safe state."
            }
        ]
    }
}


def get_all_subjects():
    """Returns metadata list of all available subjects."""
    return list(SUBJECTS.values())


def get_subject(subject_id):
    """Returns a specific subject by its ID or None if not found."""
    return SUBJECTS.get(subject_id)
