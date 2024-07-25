/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';

import { NameValuePairDigitalIoNameOnOff } from '../../models/name-value-pair-digital-io-name-on-off';

export interface StatusApiDigitalIoStatusGet$Params {
}

export function statusApiDigitalIoStatusGet(http: HttpClient, rootUrl: string, params?: StatusApiDigitalIoStatusGet$Params, context?: HttpContext): Observable<StrictHttpResponse<Array<NameValuePairDigitalIoNameOnOff>>> {
  const rb = new RequestBuilder(rootUrl, statusApiDigitalIoStatusGet.PATH, 'get');
  if (params) {
  }

  return http.request(
    rb.build({ responseType: 'json', accept: 'application/json', context })
  ).pipe(
    filter((r: any): r is HttpResponse<any> => r instanceof HttpResponse),
    map((r: HttpResponse<any>) => {
      return r as StrictHttpResponse<Array<NameValuePairDigitalIoNameOnOff>>;
    })
  );
}

statusApiDigitalIoStatusGet.PATH = '/api/digital-io/status';
