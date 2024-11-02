import matplotlib.pyplot as plt

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
    print(f"{'Process ID':<10}{'Arrival Time':<15}{'Burst Time':<15}")
    print("="*40)
    for process in process_list:
        print(f"{process[2]:<10}{process[0]:<15}{process[1]:<15}")

# Function to display calculations for each process
def display_calculations(completed, total_waiting_time, total_turn_around_time):
    print("\nProcess Calculations:")
    for process_id, details in completed.items():
        print(f"Process {process_id}: Completion Time = {details[0]}, Turn Around Time = {details[1]}, Waiting Time = {details[2]}")

    print("\nAverage Waiting Time:", total_waiting_time / len(completed))
    print("Average Turn Around Time:", total_turn_around_time / len(completed))
    print()  # Add a newline for readability

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
    ax.set_title("Gantt Chart for FCFS Scheduling with Completion Times")

    plt.show()

# FCFS Scheduling Algorithm
# Process: [arrival_time, burst_time, process_id]
def fcfs(process_list):
    time = 0
    gantt = []
    completed = {}
    process_timeline = []

    total_waiting_time = 0
    total_turn_around_time = 0

    # Sort processes by arrival time
    process_list.sort()
    
    # Processing each process
    while process_list:
        if process_list[0][0] > time:
            time += 1
            gantt.append("Idle")
            continue
        else:
            process = process_list.pop(0)
            process_id = process[2]
            gantt.append(process_id)  # Append process id to Gantt chart
            process_start_time = time
            time += process[1]
            completion_time = time
            turn_around_time = completion_time - process[0]
            waiting_time = turn_around_time - process[1]
            completed[process_id] = [completion_time, turn_around_time, waiting_time]
            
            # Add to timeline for plotting
            process_timeline.append((process_id, process_start_time, process[1]))

            total_waiting_time += waiting_time
            total_turn_around_time += turn_around_time

    return completed, total_waiting_time, total_turn_around_time, process_timeline, time

# Function to take user input and run the FCFS algorithm
def user_input_fcfs():
    process_list = []
    num_processes = int(input("Enter the number of processes: "))
    for i in range(num_processes):
        arrival_time = int(input(f"Enter arrival time for Process {i + 1}: "))
        burst_time = int(input(f"Enter burst time for Process {i + 1}: "))
        process_id = f"P{i + 1}"  # Automatically assign process ID as "P1", "P2", etc.
        process_list.append([arrival_time, burst_time, process_id])
    
    # Display the process list entered by the user
    print("\nUser-defined Process List:")
    display_process_list(process_list)
    print()
    
    return process_list

# Main function to control the flow of FCFS simulation
def main():
    initial_process_list = [[0, 8, "P1"], [3, 4, "P2"], [4, 5, "P3"], [6, 3, "P4"], [10, 2, "P5"]]
    print("Running initial FCFS simulation with predefined processes:")
    
    # Display process list and wait for user confirmation
    display_process_list(initial_process_list)
    input("Press Enter to continue to calculations...")

    # Run FCFS scheduling
    completed, total_waiting_time, total_turn_around_time, process_timeline, total_time = fcfs(initial_process_list)

    # Display calculations and wait for user confirmation
    display_calculations(completed, total_waiting_time, total_turn_around_time)
    input("Press Enter to continue to the Gantt chart...")

    # Plot the Gantt chart
    plot_gantt_chart(process_timeline, total_time)
    
    # Ask user if they want to simulate a new process set
    while input("Press Enter to simulate a new set of processes or type 'exit' to quit: ").strip().lower() != 'exit':
        # Get new process list from user input
        process_list = user_input_fcfs()

        # Display process list and wait for user confirmation
        input("Press Enter to continue to calculations...")

        # Run FCFS scheduling
        completed, total_waiting_time, total_turn_around_time, process_timeline, total_time = fcfs(process_list)

        # Display calculations and wait for user confirmation
        display_calculations(completed, total_waiting_time, total_turn_around_time)
        input("Press Enter to continue to the Gantt chart...")

        # Plot the Gantt chart
        plot_gantt_chart(process_timeline, total_time)

if __name__ == '__main__':
    main()

