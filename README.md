## COP-DataScience

A personal demo to show how you can track metadata for files ingest and transform them in Aws.

Project to tack all the metadata files ingested in Aws S3, using Aws lambda function to apply some transformations and put in S3. To track this, we use an Aws lambda function triggered by Aws Sqs and store the information in the Aws Dynamo table.

### Aws Diagram.

![Alt text](diagram/COP-data.drawio.png?raw=true "Aws Diagram.")

### Technologies

- Aws S3
- Aws Lambda(Python)
- Aws SQS
- Aws Dynamo

