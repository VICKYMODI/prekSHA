import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PhotographerDetailsComponent } from './photographer-details.component';

describe('PhotographerDetailsComponent', () => {
  let component: PhotographerDetailsComponent;
  let fixture: ComponentFixture<PhotographerDetailsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PhotographerDetailsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PhotographerDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
