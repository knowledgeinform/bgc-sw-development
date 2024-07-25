/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { BaseService } from '../base-service';
import { ControllerApiConfiguration } from '../controller-api-configuration';
import { StrictHttpResponse } from '../strict-http-response';

import { getStatusApiSystemStatusGet } from '../fn/system/get-status-api-system-status-get';
import { GetStatusApiSystemStatusGet$Params } from '../fn/system/get-status-api-system-status-get';
import { ValueStr } from '../models/value-str';

@Injectable({ providedIn: 'root' })
export class SystemService extends BaseService {
  constructor(config: ControllerApiConfiguration, http: HttpClient) {
    super(config, http);
  }

  /** Path part for operation `getStatusApiSystemStatusGet()` */
  static readonly GetStatusApiSystemStatusGetPath = '/api/system/status';

  /**
   * Get Status.
   *
   * Return aggregated system status.
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `getStatusApiSystemStatusGet()` instead.
   *
   * This method doesn't expect any request body.
   */
  getStatusApiSystemStatusGet$Response(params?: GetStatusApiSystemStatusGet$Params, context?: HttpContext): Observable<StrictHttpResponse<ValueStr>> {
    return getStatusApiSystemStatusGet(this.http, this.rootUrl, params, context);
  }

  /**
   * Get Status.
   *
   * Return aggregated system status.
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `getStatusApiSystemStatusGet$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  getStatusApiSystemStatusGet(params?: GetStatusApiSystemStatusGet$Params, context?: HttpContext): Observable<ValueStr> {
    return this.getStatusApiSystemStatusGet$Response(params, context).pipe(
      map((r: StrictHttpResponse<ValueStr>): ValueStr => r.body)
    );
  }

}
