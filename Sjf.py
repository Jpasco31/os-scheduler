#SJF (Non pre-emptive) Scheduling Algorithm
#Process: [burst_time, arrival_time, process_id]

def sjf(process_list):
    time = 0
    gantt = []
    completed = {}

    total_waiting_time = 0
    total_turn_around_time = 0

    while process_list != []:
        available = []
        for process in process_list:
            if process[1] <= time:
                available.append(process)

        # No process available
        if available == []:
            time += 1
            gantt.append("Idle")
            continue 
        else:
            available.sort()
            process = available[0]
            #Service the process
            burst_time = process[0]
            process_id = process[2]
            arrival_time = process[1]
            time += burst_time
            gantt.append(process_id)
            completion_time = time
            turn_around_time = completion_time - arrival_time
            waiting_time = turn_around_time - burst_time
            process_list.remove(process)
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
    process_list = [[8, 0, "A"], [4, 3, "B"], [5, 4, "C"], [3, 6, "D"], [2, 10, "E"]]
    sjf(process_list)
