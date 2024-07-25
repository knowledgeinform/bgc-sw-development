/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';


export interface CalApplyApiClarityCalApplyPost$Params {

/**
 * The name of the method to apply
 */
  method: string;
}

export function calApplyApiClarityCalApplyPost(http: HttpClient, rootUrl: string, params: CalApplyApiClarityCalApplyPost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
  const rb = new RequestBuilder(rootUrl, calApplyApiClarityCalApplyPost.PATH, 'post');
  if (params) {
    rb.query('method', params.method, {});
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

calApplyApiClarityCalApplyPost.PATH = '/api/clarity/cal_apply';
