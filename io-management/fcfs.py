import matplotlib.pyplot as plt

"""
This program simulates the First-Come, First-Served (FCFS) Disk Scheduling Algorithm. 
FCFS services disk requests in the order they arrive, regardless of their position, 
making it straightforward but potentially inefficient for minimizing head movement.

Key Features:
1. User input for initial disk arm position and track requests.
2. Simple scheduling where requests are serviced in the order received.
3. Calculates total head movement for performance evaluation.
4. Visualizes disk arm movement using Matplotlib.

Flow:
1. Accepts user input for disk arm position and requests.
2. Initializes a DiskArm class to track movements and sequence.
3. Processes requests using fcfs_scheduling().
4. Displays the order of service, movements, total head movement, and visualizes the sequence.
"""

class DiskArm:
    def __init__(self, initial_position):
        self.current_position = initial_position
        self.total_movement = 0
        self.track_access_sequence = [initial_position]

    def move_to(self, track):
        movement = abs(track - self.current_position)
        self.total_movement += movement
        self.current_position = track
        self.track_access_sequence.append(track)
        return movement

def fcfs_scheduling(disk_arm, requests):
    order_of_service = []
    for track in requests:
        movement = disk_arm.move_to(track)
        order_of_service.append((track, movement))
    return order_of_service

def plot_movement(track_access_sequence):
    plt.figure(figsize=(10, 6))
    plt.plot(track_access_sequence, marker='o', linestyle='-', color='b')
    plt.title('Disk Arm Movement (FCFS Scheduling)')
    plt.xlabel('Access Step')
    plt.ylabel('Track Number')
    plt.grid(True)
    plt.xticks(range(len(track_access_sequence)))
    plt.show()

def main():
    print("FCFS Disk Scheduling Simulation")

    # Get initial disk arm position
    while True:
        try:
            initial_position = int(input("Enter the initial position of the disk arm (0-199): "))
            if 0 <= initial_position <= 199:
                break
            else:
                print("Please enter a position between 0 and 199.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Get requests
    while True:
        try:
            requests_input = input("Enter the sequence of track requests separated by spaces: ")
            requests = list(map(int, requests_input.strip().split()))
            if requests and all(0 <= t <= 199 for t in requests):
                break
            else:
                print("All track numbers must be between 0 and 199.")
        except ValueError:
            print("Invalid input. Please enter integers.")

    # Initialize DiskArm
    disk_arm = DiskArm(initial_position)

    # Process requests using FCFS
    service_order = fcfs_scheduling(disk_arm, requests)

    # Display results
    print("\nOrder of Service:")
    print("Index\tTrack\tMovement")
    for idx, (track, movement) in enumerate(service_order, start=1):
        print(f"{idx}\t{track}\t{movement} tracks")

    print(f"\nTotal head movement: {disk_arm.total_movement} tracks")

    print("\nSequence of track accesses (head movement path):")
    print(" -> ".join(map(str, disk_arm.track_access_sequence)))

    # Plot the movement
    plot_movement(disk_arm.track_access_sequence)

if __name__ == "__main__":
    main()
