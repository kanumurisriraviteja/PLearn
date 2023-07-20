
using System;
using System.IO;
using Azure.Storage.Blobs;

public class BlobStorageUploader
{
    private readonly string connectionString; // Replace with your Azure Storage connection string
    private readonly string containerName; // Replace with your Blob container name

    public BlobStorageUploader(string connectionString, string containerName)
    {
        this.connectionString = connectionString;
        this.containerName = containerName;
    }

    public async Task UploadTextFileToBlobStorage(string fileName, string content)
    {
        try
        {
            // Create a BlobServiceClient using the connection string
            var blobServiceClient = new BlobServiceClient(connectionString);

            // Get a reference to the container
            var containerClient = blobServiceClient.GetBlobContainerClient(containerName);

            // Create a new text Blob in the container
            var blobClient = containerClient.GetBlobClient(fileName);

            // Convert the content to bytes and upload to the Blob
            var contentBytes = Encoding.UTF8.GetBytes(content);
            using (var stream = new MemoryStream(contentBytes))
            {
                await blobClient.UploadAsync(stream);
            }
        }
        catch (Exception ex)
        {
            // Handle any exceptions here
            Console.WriteLine("Error uploading file: " + ex.Message);
        }
    }
}
