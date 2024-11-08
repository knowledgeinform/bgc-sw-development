/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';


export interface CalSaveAsApiClarityCalSaveAsPost$Params {
  method: string;
}

export function calSaveAsApiClarityCalSaveAsPost(http: HttpClient, rootUrl: string, params: CalSaveAsApiClarityCalSaveAsPost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
  const rb = new RequestBuilder(rootUrl, calSaveAsApiClarityCalSaveAsPost.PATH, 'post');
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

calSaveAsApiClarityCalSaveAsPost.PATH = '/api/clarity/cal_save_as';
