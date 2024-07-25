import { Component, Input } from '@angular/core';
import { Method } from 'src/app/classes/method';
import { MethodSelection } from 'src/app/classes/app-interface';
import { MatDialog } from '@angular/material/dialog';
import { MethodDetailsDialogComponent } from 'src/app/dialogs/method-details-dialog/method-details-dialog/method-details-dialog.component';

@Component({
  selector: 'app-method',
  templateUrl: './method.component.html',
  styleUrls: ['./method.component.scss'],
})
export class MethodComponent {
  readonly TYPE = MethodSelection;
  @Input() _methodLoaded = new Method();

  constructor(public dialog: MatDialog) {}

  get methodLoaded(): Method {
    return this._methodLoaded;
  }

  set methodLoaded(val: Method) {
    this._methodLoaded = val;
    console.log('method type: ' + this._methodLoaded.type);
  }

  openMethodDetailsDialog() {
    this.dialog.open(MethodDetailsDialogComponent, {});
  }
}
