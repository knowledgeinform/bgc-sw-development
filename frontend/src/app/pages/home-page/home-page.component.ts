import { Component } from '@angular/core';
import { Method } from 'src/app/classes/method';

export enum OperatingModeType {
  none,
  system_parameters,
  detection_and_monitoring,
}

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss'],
})
export class HomePageComponent {
  readonly MODE = OperatingModeType;

  private _operating_mode: OperatingModeType = OperatingModeType.system_parameters;
  methodLoadedStatus = false;
  isFlameLit = false;
  methodLoaded = new Method();

  public get operatingMode(): OperatingModeType {
    return this._operating_mode;
  }

  public set operatingMode(val: OperatingModeType) {
    this._operating_mode = val;
  }

  public updateLoadMethodStatus(status: boolean) {
    this.methodLoadedStatus = status;
  }

  public updateFlameStatus(status: boolean) {
    this.isFlameLit = status;
  }

  public updateMethod(val: Method) {
    this.methodLoaded = val;
  }
}
