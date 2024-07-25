/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';

import { NameValuePairIsocraticFlowNameFloat } from '../../models/name-value-pair-isocratic-flow-name-float';

export interface GetIsocraticDefaultsApiGasFlowIsocraticDefaultsGet$Params {
}

export function getIsocraticDefaultsApiGasFlowIsocraticDefaultsGet(http: HttpClient, rootUrl: string, params?: GetIsocraticDefaultsApiGasFlowIsocraticDefaultsGet$Params, context?: HttpContext): Observable<StrictHttpResponse<Array<NameValuePairIsocraticFlowNameFloat>>> {
  const rb = new RequestBuilder(rootUrl, getIsocraticDefaultsApiGasFlowIsocraticDefaultsGet.PATH, 'get');
  if (params) {
  }

  return http.request(
    rb.build({ responseType: 'json', accept: 'application/json', context })
  ).pipe(
    filter((r: any): r is HttpResponse<any> => r instanceof HttpResponse),
    map((r: HttpResponse<any>) => {
      return r as StrictHttpResponse<Array<NameValuePairIsocraticFlowNameFloat>>;
    })
  );
}

getIsocraticDefaultsApiGasFlowIsocraticDefaultsGet.PATH = '/api/gas-flow/isocratic_defaults';
