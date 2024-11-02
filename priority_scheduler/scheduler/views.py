# scheduler/views.py
from django.shortcuts import render
from .utils import priority_scheduling, plot_gantt_chart, format_results

def priority_index(request):
    results = None
    gantt_chart = None
    display_process_list = []

    if request.method == "POST":
        num_processes = int(request.POST.get("num_processes", 0))
        process_list = []

        for i in range(num_processes):
            priority = request.POST.get(f"priority_{i}")
            arrival_time = request.POST.get(f"arrival_time_{i}")
            burst_time = request.POST.get(f"burst_time_{i}")

            if priority is None or arrival_time is None or burst_time is None:
                continue

            try:
                priority = int(priority)
                arrival_time = int(arrival_time)
                burst_time = int(burst_time)
            except ValueError:
                continue

            process_id = f"P{i+1}"
            process_list.append([priority, process_id, burst_time, arrival_time])

        display_process_list = [
            {'priority': p[0], 'process_id': p[1], 'burst_time': p[2], 'arrival_time': p[3]} for p in process_list
        ]

        if process_list:
            gantt, process_timeline, completed, avg_waiting_time, avg_turnaround_time = priority_scheduling(process_list)
            total_time = sum(duration for _, _, duration in process_timeline)
            gantt_chart = plot_gantt_chart(process_timeline, total_time)
            results = format_results(completed, avg_waiting_time, avg_turnaround_time)

    return render(request, "scheduler/priority_index.html", {
        "gantt_chart": gantt_chart,
        "results": results,
        "process_list": display_process_list
    })
