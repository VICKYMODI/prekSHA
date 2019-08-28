import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseUrl = 'http://127.0.0.1:8000/uvr/Photographer/';
  baseUrlA = 'http://127.0.0.1:8000/uvr/Booking/';

  headers = new HttpHeaders({
    'content-type':'application/json',
    Authorization:'Token a0c964ab30f9b56d02ac56c5326b5b96d638cf9e'
  });
  
  graphers = [];

  constructor(
    private httpClientcus : HttpClient
  ) 
  { 
    
  }
  get_grapherName()
  {
    return this.httpClientcus.get(this.baseUrl);
  }
  
  rate_grapher(rate:number,grapherid:number)
  {
    const body =JSON.stringify({stars:rate});
    return this.httpClientcus.post(`${this.baseUrl}${grapherid}/ratePhotographer/`,body,{headers:this.headers});
  }

  get_grapherUpdated(id:number)
  {
    return this.httpClientcus.get(`${this.baseUrl}${id}/`,{headers:this.headers});
  }
  BookPhotographer(grapherid:number,user:String, shootPurpose:String,Loc_of_shoot:String,DateOfShoot:Date,Address:String,PickGrapher:String,BookDate:Date)
  {
    const body =JSON.stringify({user:user, shootPurpose:shootPurpose, Loc_of_shoot:Loc_of_shoot,DateOfShoot:DateOfShoot,PickGrapher:PickGrapher,BookDate:BookDate,Address:Address});
    return this.httpClientcus.post(`${this.baseUrlA}${grapherid}/bookPhotographer/,{headers:this.headers});
  } 
}
