/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';

import { NameValuePairIsocraticTemperatureNameFloat } from '../../models/name-value-pair-isocratic-temperature-name-float';

export interface SetApiTemperatureSetTemperaturesPut$Params {
      body: Array<NameValuePairIsocraticTemperatureNameFloat>
}

export function setApiTemperatureSetTemperaturesPut(http: HttpClient, rootUrl: string, params: SetApiTemperatureSetTemperaturesPut$Params, context?: HttpContext): Observable<StrictHttpResponse<any>> {
  const rb = new RequestBuilder(rootUrl, setApiTemperatureSetTemperaturesPut.PATH, 'put');
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

setApiTemperatureSetTemperaturesPut.PATH = '/api/temperature/set-temperatures';
