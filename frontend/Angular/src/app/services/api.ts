import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class Api {
  private apiUrl = 'http://localhost:8000/api/data';
  private apiTasksUrl = 'http://localhost:8000/api/tasks';

  constructor(private http: HttpClient) {}

  getData(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  sendTaskData(taskData: any): Observable<any[]> {
    return this.http.post<any[]>(this.apiTasksUrl, { task: taskData });
  }

  deleteTask(index: number): Observable<any[]> {
    return this.http.delete<any[]>(`${this.apiTasksUrl}/${index}`);
  }
}
