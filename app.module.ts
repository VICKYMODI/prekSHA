import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AuthModule } from './auth/auth.module';
import { MainModule } from './main/main.module';

import { Routes, RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { AngularFontAwesomeModule } from 'angular-font-awesome';
import { AppComponent } from './app.component';
import { PhotographerComponent } from './main/photographer/photographer.component';
import { WeddingComponent } from './main/wedding/wedding.component';
import { TestComponent } from './test/test.component';





const routes: Routes = [
  {path: 'auth', pathMatch: 'full', redirectTo:'auth'}
];

@NgModule({
  declarations: [
    AppComponent,
    TestComponent
  
  ],
  imports: [
    BrowserModule,
    AuthModule,
    MainModule,
    AngularFontAwesomeModule,
    HttpClientModule,
    RouterModule.forRoot(routes)
  ],
  exports:[
    RouterModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
