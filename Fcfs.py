import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

"""
This program simulates the First-Come, First-Served (FCFS) scheduling algorithm in a non-preemptive manner.
It includes a predefined set of processes to observe the process list, calculations, and Gantt chart step-by-step.
After the initial simulation, users can input custom processes to simulate FCFS scheduling.
Key features include:
1. Displaying the process list in a table format before scheduling.
2. Calculating and displaying completion, waiting, and turnaround times.
3. Plotting a Gantt chart illustrating the scheduling order.
4. Allowing interactive input of custom process data for additional simulations.
"""

# Function to display process list in a table format
def display_process_list(process_list):
    print(f"{'Process ID':<12}{'Arrival Time':<15}{'Burst Time':<15}")
    print("="*42)
    for process in process_list:
        print(f"{process['process_id']:<12}{process['arrival_time']:<15}{process['burst_time']:<15}")
    print()

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

    for pid, start, duration in process_timeline:
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
    ax.set_title("Gantt Chart for FCFS Scheduling", fontsize=14, fontweight='bold')

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
    print("Average Turn Around Time:", round(avg_turnaround, 2))
    print()

# FCFS Scheduling Algorithm
def fcfs_scheduling(process_list):
    time = 0
    completed = {}
    process_timeline = []

    total_waiting_time = 0
    total_turnaround_time = 0

    # Sort processes by arrival time
    process_list.sort(key=lambda x: x['arrival_time'])
    
    while process_list:
        # Get the first process that has arrived
        if process_list[0]['arrival_time'] > time:
            # CPU is idle
            process_timeline.append(("Idle", time, process_list[0]['arrival_time'] - time))
            time = process_list[0]['arrival_time']
            continue
        else:
            current_process = process_list.pop(0)
            process_id = current_process['process_id']
            arrival_time = current_process['arrival_time']
            burst_time = current_process['burst_time']

            # Calculate waiting time
            waiting_time = time - arrival_time
            if waiting_time < 0:
                waiting_time = 0

            # Start execution
            process_start_time = time
            process_timeline.append((process_id, time, burst_time))
            time += burst_time

            # Calculate turnaround time and completion time
            completion_time = time
            turnaround_time = completion_time - arrival_time

            # Record completion details
            completed[process_id] = {
                'completion_time': completion_time,
                'turnaround_time': turnaround_time,
                'waiting_time': waiting_time
            }

            # Accumulate total times
            total_waiting_time += waiting_time
            total_turnaround_time += turnaround_time

    total_time = time

    return completed, total_waiting_time, total_turnaround_time, process_timeline, total_time

# Function to take user input and run the FCFS algorithm
def user_input_fcfs():
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

# Main function to control the flow of FCFS simulation
def main():
    # Predefined set of processes
    initial_process_list = [
        {'process_id': "P1", 'arrival_time': 0, 'burst_time': 8},
        {'process_id': "P2", 'arrival_time': 3, 'burst_time': 4},
        {'process_id': "P3", 'arrival_time': 4, 'burst_time': 5},
        {'process_id': "P4", 'arrival_time': 6, 'burst_time': 3},
        {'process_id': "P5", 'arrival_time': 10, 'burst_time': 2}
    ]

    print("\nRunning FCFS Scheduling simulation with predefined processes:")
    display_process_list(initial_process_list)
    input("Press Enter to continue to calculations...")

    # Run FCFS scheduling
    completed, total_waiting_time, total_turnaround_time, process_timeline, total_time = fcfs_scheduling(initial_process_list)

    # Display calculations
    display_calculations(completed, total_waiting_time, total_turnaround_time)
    input("Press Enter to continue to the Gantt chart...")

    # Plot the Gantt chart
    plot_gantt_chart(process_timeline, total_time)
    
    # Allow the user to input new process lists and rerun the simulation
    while True:
        user_choice = input("\nPress Enter to simulate a new set of processes or type 'exit' to quit: ").strip().lower()
        if user_choice == 'exit':
            print("Exiting the simulation. Goodbye!")
            break

        # Get new process list from user input
        process_list = user_input_fcfs()
        
        input("Press Enter to continue to calculations...")

        # Run FCFS scheduling
        completed, total_waiting_time, total_turnaround_time, process_timeline, total_time = fcfs_scheduling(process_list)

        # Display calculations
        display_calculations(completed, total_waiting_time, total_turnaround_time)
        input("Press Enter to continue to the Gantt chart...")

        # Plot the Gantt chart
        plot_gantt_chart(process_timeline, total_time)

if __name__ == '__main__':
    main()
