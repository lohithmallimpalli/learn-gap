"""
Subject-specific offline study guidance knowledge base for all 6 subjects in LearnGap.
Provides comprehensive, college-level conceptual explanations, key concepts, hints,
pitfalls, and practice recommendations for every assessed topic.
"""

OFFLINE_KNOWLEDGE = {
    # ----------------------------------------------------
    # Python Programming
    # ----------------------------------------------------
    "Python Programming": {
        "Python Basics": {
            "meaning": "Python Basics cover foundational syntax, operators, comments, and identifier rules in an interpreted, dynamically typed language.",
            "concepts": [
                "**Operator Precedence**: Arithmetic operations follow PEMDAS; `**` (exponentiation) takes higher precedence than multiplication and division.",
                "**Identifier Rules**: Variable names must start with a letter or underscore (`_`) and cannot begin with digits or contain special characters.",
                "**Dynamic Typing**: Python determines variable types automatically at runtime without explicit type declarations."
            ],
            "hints": [
                "Remember: `//` is floor division (returns integer), while `/` always returns a float in Python 3.",
                "Variables in Python are references/pointers to objects in memory rather than memory boxes."
            ],
            "mistakes": [
                "Starting variable names with numbers (e.g. `1count = 5` raises SyntaxError).",
                "Confusing assignment `=` with equality comparison `==`."
            ],
            "practice": "Write a script demonstrating arithmetic operators (`//`, `%`, `**`), input conversion, and type inspection using `type()` and `id()`."
        },
        "Variables and Data Types": {
            "meaning": "Variables hold references to values belonging to core data types such as integers, floats, strings, booleans, and sequences.",
            "concepts": [
                "**Mutability vs Immutability**: Integers, floats, strings, and tuples cannot be altered in-place (immutable); lists and dicts can be modified (mutable).",
                "**Single-Element Tuples**: A single item inside parentheses requires a trailing comma (e.g. `(4,)`) to be recognized as a tuple rather than a grouped integer.",
                "**Type Casting**: Explicitly converting types using `int()`, `float()`, `str()`, or `bool()` to prevent TypeError."
            ],
            "hints": [
                "Strings are immutable: methods like `.upper()` or `.replace()` return a *new* string and do not modify the original.",
                "Empty containers (`[]`, `()`, `{}`) and zero evaluate to `False` in boolean contexts."
            ],
            "mistakes": [
                "Attempting to modify a string index in-place (`s[0] = 'H'` throws TypeError).",
                "Forgetting the trailing comma in single-element tuples (`x = (5)` is an `int`, not a tuple)."
            ],
            "practice": "Build a data-cleaning utility script that takes mixed string inputs, type-checks with `isinstance()`, and casts them to appropriate numerical formats."
        },
        "Control Statements": {
            "meaning": "Control statements direct program flow using conditional branching (`if`, `elif`, `else`) and iterative loops (`for`, `while`).",
            "concepts": [
                "**Indentation Blocks**: Python uses whitespace indentation instead of curly braces to define code blocks.",
                "**Loop Controls**: `break` terminates loop execution immediately; `continue` skips the remainder of the current iteration; `pass` serves as a no-op placeholder.",
                "**`range()` Function**: Generates integer sequences with `range(start, stop, step)`, where `stop` is exclusive."
            ],
            "hints": [
                "`range(1, 10, 2)` produces 1, 3, 5, 7, 9. The stop value 10 is never reached.",
                "Python loops support an optional `else:` clause that executes only if the loop completes without hitting a `break`."
            ],
            "mistakes": [
                "Off-by-one errors with `range()` by forgetting that the end boundary is exclusive.",
                "Creating infinite `while` loops by forgetting to increment the loop control variable."
            ],
            "practice": "Implement a prime number generator and binary search algorithm using nested loops with early `break` statements."
        },
        "Functions": {
            "meaning": "Functions are modular, reusable blocks of code defined with `def` that accept inputs (arguments) and return results.",
            "concepts": [
                "**Scope & LEGB Rule**: Python resolves variable names in order: Local -> Enclosing -> Global -> Built-in.",
                "**`*args` and `**kwargs`**: `*args` collects arbitrary positional arguments into a tuple; `**kwargs` collects arbitrary keyword arguments into a dictionary.",
                "**Lambda Expressions**: Inline anonymous functions defined with syntax `lambda x, y: x + y`."
            ],
            "hints": [
                "Functions without an explicit `return` statement automatically return `None`.",
                "Default argument values are evaluated once at definition time; never use mutable objects (`[]`, `{}`) as default parameters."
            ],
            "mistakes": [
                "Using mutable defaults like `def append_to(item, target=[])`, causing persistent shared state across invocations.",
                "Forgetting that `return` terminates function execution immediately."
            ],
            "practice": "Write higher-order functions utilizing `map()`, `filter()`, and lambda expressions to process a list of numerical student records."
        },
        "Lists, Tuples and Dictionaries": {
            "meaning": "These are Python's primary collection data structures: lists are ordered mutable sequences, tuples are ordered immutable sequences, and dictionaries are key-value hash maps.",
            "concepts": [
                "**Dictionary Lookup**: Keys must be hashable (immutable); average-case lookup, insertion, and deletion are $O(1)$.",
                "**List Operations**: `.append()` adds to the end in $O(1)$; `.insert(0, val)` shifts elements in $O(n)$; `.pop()` removes by index.",
                "**Safe Retrieval with `.get()`**: `d.get(key, default)` prevents runtime `KeyError` when accessing uncertain keys."
            ],
            "hints": [
                "Use list comprehensions `[x**2 for x in data if x > 0]` for clean, optimized sequence transformation.",
                "Tuples can be used as dictionary keys because they are hashable; lists cannot."
            ],
            "mistakes": [
                "Accessing a missing dictionary key with bracket notation `d['missing']` instead of `d.get('missing')`.",
                "Modifying a list while iterating over it, causing skipped elements and index misalignment."
            ],
            "practice": "Build an in-memory student gradebook using nested dictionaries and practice sorting it by student scores using `sorted(d.items(), key=lambda x: x[1])`."
        }
    },

    # ----------------------------------------------------
    # Machine Learning
    # ----------------------------------------------------
    "Machine Learning": {
        "Linear Regression": {
            "meaning": "Linear Regression is a supervised learning algorithm that models the linear relationship between one or more input features ($X$) and a continuous numeric target ($Y$).",
            "concepts": [
                "**Line Equation & Weights**: Expressed as $y = mx + c$ (or $y = \\beta_0 + \\beta_1 x$), where $\\beta_0$ is intercept and $\\beta_1$ represents feature slope.",
                "**Mean Squared Error (MSE)**: The loss function calculating average squared difference between predictions and ground truth, penalizing large outliers heavily.",
                "**Ordinary Least Squares (OLS) & Optimization**: Closed-form normal equation or iterative Gradient Descent adjusts weights to minimize total loss."
            ],
            "hints": [
                "Remember: *Linear = Continuous Numbers*. Never use linear regression for classification classes.",
                "The regression line always passes through the centroid point $(\\bar{x}, \\bar{y})$."
            ],
            "mistakes": [
                "Assuming correlation implies causation between variables.",
                "Failing to check for extreme outliers, which heavily skew the best-fit line due to the squared penalty."
            ],
            "practice": "Train `LinearRegression` with `scikit-learn` on a housing price dataset, calculate $R^2$ score and MSE, and plot the regression line alongside actual data points."
        },
        "Logistic Regression": {
            "meaning": "Despite the name 'Regression', Logistic Regression is a supervised classification algorithm that estimates the probability of discrete outcomes.",
            "concepts": [
                "**Sigmoid Function**: The mathematical function $\\sigma(z) = \\frac{1}{1 + e^{-z}}$ that squashes real numbers into probabilities between $0$ and $1$.",
                "**Decision Threshold**: A cutoff probability (default $0.5$) used to convert continuous probabilities into discrete class decisions ($P \\ge 0.5 \\implies 1$).",
                "**Log-Loss (Binary Cross-Entropy)**: The convex cost function that heavily penalizes confident incorrect probability predictions."
            ],
            "hints": [
                "Think: *Logistic = S-curve = Probability Classification*.",
                "Predicted output is always bounded between 0 and 1, representing $P(Y=1|X)$."
            ],
            "mistakes": [
                "Confusing it with Linear Regression and attempting to predict unbounded continuous quantities.",
                "Relying solely on Accuracy on imbalanced datasets instead of Precision, Recall, and ROC-AUC."
            ],
            "practice": "Train `LogisticRegression` on the Titanic or Breast Cancer dataset. Evaluate using a Confusion Matrix, Precision, Recall, and F1-score."
        },
        "Decision Tree": {
            "meaning": "A Decision Tree is an intuitive, supervised algorithm that recursively splits data into subsets based on feature questions, creating a hierarchical tree structure.",
            "concepts": [
                "**Splitting Criteria (Purity Metrics)**: Uses Gini Impurity or Information Gain / Entropy to select the best attribute split at each node.",
                "**Tree Anatomy**: Starts at the **Root Node**, branches through **Decision Nodes**, and terminates at **Leaf Nodes** (final predictions).",
                "**Pruning & Overfitting**: Unrestricted decision trees memorize training noise; parameters like `max_depth` and cost-complexity pruning prevent overfitting."
            ],
            "hints": [
                "*Lower Gini Impurity = Purer Node*. A Gini of 0 means 100% of samples at that leaf belong to a single class.",
                "Decision trees handle both numerical and categorical features without requiring feature scaling."
            ],
            "mistakes": [
                "Leaving `max_depth` unconstrained, causing 100% training accuracy but poor generalization to test data.",
                "Assuming decision trees are invariant; small perturbations in training data can drastically alter tree structure."
            ],
            "practice": "Fit a `DecisionTreeClassifier` on the Iris dataset, plot the visual tree diagram using `plot_tree`, and experiment with tuning `max_depth`."
        },
        "K-Means": {
            "meaning": "K-Means is an unsupervised clustering algorithm that partitions unlabeled data points into $K$ distinct clusters based on geometric feature proximity.",
            "concepts": [
                "**Centroids & $K$ Value**: $K$ specifies the predetermined number of cluster centers initialized in the feature space.",
                "**Expectation-Maximization Iteration**: Repeatedly alternates between (1) assigning points to the nearest centroid, and (2) recomputing centroids as the cluster mean.",
                "**Elbow Method & Inertia**: Within-Cluster Sum of Squares (WCSS / Inertia) measures cluster tightness; the 'elbow' point identifies optimal $K$."
            ],
            "hints": [
                "Remember: *K-Means is Unsupervised*. It does not use or need ground truth labels during training.",
                "Always initialize with `k-means++` to spread initial centroids and prevent convergence to bad local minima."
            ],
            "mistakes": [
                "Skipping feature standardization (`StandardScaler`); larger scale features will dominate distance calculations.",
                "Expecting K-Means to cluster complex non-spherical shapes (e.g. concentric rings)."
            ],
            "practice": "Generate synthetic clusters using `make_blobs`, apply `KMeans` from `scikit-learn`, plot clusters with their centroids, and construct an Elbow plot."
        },
        "PCA": {
            "meaning": "Principal Component Analysis (PCA) is an unsupervised dimensionality reduction technique that transforms high-dimensional data into orthogonal components of maximum variance.",
            "concepts": [
                "**Dimensionality Reduction & Information Loss**: Compresses datasets with many features into fewer dimensions while preserving dominant patterns.",
                "**Principal Components & Variance**: Principal components are orthogonal (perpendicular and uncorrelated) linear combinations of original features.",
                "**Eigenvalues & Eigenvectors**: Computed from the covariance matrix; eigenvectors determine direction, while eigenvalues indicate explained variance magnitude."
            ],
            "hints": [
                "Think: *PCA = Maximum Variance in Minimal Dimensions*. Great for projecting 50+ features into 2D/3D scatter plots.",
                "Every Principal Component is completely uncorrelated with all other Principal Components."
            ],
            "mistakes": [
                "Not standardizing data before PCA. High-magnitude features will disproportionately dominate variance.",
                "Confusing PCA with feature selection; PCA does not select original features, it engineers brand new composite dimensions."
            ],
            "practice": "Load the Wine or Breast Cancer dataset, apply `StandardScaler`, fit `PCA(n_components=2)`, and plot the explained variance ratio along with a 2D projection."
        }
    },

    # ----------------------------------------------------
    # Data Structures
    # ----------------------------------------------------
    "Data Structures": {
        "Arrays": {
            "meaning": "An Array is a contiguous collection of elements of identical data type stored at sequential memory addresses.",
            "concepts": [
                "**O(1) Random Access**: Direct memory indexing formula `Address = Base + (Index * Element_Size)` enables constant-time element lookup.",
                "**Costly Insertion/Deletion**: Inserting or deleting an element at index 0 requires shifting all $N$ elements right or left ($O(N)$ time).",
                "**Cache Locality**: Contiguous storage ensures sequential elements are pre-fetched into CPU cache lines efficiently."
            ],
            "hints": [
                "Accessing `arr[i]` is always $O(1)$; searching an unsorted array for a value is $O(N)$.",
                "Dynamic arrays (like Python lists or C++ `vector`) double their capacity upon filling, yielding amortized $O(1)$ append."
            ],
            "mistakes": [
                "Assuming insertion at arbitrary indices in an array is $O(1)$.",
                "Out-of-bounds indexing by forgetting that array indices run from $0$ to $N-1$."
            ],
            "practice": "Implement Two Pointer techniques on sorted arrays to solve the Two-Sum problem in $O(N)$ time and $O(1)$ space."
        },
        "Linked Lists": {
            "meaning": "A Linked List is a linear data structure where elements (nodes) contain data and pointers/references to other nodes rather than contiguous memory.",
            "concepts": [
                "**Node Structure**: Each node contains a `data` payload and a `next` pointer (plus a `prev` pointer in doubly linked lists).",
                "**Dynamic Memory & Non-Contiguity**: Nodes can be allocated anywhere in heap memory without pre-allocating fixed sizes.",
                "**$O(1)$ Head Insertion**: Inserting at the head requires updating pointer references without shifting any subsequent nodes."
            ],
            "hints": [
                "Always check for edge cases: empty list (`head == None`) and single-node list (`head.next == None`).",
                "Use a **Dummy / Sentinel Node** to simplify insertion and deletion at the head of a linked list."
            ],
            "mistakes": [
                "Losing the reference to the rest of the list by overwriting `curr.next` before preserving subsequent pointers.",
                "Expecting $O(1)$ random indexing (reaching node $K$ requires sequential traversal in $O(K)$ time)."
            ],
            "practice": "Implement in-place reversal of a Singly Linked List iteratively and implement Floyd's Cycle Detection Algorithm (Tortoise and Hare)."
        },
        "Stacks": {
            "meaning": "A Stack is a constrained linear data structure that strictly enforces Last-In, First-Out (LIFO) access.",
            "concepts": [
                "**LIFO Principle**: The most recently pushed element is the first element popped from the top.",
                "**Fundamental Operations**: `push(x)` to add to top, `pop()` to remove from top, `peek()` to inspect top element (all $O(1)$).",
                "**System Call Stack**: Compilers use stacks to track function call activation frames, local variables, and return addresses."
            ],
            "hints": [
                "Think: *A stack of plates* — you can only add or remove from the very top.",
                "Whenever a problem involves matching pairs (e.g. parentheses) or backtracking, consider a Stack."
            ],
            "mistakes": [
                "Attempting to pop from an empty stack without checking, causing Stack Underflow errors.",
                "Using linear search through a stack, violating the data structure's abstraction."
            ],
            "practice": "Implement the classic Valid Parentheses problem and evaluate Reverse Polish Notation (Postfix) expressions using a stack."
        },
        "Queues": {
            "meaning": "A Queue is a linear data structure that strictly enforces First-In, First-Out (FIFO) access.",
            "concepts": [
                "**FIFO Principle**: Elements enter at the `rear` (enqueue) and exit from the `front` (dequeue).",
                "**Circular Queue**: Connects the end of the array back to the front to prevent false queue overflow and reuse memory slots.",
                "**Breadth-First Search (BFS)**: Graph and tree level-order traversals fundamentally rely on queues to explore nodes layer by layer."
            ],
            "hints": [
                "Think: *A checkout line at a store* — the first person to arrive is the first person served.",
                "In Python, use `collections.deque` for $O(1)$ appends and pops on both ends instead of `list.pop(0)` ($O(N)$)."
            ],
            "mistakes": [
                "Using standard array pop `arr.pop(0)` as a queue in performance-critical code ($O(N)$ due to element shifting).",
                "Confusing FIFO queue semantics with LIFO stack semantics."
            ],
            "practice": "Implement a Circular Queue using an array with front and rear pointers, and implement Breadth-First Search on a binary tree."
        },
        "Trees": {
            "meaning": "A Tree is a non-linear, hierarchical data structure composed of nodes connected by edges, starting from a single root node.",
            "concepts": [
                "**Binary Search Tree (BST) Property**: For every node, all values in its left subtree are strictly smaller, and all values in its right subtree are strictly greater.",
                "**Tree Traversals**: In-order (Left, Root, Right — yields sorted order in BST), Pre-order (Root, Left, Right), Post-order (Left, Right, Root).",
                "**Time Complexity**: Balanced BST operations (search, insert, delete) take $O(\\log N)$; unbalanced degenerate trees degrade to $O(N)$."
            ],
            "hints": [
                "In-order traversal of a BST always processes values in strictly ascending numerical order.",
                "Height of a balanced tree is $O(\\log N)$; height of a completely skewed tree is $O(N)$."
            ],
            "mistakes": [
                "Assuming a binary tree is automatically balanced; without AVL or Red-Black balancing, trees can degenerate into linked lists.",
                "Mixing up the visit orders of Pre-order, In-order, and Post-order traversals."
            ],
            "practice": "Write recursive functions to calculate the maximum depth of a binary tree, invert a binary tree, and validate whether a tree is a valid BST."
        }
    },

    # ----------------------------------------------------
    # Computer Networks
    # ----------------------------------------------------
    "Computer Networks": {
        "OSI Model": {
            "meaning": "The Open Systems Interconnection (OSI) reference model is a 7-layer architectural framework defining network communication standards.",
            "concepts": [
                "**7 Layers in Order**: Physical (1), Data Link (2), Network (3), Transport (4), Session (5), Presentation (6), Application (7).",
                "**Data Encapsulation**: Data packets acquire headers at each descending layer: Data -> Segments -> Packets -> Frames -> Bits.",
                "**Layer Responsibilities**: Layer 2 uses MAC addresses (frames); Layer 3 uses IP addresses (packets); Layer 4 handles ports and end-to-end reliability (segments)."
            ],
            "hints": [
                "Mnemonic: *Please Do Not Throw Sausage Pizza Away* (Physical to Application).",
                "Switches operate predominantly at Layer 2; Routers operate at Layer 3."
            ],
            "mistakes": [
                "Confusing the roles of Layer 2 (hop-to-hop MAC framing) and Layer 3 (end-to-end IP routing).",
                "Thinking HTTP operates at the Transport layer; HTTP is strictly Layer 7 (Application)."
            ],
            "practice": "Capture network traffic using Wireshark and inspect the protocol headers of an HTTP GET request layer by layer (Ethernet -> IP -> TCP -> HTTP)."
        },
        "TCP/IP": {
            "meaning": "The TCP/IP model is the practical 4-layer protocol suite powering the global internet (Network Access, Internet, Transport, Application).",
            "concepts": [
                "**Layer Mapping**: Collapses OSI layers 5, 6, and 7 into a single unified Application Layer.",
                "**Address Resolution Protocol (ARP)**: Resolves a known Layer 3 logical IP address into a Layer 2 physical MAC address on local subnets.",
                "**Internet Control Message Protocol (ICMP)**: Used for diagnostic network reporting and error signaling (powers `ping` and `traceroute`)."
            ],
            "hints": [
                "ARP operates between Layer 2 and Layer 3 to bridge IP communication with physical network cards.",
                "DNS resolves human domain names to IP addresses at the Application layer via UDP port 53."
            ],
            "mistakes": [
                "Assuming ARP broadcasts cross across routers to foreign networks (ARP is strictly local broadcast).",
                "Confusing MAC address (hardware baked-in) with IP address (logically assigned)."
            ],
            "practice": "Run `arp -a` and `traceroute` commands in terminal to inspect local ARP cache mappings and trace intermediate router hops."
        },
        "IP Addressing": {
            "meaning": "IP Addressing provides unique numerical logical identifiers for host interfaces across interconnected networks.",
            "concepts": [
                "**IPv4 vs IPv6**: IPv4 uses 32 bits (4 octets, e.g. 192.168.1.1); IPv6 uses 128 bits (hexadecimal notation) providing a virtually inexhaustible address space.",
                "**Subnetting & Subnet Masks**: Subnet masks divide an IP address into Network ID and Host ID portions (e.g. `/24` = `255.255.255.0` gives 254 usable hosts).",
                "**Private IP Ranges**: RFC 1918 addresses (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) are non-routable on the public internet and require NAT."
            ],
            "hints": [
                "Total usable hosts in a subnet with $H$ host bits is always $2^H - 2$ (excluding Network Address and Broadcast Address).",
                "Loopback address `127.0.0.1` refers to the local host machine."
            ],
            "mistakes": [
                "Forgetting to subtract 2 for network and broadcast addresses when sizing subnets.",
                "Assuming public routers can directly route private Class A/B/C addresses without Network Address Translation (NAT)."
            ],
            "practice": "Calculate usable host ranges and broadcast addresses for CIDR subnets like `192.168.10.0/26` and `10.50.0.0/22`."
        },
        "Routing": {
            "meaning": "Routing is the process of selecting optimal paths for network packets across multiple intermediate nodes from source to destination.",
            "concepts": [
                "**Layer 3 Packet Forwarding**: Routers consult their routing tables to determine the next-hop IP interface for inbound packets.",
                "**Routing Information Protocol (RIP)**: Distance-vector protocol that uses hop count as its sole metric (maximum allowable hops = 15).",
                "**Open Shortest Path First (OSPF)**: Link-state protocol using Dijkstra's algorithm to calculate shortest paths based on cost and bandwidth."
            ],
            "hints": [
                "RIP = Hop count; OSPF = Cost/Bandwidth; BGP = Path-vector for Autonomous Systems.",
                "Default gateway is the local router IP that hosts send traffic to when the destination is outside the local subnet."
            ],
            "mistakes": [
                "Believing routers forward broadcast frames; routers break broadcast domains by default.",
                "Confusing static routing (manually configured) with dynamic routing protocols (auto-converging)."
            ],
            "practice": "Set up a virtual network topology in Cisco Packet Tracer or GNS3 and configure static routes and RIP routing across 3 interconnected routers."
        },
        "TCP and UDP": {
            "meaning": "TCP and UDP are the two primary Transport layer protocols that manage communication between host processes using port numbers.",
            "concepts": [
                "**TCP 3-Way Handshake**: Establishes connection state using `SYN` -> `SYN-ACK` -> `ACK` sequence.",
                "**TCP Reliability & Flow Control**: Provides guaranteed in-order packet delivery, sequence numbering, acknowledgments, retransmission, and sliding window flow control.",
                "**UDP Characteristics**: Connectionless, lightweight, low-overhead protocol with no guarantee of packet delivery or order (best for real-time audio/video/gaming)."
            ],
            "hints": [
                "TCP = Reliable, heavy, connection-oriented (HTTP, SSH, SMTP).",
                "UDP = Fast, lightweight, connectionless (DNS, VoIP, video streaming, DHCP)."
            ],
            "mistakes": [
                "Assuming UDP is 'inferior' rather than an intentional design tradeoff prioritizing speed over retransmission latency.",
                "Forgetting that TCP teardown uses a 4-way handshake (`FIN`, `ACK`, `FIN`, `ACK`)."
            ],
            "practice": "Build a simple client-server socket program in Python: one using TCP (`socket.SOCK_STREAM`) and one using UDP (`socket.SOCK_DGRAM`)."
        }
    },

    # ----------------------------------------------------
    # Database Management Systems
    # ----------------------------------------------------
    "Database Management Systems": {
        "SQL": {
            "meaning": "Structured Query Language (SQL) is the standard declarative language used to define, query, and manipulate relational databases.",
            "concepts": [
                "**Command Classifications**: DDL (`CREATE`, `ALTER`, `DROP` modify schemas); DML (`SELECT`, `INSERT`, `UPDATE`, `DELETE` manipulate data).",
                "**WHERE vs HAVING**: `WHERE` filters individual rows prior to aggregation; `HAVING` filters aggregated group records after `GROUP BY`.",
                "**Aggregate Functions**: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()` operate on column groups to compute summary values."
            ],
            "hints": [
                "Order of SQL query execution: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT.",
                "To search for string patterns, use `LIKE '%keyword%'` (`%` represents any sequence of characters)."
            ],
            "mistakes": [
                "Using aggregate functions inside a `WHERE` clause (e.g. `WHERE AVG(salary) > 5000` causes a syntax error; use `HAVING`).",
                "Forgetting a `WHERE` clause on `UPDATE` or `DELETE`, inadvertently modifying or wiping the entire table."
            ],
            "practice": "Write complex SQL queries combining `GROUP BY`, `HAVING`, and nested subqueries on an employee-department schema."
        },
        "Keys": {
            "meaning": "Keys are attributes or sets of attributes that uniquely identify records within a table and enforce relationships across tables.",
            "concepts": [
                "**Primary Key (PK)**: Uniquely identifies each tuple; must be unique and cannot accept `NULL` values (only one PK per table).",
                "**Foreign Key (FK)**: A column referencing the primary key of another table, enforcing referential integrity.",
                "**Candidate Key vs Super Key**: A Super Key is any attribute set identifying tuples; a Candidate Key is a minimal Super Key with no redundant attributes."
            ],
            "hints": [
                "A table can have multiple Unique Keys (which may permit one `NULL`), but only one Primary Key.",
                "Foreign keys prevent orphaned records through `ON DELETE CASCADE` or `ON DELETE SET NULL` constraints."
            ],
            "mistakes": [
                "Attempting to insert a duplicate value or `NULL` into a Primary Key column.",
                "Deleting a parent table row that is currently referenced by a Foreign Key without cascading."
            ],
            "practice": "Design an e-commerce schema with Customers, Orders, and Products tables, correctly designating Primary Keys and Foreign Key constraints."
        },
        "Normalization": {
            "meaning": "Normalization is the systematic database design technique of organizing relations to minimize redundancy and prevent insertion, update, and deletion anomalies.",
            "concepts": [
                "**First Normal Form (1NF)**: All column values must be atomic (indivisible) and tables must contain no repeating groups.",
                "**Second Normal Form (2NF)**: Must be in 1NF and eliminate partial functional dependencies (all non-key attributes fully dependent on entire candidate key).",
                "**Third Normal Form (3NF)**: Must be in 2NF and eliminate transitive dependencies (non-key attributes cannot depend on other non-key attributes)."
            ],
            "hints": [
                "Mnemonic: *The key, the whole key (2NF), and nothing but the key (3NF), so help me Codd*.",
                "BCNF (Boyce-Codd Normal Form) is a stricter version of 3NF where for every functional dependency $X \\to Y$, $X$ must be a super key."
            ],
            "mistakes": [
                "Storing comma-separated values in a single cell, directly violating 1NF.",
                "Over-normalizing without considering join performance overhead in read-heavy applications."
            ],
            "practice": "Take an unnormalized invoice spreadsheet and step-by-step decompose it into relations satisfying 1NF, 2NF, and 3NF."
        },
        "Transactions": {
            "meaning": "A Transaction is an indivisible sequence of database operations executed as a single logical unit of work.",
            "concepts": [
                "**ACID Properties**: **Atomicity** (all or nothing), **Consistency** (preserves validity constraints), **Isolation** (concurrent transactions do not interfere), **Durability** (committed changes persist).",
                "**Transaction Controls**: `BEGIN TRANSACTION`, `COMMIT` (permanently saves changes), `ROLLBACK` (undoes uncommitted operations).",
                "**Isolation Levels**: Read Uncommitted, Read Committed, Repeatable Read, and Serializable (preventing dirty reads, non-repeatable reads, and phantom reads)."
            ],
            "hints": [
                "Atomicity guarantees that if a system crashes during a bank transfer after debiting Account A, Account B is never left uncredited.",
                "Durability is typically achieved by writing transaction logs to non-volatile disk storage before updating tables."
            ],
            "mistakes": [
                "Assuming database transactions automatically prevent deadlocks without proper locking order.",
                "Leaving transactions open without committing or rolling back, locking database rows indefinitely."
            ],
            "practice": "Simulate a bank transfer transaction in SQLite using `BEGIN TRANSACTION; UPDATE ...; UPDATE ...; COMMIT;` and test failure rollback."
        },
        "Joins": {
            "meaning": "Joins combine columns from one or more tables based on a related common column between them.",
            "concepts": [
                "**INNER JOIN**: Returns only rows where there is a matching value in both tables.",
                "**LEFT (OUTER) JOIN**: Returns all rows from the left table, and matched rows from the right table (unmatched right columns return `NULL`).",
                "**RIGHT & FULL OUTER JOIN**: RIGHT JOIN preserves all right table rows; FULL JOIN preserves all rows from both tables."
            ],
            "hints": [
                "To find records in Table A that have no matching record in Table B: use `LEFT JOIN ... WHERE B.id IS NULL`.",
                "Always specify explicit join criteria using `ON A.id = B.foreign_id` rather than comma joins."
            ],
            "mistakes": [
                "Omitting the `ON` condition, producing an accidental Cartesian product (Cross Join) of $M \\times N$ rows.",
                "Filtering right-table columns in the `WHERE` clause instead of the `ON` clause during a `LEFT JOIN`, inadvertently converting it into an `INNER JOIN`."
            ],
            "practice": "Execute queries demonstrating `INNER JOIN`, `LEFT JOIN`, and self-joins on an employee-manager hierarchical table."
        }
    },

    # ----------------------------------------------------
    # Operating Systems
    # ----------------------------------------------------
    "Operating Systems": {
        "Processes": {
            "meaning": "A Process is an active program in execution, encompassing the executable code, current activity, registers, program counter, and memory segments.",
            "concepts": [
                "**Process Memory Layout**: Divided into Code (Text), Data (globals), Heap (dynamically allocated memory), and Stack (local variables/activation frames).",
                "**Process States**: New -> Ready (in ready queue) -> Running (on CPU) -> Waiting/Blocked (I/O) -> Terminated.",
                "**Process Control Block (PCB)**: OS data structure storing process state, PID, registers, priority, and memory management pointers."
            ],
            "hints": [
                "A program is passive code stored on disk; a process is active code running in memory with allocated resources.",
                "In Unix, `fork()` creates a child process; `exec()` replaces the process image with a new program."
            ],
            "mistakes": [
                "Confusing a passive program executable file with an executing process instance.",
                "Leaving child processes unterminated without parent reaping, creating Zombie and Orphan processes."
            ],
            "practice": "Write a C or Python script using `fork()` or `multiprocessing` to observe process IDs (`getpid()`, `getppid()`) and separate memory spaces."
        },
        "Threads": {
            "meaning": "A Thread is the smallest unit of CPU execution within a process, often called a lightweight process.",
            "concepts": [
                "**Shared Resources**: Threads of the same process share code, global data, and open file descriptors.",
                "**Private Resources**: Each thread maintains its own independent Thread ID, Program Counter, register set, and Stack.",
                "**Low-Cost Context Switching**: Thread switching is significantly faster than process switching because the virtual address space remains unchanged."
            ],
            "hints": [
                "Multi-threading allows responsive user interfaces (e.g. background downloading while keeping the UI interactive).",
                "Watch out for Race Conditions when multiple threads read and write shared variables without synchronization."
            ],
            "mistakes": [
                "Assuming threads have independent heap or global memory spaces (they share the process heap).",
                "Failing to synchronize shared mutable state, leading to non-deterministic data corruption."
            ],
            "practice": "Implement a multi-threaded counter in Python using `threading.Thread` and resolve race conditions using `threading.Lock()`."
        },
        "CPU Scheduling": {
            "meaning": "CPU Scheduling determines which ready process is allocated CPU execution time to optimize throughput, latency, and fairness.",
            "concepts": [
                "**Scheduling Algorithms**: First-Come First-Served (FCFS, non-preemptive), Shortest Job First (SJF, optimal average waiting time), Round Robin (RR, time-slice preemption), Priority Scheduling.",
                "**Round Robin (RR)**: Allocates a fixed time slice (quantum) cyclically to each process in the ready queue, ideal for interactive time-sharing systems.",
                "**Starvation & Aging**: Starvation occurs when low-priority jobs never get CPU time; Aging solves this by gradually increasing priority over time."
            ],
            "hints": [
                "If time quantum in Round Robin is too large, it degrades to FCFS; if too small, context-switching overhead dominates.",
                "SJF yields the minimum average waiting time among all non-preemptive scheduling algorithms."
            ],
            "mistakes": [
                "Confusing Turnaround Time (Completion Time - Arrival Time) with Waiting Time (Turnaround Time - Burst Time).",
                "Assuming FCFS is optimal for short tasks (it suffers from the Convoy Effect behind large CPU bursts)."
            ],
            "practice": "Calculate Gantt charts, average waiting time, and turnaround time for a set of processes under FCFS, SJF, and Round Robin (quantum=2)."
        },
        "Memory Management": {
            "meaning": "Memory Management coordinates how main physical RAM is allocated, protected, and shared among active processes using virtual memory.",
            "concepts": [
                "**Paging & Virtual Memory**: Logical memory is divided into fixed-size **Pages**; physical RAM is divided into matching **Frames**; the Page Table translates virtual addresses to physical frames.",
                "**Page Fault**: An interrupt raised when a process attempts to access a page marked not present in physical RAM, prompting disk swap-in.",
                "**Thrashing**: Occurs when excessive page faults force the OS to spend more time swapping pages to/from disk than executing instructions."
            ],
            "hints": [
                "Paging completely eliminates External Fragmentation, though small Internal Fragmentation may exist in the final page.",
                "Translation Lookaside Buffer (TLB) is a high-speed hardware cache for page table lookups."
            ],
            "mistakes": [
                "Confusing Pages (logical memory units) with Frames (physical RAM hardware units).",
                "Thinking virtual memory increases physical RAM size; it allows execution of programs larger than physical memory using disk backing store."
            ],
            "practice": "Trace FIFO and Least Recently Used (LRU) page replacement algorithms on a reference string and calculate page fault frequencies."
        },
        "Deadlocks": {
            "meaning": "A Deadlock is a state where a set of processes are blocked because each process is holding a resource and waiting for another resource held by another process.",
            "concepts": [
                "**4 Coffman Conditions**: (1) **Mutual Exclusion** (non-shareable resources), (2) **Hold and Wait**, (3) **No Preemption** (resources cannot be forcibly taken), (4) **Circular Wait**.",
                "**Deadlock Prevention**: Invalidate at least one of the 4 Coffman conditions (e.g. enforce total global ordering on resource acquisition to eliminate circular wait).",
                "**Banker's Algorithm**: A classic deadlock avoidance algorithm that tests whether granting a resource request leaves the system in a globally safe state."
            ],
            "hints": [
                "All four Coffman conditions must hold simultaneously for a deadlock to exist.",
                "A 'Safe State' is not deadlocked, and there exists a dispatch sequence allowing every process to finish."
            ],
            "mistakes": [
                "Confusing Deadlock Avoidance (e.g. Banker's Algorithm dynamically checking safe states) with Deadlock Prevention (restricting how requests can be made).",
                "Assuming Starvation and Deadlock are identical; deadlocked processes can never recover without intervention, whereas starved processes may eventually proceed."
            ],
            "practice": "Solve a Banker's Algorithm matrix problem with Allocation, Max, and Available matrices to identify the safe execution sequence."
        }
    }
}


def generate_offline_study_guide(subject_name, score, total, weak_topics):
    """
    Generates a structured, college-level personalized study guide using the offline knowledge base.
    """
    subject_dict = OFFLINE_KNOWLEDGE.get(subject_name, {})
    lines = []

    if weak_topics:
        lines.append(f"### 📚 Personalized {subject_name} Study Guide\n")
        lines.append(
            f"**Assessment Performance:** You scored **{score}/{total}**. "
            "Here is targeted conceptual guidance for the topics that need your attention:\n"
        )

        for item in weak_topics:
            topic_name = None
            for key in subject_dict:
                if key in item:
                    topic_name = key
                    break

            if not topic_name or topic_name not in subject_dict:
                continue

            info = subject_dict[topic_name]
            lines.append(f"#### 🎯 {topic_name}\n")
            lines.append(f"• **What it means in simple words:** {info['meaning']}\n")
            lines.append("• **3 Important Concepts to Remember:**")
            for c in info["concepts"]:
                lines.append(f"  - {c}")
            lines.append("\n• **2 Quick Hints:**")
            for h in info["hints"]:
                lines.append(f"  - {h}")
            lines.append("\n• **2 Common Mistakes Students Make:**")
            for m in info["mistakes"]:
                lines.append(f"  - {m}")
            lines.append(f"\n• **What to Practice Next:** {info['practice']}\n")

    else:
        lines.append(f"### 🌟 Outstanding Performance! Complete Mastery in {subject_name}\n")
        lines.append(
            f"**Assessment Performance:** You achieved a top score of **{score}/{total}**! "
            f"All assessed topics in {subject_name} show strong conceptual understanding.\n"
        )
        lines.append("#### 🚀 Summary & Key Revision")
        lines.append(
            f"• You demonstrated clear mastery across foundational {subject_name} concepts. "
            "You answered questions across all core areas accurately and confidently.\n"
        )
        lines.append("#### 🔑 Advanced Next Steps & Deeper Study")
        lines.append("• **Core Depth**: Delve into low-level architectural internals and edge-case behavior.")
        lines.append("• **Practical Application**: Build a real-world project integrating this subject with production-grade engineering tools.")
        lines.append("• **Benchmarking & Optimization**: Analyze time/space complexity, memory footprint, and concurrency limits.\n")
        lines.append("#### 💡 3 Practice Suggestions")
        lines.append(f"1. **Mini-Project**: Build a portfolio application emphasizing robust {subject_name} architecture.")
        lines.append("2. **Mock Technical Interviews**: Practice explaining core design tradeoffs and internals without referencing notes.")
        lines.append("3. **Contribute**: Read open-source codebases or write a technical blog post dissecting advanced patterns.\n")
        lines.append("#### 🎓 Next-Level Recommendation")
        lines.append("• Continue challenging yourself with higher-level systems design and cross-disciplinary concepts.")

    return "\n".join(lines)


def generate_seven_day_study_plan(subject_id, subject_name, score=None, total=None,
                                  weak_topics=None, topic_results=None, recommended_resources=None):
    """
    Generates a structured, realistic, actionable 7-day study plan.
    Prioritizes the student's actual identified learning gaps.
    If no gaps or high score, provides an advanced mastery challenge plan.
    If no assessment data exists, provides a general starter foundation plan.
    """
    weak_topics = weak_topics or []
    subject_dict = OFFLINE_KNOWLEDGE.get(subject_name, {})
    all_subject_topics = list(subject_dict.keys())
    
    # Extract clean topic names from weak_topics (which may have percentages like 'Python Basics (50%)')
    clean_weak = []
    for item in weak_topics:
        for t in all_subject_topics:
            if t in item and t not in clean_weak:
                clean_weak.append(t)
                break

    # Resource map lookup helper
    def get_resource_for_topic(topic_name, default_url="https://docs.python.org/3/"):
        if recommended_resources:
            for r in recommended_resources:
                if r.get("topic") == topic_name or topic_name in r.get("title", ""):
                    return r.get("title"), r.get("url")
        return f"{topic_name} Verified Learning Materials", f"/resources?subject={subject_id}&topic={topic_name.replace(' ', '%20')}"

    days = []

    # Scenario A: Student has identified gaps
    if clean_weak:
        p1 = clean_weak[0]
        p2 = clean_weak[1] if len(clean_weak) > 1 else clean_weak[0]
        p3 = clean_weak[2] if len(clean_weak) > 2 else all_subject_topics[0]

        r1_title, r1_url = get_resource_for_topic(p1)
        r2_title, r2_url = get_resource_for_topic(p2)
        r3_title, r3_url = get_resource_for_topic(p3)

        info1 = subject_dict.get(p1, {})
        info2 = subject_dict.get(p2, {})

        plan_type = "Personalized Gap Closure Plan"
        is_starter = False
        description = f"Targeted 7-day study schedule specifically addressing your learning gaps in {p1} and {p2} from your recent {subject_name} assessment."

        days = [
            {
                "day_num": 1,
                "task_id": "day_1",
                "title": f"Day 1: Conceptual Foundations — {p1}",
                "topic": p1,
                "focus": info1.get("meaning", f"Master core definitions and rules in {p1}."),
                "action": f"Read the verified learning resource. Summarize 3 core principles in your own notes.",
                "resource_title": r1_title,
                "resource_url": r1_url,
                "estimated_time": "35–45 mins"
            },
            {
                "day_num": 2,
                "task_id": "day_2",
                "title": f"Day 2: Pitfalls & Common Mistakes — {p1}",
                "topic": p1,
                "focus": "Review common student mistakes and memorize quick hints.",
                "action": f"Practice: {info1.get('practice', 'Build a focused coding or analysis example.')}",
                "resource_title": r1_title,
                "resource_url": r1_url,
                "estimated_time": "30–40 mins"
            },
            {
                "day_num": 3,
                "task_id": "day_3",
                "title": f"Day 3: Deep Dive — {p2}",
                "topic": p2,
                "focus": info2.get("meaning", f"Understand foundational mechanisms in {p2}."),
                "action": f"Study the recommended reference. Identify where errors occurred on the quiz.",
                "resource_title": r2_title,
                "resource_url": r2_url,
                "estimated_time": "40 mins"
            },
            {
                "day_num": 4,
                "task_id": "day_4",
                "title": f"Day 4: Practical Application — {p2}",
                "topic": p2,
                "focus": "Hands-on execution and edge-case behavior.",
                "action": f"Practice: {info2.get('practice', 'Complete two targeted exercises.')}",
                "resource_title": r2_title,
                "resource_url": r2_url,
                "estimated_time": "35 mins"
            },
            {
                "day_num": 5,
                "task_id": "day_5",
                "title": "Day 5: Synthesis & Cross-Topic Practice",
                "topic": f"{p1} & {p2}",
                "focus": "Connecting concepts and building combined solutions.",
                "action": "Write a short summary linking both topics together. Solve 3 practical challenge questions.",
                "resource_title": f"{subject_name} Resources Catalogue",
                "resource_url": f"/resources?subject={subject_id}",
                "estimated_time": "45 mins"
            },
            {
                "day_num": 6,
                "task_id": "day_6",
                "title": "Day 6: Active Recall & Mock Self-Testing",
                "topic": subject_name,
                "focus": "Testing retention without looking at references.",
                "action": "Explain the key rules of both topics out loud or on paper. Verify against memory hooks.",
                "resource_title": "Verified Study Notes",
                "resource_url": f"/quiz/{subject_id}",
                "estimated_time": "30 mins"
            },
            {
                "day_num": 7,
                "task_id": "day_7",
                "title": "Day 7: Assessment Retake & Gap Closure Check",
                "topic": subject_name,
                "focus": "Verify improvement and measure gap closure.",
                "action": f"Retake the 10-question {subject_name} diagnostic to confirm your score improvement.",
                "resource_title": f"Retake {subject_name} Assessment",
                "resource_url": f"/quiz/{subject_id}",
                "estimated_time": "20 mins"
            }
        ]

    # Scenario B: High score / All topics strong
    elif score is not None and total is not None and score >= int(total * 0.7):
        plan_type = "Advanced Mastery & Systems Design Plan"
        is_starter = False
        description = f"Advanced 7-day roadmap to deepen your strong comprehension ({score}/{total}) in {subject_name} into production-grade systems mastery."

        r_title, r_url = get_resource_for_topic(all_subject_topics[0] if all_subject_topics else subject_name)

        days = [
            {
                "day_num": 1,
                "task_id": "day_1",
                "title": "Day 1: Architectural Internals",
                "topic": all_subject_topics[0] if all_subject_topics else subject_name,
                "focus": "Analyze underlying memory layouts, execution runtimes, and engine internals.",
                "action": "Read the advanced sections of the core reference manual.",
                "resource_title": r_title,
                "resource_url": r_url,
                "estimated_time": "40 mins"
            },
            {
                "day_num": 2,
                "task_id": "day_2",
                "title": "Day 2: Asymptotic Optimization & Profiling",
                "topic": all_subject_topics[1] if len(all_subject_topics) > 1 else subject_name,
                "focus": "Measure execution time, algorithmic bottlenecks, and memory footprints.",
                "action": "Profile code or query execution under scale constraints.",
                "resource_title": f"{subject_name} Advanced Materials",
                "resource_url": f"/resources?subject={subject_id}&difficulty=Advanced",
                "estimated_time": "45 mins"
            },
            {
                "day_num": 3,
                "task_id": "day_3",
                "title": "Day 3: Concurrency & Edge Cases",
                "topic": all_subject_topics[2] if len(all_subject_topics) > 2 else subject_name,
                "focus": "Inspect race conditions, synchronization, and boundary limits.",
                "action": "Write unit tests targeting corner cases and edge conditions.",
                "resource_title": "Official Documentation",
                "resource_url": f"/resources?subject={subject_id}",
                "estimated_time": "40 mins"
            },
            {
                "day_num": 4,
                "task_id": "day_4",
                "title": "Day 4: Production Design Patterns",
                "topic": all_subject_topics[3] if len(all_subject_topics) > 3 else subject_name,
                "focus": "Study production architectures and real-world trade-offs.",
                "action": "Review open-source codebases or standard engineering design documents.",
                "resource_title": "Curated Engineering Tutorials",
                "resource_url": f"/resources?subject={subject_id}",
                "estimated_time": "45 mins"
            },
            {
                "day_num": 5,
                "task_id": "day_5",
                "title": "Day 5: Portfolio Mini-Project",
                "topic": subject_name,
                "focus": "Implement a real-world utility showcasing end-to-end fluency.",
                "action": "Build a modular application incorporating core concepts from this subject.",
                "resource_title": "Practice Catalog",
                "resource_url": f"/resources?subject={subject_id}",
                "estimated_time": "60 mins"
            },
            {
                "day_num": 6,
                "task_id": "day_6",
                "title": "Day 6: Mock Technical Interview Defense",
                "topic": subject_name,
                "focus": "Verbalize complex design trade-offs without referencing notes.",
                "action": "Explain 3 challenging concepts to a peer or write a technical blog post.",
                "resource_title": "Progress Dashboard",
                "resource_url": "/progress",
                "estimated_time": "35 mins"
            },
            {
                "day_num": 7,
                "task_id": "day_7",
                "title": "Day 7: Next-Level Discipline Transition",
                "topic": "Curriculum Exploration",
                "focus": "Branch into related curriculum subjects (e.g. Networks, DBMS, OS).",
                "action": "Take an assessment in a complementary subject to expand curriculum coverage.",
                "resource_title": "All Subjects Catalog",
                "resource_url": "/subjects",
                "estimated_time": "20 mins"
            }
        ]

    # Scenario C: General Starter Foundation Plan (No assessment yet)
    else:
        plan_type = "General Starter Foundation Plan"
        is_starter = True
        description = f"Foundational 7-day orientation syllabus introducing core topics in {subject_name}. (Take an assessment anytime to personalize this plan!)"

        t_list = all_subject_topics if all_subject_topics else [f"Topic {i+1}" for i in range(5)]
        
        days = []
        for i in range(5):
            t_name = t_list[i] if i < len(t_list) else f"Advanced Concept {i+1}"
            r_t, r_u = get_resource_for_topic(t_name)
            t_info = subject_dict.get(t_name, {})
            days.append({
                "day_num": i + 1,
                "task_id": f"day_{i+1}",
                "title": f"Day {i+1}: Foundations of {t_name}",
                "topic": t_name,
                "focus": t_info.get("meaning", f"Introduction to {t_name} concepts and terminology."),
                "action": f"Read the beginner guide and practice key concepts.",
                "resource_title": r_t,
                "resource_url": r_u,
                "estimated_time": "30–40 mins"
            })

        days.append({
            "day_num": 6,
            "task_id": "day_6",
            "title": f"Day 6: Cross-Topic Revision & Flashcards",
            "topic": subject_name,
            "focus": "Review all 5 foundational topics and memorize common syntax/rules.",
            "action": "Review key hints and avoid common beginner mistakes.",
            "resource_title": f"{subject_name} Learning Resources",
            "resource_url": f"/resources?subject={subject_id}",
            "estimated_time": "35 mins"
        })

        days.append({
            "day_num": 7,
            "task_id": "day_7",
            "title": f"Day 7: First Diagnostic Assessment",
            "topic": subject_name,
            "focus": "Pinpoint your conceptual learning gaps with our 10-question assessment.",
            "action": f"Take the official {subject_name} diagnostic to generate a personalized gap report.",
            "resource_title": f"Start {subject_name} Assessment",
            "resource_url": f"/quiz/{subject_id}",
            "estimated_time": "15 mins"
        })

    return {
        "plan_type": plan_type,
        "is_starter": is_starter,
        "subject_id": subject_id,
        "subject_name": subject_name,
        "score": score,
        "total": total,
        "description": description,
        "days": days
    }

