# OS Scheduler

This project includes implementations of non-preemptive OS scheduling algorithms: **First-Come, First-Served (FCFS)**, **Shortest Job First (SJF)**, and **Priority Scheduling (Non-Preemptive)**.

## Schedulers Included

### Non-Preemptive Algorithms

1. **First-Come, First-Served (FCFS)**

   - Projects:
     - `Fcfs.py`: Python Script

2. **Shortest Job First (SJF)**

   - Projects:
     - `Sjf.py`: Python Script

3. **Priority Scheduling (Non-Preemptive)**
   - Projects:
     - `PriorityNonPreemptive.py`: Python Script

### Preemptive Algorithms

1. **Round Robin (RR)**

   - Projects:
     - `RoundRobin.py`: Python Script

2. **Shortest Remaining Time First (SRTF)**

   - Projects:
     - `Srtf.py`: Python Script

3. **Priority Scheduling (Preemptive)**
   - Projects:
     - `PriorityPreemptive.py`: Python Script

## Dependencies

- Python
- pip
- matplotlib
- Django

### Installation

Ensure you have Python installed, then install the dependencies using the following commands:

1. Install `pip` if not already installed:

   ```bash
   python -m ensurepip --upgrade
   ```

2. Install matplotlib:

   ```bash
   pip install matplotlib
   ```

3. Install Django:
   ```bash
   pip install django
   ```

## Running the Django Projects

To run any of the Django-based scheduler applications, follow these steps:

1. Navigate to the project directory:

   ```bash
   cd "project_name"
   ```

   Replace "project_name" with the desired project folder (e.g., fcfs_scheduler).

2. Apply migrations (if necessary):

3. Start the Django server:
   ```bash
   python manage.py runserver
   ```

### Notes

- The Python scripts (.py files) are standalone implementations of each scheduling algorithm.
- The Jupyter Notebooks (.ipynb files) contain step-by-step explanations and code for each algorithm, suitable for learning and experimenting.
