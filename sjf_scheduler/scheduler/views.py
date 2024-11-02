# scheduler/views.py
from django.shortcuts import render
from .utils import sjf, plot_gantt_chart, format_results

def sjf_index(request):
    results = None
    gantt_chart = None
    display_process_list = []  # For showing the initial process list

    if request.method == "POST":
        num_processes = int(request.POST.get("num_processes", 0))
        process_list = []
        
        for i in range(num_processes):
            arrival_time = request.POST.get(f"arrival_time_{i}")
            burst_time = request.POST.get(f"burst_time_{i}")

            if arrival_time is None or burst_time is None:
                continue

            try:
                arrival_time = int(arrival_time)
                burst_time = int(burst_time)
            except ValueError:
                continue

            process_id = f"P{i+1}"
            process_list.append([burst_time, arrival_time, process_id])

        # Store a copy for displaying purposes
        display_process_list = [
            {'process_id': process[2], 'arrival_time': process[1], 'burst_time': process[0]} for process in process_list
        ]

        if process_list:
            gantt, completed, avg_waiting_time, avg_turnaround_time = sjf(process_list)
            gantt_chart = plot_gantt_chart(gantt)
            results = format_results(completed, avg_waiting_time, avg_turnaround_time)

    # Pass display_process_list to the template
    return render(request, "scheduler/sjf_index.html", {
        "gantt_chart": gantt_chart,
        "results": results,
        "process_list": display_process_list  # For displaying the table
    })
