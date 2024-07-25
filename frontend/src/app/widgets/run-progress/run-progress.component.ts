import { Component } from '@angular/core';
import { FormControl } from '@angular/forms';
import { MatIconRegistry } from '@angular/material/icon';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'app-run-progress',
  templateUrl: './run-progress.component.html',
  styleUrls: ['./run-progress.component.scss'],
})
export class RunProgressComponent {
  readonly SVG_CYLINDER_BLANK = '../assets/images/cylinder_blank.svg';

  progressFormControl = new FormControl('');

  constructor(
    private matIconRegistry: MatIconRegistry,
    private domSantizer: DomSanitizer
  ) {
    this.matIconRegistry.addSvgIcon(
      'stop_circle',
      this.domSantizer.bypassSecurityTrustResourceUrl('../assets/icons/stop_circle_icon.svg')
    );
  }

  getSVGImage(image: string) {
    return this.domSantizer.bypassSecurityTrustUrl(`${image}`);
  }
}
