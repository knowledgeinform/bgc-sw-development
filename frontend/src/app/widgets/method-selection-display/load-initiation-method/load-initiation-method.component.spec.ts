import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoadInitiationMethodComponent } from './load-initiation-method.component';

describe('LoadInitiationMethodComponent', () => {
  let component: LoadInitiationMethodComponent;
  let fixture: ComponentFixture<LoadInitiationMethodComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [LoadInitiationMethodComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(LoadInitiationMethodComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
