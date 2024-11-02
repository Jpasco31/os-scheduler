#Priority non preemptive scheduling
#Process: [priority, process_id, burst_time, arrival_time]

def priority(process_list):
    time = 0
    gantt = []
    completed = {}

    total_waiting_time = 0
    total_turn_around_time = 0

    while process_list != []:
        available = []
        for process in process_list:
            arrival_time = process[3]
            if arrival_time <= time:
                available.append(process)
        if available == []:
            time += 1
            gantt.append("Idle")
            continue
        else:
            available.sort()
            process = available[0]
            #service the process
            #1. remove the process
            process_list.remove(process)
            #add to gantt chart
            process_id = process[1]
            gantt.append(process_id)
            #3. update the time
            burst_time = process[2]
            time += burst_time
            #4. create an entry in the completed dictionary
            #calculate completion time, turn around time and waiting time
            completion_time = time
            arrival_time = process[3]
            turn_around_time = completion_time - arrival_time
            waiting_time = turn_around_time - burst_time
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
    process_list = [[5, "A", 8, 0], [4, "B", 4, 3], [1, "C", 5, 4], [2, "D", 3, 6], [3, "E", 2, 10]]
    priority(process_list)