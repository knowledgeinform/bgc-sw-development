import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { ControllerApiModule } from 'src/api/controller/controller-api.module';
import { environment } from 'src/environments/environment';
import { ReportBarComponent } from './report-bar/report-bar.component';
import { HomePageComponent } from './pages/home-page/home-page.component';
import { SystemParametersPageComponent } from './pages/system-parameters-page/system-parameters-page.component';
import { DetectionAndMonitoringPageComponent } from './pages/detection-and-monitoring-page/detection-and-monitoring-page.component';
import { ErrorLogDialogComponent } from './dialogs/error-log-dialog/error-log-dialog.component';
import { InitiationStepsComponent } from './widgets/initiation-steps/initiation-steps.component';
import { QuickAccessComponent } from './widgets/quick-access/quick-access.component';
import { SystemStatusComponent } from './widgets/system-status/system-status.component';
import { RunProgressComponent } from './widgets/run-progress/run-progress.component';
import { MethodComponent } from './widgets/method/method.component';
import { ChannelVisualizationComponent } from './widgets/channel-visualization/channel-visualization.component';
import { AnalysisResultsComponent } from './widgets/analysis-results/analysis-results.component';
import { MethodSelectionComponent } from './widgets/method-selection-display/method-selection.component';
import { LightFpdComponent } from './widgets/method-selection-display/light-fpd/light-fpd.component';
import { LoadMethodComponent } from './widgets/method-selection-display/load-method/load-method.component';
import { StandardInjectionComponent } from './widgets/method-selection-display/standard-injection/standard-injection.component';
import { SampleComponent } from './widgets/method-selection-display/sample/sample.component';
import { LoadInitiationMethodComponent } from './widgets/method-selection-display/load-initiation-method/load-initiation-method.component';

import { MatTabsModule } from '@angular/material/tabs';
import { MatIconModule } from '@angular/material/icon';
import { MatTooltipModule } from '@angular/material/tooltip';
import { MatButtonModule } from '@angular/material/button';
import { MatMenuModule } from '@angular/material/menu';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { MatDividerModule } from '@angular/material/divider';
import { MatCardModule } from '@angular/material/card';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';
import { ReactiveFormsModule } from '@angular/forms';
import { SystemStatusLightComponent } from './widgets/system-status/system-status-light/system-status-light.component';
import { MethodDetailsDialogComponent } from './dialogs/method-details-dialog/method-details-dialog/method-details-dialog.component';
import { MatDialogModule } from '@angular/material/dialog';
import { MatInputModule } from '@angular/material/input';

// TODO: Future placeholder for backend URLs
const controllerUrl = environment.apiIdenticalUrl
  ? `${window.location.protocol}//${window.location.host}/controller`
  : `http://localhost:8000`;

@NgModule({
  declarations: [
    AppComponent,
    ReportBarComponent,
    HomePageComponent,
    SystemParametersPageComponent,
    DetectionAndMonitoringPageComponent,
    ErrorLogDialogComponent,
    InitiationStepsComponent,
    QuickAccessComponent,
    SystemStatusComponent,
    RunProgressComponent,
    MethodComponent,
    ChannelVisualizationComponent,
    AnalysisResultsComponent,
    LightFpdComponent,
    LoadMethodComponent,
    StandardInjectionComponent,
    SampleComponent,
    MethodSelectionComponent,
    LoadInitiationMethodComponent,
    SystemStatusLightComponent,
    MethodDetailsDialogComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ControllerApiModule.forRoot({ rootUrl: controllerUrl }),
    MatTabsModule,
    MatIconModule,
    BrowserAnimationsModule,
    MatTooltipModule,
    MatButtonModule,
    MatMenuModule,
    MatSnackBarModule,
    MatExpansionModule,
    MatButtonToggleModule,
    FormsModule,
    MatDividerModule,
    MatCardModule,
    MatProgressSpinnerModule,
    MatFormFieldModule,
    MatSelectModule,
    ReactiveFormsModule,
    MatDialogModule,
    MatInputModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
