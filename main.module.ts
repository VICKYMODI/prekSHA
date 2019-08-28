import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MainComponent } from './main.component';
import { AngularFontAwesomeModule } from 'angular-font-awesome';

import { Routes, RouterModule } from '@angular/router';
import { WeddingComponent } from './wedding/wedding.component';
import { PhotographerComponent } from './photographer/photographer.component';
import { BookingComponent } from './booking/booking.component';
import { PhotographerDetailsComponent } from './photographer-details/photographer-details.component';
import { AddPhotographerComponent } from './add-photographer/add-photographer.component';
import { ApiService } from '../api.service';
import { TestComponent } from '../test/test.component';
import { ReactiveFormsModule } from '@angular/forms';


const routes: Routes = [
  {path: 'photographer',component: MainComponent},
  {path: '',component: TestComponent},
  {path: 'photographer/addPhotographer' ,component: AddPhotographerComponent}
];

@NgModule({
  declarations: [
    MainComponent,
    WeddingComponent, 
    PhotographerComponent,
    BookingComponent,
    AddPhotographerComponent,
    PhotographerDetailsComponent
   
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    AngularFontAwesomeModule,
    RouterModule.forChild(routes)
  ],
  exports:[
    RouterModule
  ],
  providers:[
    ApiService
  ]
})
export class MainModule { }
