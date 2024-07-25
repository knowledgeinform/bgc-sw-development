import { MethodSelection } from './app-interface';

export class Method {
  private _type: MethodSelection;
  private _description: string;
  private _cycle_time_min: number;
  private _heart_cut: boolean;
  private _volume: 'high' | 'low';
  private _compounds: Compound[];

  constructor(
    type?: MethodSelection,
    description?: string,
    cycle_time_min?: number,
    heart_cut?: boolean,
    volume?: 'high' | 'low',
    compounds?: Compound[]
  ) {
    // use default method if not initlaized
    this._type = type ?? MethodSelection.no_selection;
    this._description = description ?? 'SAMPLE DESCRIPTION OF INITIATION METHOD';
    this._cycle_time_min = cycle_time_min ?? 12;
    this._heart_cut = heart_cut ?? true;
    this._volume = volume ?? 'high';
    this._compounds = compounds ?? [{ name: 'Compound 1' }, { name: 'Compound 2' }];
  }

  public get type(): MethodSelection {
    return this._type;
  }

  public set type(val: MethodSelection) {
    this._type = val;
  }

  public get description(): string {
    return this._description;
  }

  public set description(val: string) {
    this._description = val;
  }

  public get cycle_time_min(): number {
    return this._cycle_time_min;
  }

  public set cycle_time_min(val: number) {
    this._cycle_time_min = val;
  }

  public get cycle_time_string(): string {
    return this.cycle_time_min.toString() + ':00';
  }

  public get heart_cut(): boolean {
    return this._heart_cut;
  }

  public set heart_cut(val: boolean) {
    this._heart_cut = val;
  }

  public get heart_cut_string(): string {
    let val = '';
    if (this.heart_cut) {
      val = 'Yes';
    } else {
      val = 'No';
    }
    return val;
  }

  public get volume(): 'high' | 'low' {
    return this._volume;
  }

  public set volume(val: 'high' | 'low') {
    this._volume = val;
  }

  public get volume_string(): string {
    let val = '';
    if (this.volume === 'high') {
      val = 'High Volume';
    }
    if (this.volume === 'low') {
      val = 'low Volume';
    }
    return val;
  }

  public get compounds(): Compound[] {
    return this._compounds;
  }

  public set compounds(val: Compound[]) {
    this._compounds = val;
  }

  public get compounds_string(): string {
    let val = '';
    for (let i = 0; i < this.compounds.length; i++) {
      val += this.compounds[i].name;
      if (i != this.compounds.length - 1) {
        val += ', ';
      }
    }
    return val;
  }
}

export class Compound {
  name!: string;
}
