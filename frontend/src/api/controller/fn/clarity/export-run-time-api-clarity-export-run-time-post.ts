/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';

import { ExportRequest } from '../../models/export-request';

export interface ExportRunTimeApiClarityExportRunTimePost$Params {
      body: ExportRequest
}

export function exportRunTimeApiClarityExportRunTimePost(http: HttpClient, rootUrl: string, params: ExportRunTimeApiClarityExportRunTimePost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
  const rb = new RequestBuilder(rootUrl, exportRunTimeApiClarityExportRunTimePost.PATH, 'post');
  if (params) {
    rb.body(params.body, 'application/json');
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

exportRunTimeApiClarityExportRunTimePost.PATH = '/api/clarity/export_run_time/';
