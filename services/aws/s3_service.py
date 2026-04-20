import boto3

bucket_name = 'practica-4-722185'
bucket = boto3.resource('s3').Bucket(bucket_name)


def find_file_in_s3(file_name: str):
    for obj in bucket.objects.all():
        if obj.key == file_name:
            return f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
    return None


def upload_file_to_s3(file_content: bytes, file_name: str):
    if find_file_in_s3(file_name):
        return f"El archivo '{file_name}' ya existe en S3."
    bucket.put_object(Key=file_name, Body=file_content)
    return f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
