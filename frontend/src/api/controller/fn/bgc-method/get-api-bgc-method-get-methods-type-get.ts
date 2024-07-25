/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';

import { BgcMethodOutput } from '../../models/bgc-method-output';
import { BgcMethodRestType } from '../../models/bgc-method-rest-type';

export interface GetApiBgcMethodGetMethodsTypeGet$Params {
  type: BgcMethodRestType;
}

export function getApiBgcMethodGetMethodsTypeGet(http: HttpClient, rootUrl: string, params: GetApiBgcMethodGetMethodsTypeGet$Params, context?: HttpContext): Observable<StrictHttpResponse<Array<BgcMethodOutput>>> {
  const rb = new RequestBuilder(rootUrl, getApiBgcMethodGetMethodsTypeGet.PATH, 'get');
  if (params) {
    rb.path('type', params.type, {});
  }

  return http.request(
    rb.build({ responseType: 'json', accept: 'application/json', context })
  ).pipe(
    filter((r: any): r is HttpResponse<any> => r instanceof HttpResponse),
    map((r: HttpResponse<any>) => {
      return r as StrictHttpResponse<Array<BgcMethodOutput>>;
    })
  );
}

getApiBgcMethodGetMethodsTypeGet.PATH = '/api/bgc-method/get-methods/{type}';
