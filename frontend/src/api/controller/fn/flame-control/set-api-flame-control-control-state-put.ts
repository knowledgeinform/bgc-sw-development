/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';

import { OnOff } from '../../models/on-off';

export interface SetApiFlameControlControlStatePut$Params {
  state: OnOff;
}

export function setApiFlameControlControlStatePut(http: HttpClient, rootUrl: string, params: SetApiFlameControlControlStatePut$Params, context?: HttpContext): Observable<StrictHttpResponse<any>> {
  const rb = new RequestBuilder(rootUrl, setApiFlameControlControlStatePut.PATH, 'put');
  if (params) {
    rb.path('state', params.state, {});
  }

  return http.request(
    rb.build({ responseType: 'json', accept: 'application/json', context })
  ).pipe(
    filter((r: any): r is HttpResponse<any> => r instanceof HttpResponse),
    map((r: HttpResponse<any>) => {
      return r as StrictHttpResponse<any>;
    })
  );
}

setApiFlameControlControlStatePut.PATH = '/api/flame-control/control/{state}';
