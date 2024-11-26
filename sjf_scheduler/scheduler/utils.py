# scheduler/utils.py
import matplotlib
matplotlib.use('Agg')  # For Django-compatible backend

import matplotlib.pyplot as plt
import io
import base64

def sjf(process_list):
    time = 0
    gantt = []
    completed = {}
    process_timeline = []
    total_waiting_time = 0
    total_turn_around_time = 0

    # Sort the process list by arrival time to find the first arrival time
    process_list.sort(key=lambda x: x[1])
    first_arrival_time = process_list[0][1] if process_list else 0

    while process_list:
        # Collect processes that have arrived
        available = [p for p in process_list if p[1] <= time]
        
        # If no process is available, increment time and idle
        if not available:
            time += 1
            gantt.append(("Idle", 1))  # Add "Idle" as a tuple with burst time 1
            continue

        # Sort by burst time for SJF
        available.sort(key=lambda x: x[0])  # Sort by burst_time
        process = available[0]
        burst_time = process[0]
        process_id = process[2]
        arrival_time = process[1]

        # Record the start time
        start_time = time

        # Update time and record completion
        time += burst_time
        gantt.append((process_id, burst_time))  # Use tuple format (process_id, burst_time)
        completion_time = time
        turn_around_time = completion_time - arrival_time
        waiting_time = turn_around_time - burst_time
        process_list.remove(process)

        # Store the completion, turnaround, and waiting times
        completed[process_id] = [completion_time, turn_around_time, waiting_time]
        process_timeline.append((process_id, start_time, burst_time))

        total_waiting_time += waiting_time
        total_turn_around_time += turn_around_time

    # Calculate averages
    avg_waiting_time = total_waiting_time / len(completed) if completed else 0
    avg_turnaround_time = total_turn_around_time / len(completed) if completed else 0

    # Calculate total time as the completion time of the last process minus the arrival time of the first process
    total_time = completion_time

    return gantt, process_timeline, completed, avg_waiting_time, avg_turnaround_time, total_time




def plot_gantt_chart(process_timeline, total_time):
    fig, ax = plt.subplots(figsize=(10, 3))
    for process_id, start, duration in process_timeline:
        ax.broken_barh([(start, duration)], (10, 9), facecolors=('tab:blue'))
        ax.text(start + duration / 2, 15, process_id, ha='center', va='center', color='white')
        ax.axvline(start + duration, color='red', linestyle='--')
        ax.text(start + duration, 20, f'{start + duration}', ha='center', va='bottom', color='red')

    ax.set_ylim(5, 25)
    ax.set_xlim(0, total_time)
    ax.set_xlabel("Time")
    ax.set_yticks([])
    ax.set_title("Gantt Chart for FCFS Scheduling with Completion Times")

    # Save the chart to a PNG in memory
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    gantt_chart = base64.b64encode(image_png).decode('utf-8')
    return gantt_chart



def format_results(completed, avg_waiting_time, avg_turnaround_time):
    results = {
        'completed': completed,
        'average_waiting_time': avg_waiting_time,
        'average_turnaround_time': avg_turnaround_time
    }
    return results
