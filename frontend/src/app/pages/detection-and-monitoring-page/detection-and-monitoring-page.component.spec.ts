import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetectionAndMonitoringPageComponent } from './detection-and-monitoring-page.component';

describe('DetectionAndMonitoringPageComponent', () => {
  let component: DetectionAndMonitoringPageComponent;
  let fixture: ComponentFixture<DetectionAndMonitoringPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [DetectionAndMonitoringPageComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(DetectionAndMonitoringPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
