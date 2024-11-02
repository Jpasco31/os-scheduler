# OS Scheduler

This project includes implementations of non-preemptive OS scheduling algorithms: **First-Come, First-Served (FCFS)**, **Shortest Job First (SJF)**, and **Priority Scheduling (Non-Preemptive)**.

## Schedulers Included

### Non-Preemptive Algorithms

1. **First-Come, First-Served (FCFS)**

   - Projects:
     - `fcfs_scheduler`: Django Application
     - `Fcfs.ipynb`: Jupyter Notebook
     - `Fcfs.py`: Python Script

2. **Shortest Job First (SJF)**

   - Projects:
     - `sjf_scheduler`: Django Application
     - `Sjf.ipynb`: Jupyter Notebook
     - `Sjf.py`: Python Script

3. **Priority Scheduling (Non-Preemptive)**
   - Projects:
     - `priority_scheduler`: Django Application
     - `PriorityNonPreemptive.ipynb`: Jupyter Notebook
     - `PriorityNonPreemptive.py`: Python Script

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
   cd "project_nam"
   ```

   Replace "project_name" with the desired project folder (e.g., fcfs_scheduler).

2. Start the Django server:
   ```bash
   python manage.py runserver
   ```

### Notes

- The Python scripts (.py files) are standalone implementations of each scheduling algorithm.
- The Jupyter Notebooks (.ipynb files) contain step-by-step explanations and code for each algorithm, suitable for learning and experimenting.
