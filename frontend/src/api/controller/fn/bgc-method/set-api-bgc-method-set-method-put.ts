/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';

import { BgcMethodInput } from '../../models/bgc-method-input';

export interface SetApiBgcMethodSetMethodPut$Params {
      body: BgcMethodInput
}

export function setApiBgcMethodSetMethodPut(http: HttpClient, rootUrl: string, params: SetApiBgcMethodSetMethodPut$Params, context?: HttpContext): Observable<StrictHttpResponse<any>> {
  const rb = new RequestBuilder(rootUrl, setApiBgcMethodSetMethodPut.PATH, 'put');
  if (params) {
    rb.body(params.body, 'application/json');
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

setApiBgcMethodSetMethodPut.PATH = '/api/bgc-method/set-method';
