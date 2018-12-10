from typing import List

from examples.bio_informatics.data_types.bed import Bed
from examples.bio_informatics.data_types.ref_fasta import RefFasta
from Pipeline import File, String, Array, Tool, ToolOutput, ToolInput


class GatkBaseRecalibrator(Tool):

    inputBam_BaseRecalibrator = ToolInput("inputBam_BaseRecalibrator", File())
    outputfile_BaseRecalibrator = ToolInput("outputfile_BaseRecalibrator", String())
    reference = ToolInput("reference", RefFasta())
    known = ToolInput("known", Array(File()))
    bedFile = ToolInput("bedFile", Bed())

    out = ToolOutput("out", File())

    @staticmethod
    def tool():
        return "gatk-base-recalibrator"

    @staticmethod
    def base_command():
        return "javac"
