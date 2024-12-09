import matplotlib.pyplot as plt

class DiskArm:
    def __init__(self, initial_position):
        self.current_position = initial_position
        self.total_movement = 0
        self.track_access_sequence = [initial_position]  # To store the sequence for plotting

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
    plt.xlabel('Request Order')
    plt.ylabel('Track Number')
    plt.grid(True)
    plt.xticks(range(len(track_access_sequence)))
    plt.show()

def main():
    print("FCFS Disk Scheduling Simulation")

    # User input for initial disk arm position
    while True:
        try:
            initial_position = int(input("Enter the initial position of the disk arm (0-199): "))
            if 0 <= initial_position <= 199:
                break
            else:
                print("Please enter a position between 0 and 199.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # User input for track requests
    while True:
        try:
            requests_input = input("Enter the sequence of track requests separated by spaces (e.g., 55 58 39 18 90): ")
            requests = list(map(int, requests_input.strip().split()))
            if all(0 <= track <= 199 for track in requests):
                break
            else:
                print("All track numbers must be between 0 and 199.")
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")

    # Initialize DiskArm
    disk_arm = DiskArm(initial_position)

    # Process FCFS Scheduling
    service_order = fcfs_scheduling(disk_arm, requests)

    # Display the results
    print("\nOrder of Service:")
    print("Request\tMovement")
    for idx, (track, movement) in enumerate(service_order, start=1):
        print(f"{idx}. {track}\t{movement} track(s)")

    print(f"\nTotal head movement: {disk_arm.total_movement} track(s)")

    # Display the sequence of track accesses
    print("\nSequence of track accesses:", " -> ".join(map(str, disk_arm.track_access_sequence)))

    # Plotting the movement using the separate function
    plot_movement(disk_arm.track_access_sequence)

if __name__ == "__main__":
    main()
