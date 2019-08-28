import { Component, OnInit, Input } from '@angular/core';
import { PhotoGrapher } from '../../models/PhotoGrapher';

@Component({
  selector: 'app-add-photographer',
  templateUrl: './add-photographer.component.html',
  styleUrls: ['./add-photographer.component.css']
})
export class AddPhotographerComponent implements OnInit {
  @Input() grapher : PhotoGrapher;

  constructor() { }

  ngOnInit() {
  }

  addphotographersave()
  {
    
  }

}
