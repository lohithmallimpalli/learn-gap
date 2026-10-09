"""
Curated Learning Resources Catalogue for LearnGap.
Provides comprehensive, college-level learning materials across all 6 subjects and 30 topics:
- Python Programming
- Machine Learning
- Data Structures
- Computer Networks
- Database Management Systems
- Operating Systems

Includes textbooks, official documentation, YouTube tutorials, free courses, and interactive practice.
"""

RESOURCES = [
    # =========================================================================
    # 1. PYTHON PROGRAMMING
    # =========================================================================

    # --- Topic: Python Basics ---
    {
        "id": "py-doc-tutorial",
        "title": "Official Python 3 Tutorial: An Informal Introduction",
        "subject_id": "python",
        "subject_name": "Python Programming",
        "topic": "Python Basics",
        "resource_type": "Official Documentation",
        "provider": "Python Software Foundation",
        "description": "The definitive first stop for learning Python. Covers basic syntax, numbers, string operations, dynamic typing, and fundamental language semantics directly from the official creators.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://docs.python.org/3/tutorial/introduction.html",
        "badge": "Official Guide"
    },
    {
        "id": "py-book-crash-course",
        "title": "Python Crash Course: A Hands-On, Project-Based Introduction",
        "subject_id": "python",
        "subject_name": "Python Programming",
        "topic": "Python Basics",
        "resource_type": "Book / Reference",
        "provider": "Eric Matthes / No Starch Press",
        "description": "Best-selling guide covering Python fundamentals, syntax conventions, environment setup, and clean programming habits with beginner-friendly exercises.",
        "difficulty": "Beginner",
        "access_type": "Paid / Reference",
        "url": "https://nostarch.com/python-crash-course-3rd-edition",
        "badge": "Core Textbook"
    },
    {
        "id": "py-yt-freecodecamp-basics",
        "title": "Python for Beginners — Full Course [12-Hour Video Tutorial]",
        "subject_id": "python",
        "subject_name": "Python Programming",
        "topic": "Python Basics",
        "resource_type": "YouTube Tutorial",
        "provider": "freeCodeCamp.org",
        "description": "Comprehensive video course covering Python fundamentals from zero to writing your first real programs, with guided walkthroughs of arithmetic operators and syntax.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=rfscVS0vtbw",
        "badge": "Video Course"
    },
    {
        "id": "py-w3schools-basics",
        "title": "W3Schools Interactive Python Syntax & Operators Tutorial",
        "subject_id": "python",
        "subject_name": "Python Programming",
        "topic": "Python Basics",
        "resource_type": "Interactive Practice",
        "provider": "W3Schools",
        "description": "Interactive browser-based playground to test expressions, understand operator precedence, string formatting, and execute Python code without installation.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.w3schools.com/python/python_syntax.asp",
        "badge": "Interactive"
    },

    # --- Topic: Variables and Data Types ---
    {
        "id": "py-doc-types",
        "title": "Python Built-in Types Reference: Numeric, Sequence & Mapping Types",
        "subject_id": "python",
        "subject_name": "Python Programming",
        "topic": "Variables and Data Types",
        "resource_type": "Official Documentation",
        "provider": "Python Software Foundation",
        "description": "Exhaustive documentation on Python's core data types, mutability versus immutability, type casting functions, and boolean evaluation rules.",
        "difficulty": "Intermediate",
        "access_type": "Free",
        "url": "https://docs.python.org/3/library/stdtypes.html",
        "badge": "Official Guide"
    },
    {
        "id": "py-yt-corey-types",
        "title": "Python Tutorial: Integers, Floats, and Working with Numeric Data",
        "subject_id": "python",
        "subject_name": "Python Programming",
        "topic": "Variables and Data Types",
        "resource_type": "YouTube Tutorial",
        "provider": "Corey Schafer",
        "description": "Clear conceptual video breaking down integer vs float behavior, type conversion, string slicing, and immutability pitfalls.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=khKv-8q7YmY",
        "badge": "Video Tutorial"
    },
    {
        "id": "py-realpython-datatypes",
        "title": "Real Python: Basic Data Types in Python Guide",
        "subject_id": "python",
        "subject_name": "Python Programming",
        "topic": "Variables and Data Types",
        "resource_type": "Free Course",
        "provider": "Real Python",
        "description": "In-depth guide explaining how Python objects are stored in memory, dynamic reference binding, and single-element tuple rules.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://realpython.com/python-data-types/",
        "badge": "Study Guide"
    },

    # --- Topic: Control Statements ---
    {
        "id": "py-doc-controlflow",
        "title": "Python Documentation: More Control Flow Tools (if, for, while, break)",
        "subject_id": "python",
        "subject_name": "Python Programming",
        "topic": "Control Statements",
        "resource_type": "Official Documentation",
        "provider": "Python Software Foundation",
        "description": "Covers if-elif-else statements, for-loop iteration protocols, the range() generator function, break and continue statements, and loop else clauses.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://docs.python.org/3/tutorial/controlflow.html",
        "badge": "Official Guide"
    },
    {
        "id": "py-yt-socratica-loops",
        "title": "Python If, Elif, Else & For Loops Explained Beautifully",
        "subject_id": "python",
        "subject_name": "Python Programming",
        "topic": "Control Statements",
        "resource_type": "YouTube Tutorial",
        "provider": "Socratica",
        "description": "High-production video tutorials clearly explaining boolean conditionals, truthy/falsy evaluation, and loop nesting techniques.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=f4KOjWS_KFs",
        "badge": "Video Tutorial"
    },
    {
        "id": "py-practice-loops-hackerrank",
        "title": "HackerRank: Python Control Flow & Loops Practice Set",
        "subject_id": "python",
        "subject_name": "Python Programming",
        "topic": "Control Statements",
        "resource_type": "Interactive Practice",
        "provider": "HackerRank",
        "description": "Solve graduated coding problems testing conditionals, loop logic, off-by-one boundary checks, and sequence traversal.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.hackerrank.com/domains/python",
        "badge": "Coding Challenges"
    },

    # --- Topic: Functions ---
    {
        "id": "py-book-fluent-python",
        "title": "Fluent Python: Clear, Concise, and Effective Programming",
        "subject_id": "python",
        "subject_name": "Python Programming",
        "topic": "Functions",
        "resource_type": "Book / Reference",
        "provider": "Luciano Ramalho / O'Reilly Media",
        "description": "Industry-standard book dissecting first-class functions, closures, decorators, lambda functions, *args, and **kwargs argument unpacking.",
        "difficulty": "Advanced",
        "access_type": "Paid / Reference",
        "url": "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/",
        "badge": "Advanced Reference"
    },
    {
        "id": "py-yt-corey-functions",
        "title": "Python Tutorial: Functions and *args, **kwargs Masterclass",
        "subject_id": "python",
        "subject_name": "Python Programming",
        "topic": "Functions",
        "resource_type": "YouTube Tutorial",
        "provider": "Corey Schafer",
        "description": "Step-by-step masterclass demonstrating positional parameters, keyword parameters, variable scopes (LEGB rule), and avoiding mutable default argument traps.",
        "difficulty": "Intermediate",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=9Os0o3wzS_I",
        "badge": "Video Masterclass"
    },

    # --- Topic: Lists, Tuples and Dictionaries ---
    {
        "id": "py-doc-datastructures",
        "title": "Python Official Tutorial: Data Structures (Lists, Tuples, Dictionaries & Sets)",
        "subject_id": "python",
        "subject_name": "Python Programming",
        "topic": "Lists, Tuples and Dictionaries",
        "resource_type": "Official Documentation",
        "provider": "Python Software Foundation",
        "description": "Comprehensive tutorial covering list methods (.append, .pop, .insert), list comprehensions, immutable tuple packing, and dictionary hash-map techniques.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://docs.python.org/3/tutorial/datastructures.html",
        "badge": "Official Guide"
    },
    {
        "id": "py-yt-freecodecamp-dicts",
        "title": "Python Dictionaries, Tuples and Sets Tutorial",
        "subject_id": "python",
        "subject_name": "Python Programming",
        "topic": "Lists, Tuples and Dictionaries",
        "resource_type": "YouTube Tutorial",
        "provider": "freeCodeCamp.org",
        "description": "Hands-on video dissecting key-value retrieval using .get(), dictionary iteration, nested lists, and dictionary comprehensions.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=daefaLgNkw0",
        "badge": "Video Tutorial"
    },

    # =========================================================================
    # 2. MACHINE LEARNING
    # =========================================================================

    # --- Topic: Linear Regression ---
    {
        "id": "ml-doc-sklearn-linear",
        "title": "scikit-learn Documentation: Linear Models and Ordinary Least Squares",
        "subject_id": "ml",
        "subject_name": "Machine Learning",
        "topic": "Linear Regression",
        "resource_type": "Official Documentation",
        "provider": "scikit-learn.org",
        "description": "Official guide detailing LinearRegression mathematical formulations, Ordinary Least Squares (OLS), Mean Squared Error (MSE), and R-squared calculation.",
        "difficulty": "Intermediate",
        "access_type": "Free",
        "url": "https://scikit-learn.org/stable/modules/linear_model.html",
        "badge": "Official Guide"
    },
    {
        "id": "ml-book-hands-on",
        "title": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow",
        "subject_id": "ml",
        "subject_name": "Machine Learning",
        "topic": "Linear Regression",
        "resource_type": "Book / Reference",
        "provider": "Aurélien Géron / O'Reilly Media",
        "description": "Widely acclaimed textbook walking through the complete machine learning lifecycle, loss functions, gradient descent, and linear modeling.",
        "difficulty": "Intermediate",
        "access_type": "Paid / Reference",
        "url": "https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/",
        "badge": "Core Textbook"
    },
    {
        "id": "ml-yt-statquest-linear",
        "title": "Linear Regression Clearly Explained and Step-by-Step",
        "subject_id": "ml",
        "subject_name": "Machine Learning",
        "topic": "Linear Regression",
        "resource_type": "YouTube Tutorial",
        "provider": "StatQuest with Josh Starmer",
        "description": "World-famous visual breakdown of how the line of best fit is calculated, minimizing squared residuals, and understanding slope and intercept intuitively.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=nk2CQITm_eo",
        "badge": "Top Video Pick"
    },
    {
        "id": "ml-kaggle-intro",
        "title": "Kaggle Learn: Intro to Machine Learning & Model Evaluation",
        "subject_id": "ml",
        "subject_name": "Machine Learning",
        "topic": "Linear Regression",
        "resource_type": "Free Course",
        "provider": "Kaggle Learn",
        "description": "Interactive micro-course building and validating linear regression and tree models on the Melbourne Housing dataset with Mean Absolute Error and MSE.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.kaggle.com/learn/intro-to-machine-learning",
        "badge": "Interactive Course"
    },

    # --- Topic: Logistic Regression ---
    {
        "id": "ml-doc-sklearn-logistic",
        "title": "scikit-learn Documentation: Logistic Regression for Classification",
        "subject_id": "ml",
        "subject_name": "Machine Learning",
        "topic": "Logistic Regression",
        "resource_type": "Official Documentation",
        "provider": "scikit-learn.org",
        "description": "Mathematical documentation explaining the Sigmoid function, cross-entropy log-loss, decision thresholds, and binary vs multiclass logistic classification.",
        "difficulty": "Intermediate",
        "access_type": "Free",
        "url": "https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html",
        "badge": "Official Guide"
    },
    {
        "id": "ml-yt-statquest-logistic",
        "title": "Logistic Regression Details and Log-Odds Visually Explained",
        "subject_id": "ml",
        "subject_name": "Machine Learning",
        "topic": "Logistic Regression",
        "resource_type": "YouTube Tutorial",
        "provider": "StatQuest with Josh Starmer",
        "description": "Visual explanation of probability versus odds, converting straight lines into S-curves with the Sigmoid function, and maximum likelihood estimation.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=yIYKR4gJWPM",
        "badge": "Top Video Pick"
    },
    {
        "id": "ml-google-crash-course",
        "title": "Google Machine Learning Crash Course: Classification & Logistic Regression",
        "subject_id": "ml",
        "subject_name": "Machine Learning",
        "topic": "Logistic Regression",
        "resource_type": "Free Course",
        "provider": "Google Developers",
        "description": "Google's free ML course covering classification metrics, ROC-AUC curves, confusion matrices, and tuning decision thresholds for real-world applications.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://developers.google.com/machine-learning/crash-course/logistic-regression",
        "badge": "Interactive Course"
    },

    # --- Topic: Decision Tree ---
    {
        "id": "ml-doc-sklearn-trees",
        "title": "scikit-learn Documentation: Decision Trees for Classification & Regression",
        "subject_id": "ml",
        "subject_name": "Machine Learning",
        "topic": "Decision Tree",
        "resource_type": "Official Documentation",
        "provider": "scikit-learn.org",
        "description": "Official guide on CART algorithm implementation, Gini impurity versus Shannon entropy, tree pruning methods, and visualizing tree structures.",
        "difficulty": "Intermediate",
        "access_type": "Free",
        "url": "https://scikit-learn.org/stable/modules/tree.html",
        "badge": "Official Guide"
    },
    {
        "id": "ml-yt-statquest-tree",
        "title": "Decision Trees and Gini Impurity Step-by-Step",
        "subject_id": "ml",
        "subject_name": "Machine Learning",
        "topic": "Decision Tree",
        "resource_type": "YouTube Tutorial",
        "provider": "StatQuest with Josh Starmer",
        "description": "Clear step-by-step walkthrough calculating Gini Impurity from scratch to decide optimal splits at the root and decision nodes.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=7VeUPuFGJHk",
        "badge": "Top Video Pick"
    },

    # --- Topic: K-Means ---
    {
        "id": "ml-doc-sklearn-kmeans",
        "title": "scikit-learn Documentation: K-Means Clustering and Lloyd's Algorithm",
        "subject_id": "ml",
        "subject_name": "Machine Learning",
        "topic": "K-Means",
        "resource_type": "Official Documentation",
        "provider": "scikit-learn.org",
        "description": "Technical guide on K-Means clustering, centroid recomputation, k-means++ smart initialization, inertia metrics, and convergence criteria.",
        "difficulty": "Intermediate",
        "access_type": "Free",
        "url": "https://scikit-learn.org/stable/modules/clustering.html#k-means",
        "badge": "Official Guide"
    },
    {
        "id": "ml-yt-statquest-kmeans",
        "title": "K-Means Clustering Clearly Explained with Real Examples",
        "subject_id": "ml",
        "subject_name": "Machine Learning",
        "topic": "K-Means",
        "resource_type": "YouTube Tutorial",
        "provider": "StatQuest with Josh Starmer",
        "description": "Animated visual guide demonstrating centroid initialization, assigning data points by Euclidean distance, and using the Elbow Method to choose optimal K.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=4b5d3muPQmA",
        "badge": "Top Video Pick"
    },

    # --- Topic: PCA ---
    {
        "id": "ml-doc-sklearn-pca",
        "title": "scikit-learn Documentation: Principal Component Analysis (PCA)",
        "subject_id": "ml",
        "subject_name": "Machine Learning",
        "topic": "PCA",
        "resource_type": "Official Documentation",
        "provider": "scikit-learn.org",
        "description": "Official reference covering linear dimensionality reduction via Singular Value Decomposition (SVD), explained variance ratios, and orthogonal projections.",
        "difficulty": "Advanced",
        "access_type": "Free",
        "url": "https://scikit-learn.org/stable/modules/decomposition.html#pca",
        "badge": "Official Guide"
    },
    {
        "id": "ml-yt-statquest-pca",
        "title": "Principal Component Analysis (PCA) Step-by-Step",
        "subject_id": "ml",
        "subject_name": "Machine Learning",
        "topic": "PCA",
        "resource_type": "YouTube Tutorial",
        "provider": "StatQuest with Josh Starmer",
        "description": "The internet's most widely praised tutorial on PCA. Dissects how high-dimensional clouds are projected to 2D components while maximizing variance.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=FgakZw6K1QQ",
        "badge": "Top Video Pick"
    },

    # =========================================================================
    # 3. DATA STRUCTURES
    # =========================================================================

    # --- Topic: Arrays ---
    {
        "id": "dsa-book-clrs",
        "title": "Introduction to Algorithms (CLRS 4th Edition)",
        "subject_id": "dsa",
        "subject_name": "Data Structures",
        "topic": "Arrays",
        "resource_type": "Book / Reference",
        "provider": "Cormen, Leiserson, Rivest, Stein / MIT Press",
        "description": "The gold-standard academic computer science textbook on asymptotic analysis, memory layout, dynamic array amortization, and sorting algorithms.",
        "difficulty": "Advanced",
        "access_type": "Paid / Reference",
        "url": "https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/",
        "badge": "Core Textbook"
    },
    {
        "id": "dsa-yt-abdul-arrays",
        "title": "Array Representation in Memory & Dynamic Arrays Tutorial",
        "subject_id": "dsa",
        "subject_name": "Data Structures",
        "topic": "Arrays",
        "resource_type": "YouTube Tutorial",
        "provider": "Abdul Bari",
        "description": "Celebrated university lecturer Abdul Bari details contiguous address calculation, 2D array row-major and column-major formulas, and resizing.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=1jtrfqw5WJc",
        "badge": "Video Lecture"
    },
    {
        "id": "dsa-practice-leetcode-arrays",
        "title": "LeetCode Explore: Array 101 Interactive Problem Track",
        "subject_id": "dsa",
        "subject_name": "Data Structures",
        "topic": "Arrays",
        "resource_type": "Interactive Practice",
        "provider": "LeetCode",
        "description": "Curated track of standard array problems covering in-place element removal, two-pointer scanning, duplicate detection, and running prefix sums.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://leetcode.com/explore/learn/card/fun-with-arrays/",
        "badge": "Coding Track"
    },

    # --- Topic: Linked Lists ---
    {
        "id": "dsa-gfg-linkedlist",
        "title": "GeeksforGeeks: Linked List Data Structure Complete Guide",
        "subject_id": "dsa",
        "subject_name": "Data Structures",
        "topic": "Linked Lists",
        "resource_type": "Official Documentation",
        "provider": "GeeksforGeeks",
        "description": "Comprehensive reference guide detailing Singly Linked Lists, Doubly Linked Lists, Circular Lists, pointer manipulations, and memory comparisons.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.geeksforgeeks.org/data-structures/linked-list/",
        "badge": "Study Guide"
    },
    {
        "id": "dsa-yt-mycodeschool-ll",
        "title": "Introduction to Linked Lists and Node Pointer Implementation",
        "subject_id": "dsa",
        "subject_name": "Data Structures",
        "topic": "Linked Lists",
        "resource_type": "YouTube Tutorial",
        "provider": "mycodeschool",
        "description": "Renowned tutorial visually walking through heap node allocation, head pointers, reversing a linked list, and cycle detection.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=NobHlGUjV3g",
        "badge": "Classic Tutorial"
    },

    # --- Topic: Stacks ---
    {
        "id": "dsa-yt-abdul-stack",
        "title": "Stack Data Structure: Push, Pop, Call Stack & Infix to Postfix",
        "subject_id": "dsa",
        "subject_name": "Data Structures",
        "topic": "Stacks",
        "resource_type": "YouTube Tutorial",
        "provider": "Abdul Bari",
        "description": "Clear conceptual lecture covering LIFO operations, stack overflow/underflow, expression parsing, and recursion stack management.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=sFVxsatODVc",
        "badge": "Video Lecture"
    },
    {
        "id": "dsa-practice-leetcode-stack",
        "title": "LeetCode Practice: Valid Parentheses & Stack Applications",
        "subject_id": "dsa",
        "subject_name": "Data Structures",
        "topic": "Stacks",
        "resource_type": "Interactive Practice",
        "provider": "LeetCode",
        "description": "Practice the classic Valid Parentheses problem (Problem #20), monotonic stack problems, and evaluate reverse polish notation.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://leetcode.com/tag/stack/",
        "badge": "Coding Challenges"
    },

    # --- Topic: Queues ---
    {
        "id": "dsa-yt-neso-queues",
        "title": "Queue Data Structure & Circular Queue Implementation",
        "subject_id": "dsa",
        "subject_name": "Data Structures",
        "topic": "Queues",
        "resource_type": "YouTube Tutorial",
        "provider": "Neso Academy",
        "description": "Detailed visual lecture demonstrating front and rear pointers, circular modulo arithmetic to prevent false overflow, and double-ended queues (deque).",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=okr-XE8yTO8",
        "badge": "Video Lecture"
    },

    # --- Topic: Trees ---
    {
        "id": "dsa-yt-mycodeschool-bst",
        "title": "Binary Tree & Binary Search Tree (BST) Complete Concepts",
        "subject_id": "dsa",
        "subject_name": "Data Structures",
        "topic": "Trees",
        "resource_type": "YouTube Tutorial",
        "provider": "mycodeschool",
        "description": "Legendary tutorial covering the BST ordering property, recursive In-order, Pre-order, and Post-order traversals, and Breadth-First Level Order search.",
        "difficulty": "Intermediate",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=pYT9F8_LFTM",
        "badge": "Classic Tutorial"
    },
    {
        "id": "dsa-book-goodrich",
        "title": "Data Structures and Algorithms in Python",
        "subject_id": "dsa",
        "subject_name": "Data Structures",
        "topic": "Trees",
        "resource_type": "Book / Reference",
        "provider": "Michael T. Goodrich, Roberto Tamassia / Wiley",
        "description": "University textbook providing rigorous code implementations of BSTs, AVL balanced trees, and heap priority queues in Python.",
        "difficulty": "Intermediate",
        "access_type": "Paid / Reference",
        "url": "https://www.wiley.com/en-us/Data+Structures+and+Algorithms+in+Python-p-9781118290279",
        "badge": "University Reference"
    },

    # =========================================================================
    # 4. COMPUTER NETWORKS
    # =========================================================================

    # --- Topic: OSI Model ---
    {
        "id": "cn-book-kurose",
        "title": "Computer Networking: A Top-Down Approach (8th Edition)",
        "subject_id": "cn",
        "subject_name": "Computer Networks",
        "topic": "OSI Model",
        "resource_type": "Book / Reference",
        "provider": "James Kurose and Keith Ross / Pearson",
        "description": "The world's leading computer networking textbook. Explains protocols from the application layer down to the physical wire with clear diagrams.",
        "difficulty": "Intermediate",
        "access_type": "Paid / Reference",
        "url": "https://www.pearson.com/en-us/subject-catalog/p/computer-networking-a-top-down-approach/P200000003333",
        "badge": "Core Textbook"
    },
    {
        "id": "cn-yt-neso-osi",
        "title": "OSI Model Explained with Real World Examples (All 7 Layers)",
        "subject_id": "cn",
        "subject_name": "Computer Networks",
        "topic": "OSI Model",
        "resource_type": "YouTube Tutorial",
        "provider": "Neso Academy",
        "description": "Detailed video course breaking down encapsulation, headers, and protocol responsibilities across Physical, Data Link, Network, and Transport layers.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=vv4y_uOneC0",
        "badge": "Top Video Pick"
    },

    # --- Topic: TCP/IP ---
    {
        "id": "cn-doc-ietf-rfc",
        "title": "IETF RFC 791 & 793: Official Internet Protocol Specifications",
        "subject_id": "cn",
        "subject_name": "Computer Networks",
        "topic": "TCP/IP",
        "resource_type": "Official Documentation",
        "provider": "Internet Engineering Task Force (IETF)",
        "description": "The foundational RFC engineering documents specifying packet headers, ARP resolution, ICMP diagnostic signaling, and internet protocols.",
        "difficulty": "Advanced",
        "access_type": "Free",
        "url": "https://www.rfc-editor.org/info/rfc791",
        "badge": "Official Specs"
    },
    {
        "id": "cn-yt-ben-eater-networking",
        "title": "How the Internet Works: Packets, Routing and ARP Walkthrough",
        "subject_id": "cn",
        "subject_name": "Computer Networks",
        "topic": "TCP/IP",
        "resource_type": "YouTube Tutorial",
        "provider": "Ben Eater",
        "description": "Acclaimed hardware engineer Ben Eater inspects actual binary packets on an oscilloscope and explains how ARP translates IP addresses to MAC frames.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=rYodcvhh7b8",
        "badge": "Video Masterclass"
    },

    # --- Topic: IP Addressing ---
    {
        "id": "cn-cisco-netacad",
        "title": "Cisco Networking Academy: Free Networking Basics & IP Addressing",
        "subject_id": "cn",
        "subject_name": "Computer Networks",
        "topic": "IP Addressing",
        "resource_type": "Free Course",
        "provider": "Cisco NetAcad",
        "description": "Official Cisco introductory course on IPv4 octets, CIDR prefix notation (/24), IPv6 128-bit architecture, and subnet calculation.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.netacad.com/courses/networking/networking-basics",
        "badge": "Cisco Verified"
    },
    {
        "id": "cn-yt-prof-messer-subnetting",
        "title": "Seven Second Subnetting: Easy Subnet Mask Calculations",
        "subject_id": "cn",
        "subject_name": "Computer Networks",
        "topic": "IP Addressing",
        "resource_type": "YouTube Tutorial",
        "provider": "Professor Messer",
        "description": "Industry-standard exam prep video teaching shortcuts to calculate usable IP host ranges, broadcast addresses, and subnet boundaries instantly.",
        "difficulty": "Intermediate",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=docsTfn8Wn8",
        "badge": "Video Tutorial"
    },

    # --- Topic: Routing ---
    {
        "id": "cn-yt-powercert-routing",
        "title": "Routers, Routing Tables, and Dynamic Protocols Explained",
        "subject_id": "cn",
        "subject_name": "Computer Networks",
        "topic": "Routing",
        "resource_type": "YouTube Tutorial",
        "provider": "PowerCert Animated Videos",
        "description": "Animated visual comparison of Distance-Vector protocols (RIP hop count) versus Link-State protocols (OSPF cost and bandwidth metrics).",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=1z0ULvg_pW8",
        "badge": "Animated Guide"
    },

    # --- Topic: TCP and UDP ---
    {
        "id": "cn-yt-computerphile-tcp",
        "title": "TCP vs UDP Comparison & The Three-Way Handshake",
        "subject_id": "cn",
        "subject_name": "Computer Networks",
        "topic": "TCP and UDP",
        "resource_type": "YouTube Tutorial",
        "provider": "Computerphile",
        "description": "University professors break down packet sequencing, SYN-ACK three-way handshake, retransmission timeout, and why UDP is preferred for live video.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=Vdc8TCESIg8",
        "badge": "Video Lecture"
    },

    # =========================================================================
    # 5. DATABASE MANAGEMENT SYSTEMS
    # =========================================================================

    # --- Topic: SQL ---
    {
        "id": "dbms-doc-mysql",
        "title": "MySQL 8.0 Reference Manual: SQL Statements and Aggregations",
        "subject_id": "dbms",
        "subject_name": "Database Management Systems",
        "topic": "SQL",
        "resource_type": "Official Documentation",
        "provider": "Oracle / MySQL",
        "description": "Official documentation covering SELECT statements, WHERE filtering, GROUP BY aggregation, HAVING clauses, and DDL commands.",
        "difficulty": "Intermediate",
        "access_type": "Free",
        "url": "https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html",
        "badge": "Official Docs"
    },
    {
        "id": "dbms-practice-sqlbolt",
        "title": "SQLBolt: Interactive Lessons and Practical SQL Query Practice",
        "subject_id": "dbms",
        "subject_name": "Database Management Systems",
        "topic": "SQL",
        "resource_type": "Interactive Practice",
        "provider": "SQLBolt",
        "description": "Free interactive tutorial where you write real SQL queries directly in the browser to filter, group, aggregate, and update data.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://sqlbolt.com/",
        "badge": "Interactive Practice"
    },
    {
        "id": "dbms-yt-freecodecamp-sql",
        "title": "SQL Tutorial - Full Database Course for Beginners [4-Hour Video]",
        "subject_id": "dbms",
        "subject_name": "Database Management Systems",
        "topic": "SQL",
        "resource_type": "YouTube Tutorial",
        "provider": "freeCodeCamp.org",
        "description": "Complete beginner database course teaching schema design, CRUD operations, aggregation functions, and real-world database queries.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY",
        "badge": "Full Video Course"
    },

    # --- Topic: Keys ---
    {
        "id": "dbms-book-silberschatz",
        "title": "Database System Concepts (7th Edition)",
        "subject_id": "dbms",
        "subject_name": "Database Management Systems",
        "topic": "Keys",
        "resource_type": "Book / Reference",
        "provider": "Abraham Silberschatz, Henry Korth, S. Sudarshan / McGraw-Hill",
        "description": "The quintessential university database textbook. Comprehensive coverage of relational schemas, Primary/Foreign keys, and relational algebra.",
        "difficulty": "Intermediate",
        "access_type": "Paid / Reference",
        "url": "https://www.db-book.com/",
        "badge": "Core Textbook"
    },
    {
        "id": "dbms-yt-gate-keys",
        "title": "Primary Key, Candidate Key, Super Key & Foreign Key Demystified",
        "subject_id": "dbms",
        "subject_name": "Database Management Systems",
        "topic": "Keys",
        "resource_type": "YouTube Tutorial",
        "provider": "Gate Smashers",
        "description": "Clear conceptual video breaking down candidate keys as minimal super keys, foreign key referential constraints, and composite keys.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=84hBq_j_d5k",
        "badge": "Video Tutorial"
    },

    # --- Topic: Normalization ---
    {
        "id": "dbms-yt-deba-norm",
        "title": "Database Normalization: 1NF, 2NF, 3NF and BCNF with Real Examples",
        "subject_id": "dbms",
        "subject_name": "Database Management Systems",
        "topic": "Normalization",
        "resource_type": "YouTube Tutorial",
        "provider": "DeBary Tutorials",
        "description": "Real-world walkthrough decomposing unnormalized spreadsheets into 1NF (atomic attributes), 2NF (no partial dependencies), and 3NF.",
        "difficulty": "Intermediate",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=xoTYrQCau-Y",
        "badge": "Step-by-Step Guide"
    },

    # --- Topic: Transactions ---
    {
        "id": "dbms-doc-postgres-acid",
        "title": "PostgreSQL Documentation: Transactions, Concurrency Control & ACID",
        "subject_id": "dbms",
        "subject_name": "Database Management Systems",
        "topic": "Transactions",
        "resource_type": "Official Documentation",
        "provider": "PostgreSQL Global Development Group",
        "description": "Detailed architectural documentation explaining transaction atomicity, durability write-ahead logging (WAL), and multi-version concurrency control (MVCC).",
        "difficulty": "Advanced",
        "access_type": "Free",
        "url": "https://www.postgresql.org/docs/current/tutorial-transactions.html",
        "badge": "Official Docs"
    },
    {
        "id": "dbms-yt-gate-acid",
        "title": "ACID Properties of Database Transactions with Banking Examples",
        "subject_id": "dbms",
        "subject_name": "Database Management Systems",
        "topic": "Transactions",
        "resource_type": "YouTube Tutorial",
        "provider": "Gate Smashers",
        "description": "Uses bank transfer scenarios to explain how Atomicity prevents partial transfers, Isolation avoids dirty reads, and Durability protects against crashes.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=gaPn_8h2m8s",
        "badge": "Video Tutorial"
    },

    # --- Topic: Joins ---
    {
        "id": "dbms-w3schools-joins",
        "title": "W3Schools Visual SQL Joins Guide: INNER, LEFT, RIGHT & FULL",
        "subject_id": "dbms",
        "subject_name": "Database Management Systems",
        "topic": "Joins",
        "resource_type": "Interactive Practice",
        "provider": "W3Schools",
        "description": "Interactive Venn diagram guide with executable SQL queries demonstrating row retention in LEFT JOIN versus matched rows in INNER JOIN.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.w3schools.com/sql/sql_join.asp",
        "badge": "Interactive Tutorial"
    },

    # =========================================================================
    # 6. OPERATING SYSTEMS
    # =========================================================================

    # --- Topic: Processes ---
    {
        "id": "os-book-dinosaur",
        "title": "Operating System Concepts (The Dinosaur Book, 10th Edition)",
        "subject_id": "os",
        "subject_name": "Operating Systems",
        "topic": "Processes",
        "resource_type": "Book / Reference",
        "provider": "Silberschatz, Galvin, Gagne / Wiley",
        "description": "The quintessential computer science operating systems textbook. Thoroughly explains process states, PCB layout, fork() system calls, and context switching.",
        "difficulty": "Intermediate",
        "access_type": "Paid / Reference",
        "url": "https://www.os-book.com/OS10/",
        "badge": "Core Textbook"
    },
    {
        "id": "os-book-ostep",
        "title": "Operating Systems: Three Easy Pieces (OSTEP - Free Online Textbook)",
        "subject_id": "os",
        "subject_name": "Operating Systems",
        "topic": "Processes",
        "resource_type": "Free Course",
        "provider": "Remzi & Andrea Arpaci-Dusseau / University of Wisconsin",
        "description": "Widely beloved, freely available university textbook dissecting Virtualization, Concurrency, and Persistence with practical C coding examples.",
        "difficulty": "Intermediate",
        "access_type": "Free",
        "url": "https://pages.cs.wisc.edu/~remzi/OSTEP/",
        "badge": "Free Textbook"
    },
    {
        "id": "os-yt-neso-process",
        "title": "Process vs Program, Process States, and PCB Explained",
        "subject_id": "os",
        "subject_name": "Operating Systems",
        "topic": "Processes",
        "resource_type": "YouTube Tutorial",
        "provider": "Neso Academy",
        "description": "Visual university lecture demonstrating Process Control Block attributes, State Transition diagrams (Ready, Running, Blocked), and scheduler dispatch.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=26QPDBe-NB8",
        "badge": "Video Lecture"
    },

    # --- Topic: Threads ---
    {
        "id": "os-yt-jacob-threads",
        "title": "Multithreading vs Multiprocessing in OS: Stack, Heap & Context Switch",
        "subject_id": "os",
        "subject_name": "Operating Systems",
        "topic": "Threads",
        "resource_type": "YouTube Tutorial",
        "provider": "Jacob Sorber",
        "description": "CS professor Jacob Sorber uses real C code to demonstrate how threads share the address space while maintaining private execution stacks.",
        "difficulty": "Intermediate",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=itRLRfuLMrI",
        "badge": "Video Tutorial"
    },

    # --- Topic: CPU Scheduling ---
    {
        "id": "os-yt-neso-scheduling",
        "title": "CPU Scheduling Algorithms: FCFS, SJF, SRTF and Round Robin",
        "subject_id": "os",
        "subject_name": "Operating Systems",
        "topic": "CPU Scheduling",
        "resource_type": "YouTube Tutorial",
        "provider": "Neso Academy",
        "description": "Complete video series solving numerical scheduling problems, drawing Gantt charts, and calculating average waiting and turnaround times.",
        "difficulty": "Intermediate",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=EWkqlbflPQA",
        "badge": "Top Video Pick"
    },

    # --- Topic: Memory Management ---
    {
        "id": "os-yt-computerphile-virtual-memory",
        "title": "Virtual Memory and Paging Explained Visually",
        "subject_id": "os",
        "subject_name": "Operating Systems",
        "topic": "Memory Management",
        "resource_type": "YouTube Tutorial",
        "provider": "Computerphile",
        "description": "Fascinating visual breakdown of why virtual memory protects processes, page tables, page faults, and how thrashing degrades system throughput.",
        "difficulty": "Beginner",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=qcBIvnQt0Bw",
        "badge": "Video Lecture"
    },
    {
        "id": "os-doc-kernel-memory",
        "title": "Linux Kernel Documentation: Physical Memory Architecture & Paging",
        "subject_id": "os",
        "subject_name": "Operating Systems",
        "topic": "Memory Management",
        "resource_type": "Official Documentation",
        "provider": "The Linux Kernel Organization",
        "description": "Official documentation describing page tables, virtual address translation, demand paging, and swap space management in the Linux operating system.",
        "difficulty": "Advanced",
        "access_type": "Free",
        "url": "https://docs.kernel.org/admin-guide/mm/index.html",
        "badge": "Official Docs"
    },

    # --- Topic: Deadlocks ---
    {
        "id": "os-yt-gate-deadlocks",
        "title": "Deadlock in Operating System: 4 Coffman Conditions & Banker's Algorithm",
        "subject_id": "os",
        "subject_name": "Operating Systems",
        "topic": "Deadlocks",
        "resource_type": "YouTube Tutorial",
        "provider": "Gate Smashers",
        "description": "Step-by-step tutorial on Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait, and solving Banker's Algorithm safety matrices.",
        "difficulty": "Intermediate",
        "access_type": "Free",
        "url": "https://www.youtube.com/watch?v=rWFH6flCSBE",
        "badge": "Video Tutorial"
    }
]


# =============================================================================
# Helper Query and Filtering Functions
# =============================================================================

def get_all_resources():
    """Returns the complete list of curated resources."""
    return RESOURCES


def get_resource_by_id(resource_id):
    """Finds a single resource by its unique ID."""
    for res in RESOURCES:
        if res["id"] == resource_id:
            return res
    return None


def get_subjects_and_topics_map():
    """
    Returns a dictionary of {subject_id: {'name': subject_name, 'topics': [topic1, topic2, ...]}}
    derived from the resource catalogue.
    """
    mapping = {}
    for res in RESOURCES:
        sid = res["subject_id"]
        if sid not in mapping:
            mapping[sid] = {
                "id": sid,
                "name": res["subject_name"],
                "topics": []
            }
        if res["topic"] not in mapping[sid]["topics"]:
            mapping[sid]["topics"].append(res["topic"])
    return mapping


def filter_resources(subject_id=None, topic=None, resource_type=None,
                     difficulty=None, access_type=None, search_query=None):
    """
    Filters the resource catalogue by criteria with support for text search.
    """
    results = []
    q = (search_query or "").strip().lower()

    for res in RESOURCES:
        # Subject filter
        if subject_id and subject_id.lower() != "all" and res["subject_id"] != subject_id:
            continue

        # Topic filter
        if topic and topic.lower() != "all" and res["topic"].lower() != topic.lower():
            continue

        # Resource type filter
        if resource_type and resource_type.lower() != "all" and res["resource_type"].lower() != resource_type.lower():
            continue

        # Difficulty filter
        if difficulty and difficulty.lower() != "all" and res["difficulty"].lower() != difficulty.lower():
            continue

        # Access type filter (Free vs Paid)
        if access_type and access_type.lower() != "all":
            if access_type.lower() == "free" and "free" not in res["access_type"].lower():
                continue
            if access_type.lower() == "paid" and "paid" not in res["access_type"].lower():
                continue

        # Search query matching (matches title, description, provider, topic, subject)
        if q:
            searchable = f"{res['title']} {res['description']} {res['provider']} {res['topic']} {res['subject_name']}".lower()
            if q not in searchable:
                continue

        results.append(res)

    return results


def get_recommended_resources_for_assessment(assessment, limit=6):
    """
    Generates personalized learning resource recommendations based on the student's
    actual assessment results. Prioritizes Weak topics (<50%) first, then Needs Improvement (50-69%).
    """
    if not assessment:
        return get_popular_starter_resources(limit=limit)

    subject_id = assessment.get("subject_id")
    subject_name = assessment.get("subject_name", "")
    topic_results = assessment.get("topic_results") or []

    # Partition topics by performance
    weak_topics = []
    improve_topics = []
    strong_topics = []

    for t in topic_results:
        topic_name = t.get("topic")
        score = t.get("score", 0)
        status = t.get("status", "")

        if score < 50 or status == "Weak":
            weak_topics.append((topic_name, score))
        elif score < 70 or status == "Needs Improvement":
            improve_topics.append((topic_name, score))
        else:
            strong_topics.append((topic_name, score))

    # Sort so lowest scores come first
    weak_topics.sort(key=lambda x: x[1])
    improve_topics.sort(key=lambda x: x[1])

    recommended = []
    seen_ids = set()

    # 1. First add resources for weak topics
    for topic_name, score in weak_topics:
        matching = [r for r in RESOURCES if r["subject_id"] == subject_id and r["topic"] == topic_name]
        for res in matching:
            if res["id"] not in seen_ids:
                item = dict(res)
                item["recommendation_reason"] = (
                    f"Recommended because your {subject_name} assessment indicates that "
                    f"{topic_name} ({score}%) needs more practice."
                )
                item["priority_level"] = "Critical Gap"
                recommended.append(item)
                seen_ids.add(res["id"])
                if len(recommended) >= limit:
                    break
        if len(recommended) >= limit:
            break

    # 2. Then add resources for topics needing improvement
    if len(recommended) < limit:
        for topic_name, score in improve_topics:
            matching = [r for r in RESOURCES if r["subject_id"] == subject_id and r["topic"] == topic_name]
            for res in matching:
                if res["id"] not in seen_ids:
                    item = dict(res)
                    item["recommendation_reason"] = (
                        f"Recommended because your score in {topic_name} ({score}%) has room for improvement."
                    )
                    item["priority_level"] = "Needs Practice"
                    recommended.append(item)
                    seen_ids.add(res["id"])
                    if len(recommended) >= limit:
                        break
            if len(recommended) >= limit:
                break

    # 3. If student was strong in everything, provide advanced revision/depth materials
    if not recommended:
        for topic_name, score in strong_topics:
            matching = [r for r in RESOURCES if r["subject_id"] == subject_id and r["topic"] == topic_name and r["difficulty"] in ("Intermediate", "Advanced")]
            for res in matching:
                if res["id"] not in seen_ids:
                    item = dict(res)
                    item["recommendation_reason"] = (
                        f"Great job scoring {score}% in {topic_name}! Here is an advanced resource to deepen your mastery."
                    )
                    item["priority_level"] = "Advanced Exploration"
                    recommended.append(item)
                    seen_ids.add(res["id"])
                    if len(recommended) >= limit:
                        break
            if len(recommended) >= limit:
                break

    # 4. Fallback if still empty
    if not recommended:
        return get_popular_starter_resources(limit=limit)

    return recommended


def get_popular_starter_resources(limit=6):
    """
    Curates foundational starter resources when the student has not yet taken any assessments.
    """
    starter_ids = [
        "py-doc-tutorial",
        "ml-yt-statquest-linear",
        "dsa-book-clrs",
        "cn-yt-neso-osi",
        "dbms-practice-sqlbolt",
        "os-book-ostep"
    ]
    results = []
    for sid in starter_ids:
        r = get_resource_by_id(sid)
        if r:
            item = dict(r)
            item["recommendation_reason"] = "Featured foundational material to start exploring this subject."
            item["priority_level"] = "Starter Resource"
            results.append(item)
            if len(results) >= limit:
                break
    return results
