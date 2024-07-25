/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { BaseService } from '../base-service';
import { ControllerApiConfiguration } from '../controller-api-configuration';
import { StrictHttpResponse } from '../strict-http-response';

import { getIsocraticDefaultsApiTemperatureIsocraticDefaultsGet } from '../fn/temperature/get-isocratic-defaults-api-temperature-isocratic-defaults-get';
import { GetIsocraticDefaultsApiTemperatureIsocraticDefaultsGet$Params } from '../fn/temperature/get-isocratic-defaults-api-temperature-isocratic-defaults-get';
import { getTemperaturesApiTemperatureStatusGet } from '../fn/temperature/get-temperatures-api-temperature-status-get';
import { GetTemperaturesApiTemperatureStatusGet$Params } from '../fn/temperature/get-temperatures-api-temperature-status-get';
import { NameValuePairIsocraticTemperatureNameFloat } from '../models/name-value-pair-isocratic-temperature-name-float';
import { NameValuePairTemperatureNameFloat } from '../models/name-value-pair-temperature-name-float';
import { setApiTemperatureSetTemperaturesPut } from '../fn/temperature/set-api-temperature-set-temperatures-put';
import { SetApiTemperatureSetTemperaturesPut$Params } from '../fn/temperature/set-api-temperature-set-temperatures-put';

@Injectable({ providedIn: 'root' })
export class TemperatureService extends BaseService {
  constructor(config: ControllerApiConfiguration, http: HttpClient) {
    super(config, http);
  }

  /** Path part for operation `getTemperaturesApiTemperatureStatusGet()` */
  static readonly GetTemperaturesApiTemperatureStatusGetPath = '/api/temperature/status';

  /**
   * Get Temperatures.
   *
   * Return status of all temperatures.
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `getTemperaturesApiTemperatureStatusGet()` instead.
   *
   * This method doesn't expect any request body.
   */
  getTemperaturesApiTemperatureStatusGet$Response(params?: GetTemperaturesApiTemperatureStatusGet$Params, context?: HttpContext): Observable<StrictHttpResponse<Array<NameValuePairTemperatureNameFloat>>> {
    return getTemperaturesApiTemperatureStatusGet(this.http, this.rootUrl, params, context);
  }

  /**
   * Get Temperatures.
   *
   * Return status of all temperatures.
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `getTemperaturesApiTemperatureStatusGet$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  getTemperaturesApiTemperatureStatusGet(params?: GetTemperaturesApiTemperatureStatusGet$Params, context?: HttpContext): Observable<Array<NameValuePairTemperatureNameFloat>> {
    return this.getTemperaturesApiTemperatureStatusGet$Response(params, context).pipe(
      map((r: StrictHttpResponse<Array<NameValuePairTemperatureNameFloat>>): Array<NameValuePairTemperatureNameFloat> => r.body)
    );
  }

  /** Path part for operation `getIsocraticDefaultsApiTemperatureIsocraticDefaultsGet()` */
  static readonly GetIsocraticDefaultsApiTemperatureIsocraticDefaultsGetPath = '/api/temperature/isocratic_defaults';

  /**
   * Get Isocratic Defaults.
   *
   * Return all isocratic temperature defaults
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `getIsocraticDefaultsApiTemperatureIsocraticDefaultsGet()` instead.
   *
   * This method doesn't expect any request body.
   */
  getIsocraticDefaultsApiTemperatureIsocraticDefaultsGet$Response(params?: GetIsocraticDefaultsApiTemperatureIsocraticDefaultsGet$Params, context?: HttpContext): Observable<StrictHttpResponse<Array<NameValuePairIsocraticTemperatureNameFloat>>> {
    return getIsocraticDefaultsApiTemperatureIsocraticDefaultsGet(this.http, this.rootUrl, params, context);
  }

  /**
   * Get Isocratic Defaults.
   *
   * Return all isocratic temperature defaults
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `getIsocraticDefaultsApiTemperatureIsocraticDefaultsGet$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  getIsocraticDefaultsApiTemperatureIsocraticDefaultsGet(params?: GetIsocraticDefaultsApiTemperatureIsocraticDefaultsGet$Params, context?: HttpContext): Observable<Array<NameValuePairIsocraticTemperatureNameFloat>> {
    return this.getIsocraticDefaultsApiTemperatureIsocraticDefaultsGet$Response(params, context).pipe(
      map((r: StrictHttpResponse<Array<NameValuePairIsocraticTemperatureNameFloat>>): Array<NameValuePairIsocraticTemperatureNameFloat> => r.body)
    );
  }

  /** Path part for operation `setApiTemperatureSetTemperaturesPut()` */
  static readonly SetApiTemperatureSetTemperaturesPutPath = '/api/temperature/set-temperatures';

  /**
   * Set.
   *
   * Set one or more temperatures.
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `setApiTemperatureSetTemperaturesPut()` instead.
   *
   * This method sends `application/json` and handles request body of type `application/json`.
   */
  setApiTemperatureSetTemperaturesPut$Response(params: SetApiTemperatureSetTemperaturesPut$Params, context?: HttpContext): Observable<StrictHttpResponse<any>> {
    return setApiTemperatureSetTemperaturesPut(this.http, this.rootUrl, params, context);
  }

  /**
   * Set.
   *
   * Set one or more temperatures.
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `setApiTemperatureSetTemperaturesPut$Response()` instead.
   *
   * This method sends `application/json` and handles request body of type `application/json`.
   */
  setApiTemperatureSetTemperaturesPut(params: SetApiTemperatureSetTemperaturesPut$Params, context?: HttpContext): Observable<any> {
    return this.setApiTemperatureSetTemperaturesPut$Response(params, context).pipe(
      map((r: StrictHttpResponse<any>): any => r.body)
    );
  }

}
