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

  constructor(private api: Api) {}

  ngOnInit() {
    this.api.getData().subscribe({
      next: (data) => {
        this.backendData = data;
        console.log('Dane pobrane pomyślnie:', data)
      },
      error: (err) => {
        console.error('Błąd połączenia z FastAPI:', err);
      }
    })
  }
}
