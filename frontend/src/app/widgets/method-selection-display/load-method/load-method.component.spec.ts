import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoadMethodComponent } from './load-method.component';

describe('LoadMethodComponent', () => {
  let component: LoadMethodComponent;
  let fixture: ComponentFixture<LoadMethodComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [LoadMethodComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(LoadMethodComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
