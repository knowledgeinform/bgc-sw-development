import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-light-fpd',
  templateUrl: './light-fpd.component.html',
  styleUrls: ['./light-fpd.component.scss'],
})
export class LightFpdComponent {
  @Input() lightFPDStatus = false;
}
