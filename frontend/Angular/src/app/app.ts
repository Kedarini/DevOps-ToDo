import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Api } from './services/api'

@Component({
  selector: 'app-root',
  templateUrl: './app.html',
  imports: [ FormsModule, CommonModule ],
  styleUrl: './app.css'
})
export class App implements OnInit {
  backendData: any;
  task !: string;

  constructor(private api: Api) {}

  ngOnInit() {
    this.refreshList();
  }

  refreshList() {
    this.api.getData().subscribe({
      next: (data) => this.backendData = data,
      error: (err) => console.error('Błąd połączenia:', err)
    });
  }

  newTask() {
    if (!this.task) return;

    this.api.sendTaskData(this.task).subscribe({
      next: (updatedList) => {
        this.backendData = updatedList;
        this.task = '';
      },
      error: (err) => console.error('Błąd zapisu:', err)
    })
  }

  removeTask(index: number) {
    this.api.deleteTask(index).subscribe({
      next: (updatedList) => {
        this.backendData = updatedList;
      },
      error: (err) => console.error('Błąd usuwania:', err)
    })
  }
}
