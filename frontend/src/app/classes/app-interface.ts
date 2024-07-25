export enum MethodStep {
  none,
  load_initiation_method,
  light_fpd,
  load_method,
  standard_injection,
  sample,
}

export enum MethodSelection {
  high_exposure_hd_gb = 'High Exposure - HD and GB',
  low_exposure_hd_gb = 'Low Exposure - HD and GB',
  high_exposure_vx = 'High Exposure - Vx',
  no_selection = 'No selection',
}

export enum SystemStatusLight {
  good,
  warning,
  no_status,
}
