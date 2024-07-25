import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StandardInjectionComponent } from './standard-injection.component';

describe('StandardInjectionComponent', () => {
  let component: StandardInjectionComponent;
  let fixture: ComponentFixture<StandardInjectionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [StandardInjectionComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(StandardInjectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
