# scheduler/utils.py
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-GUI rendering

import matplotlib.pyplot as plt
import io
import base64

def fcfs(process_list):
    # Initialize time and tracking variables
    time = 0
    gantt = []
    completed = {}
    process_timeline = []

    total_waiting_time = 0
    total_turn_around_time = 0

    # Sort processes by arrival time
    process_list = sorted(process_list)

    # Process each job
    while process_list:
        if process_list[0][0] > time:
            time += 1
            gantt.append(("Idle", 1))
            continue
        else:
            process = process_list.pop(0)
            arrival_time, burst_time, _, process_id = process
            gantt.append((process_id, burst_time))
            start_time = time
            time += burst_time
            completion_time = time
            turn_around_time = completion_time - arrival_time
            waiting_time = turn_around_time - burst_time
            completed[process_id] = [completion_time, turn_around_time, waiting_time]
            process_timeline.append((process_id, start_time, burst_time))
            total_waiting_time += waiting_time
            total_turn_around_time += turn_around_time

    # Calculate averages
    avg_waiting_time = total_waiting_time / len(completed)
    avg_turnaround_time = total_turn_around_time / len(completed)

    return gantt, process_timeline, completed, avg_waiting_time, avg_turnaround_time


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
    return {
        'completed': completed,
        'average_waiting_time': avg_waiting_time,
        'average_turnaround_time': avg_turnaround_time
    }