import { Component, EventEmitter, Input, Output } from '@angular/core';
import { MethodStep } from 'src/app/classes/app-interface';

@Component({
  selector: 'app-initiation-steps',
  templateUrl: './initiation-steps.component.html',
  styleUrls: ['./initiation-steps.component.scss'],
})
export class InitiationStepsComponent {
  readonly MODE = MethodStep;

  private _method_step: MethodStep = MethodStep.load_initiation_method;
  @Input() loadInitiationMethodStatus = false;
  @Input() lightFPDStatus = false;
  @Input() loadMethodStatus = false;

  @Output() currentDisplay: EventEmitter<MethodStep> = new EventEmitter();

  public get methodStep(): MethodStep {
    return this._method_step;
  }

  public set methodStep(val: MethodStep) {
    this._method_step = val;
    this.currentDisplay.emit(val);
  }
}
