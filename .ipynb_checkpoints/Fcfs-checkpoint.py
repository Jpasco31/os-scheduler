#FCFS
#Process: [arrival_time, burst_time, waiting_time, process_id]
def fcfs(process_list):
    time = 0
    gantt = []
    completed = {}

    total_waiting_time = 0
    total_turn_around_time = 0

    # Sort processes by arrival time
    process_list.sort()
    
    # Processing each process
    while process_list != []:
        if process_list[0][0] > time:
            time += 1
            gantt.append("Idle")
            continue
        else:
            process = process_list.pop(0)
            process_id = process[2]
            gantt.append(process_id)  # Append process id to Gantt chart
            time += process[1]
            completion_time = time
            turn_around_time = completion_time - process[0]
            waiting_time = turn_around_time - process[1]
            completed[process_id] = [completion_time, turn_around_time, waiting_time]

            total_waiting_time += waiting_time
            total_turn_around_time += turn_around_time

    # Print the Gantt Chart step-by-step with cumulative completion times
    for i in range(1, len(completed) + 1):
        gantt_display = " | ".join(gantt[:i])
        print(gantt_display)

        # Print the completion times for each process up to the current one
        completion_time_display = " | ".join(
            f"{completed[process_id][0]}" for process_id in list(completed.keys())[:i]
        )
        print(completion_time_display)
        
        print()  # Add a newline for readability
        
    
    
    print("Average Waiting Time:", total_waiting_time / len(completed))
    print("Average Turn Around Time:", total_turn_around_time / len(completed))
    print()  # Add a newline for readability
    
    # Print each entry in the completed dictionary
    print("Completed Processes with Details:")
    for process_id, details in completed.items():
        print(f"Process {process_id}: Completion Time = {details[0]}, Turn Around Time = {details[1]}, Waiting Time = {details[2]}")

if __name__ == '__main__':
    process_list = [[0, 8, "A"], [3, 4, "B"], [4, 5, "C"], [6, 3, "D"], [10, 2, "E"]]
    fcfs(process_list)