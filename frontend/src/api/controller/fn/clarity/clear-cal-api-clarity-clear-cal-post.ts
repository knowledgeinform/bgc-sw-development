/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';


export interface ClearCalApiClarityClearCalPost$Params {
}

export function clearCalApiClarityClearCalPost(http: HttpClient, rootUrl: string, params?: ClearCalApiClarityClearCalPost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
  const rb = new RequestBuilder(rootUrl, clearCalApiClarityClearCalPost.PATH, 'post');
  if (params) {
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

clearCalApiClarityClearCalPost.PATH = '/api/clarity/clear_cal';
