# OS Scheduler

This project includes implementations of non-preemptive OS scheduling algorithms: **Non-Preemptive** and **Preemptive OS Scheduling Algorithms**, as well ass **I/O Management Algorithms**.

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

### I/O Management Algorithms

1. **First-Come, First-Serve (fcfs)**

   - Projects:
     - `io-management/fcfs.py`: Python Script

2. **C-LOOK**

   - Projects:
     - `cLook.py`: Python Script

3. **C-SCAN**
   - Projects:
     - `cScan.py`: Python Script

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

3. Install Django: (If running the Django Apps)
   ```bash
   pip install django
   ```

## Running the Django Projects

To run any of the Django-based scheduler applications, follow these steps:
_Note: Only Non-preemptive Scheduling algorithms have django app_

### Django Projects

- Fcfc_scheduler
- priority_scheduler
- sjf_scheduler

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
- Ensure the required dependencies are installed before executing the scripts or running Django applications.
