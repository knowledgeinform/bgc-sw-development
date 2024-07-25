import argparse
import asyncio
import os
import sys
from typing import Final, Sequence, Optional
import warnings

from pyparsing import ParseException

from drivers.mfc.alicat_basis_mfc_driver import AlicatBasisMfcDriver, TbdSerialPort

"""
Test code for the Alicat Basis MFC driver.

See See https://gitlab.jhuapl.edu/qai/ltpms/mms-sw.git code/software/applications/aerosol/alicat/src/main.* for
more information.
"""


class ToolOptions:
    ALL_STATUS: Final[str] = "all-status"
    FULL_SCALE_RANGE: Final[str] = "full-scale-range"
    SET_ID: Final[str] = "set-id"
    SET_FLOWPOINT_SLPM: Final[str] = "set-flowpoint-slpm"
    # ...

    def __init__(self) -> None:
        self.sub_command: str = ""  # Required
        self.id: str  # required
        self.flow: Optional[float]

        filename = os.path.basename(__file__)
        filename_wo_ext = os.path.splitext(filename)[0]
        driver_name = filename[0 : len(filename_wo_ext) - len("_hw_test.py") - 1]
        self.parser = argparse.ArgumentParser(description=f"Test the {driver_name}_driver")

        subparsers = self.parser.add_subparsers(title="sub commands", help="sub-command help")

        #########################################################
        # general options
        #########################################################

        # TBD are there any?
        # self.parser.add_argument(
        #     f"--{self.VERSION}",
        #     help="Display the version of the tool and exit",
        #     required=False,
        #     action="store_true",
        # )

        #########################################################
        # all-status subcommand
        #########################################################

        parser_all_status = subparsers.add_parser(
            name=self.ALL_STATUS,
            help="displays all device status",
        )
        parser_all_status.set_defaults(sub_command=self.ALL_STATUS)
        parser_all_status.add_argument(
            # name="id",
            help="[A-Z]",
            dest="id",
            # required=True,
        )

        parser_full_scale_range = subparsers.add_parser(
            name=self.FULL_SCALE_RANGE,
            help="Displays device full scale range",
        )
        parser_full_scale_range.set_defaults(sub_command=self.FULL_SCALE_RANGE)

        parser_full_scale_range.add_argument(
            # name="id",
            help="[A-Z]",
            dest="id",
            # required=True,
        )

        #########################################################
        # set-id subcommand
        #########################################################

        parser_set_id = subparsers.add_parser(
            name=self.SET_ID,
            help="Set the ID of all Alicats connected to the system",
        )
        parser_set_id.set_defaults(sub_command=self.SET_ID)

        #########################################################
        # set-flowpoint-slpm subcommand
        #########################################################

        parser_set_flowpoint_slpm = subparsers.add_parser(
            name=self.SET_FLOWPOINT_SLPM,
            help="Set the flowpoint in SLPM units.",
        )
        parser_set_flowpoint_slpm.set_defaults(sub_command=self.SET_ID)

        parser_set_flowpoint_slpm.add_argument(
            # name="id",
            help="[A-Z]",
            dest="id",
            # required=True,
        )

        parser_set_flowpoint_slpm.add_argument(
            # name="value",
            help="[0..max]",
            dest="flow",
            # required=True,
        )

    def help(self) -> None:
        print(self.parser.parse_args(["--help"]))

    def parseAndVerify(self, args: Sequence[str]) -> bool:
        try:
            # result = self.parser.parse_args()
            parsed, extras = self.parser.parse_known_args(args)
            if extras:
                warnings.warn(f'Ignoring unknown arguments: {", ".join(extras)}')
            if not hasattr(parsed, "sub_command"):
                self.help()
                return False
        except ParseException as ex:
            print(ex.msg)
            return False

        self.sub_command = parsed.sub_command

        self.id = parsed.id
        if self.sub_command == self.SET_FLOWPOINT_SLPM:
            self.flow = parsed.flow

        return True


async def PrepareToUseSlpm(mfc: AlicatBasisMfcDriver) -> None:
    max_lpm = mfc.prepare_to_use_slpm()
    # MMSLOG->info(LOCATED_FORMAT("Prepared to use SLPM... {}"), mfc->ToString());
    if max_lpm == 0.0:
        # MMSLOG->warn(
        #     LOCATED_FORMAT("Max SLPM = 0.0, checking that the full scale range is working"));

        full_scale_range = await mfc.get_full_scale_range()
        if isinstance(full_scale_range, bool):
            # MMSLOG->error(LOCATED_FORMAT("Couldn't read full scale range"));
            warnings.warn("Couldn't read full scale range")

        # MMSLOG->info("GetFullScaleRange() => {} {}", fullScaleRange, fullScaleUnits);
        print(f"GetFullScaleRange() => {full_scale_range}")


async def main() -> None:
    # TODO initialize the hardware

    # TODO would be nice to log location and configuration info

    options = ToolOptions()

    if not options.parseAndVerify((sys.argv[1:])):
        sys.exit(1)

    # MMSLOG->debug(LOCATED_FORMAT("running test - {} "), testToRun.testName);
    print(f"running test - {options.sub_command}")

    # Initialize serial port
    mfc_serial_port: TbdSerialPort = 0

    # TODO
    # int ret = mfcSerialPort->Init(HardwareDefinition::MFC_DEV, HardwareDefinition::MFC_BAUD);
    # if (ret < 0) {
    #     MMSLOG->error(LOCATED_FORMAT("error to initialize serial port"));
    #     return -1;
    # }

    if options.sub_command == options.ALL_STATUS:
        pass

    if options.sub_command == options.FULL_SCALE_RANGE:
        mfc: AlicatBasisMfcDriver = AlicatBasisMfcDriver(options.id, mfc_serial_port)
        # mfc->EnableLogging(RuntimeFlags::MinorAlicatLoggingEnabled());
        await PrepareToUseSlpm(mfc)

        full_scale_range = await mfc.get_full_scale_range()
        if not full_scale_range:
            # MMSLOG->error(LOCATED_FORMAT("Error reading full scale range"));
            warnings.warn("Error reading full scale range")
        else:
            # MMSLOG->info(
            #     LOCATED_FORMAT("ID: {} Range: {} {} ({})"),
            #     idToUse,
            #     range,
            #     rangeUnits,
            #     rangeUnits.length());
            print(f"ID: {options.id} Range: {full_scale_range}")

    if options.sub_command == options.SET_FLOWPOINT_SLPM:
        pass

    if options.sub_command == options.SET_ID:
        pass


if __name__ == "__main__":
    asyncio.run(main())
