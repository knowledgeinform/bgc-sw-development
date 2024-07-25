/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';


export interface AbortAnalysisApiClarityAbortPost$Params {
  value: number;
}

export function abortAnalysisApiClarityAbortPost(http: HttpClient, rootUrl: string, params: AbortAnalysisApiClarityAbortPost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
  const rb = new RequestBuilder(rootUrl, abortAnalysisApiClarityAbortPost.PATH, 'post');
  if (params) {
    rb.query('value', params.value, {});
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

abortAnalysisApiClarityAbortPost.PATH = '/api/clarity/abort';
