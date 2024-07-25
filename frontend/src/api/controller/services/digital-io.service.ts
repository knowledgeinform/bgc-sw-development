/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { BaseService } from '../base-service';
import { ControllerApiConfiguration } from '../controller-api-configuration';
import { StrictHttpResponse } from '../strict-http-response';

import { NameValuePairDigitalIoNameOnOff } from '../models/name-value-pair-digital-io-name-on-off';
import { statusApiDigitalIoStatusGet } from '../fn/digital-io/status-api-digital-io-status-get';
import { StatusApiDigitalIoStatusGet$Params } from '../fn/digital-io/status-api-digital-io-status-get';

@Injectable({ providedIn: 'root' })
export class DigitalIoService extends BaseService {
  constructor(config: ControllerApiConfiguration, http: HttpClient) {
    super(config, http);
  }

  /** Path part for operation `statusApiDigitalIoStatusGet()` */
  static readonly StatusApiDigitalIoStatusGetPath = '/api/digital-io/status';

  /**
   * Status.
   *
   * Read the status of the digital IO lines
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `statusApiDigitalIoStatusGet()` instead.
   *
   * This method doesn't expect any request body.
   */
  statusApiDigitalIoStatusGet$Response(params?: StatusApiDigitalIoStatusGet$Params, context?: HttpContext): Observable<StrictHttpResponse<Array<NameValuePairDigitalIoNameOnOff>>> {
    return statusApiDigitalIoStatusGet(this.http, this.rootUrl, params, context);
  }

  /**
   * Status.
   *
   * Read the status of the digital IO lines
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `statusApiDigitalIoStatusGet$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  statusApiDigitalIoStatusGet(params?: StatusApiDigitalIoStatusGet$Params, context?: HttpContext): Observable<Array<NameValuePairDigitalIoNameOnOff>> {
    return this.statusApiDigitalIoStatusGet$Response(params, context).pipe(
      map((r: StrictHttpResponse<Array<NameValuePairDigitalIoNameOnOff>>): Array<NameValuePairDigitalIoNameOnOff> => r.body)
    );
  }

}
