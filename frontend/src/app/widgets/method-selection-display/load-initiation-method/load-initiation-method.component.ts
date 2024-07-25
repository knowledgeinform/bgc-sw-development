import { Component, Input } from '@angular/core';
import { Method } from 'src/app/classes/method';

@Component({
  selector: 'app-load-initiation-method',
  templateUrl: './load-initiation-method.component.html',
  styleUrls: ['./load-initiation-method.component.scss'],
})
export class LoadInitiationMethodComponent {
  private _defaultMethod: Method = new Method();

  @Input() loadInitiationMethodStatus = false;

  public get defaultMethod(): Method {
    return this._defaultMethod;
  }

  public set defaultMethod(val: Method) {
    this._defaultMethod = val;
  }
}
