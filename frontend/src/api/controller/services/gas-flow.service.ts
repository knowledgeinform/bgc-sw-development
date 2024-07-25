/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { BaseService } from '../base-service';
import { ControllerApiConfiguration } from '../controller-api-configuration';
import { StrictHttpResponse } from '../strict-http-response';

import { getIdsApiGasFlowIdsGet } from '../fn/gas-flow/get-ids-api-gas-flow-ids-get';
import { GetIdsApiGasFlowIdsGet$Params } from '../fn/gas-flow/get-ids-api-gas-flow-ids-get';
import { getIsocraticDefaultsApiGasFlowIsocraticDefaultsGet } from '../fn/gas-flow/get-isocratic-defaults-api-gas-flow-isocratic-defaults-get';
import { GetIsocraticDefaultsApiGasFlowIsocraticDefaultsGet$Params } from '../fn/gas-flow/get-isocratic-defaults-api-gas-flow-isocratic-defaults-get';
import { getStatusApiGasFlowStatusGet } from '../fn/gas-flow/get-status-api-gas-flow-status-get';
import { GetStatusApiGasFlowStatusGet$Params } from '../fn/gas-flow/get-status-api-gas-flow-status-get';
import { NameValuePairFlowNameStr } from '../models/name-value-pair-flow-name-str';
import { NameValuePairIsocraticFlowNameFloat } from '../models/name-value-pair-isocratic-flow-name-float';
import { setApiGasFlowSetFlowsPut } from '../fn/gas-flow/set-api-gas-flow-set-flows-put';
import { SetApiGasFlowSetFlowsPut$Params } from '../fn/gas-flow/set-api-gas-flow-set-flows-put';
import { UnknownPairFlowName } from '../models/unknown-pair-flow-name';

@Injectable({ providedIn: 'root' })
export class GasFlowService extends BaseService {
  constructor(config: ControllerApiConfiguration, http: HttpClient) {
    super(config, http);
  }

  /** Path part for operation `getIdsApiGasFlowIdsGet()` */
  static readonly GetIdsApiGasFlowIdsGetPath = '/api/gas-flow/ids';

  /**
   * Get Ids.
   *
   * Get the device ids for all of the gas flows
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `getIdsApiGasFlowIdsGet()` instead.
   *
   * This method doesn't expect any request body.
   */
  getIdsApiGasFlowIdsGet$Response(params?: GetIdsApiGasFlowIdsGet$Params, context?: HttpContext): Observable<StrictHttpResponse<Array<NameValuePairFlowNameStr>>> {
    return getIdsApiGasFlowIdsGet(this.http, this.rootUrl, params, context);
  }

  /**
   * Get Ids.
   *
   * Get the device ids for all of the gas flows
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `getIdsApiGasFlowIdsGet$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  getIdsApiGasFlowIdsGet(params?: GetIdsApiGasFlowIdsGet$Params, context?: HttpContext): Observable<Array<NameValuePairFlowNameStr>> {
    return this.getIdsApiGasFlowIdsGet$Response(params, context).pipe(
      map((r: StrictHttpResponse<Array<NameValuePairFlowNameStr>>): Array<NameValuePairFlowNameStr> => r.body)
    );
  }

  /** Path part for operation `getStatusApiGasFlowStatusGet()` */
  static readonly GetStatusApiGasFlowStatusGetPath = '/api/gas-flow/status';

  /**
   * Get Status.
   *
   * Get the status of all of the gas flows.
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `getStatusApiGasFlowStatusGet()` instead.
   *
   * This method doesn't expect any request body.
   */
  getStatusApiGasFlowStatusGet$Response(params?: GetStatusApiGasFlowStatusGet$Params, context?: HttpContext): Observable<StrictHttpResponse<Array<UnknownPairFlowName>>> {
    return getStatusApiGasFlowStatusGet(this.http, this.rootUrl, params, context);
  }

  /**
   * Get Status.
   *
   * Get the status of all of the gas flows.
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `getStatusApiGasFlowStatusGet$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  getStatusApiGasFlowStatusGet(params?: GetStatusApiGasFlowStatusGet$Params, context?: HttpContext): Observable<Array<UnknownPairFlowName>> {
    return this.getStatusApiGasFlowStatusGet$Response(params, context).pipe(
      map((r: StrictHttpResponse<Array<UnknownPairFlowName>>): Array<UnknownPairFlowName> => r.body)
    );
  }

  /** Path part for operation `getIsocraticDefaultsApiGasFlowIsocraticDefaultsGet()` */
  static readonly GetIsocraticDefaultsApiGasFlowIsocraticDefaultsGetPath = '/api/gas-flow/isocratic_defaults';

  /**
   * Get Isocratic Defaults.
   *
   * Return all isocratic temperature defaults.
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `getIsocraticDefaultsApiGasFlowIsocraticDefaultsGet()` instead.
   *
   * This method doesn't expect any request body.
   */
  getIsocraticDefaultsApiGasFlowIsocraticDefaultsGet$Response(params?: GetIsocraticDefaultsApiGasFlowIsocraticDefaultsGet$Params, context?: HttpContext): Observable<StrictHttpResponse<Array<NameValuePairIsocraticFlowNameFloat>>> {
    return getIsocraticDefaultsApiGasFlowIsocraticDefaultsGet(this.http, this.rootUrl, params, context);
  }

  /**
   * Get Isocratic Defaults.
   *
   * Return all isocratic temperature defaults.
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `getIsocraticDefaultsApiGasFlowIsocraticDefaultsGet$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  getIsocraticDefaultsApiGasFlowIsocraticDefaultsGet(params?: GetIsocraticDefaultsApiGasFlowIsocraticDefaultsGet$Params, context?: HttpContext): Observable<Array<NameValuePairIsocraticFlowNameFloat>> {
    return this.getIsocraticDefaultsApiGasFlowIsocraticDefaultsGet$Response(params, context).pipe(
      map((r: StrictHttpResponse<Array<NameValuePairIsocraticFlowNameFloat>>): Array<NameValuePairIsocraticFlowNameFloat> => r.body)
    );
  }

  /** Path part for operation `setApiGasFlowSetFlowsPut()` */
  static readonly SetApiGasFlowSetFlowsPutPath = '/api/gas-flow/set-flows';

  /**
   * Set.
   *
   * Set one or more gas flows
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `setApiGasFlowSetFlowsPut()` instead.
   *
   * This method sends `application/json` and handles request body of type `application/json`.
   */
  setApiGasFlowSetFlowsPut$Response(params: SetApiGasFlowSetFlowsPut$Params, context?: HttpContext): Observable<StrictHttpResponse<any>> {
    return setApiGasFlowSetFlowsPut(this.http, this.rootUrl, params, context);
  }

  /**
   * Set.
   *
   * Set one or more gas flows
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `setApiGasFlowSetFlowsPut$Response()` instead.
   *
   * This method sends `application/json` and handles request body of type `application/json`.
   */
  setApiGasFlowSetFlowsPut(params: SetApiGasFlowSetFlowsPut$Params, context?: HttpContext): Observable<any> {
    return this.setApiGasFlowSetFlowsPut$Response(params, context).pipe(
      map((r: StrictHttpResponse<any>): any => r.body)
    );
  }

}
