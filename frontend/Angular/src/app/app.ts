import { Component, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.html',
  imports: [ FormsModule ],
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('Angular');
  todos: any[] = [];
  newTask: string = '';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.loadTodos();
  }

  loadTodos() {
    this.http.get<any[]>('/api/todos').subscribe(data => {
      this.todos = data;
    });
  }

  addTodo() {
    this.http.post('/api/todos', { task: this.newTask }).subscribe(() => {
      this.newTask = '';
      this.loadTodos();
    });
  }

  removeTodo(taskText: string) {
    this.http.post('/api/todos/remove', { task: taskText }).subscribe(() => {
      this.loadTodos();
    });
  }
}
