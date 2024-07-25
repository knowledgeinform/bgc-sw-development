/* tslint:disable */
/* eslint-disable */
import { Injectable } from '@angular/core';

/**
 * Global configuration
 */
@Injectable({
  providedIn: 'root',
})
export class ControllerApiConfiguration {
  rootUrl: string = '';
}

/**
 * Parameters for `ControllerApiModule.forRoot()`
 */
export interface ControllerApiConfigurationParams {
  rootUrl?: string;
}
