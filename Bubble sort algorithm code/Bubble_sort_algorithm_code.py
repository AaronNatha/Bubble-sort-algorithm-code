def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Function to take user input
def get_user_input():
    user_input = input("Enter numbers seperated by spaces: ")
    arr = list(map(int, user_input.split()))
    return arr

# Main function
def main():
    arr = get_user_input()
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)
    
if __name__== "__main__":
    main()