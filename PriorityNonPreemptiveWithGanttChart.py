import matplotlib.pyplot as plt

"""
This program simulates the Priority Scheduling algorithm in a non-preemptive manner. 
It initially runs a predefined set of processes, allowing the user to observe the process list, 
calculations, and Gantt chart step-by-step. Afterward, users can input custom processes to simulate 
the scheduling. Key features include:
1. Displaying the process list in a table format before scheduling.
2. Simulating priority scheduling by selecting the process with the highest priority (lowest value).
3. Printing the cumulative Gantt chart in stages as each process completes.
4. Calculating and displaying average waiting and turnaround times.
5. Allowing for interactive input of custom process data for multiple simulations.
"""

# Function to display process list in a table format
def display_process_list(process_list):
    print(f"{'Process ID':<10}{'Arrival Time':<15}{'Burst Time':<15}{'Priority'}")
    print("="*50)
    for process in process_list:
        print(f"{process[1]:<10}{process[3]:<15}{process[2]:<15}{process[0]}")

# Function to plot the Gantt chart
def plot_gantt_chart(process_timeline, total_time):
    fig, ax = plt.subplots(figsize=(10, 3))
    
    for process_id, start, duration in process_timeline:
        ax.broken_barh([(start, duration)], (10, 9), facecolors=('tab:blue'))
        ax.text(start + duration / 2, 15, process_id, ha='center', va='center', color='white')
        
        # Add a vertical line at the completion time
        completion_time = start + duration
        ax.axvline(completion_time, color='red', linestyle='--')
        ax.text(completion_time, 20, f'{completion_time}', ha='center', va='bottom', color='red')

    ax.set_ylim(5, 25)
    ax.set_xlim(0, total_time)
    ax.set_xlabel("Time")
    ax.set_yticks([])
    ax.set_title("Gantt Chart for Priority Scheduling (Non-preemptive) with Completion Times")

    plt.show()

# Function to display calculations for each process
def display_calculations(completed, total_waiting_time, total_turn_around_time):
    print("\nProcess Calculations:")
    for process_id, details in completed.items():
        print(f"Process {process_id}: Completion Time = {details[0]}, Turn Around Time = {details[1]}, Waiting Time = {details[2]}")

    print("\nAverage Waiting Time:", total_waiting_time / len(completed))
    print("Average Turn Around Time:", total_turn_around_time / len(completed))
    print()  # Add a newline for readability

# Priority Scheduling Algorithm (Non-preemptive)
# Process: [priority, process_id, burst_time, arrival_time]
def priority(process_list):
    time = 0
    gantt = []
    completed = {}
    process_timeline = []

    total_waiting_time = 0
    total_turn_around_time = 0

    while process_list:
        available = [process for process in process_list if process[3] <= time]

        # If no process is available at the current time, increment time
        if not available:
            time += 1
            gantt.append("Idle")
            continue
        else:
            # Sort available processes by priority (lower value = higher priority)
            available.sort()
            process = available[0]

            # Remove the selected process from the process list
            process_list.remove(process)

            # Add to Gantt chart
            process_id = process[1]
            gantt.append(process_id)

            # Update the time and calculate times
            burst_time = process[2]
            process_start_time = time
            time += burst_time
            completion_time = time
            arrival_time = process[3]
            turn_around_time = completion_time - arrival_time
            waiting_time = turn_around_time - burst_time
            
            # Record completion details
            completed[process_id] = [completion_time, turn_around_time, waiting_time]
            process_timeline.append((process_id, process_start_time, burst_time))

            total_waiting_time += waiting_time
            total_turn_around_time += turn_around_time

    return completed, total_waiting_time, total_turn_around_time, process_timeline, time

# Function to take user input and run the Priority Scheduling algorithm
def user_input_priority():
    process_list = []
    num_processes = int(input("Enter the number of processes: "))
    for i in range(num_processes):
        arrival_time = int(input(f"Enter arrival time for Process {i + 1}: "))
        burst_time = int(input(f"Enter burst time for Process {i + 1}: "))
        priority_value = int(input(f"Enter priority for Process {i + 1} (lower number = higher priority): "))
        process_id = f"P{i + 1}"  # Automatically assign process ID as "P1", "P2", etc.
        process_list.append([priority_value, process_id, burst_time, arrival_time])
    
    # Display the process list entered by the user
    print("\nUser-defined Process List:")
    display_process_list(process_list)
    print()
    
    return process_list

# Main function to control the flow of Priority scheduling simulation
def main():
    initial_process_list = [[5, "P1", 8, 0], [4, "P2", 4, 3], [1, "P3", 5, 4], [2, "P4", 3, 6], [3, "P5", 2, 10]]
    print("Running initial Priority Scheduling simulation with predefined processes:")
    
    # Display process list and wait for user confirmation
    display_process_list(initial_process_list)
    input("Press Enter to continue to calculations...")

    # Run Priority scheduling
    completed, total_waiting_time, total_turn_around_time, process_timeline, total_time = priority(initial_process_list)

    # Display calculations and wait for user confirmation
    display_calculations(completed, total_waiting_time, total_turn_around_time)
    input("Press Enter to continue to the Gantt chart...")

    # Plot the Gantt chart
    plot_gantt_chart(process_timeline, total_time)
    
    # Ask user if they want to simulate a new process set
    while input("Press Enter to simulate a new set of processes or type 'exit' to quit: ").strip().lower() != 'exit':
        # Get new process list from user input
        process_list = user_input_priority()

        # Display process list and wait for user confirmation
        input("Press Enter to continue to calculations...")

        # Run Priority scheduling
        completed, total_waiting_time, total_turn_around_time, process_timeline, total_time = priority(process_list)

        # Display calculations and wait for user confirmation
        display_calculations(completed, total_waiting_time, total_turn_around_time)
        input("Press Enter to continue to the Gantt chart...")

        # Plot the Gantt chart
        plot_gantt_chart(process_timeline, total_time)

if __name__ == '__main__':
    main()
