/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { BaseService } from '../base-service';
import { ControllerApiConfiguration } from '../controller-api-configuration';
import { StrictHttpResponse } from '../strict-http-response';

import { abortAnalysisApiClarityAbortPost } from '../fn/clarity/abort-analysis-api-clarity-abort-post';
import { AbortAnalysisApiClarityAbortPost$Params } from '../fn/clarity/abort-analysis-api-clarity-abort-post';
import { calApplyApiClarityCalApplyPost } from '../fn/clarity/cal-apply-api-clarity-cal-apply-post';
import { CalApplyApiClarityCalApplyPost$Params } from '../fn/clarity/cal-apply-api-clarity-cal-apply-post';
import { calSaveApiClarityCalSavePost } from '../fn/clarity/cal-save-api-clarity-cal-save-post';
import { CalSaveApiClarityCalSavePost$Params } from '../fn/clarity/cal-save-api-clarity-cal-save-post';
import { calSaveAsApiClarityCalSaveAsPost } from '../fn/clarity/cal-save-as-api-clarity-cal-save-as-post';
import { CalSaveAsApiClarityCalSaveAsPost$Params } from '../fn/clarity/cal-save-as-api-clarity-cal-save-as-post';
import { calTypeApiClarityCalTypePost } from '../fn/clarity/cal-type-api-clarity-cal-type-post';
import { CalTypeApiClarityCalTypePost$Params } from '../fn/clarity/cal-type-api-clarity-cal-type-post';
import { cfgApiClarityCfgPost } from '../fn/clarity/cfg-api-clarity-cfg-post';
import { CfgApiClarityCfgPost$Params } from '../fn/clarity/cfg-api-clarity-cfg-post';
import { clearCalApiClarityClearCalPost } from '../fn/clarity/clear-cal-api-clarity-clear-cal-post';
import { ClearCalApiClarityClearCalPost$Params } from '../fn/clarity/clear-cal-api-clarity-clear-cal-post';
import { exitClarityApiClarityExitClarityPost } from '../fn/clarity/exit-clarity-api-clarity-exit-clarity-post';
import { ExitClarityApiClarityExitClarityPost$Params } from '../fn/clarity/exit-clarity-api-clarity-exit-clarity-post';
import { exportResultsApiClarityExportResultsPost } from '../fn/clarity/export-results-api-clarity-export-results-post';
import { ExportResultsApiClarityExportResultsPost$Params } from '../fn/clarity/export-results-api-clarity-export-results-post';
import { exportResultsDbfApiClarityExportResultsDbfPost } from '../fn/clarity/export-results-dbf-api-clarity-export-results-dbf-post';
import { ExportResultsDbfApiClarityExportResultsDbfPost$Params } from '../fn/clarity/export-results-dbf-api-clarity-export-results-dbf-post';
import { exportRunTimeApiClarityExportRunTimePost } from '../fn/clarity/export-run-time-api-clarity-export-run-time-post';
import { ExportRunTimeApiClarityExportRunTimePost$Params } from '../fn/clarity/export-run-time-api-clarity-export-run-time-post';
import { startClarityApiClarityStartClarityPost } from '../fn/clarity/start-clarity-api-clarity-start-clarity-post';
import { StartClarityApiClarityStartClarityPost$Params } from '../fn/clarity/start-clarity-api-clarity-start-clarity-post';

@Injectable({ providedIn: 'root' })
export class ClarityService extends BaseService {
  constructor(config: ControllerApiConfiguration, http: HttpClient) {
    super(config, http);
  }

  /** Path part for operation `startClarityApiClarityStartClarityPost()` */
  static readonly StartClarityApiClarityStartClarityPostPath = '/api/clarity/start_clarity';

  /**
   * Start Clarity.
   *
   *
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `startClarityApiClarityStartClarityPost()` instead.
   *
   * This method doesn't expect any request body.
   */
  startClarityApiClarityStartClarityPost$Response(params?: StartClarityApiClarityStartClarityPost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
}>> {
    return startClarityApiClarityStartClarityPost(this.http, this.rootUrl, params, context);
  }

  /**
   * Start Clarity.
   *
   *
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `startClarityApiClarityStartClarityPost$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  startClarityApiClarityStartClarityPost(params?: StartClarityApiClarityStartClarityPost$Params, context?: HttpContext): Observable<{
}> {
    return this.startClarityApiClarityStartClarityPost$Response(params, context).pipe(
      map((r: StrictHttpResponse<{
}>): {
} => r.body)
    );
  }

  /** Path part for operation `exitClarityApiClarityExitClarityPost()` */
  static readonly ExitClarityApiClarityExitClarityPostPath = '/api/clarity/exit_clarity';

  /**
   * Exit Clarity.
   *
   *
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `exitClarityApiClarityExitClarityPost()` instead.
   *
   * This method doesn't expect any request body.
   */
  exitClarityApiClarityExitClarityPost$Response(params?: ExitClarityApiClarityExitClarityPost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
}>> {
    return exitClarityApiClarityExitClarityPost(this.http, this.rootUrl, params, context);
  }

  /**
   * Exit Clarity.
   *
   *
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `exitClarityApiClarityExitClarityPost$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  exitClarityApiClarityExitClarityPost(params?: ExitClarityApiClarityExitClarityPost$Params, context?: HttpContext): Observable<{
}> {
    return this.exitClarityApiClarityExitClarityPost$Response(params, context).pipe(
      map((r: StrictHttpResponse<{
}>): {
} => r.body)
    );
  }

  /** Path part for operation `calApplyApiClarityCalApplyPost()` */
  static readonly CalApplyApiClarityCalApplyPostPath = '/api/clarity/cal_apply';

  /**
   * Cal Apply.
   *
   *
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `calApplyApiClarityCalApplyPost()` instead.
   *
   * This method doesn't expect any request body.
   */
  calApplyApiClarityCalApplyPost$Response(params: CalApplyApiClarityCalApplyPost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
    return calApplyApiClarityCalApplyPost(this.http, this.rootUrl, params, context);
  }

  /**
   * Cal Apply.
   *
   *
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `calApplyApiClarityCalApplyPost$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  calApplyApiClarityCalApplyPost(params: CalApplyApiClarityCalApplyPost$Params, context?: HttpContext): Observable<{
[key: string]: string;
}> {
    return this.calApplyApiClarityCalApplyPost$Response(params, context).pipe(
      map((r: StrictHttpResponse<{
[key: string]: string;
}>): {
[key: string]: string;
} => r.body)
    );
  }

  /** Path part for operation `calSaveApiClarityCalSavePost()` */
  static readonly CalSaveApiClarityCalSavePostPath = '/api/clarity/cal_save';

  /**
   * Cal Save.
   *
   *
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `calSaveApiClarityCalSavePost()` instead.
   *
   * This method doesn't expect any request body.
   */
  calSaveApiClarityCalSavePost$Response(params?: CalSaveApiClarityCalSavePost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
    return calSaveApiClarityCalSavePost(this.http, this.rootUrl, params, context);
  }

  /**
   * Cal Save.
   *
   *
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `calSaveApiClarityCalSavePost$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  calSaveApiClarityCalSavePost(params?: CalSaveApiClarityCalSavePost$Params, context?: HttpContext): Observable<{
[key: string]: string;
}> {
    return this.calSaveApiClarityCalSavePost$Response(params, context).pipe(
      map((r: StrictHttpResponse<{
[key: string]: string;
}>): {
[key: string]: string;
} => r.body)
    );
  }

  /** Path part for operation `calSaveAsApiClarityCalSaveAsPost()` */
  static readonly CalSaveAsApiClarityCalSaveAsPostPath = '/api/clarity/cal_save_as';

  /**
   * Cal Save As.
   *
   *
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `calSaveAsApiClarityCalSaveAsPost()` instead.
   *
   * This method doesn't expect any request body.
   */
  calSaveAsApiClarityCalSaveAsPost$Response(params: CalSaveAsApiClarityCalSaveAsPost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
    return calSaveAsApiClarityCalSaveAsPost(this.http, this.rootUrl, params, context);
  }

  /**
   * Cal Save As.
   *
   *
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `calSaveAsApiClarityCalSaveAsPost$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  calSaveAsApiClarityCalSaveAsPost(params: CalSaveAsApiClarityCalSaveAsPost$Params, context?: HttpContext): Observable<{
[key: string]: string;
}> {
    return this.calSaveAsApiClarityCalSaveAsPost$Response(params, context).pipe(
      map((r: StrictHttpResponse<{
[key: string]: string;
}>): {
[key: string]: string;
} => r.body)
    );
  }

  /** Path part for operation `calTypeApiClarityCalTypePost()` */
  static readonly CalTypeApiClarityCalTypePostPath = '/api/clarity/cal_type';

  /**
   * Cal Type.
   *
   *
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `calTypeApiClarityCalTypePost()` instead.
   *
   * This method doesn't expect any request body.
   */
  calTypeApiClarityCalTypePost$Response(params: CalTypeApiClarityCalTypePost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
    return calTypeApiClarityCalTypePost(this.http, this.rootUrl, params, context);
  }

  /**
   * Cal Type.
   *
   *
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `calTypeApiClarityCalTypePost$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  calTypeApiClarityCalTypePost(params: CalTypeApiClarityCalTypePost$Params, context?: HttpContext): Observable<{
[key: string]: string;
}> {
    return this.calTypeApiClarityCalTypePost$Response(params, context).pipe(
      map((r: StrictHttpResponse<{
[key: string]: string;
}>): {
[key: string]: string;
} => r.body)
    );
  }

  /** Path part for operation `clearCalApiClarityClearCalPost()` */
  static readonly ClearCalApiClarityClearCalPostPath = '/api/clarity/clear_cal';

  /**
   * Clear Cal.
   *
   *
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `clearCalApiClarityClearCalPost()` instead.
   *
   * This method doesn't expect any request body.
   */
  clearCalApiClarityClearCalPost$Response(params?: ClearCalApiClarityClearCalPost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
    return clearCalApiClarityClearCalPost(this.http, this.rootUrl, params, context);
  }

  /**
   * Clear Cal.
   *
   *
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `clearCalApiClarityClearCalPost$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  clearCalApiClarityClearCalPost(params?: ClearCalApiClarityClearCalPost$Params, context?: HttpContext): Observable<{
[key: string]: string;
}> {
    return this.clearCalApiClarityClearCalPost$Response(params, context).pipe(
      map((r: StrictHttpResponse<{
[key: string]: string;
}>): {
[key: string]: string;
} => r.body)
    );
  }

  /** Path part for operation `cfgApiClarityCfgPost()` */
  static readonly CfgApiClarityCfgPostPath = '/api/clarity/cfg';

  /**
   * Cfg.
   *
   *
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `cfgApiClarityCfgPost()` instead.
   *
   * This method doesn't expect any request body.
   */
  cfgApiClarityCfgPost$Response(params: CfgApiClarityCfgPost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
    return cfgApiClarityCfgPost(this.http, this.rootUrl, params, context);
  }

  /**
   * Cfg.
   *
   *
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `cfgApiClarityCfgPost$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  cfgApiClarityCfgPost(params: CfgApiClarityCfgPost$Params, context?: HttpContext): Observable<{
[key: string]: string;
}> {
    return this.cfgApiClarityCfgPost$Response(params, context).pipe(
      map((r: StrictHttpResponse<{
[key: string]: string;
}>): {
[key: string]: string;
} => r.body)
    );
  }

  /** Path part for operation `abortAnalysisApiClarityAbortPost()` */
  static readonly AbortAnalysisApiClarityAbortPostPath = '/api/clarity/abort';

  /**
   * Abort Analysis.
   *
   *
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `abortAnalysisApiClarityAbortPost()` instead.
   *
   * This method doesn't expect any request body.
   */
  abortAnalysisApiClarityAbortPost$Response(params: AbortAnalysisApiClarityAbortPost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
    return abortAnalysisApiClarityAbortPost(this.http, this.rootUrl, params, context);
  }

  /**
   * Abort Analysis.
   *
   *
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `abortAnalysisApiClarityAbortPost$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  abortAnalysisApiClarityAbortPost(params: AbortAnalysisApiClarityAbortPost$Params, context?: HttpContext): Observable<{
[key: string]: string;
}> {
    return this.abortAnalysisApiClarityAbortPost$Response(params, context).pipe(
      map((r: StrictHttpResponse<{
[key: string]: string;
}>): {
[key: string]: string;
} => r.body)
    );
  }

  /** Path part for operation `exportResultsApiClarityExportResultsPost()` */
  static readonly ExportResultsApiClarityExportResultsPostPath = '/api/clarity/export_results/';

  /**
   * Export Results.
   *
   *
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `exportResultsApiClarityExportResultsPost()` instead.
   *
   * This method sends `application/json` and handles request body of type `application/json`.
   */
  exportResultsApiClarityExportResultsPost$Response(params: ExportResultsApiClarityExportResultsPost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
    return exportResultsApiClarityExportResultsPost(this.http, this.rootUrl, params, context);
  }

  /**
   * Export Results.
   *
   *
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `exportResultsApiClarityExportResultsPost$Response()` instead.
   *
   * This method sends `application/json` and handles request body of type `application/json`.
   */
  exportResultsApiClarityExportResultsPost(params: ExportResultsApiClarityExportResultsPost$Params, context?: HttpContext): Observable<{
[key: string]: string;
}> {
    return this.exportResultsApiClarityExportResultsPost$Response(params, context).pipe(
      map((r: StrictHttpResponse<{
[key: string]: string;
}>): {
[key: string]: string;
} => r.body)
    );
  }

  /** Path part for operation `exportResultsDbfApiClarityExportResultsDbfPost()` */
  static readonly ExportResultsDbfApiClarityExportResultsDbfPostPath = '/api/clarity/export_results_dbf/';

  /**
   * Export Results Dbf.
   *
   *
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `exportResultsDbfApiClarityExportResultsDbfPost()` instead.
   *
   * This method sends `application/json` and handles request body of type `application/json`.
   */
  exportResultsDbfApiClarityExportResultsDbfPost$Response(params: ExportResultsDbfApiClarityExportResultsDbfPost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
    return exportResultsDbfApiClarityExportResultsDbfPost(this.http, this.rootUrl, params, context);
  }

  /**
   * Export Results Dbf.
   *
   *
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `exportResultsDbfApiClarityExportResultsDbfPost$Response()` instead.
   *
   * This method sends `application/json` and handles request body of type `application/json`.
   */
  exportResultsDbfApiClarityExportResultsDbfPost(params: ExportResultsDbfApiClarityExportResultsDbfPost$Params, context?: HttpContext): Observable<{
[key: string]: string;
}> {
    return this.exportResultsDbfApiClarityExportResultsDbfPost$Response(params, context).pipe(
      map((r: StrictHttpResponse<{
[key: string]: string;
}>): {
[key: string]: string;
} => r.body)
    );
  }

  /** Path part for operation `exportRunTimeApiClarityExportRunTimePost()` */
  static readonly ExportRunTimeApiClarityExportRunTimePostPath = '/api/clarity/export_run_time/';

  /**
   * Export Run Time.
   *
   *
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `exportRunTimeApiClarityExportRunTimePost()` instead.
   *
   * This method sends `application/json` and handles request body of type `application/json`.
   */
  exportRunTimeApiClarityExportRunTimePost$Response(params: ExportRunTimeApiClarityExportRunTimePost$Params, context?: HttpContext): Observable<StrictHttpResponse<{
[key: string]: string;
}>> {
    return exportRunTimeApiClarityExportRunTimePost(this.http, this.rootUrl, params, context);
  }

  /**
   * Export Run Time.
   *
   *
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `exportRunTimeApiClarityExportRunTimePost$Response()` instead.
   *
   * This method sends `application/json` and handles request body of type `application/json`.
   */
  exportRunTimeApiClarityExportRunTimePost(params: ExportRunTimeApiClarityExportRunTimePost$Params, context?: HttpContext): Observable<{
[key: string]: string;
}> {
    return this.exportRunTimeApiClarityExportRunTimePost$Response(params, context).pipe(
      map((r: StrictHttpResponse<{
[key: string]: string;
}>): {
[key: string]: string;
} => r.body)
    );
  }

}
