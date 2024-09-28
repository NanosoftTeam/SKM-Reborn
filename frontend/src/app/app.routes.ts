import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { TaskCreateComponent } from './task-create/task-create.component';

export const routes: Routes = [
    { path: 'login', component: LoginComponent },
    { path: 'tasks/new', component: TaskCreateComponent }
];
