import { Component, OnInit, Input } from '@angular/core';
import { PhotoGrapher } from '../../models/PhotoGrapher';
import { FormGroup, FormControl } from '@angular/forms';
import { ApiService } from '../../api.service';
import { getLocaleDateFormat } from '../../../../node_modules/@angular/common';

@Component({
  selector: 'app-booking',
  templateUrl: './booking.component.html',
  styleUrls: ['./booking.component.css']
})
export class BookingComponent implements OnInit {

  @Input() grapher : PhotoGrapher;

  abc:string;
  BookDate:Date = new Date(); 

  bookingform = new FormGroup({
    user : new FormControl(),
    shootPurpose : new FormControl(),
    Loc_of_shoot : new FormControl(),
    DateOfShoot : new FormControl(),
    Address : new FormControl(),
    PickGrapher : new FormControl(),
  })

  constructor(
    private apiService : ApiService
  ) { }

  ngOnInit() {
  }
  bookSave()
  {
    console.log(this.bookingform.value);
    this.apiService.BookPhotographer(
      this.bookingform.value.user,
      this.bookingform.value.shootPurpose,
      this.bookingform.value.Loc_of_shoot,
      this.bookingform.value.DateOfShoot,
      this.bookingform.value.Address,
      this.bookingform.value.PickGrapher,
      this.BookDate
    ).subscribe(
      result => console.log(result),
      error => console.log(error)
    )
  }
}
