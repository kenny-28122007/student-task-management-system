from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.counter = 1

    def add_task(self, title):
        task = Task(self.counter, title)
        self.tasks.append(task)
        self.counter += 1

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"{task.task_id}. {task.title} - {status}")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_completed()
                print("Task marked as completed.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted.")
