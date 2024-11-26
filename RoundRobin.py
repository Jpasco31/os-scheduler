import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

"""
This program simulates the Round Robin Scheduling algorithm in a preemptive manner. 
It initially runs a predefined set of processes, allowing the user to observe the process list, 
calculations, and Gantt chart step-by-step. Afterward, users can input custom processes to simulate 
the scheduling. Key features include:
1. Displaying the process list in a table format before scheduling.
2. Simulating Round Robin scheduling by allocating a fixed time quantum to each process.
3. Printing the cumulative Gantt chart as each process completes its allocated time slices.
4. Calculating and displaying average waiting and turnaround times.
5. Allowing for interactive input of custom process data for multiple simulations.
"""

# Function to display process list in a table format
def display_process_list(process_list):
    print(f"{'Process ID':<12}{'Arrival Time':<15}{'Burst Time':<15}")
    print("="*42)
    for process in process_list:
        print(f"{process['process_id']:<12}{process['arrival_time']:<15}{process['burst_time']:<15}")

# Function to generate distinct colors for each process
def get_process_colors(process_ids):
    colors = {}
    cmap = plt.get_cmap('tab20')  # Use a colormap with many distinct colors
    for i, pid in enumerate(process_ids):
        colors[pid] = cmap(i % 20)
    colors['Idle'] = 'lightgray'  # Assign a specific color for idle time
    return colors

# Function to plot the Gantt chart
def plot_gantt_chart(process_timeline, total_time):
    fig, ax = plt.subplots(figsize=(14, 6))

    # Extract unique process IDs for color assignment
    process_ids = list(set([pid for pid, _, _ in process_timeline if pid != "Idle"]))
    colors = get_process_colors(process_ids)

    # Initialize variables for tracking the Gantt chart blocks
    current_start = 0
    current_pid = process_timeline[0][0] if process_timeline else "Idle"

    for pid, start, duration in process_timeline:
        if pid != current_pid:
            current_start = start
            current_pid = pid
        # Determine the color
        color = colors.get(pid, 'lightgray')  # Default to lightgray if not found
        # Draw the process block
        ax.broken_barh([(start, duration)], (10, 9), facecolors=(color))
        # Add process label
        ax.text(start + duration / 2, 15, pid, ha='center', va='center', color='white', fontsize=9, fontweight='bold')

    # Draw time markers
    for pid, start, duration in process_timeline:
        ax.axvline(start, color='black', linestyle='-', linewidth=0.5)
        ax.text(start, 22, f'{start}', ha='center', va='bottom', color='black', fontsize=8)
    
    # Add the end time marker
    if process_timeline:
        last_end_time = process_timeline[-1][1] + process_timeline[-1][2]
        ax.axvline(last_end_time, color='black', linestyle='-', linewidth=0.5)
        ax.text(last_end_time, 22, f'{last_end_time}', ha='center', va='bottom', color='black', fontsize=8)

    # Create legend patches
    legend_patches = [mpatches.Patch(color=colors[pid], label=pid) for pid in process_ids]
    if "Idle" in [pid for pid, _, _ in process_timeline]:
        legend_patches.append(mpatches.Patch(color=colors['Idle'], label='Idle'))

    ax.legend(handles=legend_patches, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    # Set labels and title
    ax.set_ylim(5, 25)
    ax.set_xlim(0, total_time)
    ax.set_xlabel("Time", fontsize=12)
    ax.set_yticks([])
    ax.set_title("Gantt Chart for Round Robin Scheduling", fontsize=14, fontweight='bold')

    # Add gridlines
    ax.grid(True, axis='x', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()

# Function to display calculations for each process
def display_calculations(completed, total_waiting_time, total_turnaround_time):
    print("\nProcess Calculations:")
    print(f"{'Process ID':<12}{'Completion Time':<20}{'Turnaround Time':<20}{'Waiting Time'}")
    print("="*60)
    for process_id, details in completed.items():
        print(f"{process_id:<12}{details['completion_time']:<20}{details['turnaround_time']:<20}{details['waiting_time']}")
    
    avg_waiting = total_waiting_time / len(completed) if completed else 0
    avg_turnaround = total_turnaround_time / len(completed) if completed else 0
    print("\nAverage Waiting Time:", round(avg_waiting, 2))
    print("Average Turnaround Time:", round(avg_turnaround, 2))
    print()

# Round Robin Scheduling Algorithm
def round_robin_scheduling(process_list, quantum):
    time = 0
    process_timeline = []
    completed = {}
    total_waiting_time = 0
    total_turnaround_time = 0

    # Initialize remaining burst times and arrival tracking
    for process in process_list:
        process['remaining_time'] = process['burst_time']
        process['start_time'] = None

    # Sort processes by arrival time
    process_list.sort(key=lambda x: x['arrival_time'])
    ready_queue = []
    n = len(process_list)
    i = 0  # Index for processes

    while i < n or ready_queue:
        # Add all processes that have arrived by current time to the ready queue
        while i < n and process_list[i]['arrival_time'] <= time:
            ready_queue.append(process_list[i])
            i += 1

        if ready_queue:
            current_process = ready_queue.pop(0)
            if current_process['start_time'] is None:
                current_process['start_time'] = time

            exec_time = min(quantum, current_process['remaining_time'])
            process_timeline.append((current_process['process_id'], time, exec_time))
            time += exec_time
            current_process['remaining_time'] -= exec_time

            # Add any new processes that have arrived during the execution
            while i < n and process_list[i]['arrival_time'] <= time:
                ready_queue.append(process_list[i])
                i += 1

            if current_process['remaining_time'] > 0:
                ready_queue.append(current_process)  # Re-queue the process
            else:
                completion_time = time
                turnaround_time = completion_time - current_process['arrival_time']
                waiting_time = turnaround_time - current_process['burst_time']
                completed[current_process['process_id']] = {
                    'completion_time': completion_time,
                    'turnaround_time': turnaround_time,
                    'waiting_time': waiting_time
                }
                total_waiting_time += waiting_time
                total_turnaround_time += turnaround_time
        else:
            # If no process is ready, CPU is idle
            process_timeline.append(("Idle", time, 1))
            time += 1

    total_time = time

    return completed, total_waiting_time, total_turnaround_time, process_timeline, total_time

# Function to get user input for Round Robin Scheduling
def user_input_round_robin():
    process_list = []
    while True:
        try:
            num_processes = int(input("Enter the number of processes: "))
            if num_processes <= 0:
                print("Number of processes must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")

    for i in range(num_processes):
        process_id = f"P{i + 1}"
        while True:
            try:
                arrival_time = int(input(f"Enter arrival time for {process_id}: "))
                if arrival_time < 0:
                    print("Arrival time cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer value.")
        
        while True:
            try:
                burst_time = int(input(f"Enter burst time for {process_id}: "))
                if burst_time <= 0:
                    print("Burst time must be a positive integer. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer value.")
        
        process_list.append({
            'process_id': process_id,
            'arrival_time': arrival_time,
            'burst_time': burst_time
        })
    
    print("\nUser-defined Process List:")
    display_process_list(process_list)
    return process_list

# Main function to control the flow of scheduling simulation
def main():
    # Predefined set of processes
    initial_process_list = [
        {'process_id': "P1", 'arrival_time': 0, 'burst_time': 8},
        {'process_id': "P2", 'arrival_time': 3, 'burst_time': 4},
        {'process_id': "P3", 'arrival_time': 4, 'burst_time': 5},
        {'process_id': "P4", 'arrival_time': 6, 'burst_time': 3},
        {'process_id': "P5", 'arrival_time': 10, 'burst_time': 2}
    ]

    print("\nRunning Round Robin Scheduling simulation with predefined processes:")
    display_process_list(initial_process_list)
    
    # Get quantum from user
    while True:
        try:
            quantum = int(input("\nEnter the time quantum: "))
            if quantum <= 0:
                print("Quantum must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer value for the quantum.")

    input("\nPress Enter to continue to calculations...")

    # Run the Round Robin scheduling with the initial process list
    completed, total_waiting_time, total_turnaround_time, process_timeline, total_time = round_robin_scheduling(initial_process_list, quantum)
    
    # Display the results
    display_calculations(completed, total_waiting_time, total_turnaround_time)
    input("\nPress Enter to continue to the Gantt chart...")

    # Plot the Gantt chart
    plot_gantt_chart(process_timeline, total_time)

    # Allow the user to input new process lists and rerun the simulation
    while True:
        user_choice = input("\nPress Enter to simulate a new set of processes or type 'exit' to quit: ").strip().lower()
        if user_choice == 'exit':
            print("Exiting the simulation. Goodbye!")
            break

        # Get new process list from the user
        process_list = user_input_round_robin()
        
        # Get quantum from user
        while True:
            try:
                quantum = int(input("\nEnter the time quantum: "))
                if quantum <= 0:
                    print("Quantum must be a positive integer. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer value for the quantum.")

        input("\nPress Enter to continue to calculations...")

        # Run the scheduling algorithm with the user-defined process list
        completed, total_waiting_time, total_turnaround_time, process_timeline, total_time = round_robin_scheduling(process_list, quantum)

        # Display the results
        display_calculations(completed, total_waiting_time, total_turnaround_time)
        input("\nPress Enter to continue to the Gantt chart...")

        # Plot the Gantt chart
        plot_gantt_chart(process_timeline, total_time)

if __name__ == '__main__':
    main()
