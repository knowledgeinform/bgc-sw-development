/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';

import { ValueStr } from '../../models/value-str';

export interface GetStatusApiSystemStatusGet$Params {
}

export function getStatusApiSystemStatusGet(http: HttpClient, rootUrl: string, params?: GetStatusApiSystemStatusGet$Params, context?: HttpContext): Observable<StrictHttpResponse<ValueStr>> {
  const rb = new RequestBuilder(rootUrl, getStatusApiSystemStatusGet.PATH, 'get');
  if (params) {
  }

  return http.request(
    rb.build({ responseType: 'json', accept: 'application/json', context })
  ).pipe(
    filter((r: any): r is HttpResponse<any> => r instanceof HttpResponse),
    map((r: HttpResponse<any>) => {
      return r as StrictHttpResponse<ValueStr>;
    })
  );
}

getStatusApiSystemStatusGet.PATH = '/api/system/status';
