import matplotlib.pyplot as plt

"""
This program simulates the C-LOOK Disk Scheduling Algorithm, optimizing disk head movement by servicing requests 
in ascending order from the current position, then jumping to the lowest request and continuing in the same direction.

Key Features:
1. User input for initial disk arm position and track requests.
2. Efficient servicing of requests with minimal head movement.
3. Calculates total head movement for performance evaluation.
4. Visualizes disk arm movement using Matplotlib.

Flow:
1. Accepts user input for disk arm position and requests.
2. Initializes a `DiskArm` class to track movements and sequence.
3. Processes requests using `c_look_scheduling()`.
4. Displays the order of service, movements, total head movement, and visualizes the sequence.
"""


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

def c_look_scheduling(disk_arm, requests):
    order_of_service = []

    # Sort the requests
    sorted_requests = sorted(requests)

    # Split requests into two lists
    higher = [track for track in sorted_requests if track >= disk_arm.current_position]
    lower = [track for track in sorted_requests if track < disk_arm.current_position]

    # Service higher requests first
    for track in higher:
        movement = disk_arm.move_to(track)
        order_of_service.append((track, movement))

    if lower:
        # Jump to the first request in the lower list
        jump_movement = abs(disk_arm.current_position - lower[0])
        disk_arm.total_movement += jump_movement  # Add jump movement
        disk_arm.current_position = lower[0]
        disk_arm.track_access_sequence.append(lower[0])
        order_of_service.append((lower[0], jump_movement))

        # Service the remaining lower requests
        for track in lower[1:]:
            movement = disk_arm.move_to(track)
            order_of_service.append((track, movement))

    return order_of_service

def plot_movement(track_access_sequence, algorithm_name='C-LOOK Scheduling'):
    plt.figure(figsize=(10, 6))
    plt.plot(track_access_sequence, marker='o', linestyle='-', color='g')
    plt.title(f'Disk Arm Movement ({algorithm_name})')
    plt.xlabel('Request Order')
    plt.ylabel('Track Number')
    plt.grid(True)
    plt.xticks(range(len(track_access_sequence)))
    plt.show()

def main():
    print("C-LOOK Disk Scheduling Simulation")

    # Define disk track range
    MIN_TRACK = 0
    MAX_TRACK = 199

    # User input for initial disk arm position
    while True:
        try:
            initial_position = int(input(f"Enter the initial position of the disk arm ({MIN_TRACK}-{MAX_TRACK}): "))
            if MIN_TRACK <= initial_position <= MAX_TRACK:
                break
            else:
                print(f"Please enter a position between {MIN_TRACK} and {MAX_TRACK}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # User input for track requests
    while True:
        try:
            requests_input = input("Enter the sequence of track requests separated by spaces (e.g., 55 58 39 18 90): ")
            if not requests_input.strip():
                print("No input detected. Please enter at least one track request.")
                continue
            requests = list(map(int, requests_input.strip().split()))
            if all(MIN_TRACK <= track <= MAX_TRACK for track in requests):
                break
            else:
                print(f"All track numbers must be between {MIN_TRACK} and {MAX_TRACK}.")
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")

    # Initialize DiskArm
    disk_arm = DiskArm(initial_position)

    # Process C-LOOK Scheduling
    service_order = c_look_scheduling(disk_arm, requests)

    # Display the results
    print("\nOrder of Service:")
    print("Request\tMovement")
    for idx, (track, movement) in enumerate(service_order, start=1):
        print(f"{idx}. {track}\t{movement} track(s)")

    print(f"\nTotal head movement: {disk_arm.total_movement} track(s)")

    # Display the sequence of track accesses
    print("\nSequence of track accesses:", " -> ".join(map(str, disk_arm.track_access_sequence)))

    # Plotting the movement using the separate function
    plot_movement(disk_arm.track_access_sequence, algorithm_name='C-LOOK Scheduling')

if __name__ == "__main__":
    main()
