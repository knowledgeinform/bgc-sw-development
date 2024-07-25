import { Component, EventEmitter, Input, Output } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { MethodSelection } from 'src/app/classes/app-interface';
import { Method } from 'src/app/classes/method';

@Component({
  selector: 'app-load-method',
  templateUrl: './load-method.component.html',
  styleUrls: ['./load-method.component.scss'],
})
export class LoadMethodComponent {
  methodControl = new FormControl<Method | null>(null, Validators.required);
  methods: Method[] = [
    new Method(
      MethodSelection.high_exposure_hd_gb,
      'SAMPLE DESCRIPTION OF high exposure hd gb METHOD',
      12,
      true,
      'high',
      [{ name: 'HD' }, { name: 'GB' }]
    ),
    new Method(MethodSelection.low_exposure_hd_gb, 'SAMPLE DESCRIPTION OF low exposure hd gb METHOD', 12, true, 'low', [
      { name: 'HD' },
      { name: 'GB' },
    ]),
    new Method(MethodSelection.high_exposure_vx, 'SAMPLE DESCRIPTION OF high exposure vx METHOD', 12, true, 'high', [
      { name: 'Vx' },
    ]),
  ];
  @Input() loadMethodStatus = false;
  @Output() methodSelected: EventEmitter<[boolean, Method]> = new EventEmitter();

  isMethodSelected() {
    const validSelected = !this.methodControl.hasError('required');
    this.methodSelected.emit([validSelected, this.methodControl.value ?? new Method()]);
  }
}
