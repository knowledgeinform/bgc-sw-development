import { Component, EventEmitter, Output } from '@angular/core';
import { MethodStep } from 'src/app/classes/app-interface';
import { Method } from 'src/app/classes/method';

@Component({
  selector: 'app-system-parameters-page',
  templateUrl: './system-parameters-page.component.html',
  styleUrls: ['./system-parameters-page.component.scss'],
})
export class SystemParametersPageComponent {
  readonly MODE = MethodStep;

  @Output() loadMethodStatus: EventEmitter<boolean> = new EventEmitter();
  @Output() isFlameLit: EventEmitter<boolean> = new EventEmitter();
  @Output() method: EventEmitter<Method> = new EventEmitter();

  currentMethodDisplay: MethodStep = this.MODE.load_initiation_method;
  initiationMethodLoaded = false;
  lightFPDStatus = false;
  methodLoaded = false;
  methodSelected: [boolean, Method] = [false, new Method()];

  public updateMethodDisplay(display: MethodStep) {
    this.currentMethodDisplay = display;
  }

  public updateInitiationMethodStatus(status: boolean) {
    this.initiationMethodLoaded = status;
  }

  public updateLightFPDStatus(status: boolean) {
    this.lightFPDStatus = status;
    this.isFlameLit.emit(this.lightFPDStatus);
  }

  public updateMethodSelection(status: [boolean, Method]) {
    this.methodSelected = status;
  }

  public updateMethodStatus(status: boolean) {
    this.methodLoaded = status;
    this.loadMethodStatus.emit(this.methodLoaded);
  }

  public updateLoadedMethod(status: Method) {
    this.method.emit(status);
  }
}
