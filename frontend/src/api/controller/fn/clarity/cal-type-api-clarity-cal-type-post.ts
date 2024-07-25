/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';


export interface CalTypeApiClarityCalTypePost$Params {
  calibration_type: string;
}

export function calTypeApiClarityCalTypePost(http: HttpClient, rootUrl: string, params: CalTypeApiClarityCalTypePost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
  const rb = new RequestBuilder(rootUrl, calTypeApiClarityCalTypePost.PATH, 'post');
  if (params) {
    rb.query('calibration_type', params.calibration_type, {});
  }

  return http.request(
    rb.build({ responseType: 'json', accept: 'application/json', context })
  ).pipe(
    filter((r: any): r is HttpResponse<any> => r instanceof HttpResponse),
    map((r: HttpResponse<any>) => {
      return r as StrictHttpResponse<{
      [key: string]: string;
      }>;
    })
  );
}

calTypeApiClarityCalTypePost.PATH = '/api/clarity/cal_type';
