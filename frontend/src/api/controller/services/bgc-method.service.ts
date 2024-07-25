/* tslint:disable */
/* eslint-disable */
import { HttpClient, HttpContext } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { BaseService } from '../base-service';
import { ControllerApiConfiguration } from '../controller-api-configuration';
import { StrictHttpResponse } from '../strict-http-response';

import { BgcMethodOutput } from '../models/bgc-method-output';
import { getApiBgcMethodGetMethodsTypeGet } from '../fn/bgc-method/get-api-bgc-method-get-methods-type-get';
import { GetApiBgcMethodGetMethodsTypeGet$Params } from '../fn/bgc-method/get-api-bgc-method-get-methods-type-get';
import { setApiBgcMethodSetMethodPut } from '../fn/bgc-method/set-api-bgc-method-set-method-put';
import { SetApiBgcMethodSetMethodPut$Params } from '../fn/bgc-method/set-api-bgc-method-set-method-put';

@Injectable({ providedIn: 'root' })
export class BgcMethodService extends BaseService {
  constructor(config: ControllerApiConfiguration, http: HttpClient) {
    super(config, http);
  }

  /** Path part for operation `getApiBgcMethodGetMethodsTypeGet()` */
  static readonly GetApiBgcMethodGetMethodsTypeGetPath = '/api/bgc-method/get-methods/{type}';

  /**
   * Get.
   *
   * Get all BGC methods of a given type
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `getApiBgcMethodGetMethodsTypeGet()` instead.
   *
   * This method doesn't expect any request body.
   */
  getApiBgcMethodGetMethodsTypeGet$Response(params: GetApiBgcMethodGetMethodsTypeGet$Params, context?: HttpContext): Observable<StrictHttpResponse<Array<BgcMethodOutput>>> {
    return getApiBgcMethodGetMethodsTypeGet(this.http, this.rootUrl, params, context);
  }

  /**
   * Get.
   *
   * Get all BGC methods of a given type
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `getApiBgcMethodGetMethodsTypeGet$Response()` instead.
   *
   * This method doesn't expect any request body.
   */
  getApiBgcMethodGetMethodsTypeGet(params: GetApiBgcMethodGetMethodsTypeGet$Params, context?: HttpContext): Observable<Array<BgcMethodOutput>> {
    return this.getApiBgcMethodGetMethodsTypeGet$Response(params, context).pipe(
      map((r: StrictHttpResponse<Array<BgcMethodOutput>>): Array<BgcMethodOutput> => r.body)
    );
  }

  /** Path part for operation `setApiBgcMethodSetMethodPut()` */
  static readonly SetApiBgcMethodSetMethodPutPath = '/api/bgc-method/set-method';

  /**
   * Set.
   *
   * Set all values for a BGC method, overwrites existing method
   *
   * This method provides access to the full `HttpResponse`, allowing access to response headers.
   * To access only the response body, use `setApiBgcMethodSetMethodPut()` instead.
   *
   * This method sends `application/json` and handles request body of type `application/json`.
   */
  setApiBgcMethodSetMethodPut$Response(params: SetApiBgcMethodSetMethodPut$Params, context?: HttpContext): Observable<StrictHttpResponse<any>> {
    return setApiBgcMethodSetMethodPut(this.http, this.rootUrl, params, context);
  }

  /**
   * Set.
   *
   * Set all values for a BGC method, overwrites existing method
   *
   * This method provides access only to the response body.
   * To access the full response (for headers, for example), `setApiBgcMethodSetMethodPut$Response()` instead.
   *
   * This method sends `application/json` and handles request body of type `application/json`.
   */
  setApiBgcMethodSetMethodPut(params: SetApiBgcMethodSetMethodPut$Params, context?: HttpContext): Observable<any> {
    return this.setApiBgcMethodSetMethodPut$Response(params, context).pipe(
      map((r: StrictHttpResponse<any>): any => r.body)
    );
  }

}
