/* tslint:disable */
/* eslint-disable */
import { NgModule, ModuleWithProviders, SkipSelf, Optional } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ControllerApiConfiguration, ControllerApiConfigurationParams } from './controller-api-configuration';

import { BgcMethodService } from './services/bgc-method.service';
import { ClarityService } from './services/clarity.service';
import { DigitalIoService } from './services/digital-io.service';
import { FlameControlService } from './services/flame-control.service';
import { GasFlowService } from './services/gas-flow.service';
import { SystemService } from './services/system.service';
import { TemperatureService } from './services/temperature.service';

/**
 * Module that provides all services and configuration.
 */
@NgModule({
  imports: [],
  exports: [],
  declarations: [],
  providers: [
    BgcMethodService,
    ClarityService,
    DigitalIoService,
    FlameControlService,
    GasFlowService,
    SystemService,
    TemperatureService,
    ControllerApiConfiguration
  ],
})
export class ControllerApiModule {
  static forRoot(params: ControllerApiConfigurationParams): ModuleWithProviders<ControllerApiModule> {
    return {
      ngModule: ControllerApiModule,
      providers: [
        {
          provide: ControllerApiConfiguration,
          useValue: params
        }
      ]
    }
  }

  constructor( 
    @Optional() @SkipSelf() parentModule: ControllerApiModule,
    @Optional() http: HttpClient
  ) {
    if (parentModule) {
      throw new Error('ControllerApiModule is already loaded. Import in your base AppModule only.');
    }
    if (!http) {
      throw new Error('You need to import the HttpClientModule in your AppModule! \n' +
      'See also https://github.com/angular/angular/issues/20575');
    }
  }
}
