/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';


export interface CfgApiClarityCfgPost$Params {
  filepath: string;
}

export function cfgApiClarityCfgPost(http: HttpClient, rootUrl: string, params: CfgApiClarityCfgPost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
  const rb = new RequestBuilder(rootUrl, cfgApiClarityCfgPost.PATH, 'post');
  if (params) {
    rb.query('filepath', params.filepath, {});
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

cfgApiClarityCfgPost.PATH = '/api/clarity/cfg';
