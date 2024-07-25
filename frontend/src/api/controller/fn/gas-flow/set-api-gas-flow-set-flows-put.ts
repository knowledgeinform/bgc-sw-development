/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';

import { NameValuePairIsocraticFlowNameFloat } from '../../models/name-value-pair-isocratic-flow-name-float';

export interface SetApiGasFlowSetFlowsPut$Params {
      body: Array<NameValuePairIsocraticFlowNameFloat>
}

export function setApiGasFlowSetFlowsPut(http: HttpClient, rootUrl: string, params: SetApiGasFlowSetFlowsPut$Params, context?: HttpContext): Observable<StrictHttpResponse<any>> {
  const rb = new RequestBuilder(rootUrl, setApiGasFlowSetFlowsPut.PATH, 'put');
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

setApiGasFlowSetFlowsPut.PATH = '/api/gas-flow/set-flows';
