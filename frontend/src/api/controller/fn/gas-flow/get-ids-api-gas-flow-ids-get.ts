/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';

import { NameValuePairFlowNameStr } from '../../models/name-value-pair-flow-name-str';

export interface GetIdsApiGasFlowIdsGet$Params {
}

export function getIdsApiGasFlowIdsGet(http: HttpClient, rootUrl: string, params?: GetIdsApiGasFlowIdsGet$Params, context?: HttpContext): Observable<StrictHttpResponse<Array<NameValuePairFlowNameStr>>> {
  const rb = new RequestBuilder(rootUrl, getIdsApiGasFlowIdsGet.PATH, 'get');
  if (params) {
  }

  return http.request(
    rb.build({ responseType: 'json', accept: 'application/json', context })
  ).pipe(
    filter((r: any): r is HttpResponse<any> => r instanceof HttpResponse),
    map((r: HttpResponse<any>) => {
      return r as StrictHttpResponse<Array<NameValuePairFlowNameStr>>;
    })
  );
}

getIdsApiGasFlowIdsGet.PATH = '/api/gas-flow/ids';
