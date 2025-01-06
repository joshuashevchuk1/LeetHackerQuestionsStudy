import sys
import heapq

def query():
    li = []  # Min-heap to store elements
    present = set()  # Set to keep track of valid elements in the heap

    for line in sys.stdin:
        items = line.split()
        command = items[0]

        if command == '1' and len(items) > 1:  # Add element
            value = int(items[1])
            heapq.heappush(li, value)
            present.add(value)
        elif command == '2' and len(items) > 1:  # Remove element
            value = int(items[1])
            if value in present:
                present.remove(value)
        elif command == '3':  # Print minimum
            while li and li[0] not in present:  # Remove invalid elements
                heapq.heappop(li)
            if li:  # Check if heap is not empty
                print(li[0])
            else:
                print("List is empty")  # Optional: Handle empty case explicitly

a = [1,2,3,4,5]

def get_n_smallest(a):
    return heapq.nsmallest(2, set(a))

smallest = get_n_smallest(a)

print(smallest)
