import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1708894026236 = glueContext.create_dynamic_frame.from_catalog(
    database="de-youtube-cleaned",
    table_name="raw_statistics",
    transformation_ctx="AWSGlueDataCatalog_node1708894026236",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1708894023290 = glueContext.create_dynamic_frame.from_catalog(
    database="de-youtube-cleaned",
    table_name="cleaned_stats_reference_data",
    transformation_ctx="AWSGlueDataCatalog_node1708894023290",
)

# Script generated for node Join
Join_node1708894064920 = Join.apply(
    frame1=AWSGlueDataCatalog_node1708894023290,
    frame2=AWSGlueDataCatalog_node1708894026236,
    keys1=["id"],
    keys2=["category_id"],
    transformation_ctx="Join_node1708894064920",
)

# Script generated for node Amazon S3
AmazonS3_node1708894127768 = glueContext.getSink(
    path="s3://portfolioproject-analytics",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["region", "category_id"],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1708894127768",
)
AmazonS3_node1708894127768.setCatalogInfo(
    catalogDatabase="de-youtube-analytics", catalogTableName="final_analytics"
)
AmazonS3_node1708894127768.setFormat("glueparquet", compression="snappy")
AmazonS3_node1708894127768.writeFrame(Join_node1708894064920)
job.commit()
