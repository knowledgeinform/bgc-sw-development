/* tslint:disable */
/* eslint-disable */
import { BgcMethodTypeNames } from '../models/bgc-method-type-names';
import { NameValuePairIsocraticFlowNameFloat } from '../models/name-value-pair-isocratic-flow-name-float';
import { NameValuePairIsocraticTemperatureNameFloat } from '../models/name-value-pair-isocratic-temperature-name-float';
export interface BgcMethodInput {
  clarity_name: string;

  /**
   * Overridden isocratic flows.
   */
  flows: Array<NameValuePairIsocraticFlowNameFloat>;
  name: string;

  /**
   * Overridden isocratic temperatures.
   */
  temperatures: Array<NameValuePairIsocraticTemperatureNameFloat>;
  type: BgcMethodTypeNames;
}
