import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Method } from 'src/app/classes/method';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-quick-access',
  templateUrl: './quick-access.component.html',
  styleUrls: ['./quick-access.component.scss'],
})
export class QuickAccessComponent {
  @Input() methodSelected: [boolean, Method] = [false, new Method()];

  @Output() isInitiationMethodLoaded: EventEmitter<boolean> = new EventEmitter();
  @Output() isLightFPDRunning: EventEmitter<boolean> = new EventEmitter();
  @Output() isMethodLoaded: EventEmitter<boolean> = new EventEmitter();
  @Output() loadedMethod: EventEmitter<Method> = new EventEmitter();

  async loadInitiationMethod() {
    await Swal.fire({
      title: 'Loading Initiation Method',
      icon: 'success',
      confirmButtonText: 'Continue',
      confirmButtonColor: '#198754',
      scrollbarPadding: false,
      heightAuto: false,
    });

    this.isInitiationMethodLoaded.emit(true);
  }

  async lightFPDRun() {
    await Swal.fire({
      title: 'Light FPD',
      icon: 'success',
      confirmButtonText: 'Continue',
      confirmButtonColor: '#198754',
      scrollbarPadding: false,
      heightAuto: false,
    });

    this.isLightFPDRunning.emit(true);
  }

  async loadMethod() {
    await Swal.fire({
      title: 'Load Method',
      icon: 'success',
      confirmButtonText: 'Continue',
      confirmButtonColor: '#198754',
      scrollbarPadding: false,
      heightAuto: false,
    });

    this.isMethodLoaded.emit(true);
    this.loadedMethod.emit(this.methodSelected[1]);
  }
}
