import { Component, EventEmitter, Input, Output } from '@angular/core';
import { MethodStep } from 'src/app/classes/app-interface';
import { Method } from 'src/app/classes/method';

@Component({
  selector: 'app-method-selection',
  templateUrl: './method-selection.component.html',
  styleUrls: ['./method-selection.component.scss'],
})
export class MethodSelectionComponent {
  readonly MODE = MethodStep;

  @Input() display?: MethodStep;
  @Input() loadInitiationMethodStatus = false;
  @Input() lightFPDStatus = false;
  @Input() loadMethodStatus = false;
  @Output() methodSelectedStatus: EventEmitter<[boolean, Method]> = new EventEmitter();

  public isMethodSelected(status: [boolean, Method]) {
    this.methodSelectedStatus.emit(status);
  }
}
