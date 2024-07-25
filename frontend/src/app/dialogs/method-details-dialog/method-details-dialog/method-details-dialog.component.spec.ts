import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MethodDetailsDialogComponent } from './method-details-dialog.component';

describe('MethodDetailsDialogComponent', () => {
  let component: MethodDetailsDialogComponent;
  let fixture: ComponentFixture<MethodDetailsDialogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [MethodDetailsDialogComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(MethodDetailsDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
