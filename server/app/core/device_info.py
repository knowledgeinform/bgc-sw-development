from enum import Enum

# not sure we want to stick all of this stuff in the same file but for now...


class FlowName(str, Enum):
    """
    Derived from "Box/Ballistic GC/2023 BGC Redesign/Hammerhead BGC Event Timeline.pptx"

    NOTE: This belongs elsewhere as it's used by flow system drivers too
    """

    # isocratic
    WASTE = "waste"
    CT_N2 = "ct_n2"
    PCT_N2 = "pct_n2"
    HC_N2 = "hc_n2"
    H2_FPD = "h2_fpd"
    AIR_FPD = "air_fpd"

    # These aren't isocratic in the chemical sense but we set them and forget them
    SAMPLE_LINE_PURGE = "sample_line_purge"
    SAMPLE_FLOW = "sample_flow"


class IsocraticFlowName(str, Enum):
    SAMPLE_LINE_PURGE = FlowName.SAMPLE_LINE_PURGE.value
    SAMPLE_FLOW = FlowName.SAMPLE_FLOW.value
    WASTE = FlowName.WASTE.value
    CT_N2 = FlowName.CT_N2.value
    PCT_N2 = FlowName.PCT_N2.value
    HC_N2 = FlowName.HC_N2.value
    H2_FPD = FlowName.H2_FPD.value
    AIR_FPD = FlowName.AIR_FPD.value


class TemperatureName(str, Enum):
    """
    Derived from "Box/Ballistic GC/2023 BGC Redesign/Hammerhead BGC Event Timeline.pptx"
    """

    # isocratic
    SAMPLE_LINE = "sample_line"
    VALVE_OVEN = "valve_oven"
    COLUMN_XFER = "column_xfer"

    # non-isocratic
    CT_A = "ct_a"
    CT_B = "ct_b"
    PCT = "pct"
    COLUMN = "column"


class IsocraticTemperatureName(str, Enum):
    """
    Derived from "Box/Ballistic GC/2023 BGC Redesign/Hammerhead BGC Event Timeline.pptx"
    """

    SAMPLE_LINE = TemperatureName.SAMPLE_LINE.value
    VALVE_OVEN = TemperatureName.VALVE_OVEN.value
    COLUMN_XFER = TemperatureName.COLUMN_XFER.value


class DigitalIoName(Enum):
    """
    TODO find a source and populate this
    """

    TBD = "TBD"
