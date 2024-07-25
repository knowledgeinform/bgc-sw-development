import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InitiationStepsComponent } from './initiation-steps.component';

describe('InitiationStepsComponent', () => {
  let component: InitiationStepsComponent;
  let fixture: ComponentFixture<InitiationStepsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [InitiationStepsComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(InitiationStepsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
