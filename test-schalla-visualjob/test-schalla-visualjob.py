import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglueml.transforms import EntityDetector
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.types import ArrayType, StringType, StructType, StructField

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1687295220122 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={"paths": ["s3://test-glue-schalla-iad"], "recurse": True},
    transformation_ctx="AmazonS3_node1687295220122",
)

# Script generated for node Amazon S3
AmazonS3_node1687295476630 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={"paths": ["s3://test-glue-schalla-iad"], "recurse": True},
    transformation_ctx="AmazonS3_node1687295476630",
)

# Script generated for node Detect Sensitive Data
entity_detector = EntityDetector()
classified_map = entity_detector.classify_columns(
    AmazonS3_node1687295220122, [], 1.0, 0.1
)
items = classified_map.items()
schema = StructType(
    [
        StructField("columnName", StringType(), True),
        StructField("entityTypes", ArrayType(StringType(), True)),
    ]
)
# data_frame test new comment
data_frame = spark.createDataFrame(data=items, schema=schema)
DetectSensitiveData_node1687295371089 = DynamicFrame.fromDF(
    data_frame, glueContext, "df_for_pii"
)

job.commit()
