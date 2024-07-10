# Assignment-1: Data Structures and Efficient Sorting in Online Shopping Management
# The objective of this code is to employ fundamentals data structures for effective data management
# Allowing data manipulation as sorting, insertion, deletion, update and search.

import time

# Raw product data to be managed. Read from array product_data
Raw_Product_Data = [
    [57353, "Camera SBBHC", 546.88, "Electronics"],
    [40374, "Smartphone ILGCU", 947.54, "Electronics"],
    [34863, "Biography XPESK", 287.31, "Books"],
    [18086, "Shirt ZQLTI", 439.07, "Clothing"],
    [16041, "Jacket OTBKQ", 986.73, "Clothing"],
    [43566, "Mystery COKPK", 836.57, "Books"],
    [69260, "Toaster FODKJ", 867.6, "Home & Kitchen"],
    [30895, "Knife Set KGFUF", 385.77, "Home & Kitchen"],
    [19897, "Blender DPKLR", 488.62, "Home & Kitchen"],
    [87296, "Skirt IRTZX", 261.08, "Clothing"],
    [68215, "Laptop QLBQC", 404.21, "Electronics"],
    [68097, "Camera SGSRZ", 36.39, "Electronics"],
    [26556, "Novel METLI", 376.45, "Books"],
    [30483, "Knife Set WRSZZ", 55.97, "Home & Kitchen"],
    [62422, "Camera VFQWS", 382.69, "Electronics"],
    [22806, "Smartwatch VVFNT", 203.55, "Electronics"],
    [24976, "Pants YZMAK", 449.56, "Clothing"],
    [30631, "Headphones JFGYQ", 115.08, "Electronics"],
    [27939, "Textbook TWQKZ", 108.5, "Books"],
    [41355, "Headphones JOUXM", 211.57, "Electronics"],
    [94162, "Laptop WRJOZ", 956.53, "Electronics"],
    [28710, "Dress FRSMO", 879.09, "Clothing"],
    [90291, "Pants TIPUD", 853.38, "Clothing"],
    [20368, "Shirt FQFPK", 83.19, "Clothing"],
    [68960, "Blender OMDPS", 720.06, "Home & Kitchen"],
    [40852, "Novel IRROY", 603.68, "Books"],
    [97895, "Blender KSJHL", 123.25, "Home & Kitchen"],
    [96314, "Cutting Board LUICX", 628.29, "Home & Kitchen"],
    [85719, "Laptop GZORF", 641.33, "Electronics"],
    [98625, "Mystery BOPTP", 160.68, "Books"],
    [66208, "Blender GCZSK", 161.83, "Home & Kitchen"],
    [86128, "Biography ASTVE", 90.44, "Books"],
    [10889, "Shirt DNRZU", 316.48, "Clothing"],
    [82777, "Shirt OZWXU", 790.46, "Clothing"],
    [43451, "Mixer CKVJQ", 379.5, "Home & Kitchen"],
    [12848, "Toaster VZXUE", 867.97, "Home & Kitchen"],
    [17646, "Biography BPWXR", 424.83, "Books"],
    [85197, "Cutting Board IJVPP", 986.89, "Home & Kitchen"],
    [13471, "Knife Set TPCMO", 831.9, "Home & Kitchen"],
    [66237, "Headphones LTPLK", 995.13, "Electronics"],
    [30251, "Pants HCBKI", 450.68, "Clothing"],
    [46944, "Smartwatch QNALX", 647.08, "Electronics"],
    [93533, "Novel WOHSN", 516.39, "Books"],
    [95090, "Cutting Board RBACL", 568.63, "Home & Kitchen"],
    [98827, "Shirt RSQGL", 231.54, "Clothing"],
    [64489, "Novel EFPYC", 502.61, "Books"],
    [39148, "Cutting Board OYHCV", 220.15, "Home & Kitchen"],
    [25425, "Mystery MGSPG", 783.17, "Books"],
    [69525, "Camera XROCD", 76.05, "Electronics"],
    [44574, "Knife Set ASRHX", 64.62, "Home & Kitchen"],
]


# Define a product Class, This will be the elements to be stored in the list
class Product:
    def __init__(self, ID: int = 0, name="", price: float = 0, category=""):
        self.ID = ID
        self.name = name
        self.price = price
        self.category = category

    def getID(self):
        return self.ID

    def setID(self, ID):
        self.ID = ID

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getCategory(self):
        return self.category

    def setCategory(self, category):
        self.category = category

    def __str__(self):
        return f"({self.ID}, {self.name}, {self.price}, {self.category})"


#Define the doubleLinkList  class
class DoubleLinkList:
    # Define the Node class that compound the list.
    class Node:
        def __init__(self, element, next, prev):
            self.element = element
            self.next = next
            self.prev = prev

    # Initialize the list (Constructor)
    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.sorted = False
        self.found = False
        self.found_node = self.Node(None, None, None)


    # Return size of the list
    def __len__(self):
        return self.size

    # True if the list is empty
    def is_empty(self):
        return self.size == 0

    # Insert a new node
    def _insert_node(self, new_node):
        nextnode = new_node.next
        prevnode = new_node.prev
        nextnode.prev = new_node
        prevnode.next = new_node
        self.size += 1
        return new_node

    # Delete an existing node
    def _delete_node(self, _node):
        nextnode = _node.next
        prevnode = _node.prev

        nextnode.prev = prevnode
        prevnode.next = nextnode
        self.size -= 1
        erased_element = _node.element
        _node.element = None
        _node.next = None
        _node.prev = None
        return erased_element

    # Insert a new element at the front of the list (head)
    def _insert_head(self, element):
        new_node = self.Node(element, None, None)
        new_node.prev = self.head
        new_node.next = self.head.next

        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1

    # Insert a new element at the end of the list
    def _insert_tail(self, element):
        new_node = self.Node(element, None, None)
        new_node.prev = self.tail.prev
        new_node.next = self.tail

        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1

    # Update the element in a specified node
    def _update_node(self, element, target):
        target.element = element

    def _print_list(self):
        current = self.head.next
        while current:
            print(
                f"{current.element.ID}, {current.element.name}, {current.element.price}, {current.element.category}")
            current = current.next
            if current == self.tail:
                current = current.next
        print("\n")

    # Search within the lis by ID
    def _searchbyID(self, ID):
        current = self.head.next
        while current:
            if current.element.ID == ID:
                self.found_node = current
                self.found = True
                current = self.tail

            current = current.next
            if current == self.tail:
                current = current.next


# Load function, it loads the data from the initial array data (Raw data) to the list.
# Prints the loaded list
def load(data, data_list: DoubleLinkList):
    n = len(data)

    for i in range(0, n):
        new_product = Product(0, "", 000.00, "")
        new_product.ID = data[i][0]
        new_product.name = data[i][1]
        new_product.price = data[i][2]
        new_product.category = data[i][3]

        data_list._insert_tail(new_product)

    data_list._print_list()


# Search function, allows to look for a product by any attribute (e.g. ID, name, price or category)
# Algorithm implemented based on sequential search
# Prints the searched element
def search_product(attribute, element, list: DoubleLinkList):
    searched = list.head.next
    found_it = False
    category_list = [0]

    ''' Sequential search, compare each element until it finds the searched element'''
    while searched:
        if attribute == "1":
            if searched.element.ID == int(element):
                print("Element found\n")
                print(searched.element)
                found_it = True
                searched = list.tail

        if attribute == "2":
            if searched.element.name == element:
                print("Element found\n")
                print(searched.element)
                found_it = True
                searched = list.tail

        if attribute == "3":
            if searched.element.price == float(element):
                print("Element found\n")
                print(searched.element)
                found_it = True
                searched = list.tail

        if attribute == "4":
            # Category print an array of elements (Could be many products of the same category)
            if searched.element.category == element:
                category_list.insert(0, searched.element)
                found_it = True
            if searched == list.tail.prev and found_it is True:
                print("Elements found\n")
                for item in category_list:
                    print(item)

        searched = searched.next
        if searched == list.tail:
            searched = searched.next
    if not found_it:
        print("Element not found")


# Insert function, insert a new product into the list of data
# Prints the inserted element
def insert_product(data_list: DoubleLinkList):
    newproduct = Product(0, "", 000.00, "")
    newproduct.ID = input("Enter product ID: ")
    newproduct.name = input("Enter product name: ")
    newproduct.price = input("Enter product price: ")
    newproduct.category = input("Enter product category: ")

    if not data_list.sorted:  # Insert Product at the end of the list
        data_list._insert_tail(newproduct)

    elif data_list.sorted:
        # Insertion Algorithm to include the new product in the correct position
        # Simplified Insertion sort for only one sort element (The new node to insert)
        # Maximum time complexity will be O(n) n - Number of elements in the list.
        current = data_list.head.next
        new_node = DoubleLinkList.Node(None, None, None)

        while current:
            if current.element.price > newproduct.price:
                new_node = DoubleLinkList.Node(newproduct, current, current.prev)

            current = current.next
            if current == data_list.tail:
                new_node = DoubleLinkList.Node(newproduct, current, current.prev)
                current = current.next

        data_list._insert_node(new_node)

    print(f"Product inserted\n {newproduct}")


# Delete function, it deletes any product from the list.
# First, it searches the product to identify its position, and then delete the node.
# Prints the deleted element
def delete_product(data_list: DoubleLinkList):
    print("Enter the product ID and name to Delete")
    delete_id: int = int(input("Enter product ID: "))
    delete_name = input("Enter product name: ")
    delete_element = DoubleLinkList.Node(None, None, None)
    data_list._searchbyID(delete_id)

    if data_list.found:
        delete_element = data_list._delete_node(data_list._found_node)
    elif data_list.found is False:
        print("Element to delete not found in the list")

    print(f"Product deleted:\n {delete_element}")


# Update the attributes of a specific product from the list.
# First, it searches the product to identify its position, and then update the node with new data.
# Prints the updated element
def update_product(data_list: DoubleLinkList):
    print("Enter the product ID and name of the product to Update")
    old_id = int(input("Enter product ID: "))
    old_name = input("Enter product name: ")

    print("\n Enter the updated data for the product:")
    update_id: int = int(input("Enter new product ID: "))
    update_name = input("Enter new product name: ")
    update_price = float(input("Enter new product price: "))
    update_category = input("Enter new product category: ")

    data_list._searchbyID(old_id)
    current = data_list.found_node

    if data_list.found:
        current.element.ID = update_id
        current.element.name = update_name
        current.element.price = update_price
        current.element.category = update_category

        print(f"Product updated:\n {current.element}")

    if not data_list.found:
        print("Element to update not found in the list")


# Merge list, this is a complement function for merge sort algorithm.
# merge two lists into one in a sorted way (first lower then higher)
# Return the sorted merged list
def merge_list(a: DoubleLinkList, b: DoubleLinkList):
    current = a.head.next
    _node = b.head.next

    List = DoubleLinkList()

    while not a.is_empty() and not b.is_empty():

        if current.element.price < _node.element.price:
            List._insert_tail(current.element)
            current = current.next
            a._delete_node(current.prev)

        else:
            List._insert_tail(_node.element)
            _node = _node.next
            b._delete_node(_node.prev)

    while not a.is_empty():
        List._insert_tail(current.element)
        current = current.next
        a._delete_node(current.prev)

    while not b.is_empty():
        List._insert_tail(_node.element)
        _node = _node.next
        b._delete_node(_node.prev)

    return List


# Merge Sort Algorithm
# Return the Sorted List
def merge_sort(data_list: DoubleLinkList):
    n = data_list.size
    if n < 2:                   # If only one element then the list is already sorted
        return data_list

    else:
        _S1 = DoubleLinkList()  # Initializes two new lists
        _S2 = DoubleLinkList()

        while _S1.size < n / 2:                # Insert the first half of the list in a new list _S1
            current = data_list.head.next
            _S1._insert_tail(current.element)  # Insert first element in new list (Enqueue)
            data_list._delete_node(current)  # Delete first element of the list (Dequeue)

        while not data_list.is_empty():         # Insert the second half of the list in a new list _S2
            current = data_list.head.next
            _S2._insert_tail(current.element)
            data_list._delete_node(current)

        # Recursion ----- (Keeps splitting the list until it reaches size = 1)
        # As for each recursion size is divided by 2, then recursion is called log n times
        # As each recursion visit all the elements of the list, each recursion has n time
        # The overall time complexity then is n-log(n)
        s1 = merge_sort(_S1)
        s2 = merge_sort(_S2)

        # merge sorted lists
        data_list = merge_list(s1, s2)          # Merge the lists
        data_list.sorted = True
        return data_list


# Method to reverse the positions of the elements in a list.
# It returns a reversed list ( Is useful to sort the list from higher to lower)
def reverse_list(data_list: DoubleLinkList):
    current = data_list.tail.prev
    reversed_list = DoubleLinkList()
    while current:
        reversed_list._insert_tail(current.element)
        current = current.prev
        if current == data_list.head:
            current = current.prev
    data_list = reversed_list
    return data_list


# Principal menu, allows to select the preferred option.
def input_menu():
    print("\nPlease choose an action:\n 1. Load product data\n 2. Insert product to the list"
          "\n 3. Delete product from the list\n 4. Update product from the list\n 5. Search a product from the list"
          "\n 6. Sort product list by price\n 7. Reverse list\n 8. print list\n 9. Exit")

    user_input = input("Please enter number action: ")
    return user_input


# Main Algorithm
data_list = DoubleLinkList() # Initialize a new empty list
running = True               # Boolean to finish the execution of the program when false
_available = False           # Boolean to define if the input action is available or not

while running:
    user_input = input_menu()   # Take the input from the user

    if (user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4"
            or user_input == "5" or user_input == "6" or user_input == "7" or user_input == "8" or user_input== "9"):
        _available = True
    else:
        _available = False

    if _available is True:
        if user_input == "1":                       # Option 1 Load the data to the list
            load(Raw_Product_Data, data_list)

        if user_input == "2":                       # Option 2 Insert a new product to the list
            insert_product(data_list)

        if user_input == "3":                       # Option 3 Delete a product from the list.
            delete_product(data_list)

        if user_input == "4":                       # Option 4 Update a product data from the list
            update_product(data_list)

        if user_input == "5":                       # Option 5 search a product within the list
            search_by = input("Enter product attribute\n Search by:\n "
                              "ID = 1\n name = 2\n price = 3\n category = 4\n=> ")
            element = input("Enter element to search: ")
            search_product(search_by, element, data_list)

        if user_input == "6":                       # Option 6 Sort the data (from lower to higher)
            start: float = time.time_ns()
            data_list = merge_sort(data_list)
            end: float = time.time_ns()
            record_time = end - start

            print("\nSorted list:\n")
            data_list._print_list()

            print(f"Time taken to sort list:, {record_time:.6f}, nano seconds")

        if user_input == "7":                       # Option 7 Reverse list (from end to front)
            if not data_list.is_empty():
                data_list = reverse_list(data_list)
                print(f"\nReversed list:\n")
                data_list._print_list()
            else:
                print("\nthe list is empty")

        if user_input == "8":                       # Option 8 print the list
            if not data_list.is_empty():
                data_list._print_list()
            else:
                print("\nthe list is empty")

        if user_input == "9":                       # Option 9 Exit the program - Finish execution
            running = False

    elif _available is False:
        print("\nNo action for that selection \nPlease choose an available action:\n")
