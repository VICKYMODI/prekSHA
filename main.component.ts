import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  graphers : any=[];
  selectedGrapher = null;
  bookedGrapher = null;
  addGrapher = null;

  constructor(
    private apiServiceCus : ApiService
  ) { }

  ngOnInit() 
  {

    this.apiServiceCus.get_grapherName().subscribe
    (
      data => 
      {
        this.graphers = data;
      },
      error => console.log(error)
    );
  }
  selectGrapher(grapher)
  {
    this.selectedGrapher=grapher;
    this.bookedGrapher=null;
  }
  bookGrapher(grapher)
  {
    this.bookedGrapher=grapher;
    this.selectedGrapher=null;
    this.addGrapher = null;
  }
  addedGrapher()
  {
    this.addGrapher=true;
    this.selectedGrapher=null; 
  }

  
}
