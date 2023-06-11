#TUGAS NO 1

class Task :
    def __init__ (self, deskripsi, prioritas) :
        self.deskripsi = deskripsi
        self.prioritas = prioritas
        self.next_task = None

class TaskList :
    def __init__ (self) :
        self.head = None

    def add_task (self, deskripsi, prioritas) :
        new_task = Task(deskripsi, prioritas)

        if self.head is None:
            self.head = new_task
        else :
            current_task = self.head
            while current_task.next_task is not None :
                current_task = current_task.next_task
            current_task.next_task = new_task

    def remove_task (self, deskripsi) :
        if self.head is None :
            print ("Daftar tugas kosong")
            return
        
        if self.head.deskripsi == deskripsi :
            self.head = self.head.next_task
            print ("Tugas", deskripsi, "telah dihapus")

            current_task = self.head
            prev_task = None
            while current_task is not None :
                prev_task.next_task = current_task.next_task
                print ("Tugas", deskripsi, "telah dihapus")
                return
            prev_task = current_task
            current_task = current_task.next_task
        
        print ("Tugas", deskripsi, "tidak ditemukan")

    def print_tasks_by_prioritas(self) :
        if self.head is None :
            print ("Tidak ada tugas di dalam daftar")
            return 
        
        sorted_tasks = self._sort_tasks_by_prioritas()
        print("Daftar tugas berdasarka prioritas : ")
        for task in sorted_tasks :
            print ("Deskripsi : ", task.deskripsi, "| Prioritas : ", task.prioritas)

    def _sort_tasks_by_prioritas(self) :
        tasks = []
        current_task = self.head
        while current_task is not None :
            tasks.append (current_task)
            current_task = current_task.next_task
        tasks.sort (key=lambda x: x.prioritas, reverse=True)
        return tasks

task_list =TaskList()

task_list.add_task ("Mengerjakan tugas kuliah.", 3)
task_list.add_task ("Tidak mengerjakan tugas kuliah.", 1)
task_list.add_task ("Lupa mengerjakan tugas kuliah.", 2)

task_list.print_tasks_by_prioritas()

task_list.remove_task("Tidak mengerjakan tugas kuliah.")

task_list.print_tasks_by_prioritas()