/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { BaseService } from '../base-service';
import { ControllerApiConfiguration } from '../controller-api-configuration';
import { StrictHttpResponse } from '../strict-http-response';

import { setApiFlameControlControlStatePut } from '../fn/flame-control/set-api-flame-control-control-state-put';
import { SetApiFlameControlControlStatePut$Params } from '../fn/flame-control/set-api-flame-control-control-state-put';
import { temperatureApiFlameControlTemperatureGet } from '../fn/flame-control/temperature-api-flame-control-temperature-get';
import { TemperatureApiFlameControlTemperatureGet$Params } from '../fn/flame-control/temperature-api-flame-control-temperature-get';

@Injectable({ providedIn: 'root' })
export class FlameControlService extends BaseService {
  constructor(config: ControllerApiConfiguration, http: HttpClient) {
    super(config, http);
  }

  /** Path part for operation `temperatureApiFlameControlTemperatureGet()` */
  static readonly TemperatureApiFlameControlTemperatureGetPath = '/api/flame-control/temperature';

  /**
   * Temperature.
   *
   * Read the flame controller temperature
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `temperatureApiFlameControlTemperatureGet()` instead.
   *
   * This method doesn't expect any request body.
   */
  temperatureApiFlameControlTemperatureGet$Response(params?: TemperatureApiFlameControlTemperatureGet$Params, context?: HttpContext): Observable<StrictHttpResponse<number>> {
    return temperatureApiFlameControlTemperatureGet(this.http, this.rootUrl, params, context);
  }

  /**
   * Temperature.
   *
   * Read the flame controller temperature
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `temperatureApiFlameControlTemperatureGet$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  temperatureApiFlameControlTemperatureGet(params?: TemperatureApiFlameControlTemperatureGet$Params, context?: HttpContext): Observable<number> {
    return this.temperatureApiFlameControlTemperatureGet$Response(params, context).pipe(
      map((r: StrictHttpResponse<number>): number => r.body)
    );
  }

  /** Path part for operation `setApiFlameControlControlStatePut()` */
  static readonly SetApiFlameControlControlStatePutPath = '/api/flame-control/control/{state}';

  /**
   * Set.
   *
   * Turn the flame on or off
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `setApiFlameControlControlStatePut()` instead.
   *
   * This method doesn't expect any request body.
   */
  setApiFlameControlControlStatePut$Response(params: SetApiFlameControlControlStatePut$Params, context?: HttpContext): Observable<StrictHttpResponse<any>> {
    return setApiFlameControlControlStatePut(this.http, this.rootUrl, params, context);
  }

  /**
   * Set.
   *
   * Turn the flame on or off
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `setApiFlameControlControlStatePut$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  setApiFlameControlControlStatePut(params: SetApiFlameControlControlStatePut$Params, context?: HttpContext): Observable<any> {
    return this.setApiFlameControlControlStatePut$Response(params, context).pipe(
      map((r: StrictHttpResponse<any>): any => r.body)
    );
  }

}
