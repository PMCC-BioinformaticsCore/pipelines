
GATK4: Merge SAM Files
===========================================
Tool identifier: ``Gatk4MergeSamFiles``

Tool path: ``from janis_bioinformatics.tools.gatk4 import Gatk4MergeSamFiles_4_0``

Documentation
-------------

Docker
******
``broadinstitute/gatk:4.0.12.0``

URL
******
`https://software.broadinstitute.org/gatk/documentation/tooldocs/4.beta.3/org_broadinstitute_hellbender_tools_picard_sam_MergeSamFiles.php <https://software.broadinstitute.org/gatk/documentation/tooldocs/4.beta.3/org_broadinstitute_hellbender_tools_picard_sam_MergeSamFiles.php>`_

Docstring
*********
Merges multiple SAM/BAM files into one file

Outputs
-------
======  =======  ===============
name    type     documentation
======  =======  ===============
out     BamPair
======  =======  ===============

Inputs
------
Find the inputs below

Required inputs
***************

======  ==============  ========  ==========  =========================
name    type            prefix      position  documentation
======  ==============  ========  ==========  =========================
bams    Array<BamPair>  -I                10  The SAM/BAM file to sort.
======  ==============  ========  ==========  =========================

Optional inputs
***************

=========================  =======================  =======================  ==========  ================================================================================================================================================================================================================================================================================================================================================================================================
name                       type                     prefix                     position  documentation
=========================  =======================  =======================  ==========  ================================================================================================================================================================================================================================================================================================================================================================================================
outputFilename             Optional<Filename>       -O                               10  SAM/BAM file to write merged result to
argumentsFile              Optional<Array<File>>    --arguments_file                 10  read one or more arguments files and add them to the command line
assumeSorted               Optional<Boolean>        -AS                                  If true, assume that the input files are in the same sort order as the requested output sort order, even if their headers say otherwise.
comment                    Optional<Array<String>>  -CO                                  Comment(s) to include in the merged output file's header.
mergeSequenceDictionaries  Optional<Boolean>        -MSD                                 Merge the sequence dictionaries
sortOrder                  Optional<String>         -SO                              10  The --SORT_ORDER argument is an enumerated type (SortOrder), which can have one of the following values: [unsorted, queryname, coordinate, duplicate, unknown]
useThreading               Optional<Boolean>        --USE_THREADING                      Option to create a background thread to encode, compress and write to disk the output file. The threaded version uses about 20% more CPU and decreases runtime by ~20% when writing out a compressed BAM file.
compressionLevel           Optional<Integer>        --COMPRESSION_LEVEL              11  Compression level for all compressed files created (e.g. BAM and GELI).
createIndex                Optional<Boolean>        --CREATE_INDEX                   11  Whether to create a BAM index when writing a coordinate-sorted BAM file.
createMd5File              Optional<Boolean>        --CREATE_MD5_FILE                11  Whether to create an MD5 digest for any BAM or FASTQ files created.
maxRecordsInRam            Optional<Integer>        --MAX_RECORDS_IN_RAM             11  When writing SAM files that need to be sorted, this will specify the number of records stored in RAM before spilling to disk. Increasing this number reduces the number of file handles needed to sort a SAM file, and increases the amount of RAM needed.
quiet                      Optional<Boolean>        --QUIET                          11  Whether to suppress job-summary info on System.err.
reference                  Optional<FastaWithDict>  --reference                      11  Reference sequence file.
tmpDir                     Optional<String>         --TMP_DIR                        11  Undocumented option
useJdkDeflater             Optional<Boolean>        --use_jdk_deflater               11  Whether to use the JdkDeflater (as opposed to IntelDeflater)
useJdkInflater             Optional<Boolean>        --use_jdk_inflater               11  Whether to use the JdkInflater (as opposed to IntelInflater)
validationStringency       Optional<String>         --VALIDATION_STRINGENCY          11  Validation stringency for all SAM files read by this program. Setting stringency to SILENT can improve performance when processing a BAM file in which variable-length data (read, qualities, tags) do not otherwise need to be decoded.The --VALIDATION_STRINGENCY argument is an enumerated type (ValidationStringency), which can have one of the following values: [STRICT, LENIENT, SILENT]
verbosity                  Optional<String>         --verbosity                      11  The --verbosity argument is an enumerated type (LogLevel), which can have one of the following values: [ERROR, WARNING, INFO, DEBUG]
=========================  =======================  =======================  ==========  ================================================================================================================================================================================================================================================================================================================================================================================================


Metadata
********

Author: Michael Franklin


*GATK4: Merge SAM Files was last updated on 2019-01-24*.
*This page was automatically generated on 2019-07-09*.