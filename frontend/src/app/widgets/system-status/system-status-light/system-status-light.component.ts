import { Component, Input } from '@angular/core';
import { SystemStatusLight } from 'src/app/classes/app-interface';

@Component({
  selector: 'app-system-status-light',
  templateUrl: './system-status-light.component.html',
  styleUrls: ['./system-status-light.component.scss'],
})
export class SystemStatusLightComponent {
  readonly STATUS = SystemStatusLight;

  @Input() status: SystemStatusLight = SystemStatusLight.no_status;

  public get systemStatus(): SystemStatusLight {
    return this.status;
  }

  public set systemStatus(val: SystemStatusLight) {
    this.status = val;
  }
}
