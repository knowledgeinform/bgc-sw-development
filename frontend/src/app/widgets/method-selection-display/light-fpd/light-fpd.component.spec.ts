import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LightFpdComponent } from './light-fpd.component';

describe('LightFpdComponent', () => {
  let component: LightFpdComponent;
  let fixture: ComponentFixture<LightFpdComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [LightFpdComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(LightFpdComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
