import matplotlib.pyplot as plt

"""
This program simulates the Shortest Job First (SJF) scheduling algorithm in a non-preemptive manner. 
It includes a predefined set of processes to run the initial simulation. After the initial simulation, 
the user can interactively input new sets of processes, specifying each process's arrival and burst time. 
The program calculates completion, waiting, and turnaround times for each process and displays a Gantt chart 
illustrating the scheduling sequence. Key features include:
1. Displaying the process list in a table format before scheduling.
2. Simulating SJF scheduling by selecting the process with the shortest burst time from the available processes.
3. Printing the cumulative Gantt chart in stages as each process completes.
4. Calculating and displaying average waiting and turnaround times.
5. Allowing for interactive input of custom process data for multiple simulations.
"""

# Function to display process list in a table format
def display_process_list(process_list):
    print(f"{'Process ID':<10}{'Arrival Time':<15}{'Burst Time':<15}")
    print("="*40)
    for process in process_list:
        print(f"{process[2]:<10}{process[1]:<15}{process[0]:<15}")

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
    ax.set_title("Gantt Chart for SJF (Non-preemptive) Scheduling with Completion Times")

    plt.show()

# Function to display calculations for each process
def display_calculations(completed, total_waiting_time, total_turn_around_time):
    print("\nProcess Calculations:")
    for process_id, details in completed.items():
        print(f"Process {process_id}: Completion Time = {details[0]}, Turn Around Time = {details[1]}, Waiting Time = {details[2]}")

    print("\nAverage Waiting Time:", total_waiting_time / len(completed))
    print("Average Turn Around Time:", total_turn_around_time / len(completed))
    print()  # Add a newline for readability

# SJF Scheduling Algorithm (Non-preemptive)
# Process: [burst_time, arrival_time, process_id]
def sjf(process_list):
    time = 0
    gantt = []
    completed = {}
    process_timeline = []

    total_waiting_time = 0
    total_turn_around_time = 0

    while process_list:
        available = [process for process in process_list if process[1] <= time]

        # No process available
        if not available:
            time += 1
            gantt.append("Idle")
            continue
        else:
            # Sort available processes by burst time (SJF)
            available.sort()
            process = available[0]
            
            # Service the selected process
            burst_time = process[0]
            process_id = process[2]
            arrival_time = process[1]
            
            process_start_time = time
            time += burst_time
            gantt.append(process_id)
            
            completion_time = time
            turn_around_time = completion_time - arrival_time
            waiting_time = turn_around_time - burst_time
            process_list.remove(process)
            
            completed[process_id] = [completion_time, turn_around_time, waiting_time]
            
            # Add to timeline for plotting
            process_timeline.append((process_id, process_start_time, burst_time))

            total_waiting_time += waiting_time
            total_turn_around_time += turn_around_time

    return completed, total_waiting_time, total_turn_around_time, process_timeline, time

# Function to take user input and run the SJF algorithm
def user_input_sjf():
    process_list = []
    num_processes = int(input("Enter the number of processes: "))
    for i in range(num_processes):
        arrival_time = int(input(f"Enter arrival time for Process {i + 1}: "))
        burst_time = int(input(f"Enter burst time for Process {i + 1}: "))
        process_id = f"P{i + 1}"  # Automatically assign process ID as "P1", "P2", etc.
        process_list.append([burst_time, arrival_time, process_id])
    
    # Display the process list entered by the user
    print("\nUser-defined Process List:")
    display_process_list(process_list)
    print()
    
    return process_list

# Main function to control the flow of SJF simulation
def main():
    initial_process_list = [[8, 0, "P1"], [4, 3, "P2"], [5, 4, "P3"], [3, 6, "P4"], [2, 10, "P5"]]
    print("Running initial SJF simulation with predefined processes:")
    
    # Display process list and wait for user confirmation
    display_process_list(initial_process_list)
    input("Press Enter to continue to calculations...")

    # Run SJF scheduling
    completed, total_waiting_time, total_turn_around_time, process_timeline, total_time = sjf(initial_process_list)

    # Display calculations and wait for user confirmation
    display_calculations(completed, total_waiting_time, total_turn_around_time)
    input("Press Enter to continue to the Gantt chart...")

    # Plot the Gantt chart
    plot_gantt_chart(process_timeline, total_time)
    
    # Ask user if they want to simulate a new process set
    while input("Press Enter to simulate a new set of processes or type 'exit' to quit: ").strip().lower() != 'exit':
        # Get new process list from user input
        process_list = user_input_sjf()

        # Display process list and wait for user confirmation
        input("Press Enter to continue to calculations...")

        # Run SJF scheduling
        completed, total_waiting_time, total_turn_around_time, process_timeline, total_time = sjf(process_list)

        # Display calculations and wait for user confirmation
        display_calculations(completed, total_waiting_time, total_turn_around_time)
        input("Press Enter to continue to the Gantt chart...")

        # Plot the Gantt chart
        plot_gantt_chart(process_timeline, total_time)

if __name__ == '__main__':
    main()
