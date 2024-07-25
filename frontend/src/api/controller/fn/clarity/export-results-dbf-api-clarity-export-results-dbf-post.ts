/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';
import { StrictHttpResponse } from '../../strict-http-response';
import { RequestBuilder } from '../../request-builder';

import { ExportRequest } from '../../models/export-request';

export interface ExportResultsDbfApiClarityExportResultsDbfPost$Params {
      body: ExportRequest
}

export function exportResultsDbfApiClarityExportResultsDbfPost(http: HttpClient, rootUrl: string, params: ExportResultsDbfApiClarityExportResultsDbfPost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
  const rb = new RequestBuilder(rootUrl, exportResultsDbfApiClarityExportResultsDbfPost.PATH, 'post');
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

exportResultsDbfApiClarityExportResultsDbfPost.PATH = '/api/clarity/export_results_dbf/';
