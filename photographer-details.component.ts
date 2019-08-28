import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { ApiService } from '../../api.service';

@Component({
  selector: 'app-photographer-details',
  templateUrl: './photographer-details.component.html',
  styleUrls: ['./photographer-details.component.css']
})
export class PhotographerDetailsComponent implements OnInit {

  @Input() grapher;
  @Output() updategrapher = new EventEmitter();
 
  hovervalue = 0;
  constructor(
    private apiservice:ApiService
  ) { }

  ngOnInit() {
  }
  rateHover(rate)
  {
    this.hovervalue=rate;
  }
  
  rateClicked(rate)
  {
    this.apiservice.rate_grapher(rate,this.grapher.id).subscribe(
      result => this.getGrapher(),
      error=>console.log(error)
    );
  }
  getGrapher()
  {
    this.apiservice.get_grapherUpdated(this.grapher.id).subscribe(
      phototgrapher => {
        this.updategrapher.emit(phototgrapher);
      },
      error=>console.log(error)
    );
  }
}