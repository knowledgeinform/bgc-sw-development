import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SystemStatusLightComponent } from './system-status-light.component';

describe('SystemStatusLightComponent', () => {
  let component: SystemStatusLightComponent;
  let fixture: ComponentFixture<SystemStatusLightComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SystemStatusLightComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(SystemStatusLightComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
