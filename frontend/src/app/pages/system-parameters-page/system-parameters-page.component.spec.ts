import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SystemParametersPageComponent } from './system-parameters-page.component';

describe('SystemParametersPageComponent', () => {
  let component: SystemParametersPageComponent;
  let fixture: ComponentFixture<SystemParametersPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SystemParametersPageComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(SystemParametersPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
