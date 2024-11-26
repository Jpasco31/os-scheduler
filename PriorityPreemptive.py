import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random

"""
This program simulates the Preemptive Priority Scheduling algorithm.
It initially runs a predefined set of processes, allowing the user to observe the process list,
calculations, and Gantt chart step-by-step. Afterward, users can input custom processes to simulate
the scheduling. Key features include:
1. Displaying the process list in a table format before scheduling.
2. Simulating priority scheduling by preempting processes with higher priority (lower value).
3. Printing the cumulative Gantt chart as each process completes.
4. Calculating and displaying average waiting and turnaround times.
5. Allowing for interactive input of custom process data for multiple simulations.
"""

# Function to display process list in a table format
def display_process_list(process_list):
    print(f"{'Process ID':<12}{'Arrival Time':<15}{'Burst Time':<15}{'Priority'}")
    print("="*55)
    for process in process_list:
        print(f"{process['process_id']:<12}{process['arrival_time']:<15}{process['burst_time']:<15}{process['priority']}")

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
    ax.set_title("Gantt Chart for Priority Scheduling (Preemptive)", fontsize=14, fontweight='bold')

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

# Preemptive Priority Scheduling Algorithm
def preemptive_priority(process_list):
    time = 0
    completed = {}
    process_timeline = []
    
    total_waiting_time = 0
    total_turnaround_time = 0
    remaining_burst_times = {process['process_id']: process['burst_time'] for process in process_list}
    
    current_process = None
    first_process_arrival_time = None

    while process_list or current_process:
        # Get all processes that have arrived up to the current time
        available = [process for process in process_list if process['arrival_time'] <= time]

        # If there are available processes, choose the highest priority process
        if available:
            # Sort by priority (ascending) and arrival time (ascending)
            available.sort(key=lambda x: (x['priority'], x['arrival_time']))
            
            # Preempt the current process if a higher priority process arrives
            if current_process is None or available[0]['priority'] < current_process['priority']:
                if current_process is not None:
                    process_list.append(current_process)
                
                # Select the new highest priority process
                current_process = available[0]
                process_list.remove(current_process)
                
                # Capture the arrival time of the first executed process
                if first_process_arrival_time is None:
                    first_process_arrival_time = current_process['arrival_time']

        if current_process:
            process_id = current_process['process_id']
            
            # Execute the current process for 1 time unit
            process_timeline.append((process_id, time, 1))  # Record each time slice
            remaining_burst_times[process_id] -= 1

            # If the current process finishes execution
            if remaining_burst_times[process_id] == 0:
                completion_time = time + 1
                arrival_time = current_process['arrival_time']
                burst_time = current_process['burst_time']
                turnaround_time = completion_time - arrival_time
                waiting_time = turnaround_time - burst_time

                # Record completion details
                completed[process_id] = {
                    'completion_time': completion_time,
                    'turnaround_time': turnaround_time,
                    'waiting_time': waiting_time
                }
                total_waiting_time += waiting_time
                total_turnaround_time += turnaround_time

                # Mark the current process as finished
                current_process = None
        else:
            # CPU is idle
            process_timeline.append(("Idle", time, 1))
        
        # Increment time by 1 unit
        time += 1

    total_time = time  # Corrected total time

    return completed, total_waiting_time, total_turnaround_time, process_timeline, total_time

# Function to get user input for Priority Scheduling
def user_input_priority():
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
        
        while True:
            try:
                priority = int(input(f"Enter priority for {process_id} (lower number = higher priority): "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer value.")
        
        process_list.append({
            'priority': priority,
            'process_id': process_id,
            'burst_time': burst_time,
            'arrival_time': arrival_time
        })
    
    print("\nUser-defined Process List:")
    display_process_list(process_list)
    return process_list

# Main function to control the flow of scheduling simulation
def main():
    # Predefined set of processes
    initial_process_list = [
        {'priority': 5, 'process_id': "P1", 'burst_time': 8, 'arrival_time': 0}, 
        {'priority': 4, 'process_id': "P2", 'burst_time': 4, 'arrival_time': 3}, 
        {'priority': 1, 'process_id': "P3", 'burst_time': 5, 'arrival_time': 4}, 
        {'priority': 2, 'process_id': "P4", 'burst_time': 3, 'arrival_time': 6}, 
        {'priority': 3, 'process_id': "P5", 'burst_time': 2, 'arrival_time': 10}
    ]

    print("\nRunning Priority Scheduling simulation with predefined processes:")
    display_process_list(initial_process_list)
    input("\nPress Enter to continue to calculations...")

    # Run the preemptive priority scheduling with the initial process list
    completed, total_waiting_time, total_turnaround_time, process_timeline, total_time = preemptive_priority(initial_process_list)
    
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
        process_list = user_input_priority()
        
        input("\nPress Enter to continue to calculations...")

        # Run the scheduling algorithm with the user-defined process list
        completed, total_waiting_time, total_turnaround_time, process_timeline, total_time = preemptive_priority(process_list)

        # Display the results
        display_calculations(completed, total_waiting_time, total_turnaround_time)
        input("\nPress Enter to continue to the Gantt chart...")

        # Plot the Gantt chart
        plot_gantt_chart(process_timeline, total_time)

if __name__ == '__main__':
    main()
