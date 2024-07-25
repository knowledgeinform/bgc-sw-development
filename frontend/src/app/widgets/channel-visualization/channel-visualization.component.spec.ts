import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChannelVisualizationComponent } from './channel-visualization.component';

describe('ChannelVisualizationComponent', () => {
  let component: ChannelVisualizationComponent;
  let fixture: ComponentFixture<ChannelVisualizationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ChannelVisualizationComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(ChannelVisualizationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
