import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
//import { ApiService } from '../../api.service';

@Component({
  selector: 'app-photographer',
  templateUrl: './photographer.component.html',
  styleUrls: ['./photographer.component.css']
})
export class PhotographerComponent implements OnInit {

  @Input() graphers = [];
  @Output() selectGrapher = new EventEmitter();
  @Output() bookedGrapher = new EventEmitter();
  @Output() addGrapher = new EventEmitter();

  constructor() { }

  ngOnInit() { }
  
  GrapherClicked(grapher)
  {
    return this.selectGrapher.emit(grapher);
  }
  bookPhotographer(grapher)
  {
    return this.bookedGrapher.emit(grapher);
  }

  newPhotographer()
  {
    return this.addGrapher.emit();
  }
  

}
