import { Component, Input } from '@angular/core';
import { MatIconRegistry } from '@angular/material/icon';
import { DomSanitizer } from '@angular/platform-browser';
import { SystemStatusLight } from 'src/app/classes/app-interface';

@Component({
  selector: 'app-system-status',
  templateUrl: './system-status.component.html',
  styleUrls: ['./system-status.component.scss'],
})
export class SystemStatusComponent {
  @Input() _methodLoadedStatus = false;
  @Input() _isFlameLit = false;

  private _tempStatus: SystemStatusLight = SystemStatusLight.good;
  private _commStatus: SystemStatusLight = SystemStatusLight.good;
  private _runStatus: SystemStatusLight = SystemStatusLight.good;
  private _componentTempNumber = 0;

  constructor(
    private matIconRegistry: MatIconRegistry,
    private domSanitizer: DomSanitizer
  ) {
    this.matIconRegistry.addSvgIcon(
      'flame_on',
      this.domSanitizer.bypassSecurityTrustResourceUrl('../assets/icons/flame_on_icon.svg')
    );
    this.matIconRegistry.addSvgIcon(
      'flame_off',
      this.domSanitizer.bypassSecurityTrustResourceUrl('../assets/icons/flame_off_icon.svg')
    );
  }

  get tempStatus(): SystemStatusLight {
    return this._tempStatus;
  }

  set tempStatus(val: SystemStatusLight) {
    this._tempStatus = val;
  }

  get commStatus(): SystemStatusLight {
    return this._commStatus;
  }

  set commStatus(val: SystemStatusLight) {
    this._commStatus = val;
  }

  get runStatus(): SystemStatusLight {
    return this._runStatus;
  }

  set runStatus(val: SystemStatusLight) {
    this._runStatus = val;
  }

  get methodLoadedStatus(): boolean {
    return this._methodLoadedStatus;
  }

  set methodLoadedStatus(val: boolean) {
    this._methodLoadedStatus = val;
  }

  get isFlameLit(): boolean {
    return this._isFlameLit;
  }

  set isFlameLit(val: boolean) {
    this._isFlameLit = val;
  }

  get componentTempNumber(): number {
    return this._componentTempNumber;
  }

  set componentTempNumber(val: number) {
    this._componentTempNumber = val;
  }
}
