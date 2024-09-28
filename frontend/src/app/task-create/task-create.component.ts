import { Component } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-task-create',
  standalone: true,
  imports: [ReactiveFormsModule, HttpClientModule],
  templateUrl: './task-create.component.html',
  styleUrl: './task-create.component.scss'
})
export class TaskCreateComponent {
  newTaskForm: FormGroup;

  constructor(private fb: FormBuilder, private http: HttpClient) {
    this.newTaskForm = this.fb.group({
      name: ['', [Validators.required]],
      content: ['', Validators.required]
    });
  }

  onSubmit() {
    if (this.newTaskForm.valid) {
      // Here we should send login
      const taskData = this.newTaskForm.value;
      console.log('Form submitted: ', taskData);
      this.http.post('http://127.0.0.1:5000/api/task', taskData)
        .subscribe(response => {
          console.log('Task successfully created:', response);
        }, error => {
          console.error('Error creating task:', error);
        });
    }
  }
}
