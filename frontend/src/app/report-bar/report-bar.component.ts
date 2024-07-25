import { Component, Input } from '@angular/core';
import { ClarityService } from 'src/api/controller/services';
import Swal from 'sweetalert2';
import { MatSnackBar } from '@angular/material/snack-bar';
import { MatIconRegistry } from '@angular/material/icon';
import { DomSanitizer } from '@angular/platform-browser';
import { Method } from '../classes/method';

export type ClarityStatus = 'stopped' | 'running';

@Component({
  selector: 'app-report-bar',
  templateUrl: './report-bar.component.html',
  styleUrls: ['./report-bar.component.scss'],
})
export class ReportBarComponent {
  @Input() _methodLoadedStatus = false;
  @Input() _isFlameLit = false;
  @Input() _methodLoaded = new Method();
  protected readonly CLARITY_RUNNING = 'running';
  protected readonly CLARITY_STOPPED = 'stopped';
  protected clarityStatus: ClarityStatus;

  constructor(
    private clarityApi: ClarityService,
    private snackBarService: MatSnackBar,
    private matIconRegistry: MatIconRegistry,
    private domSanitizer: DomSanitizer
  ) {
    this.clarityStatus = this.CLARITY_STOPPED;
    this.matIconRegistry.addSvgIcon(
      'valve',
      this.domSanitizer.bypassSecurityTrustResourceUrl('../assets/icons/valve_icon.svg')
    );
  }

  startClarity(): void {
    this.clarityApi.startClarityApiClarityStartClarityPost().subscribe();
    this.clarityStatus = this.CLARITY_RUNNING;
    this.snackBarService.open('Clarity Started!', '', { verticalPosition: 'bottom', duration: 3000 });
  }

  async stopClarity() {
    const result = await Swal.fire({
      title: 'Are you sure you want to close Clarity?',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Yes',
      confirmButtonColor: '#198754',
      cancelButtonText: 'Cancel',
      cancelButtonColor: '#d33',
      scrollbarPadding: false,
      heightAuto: false,
    });

    if (!result.value) {
      return;
    }

    this.clarityApi.exitClarityApiClarityExitClarityPost().subscribe();
    this.clarityStatus = this.CLARITY_STOPPED;
    this.snackBarService.open('Clarity Stopped', '', { verticalPosition: 'bottom', duration: 3000 });
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

  get methodLoaded(): Method {
    return this._methodLoaded;
  }

  set methodLoaded(val: Method) {
    this._methodLoaded = val;
  }
}
