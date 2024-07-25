/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';

import { NameValuePairTemperatureNameFloat } from '../../models/name-value-pair-temperature-name-float';

export interface GetTemperaturesApiTemperatureStatusGet$Params {
}

export function getTemperaturesApiTemperatureStatusGet(http: HttpClient, rootUrl: string, params?: GetTemperaturesApiTemperatureStatusGet$Params, context?: HttpContext): Observable<StrictHttpResponse<Array<NameValuePairTemperatureNameFloat>>> {
  const rb = new RequestBuilder(rootUrl, getTemperaturesApiTemperatureStatusGet.PATH, 'get');
  if (params) {
  }

  return http.request(
    rb.build({ responseType: 'json', accept: 'application/json', context })
  ).pipe(
    filter((r: any): r is HttpResponse<any> => r instanceof HttpResponse),
    map((r: HttpResponse<any>) => {
      return r as StrictHttpResponse<Array<NameValuePairTemperatureNameFloat>>;
    })
  );
}

getTemperaturesApiTemperatureStatusGet.PATH = '/api/temperature/status';
