
using System;
using System.IO;
using Azure.Storage.Blobs;

public class BlobStorageUploader
{using Microsoft.CognitiveServices.Speech.Audio;

// ...

// Assuming you already have a regular stream named "inputStream"
using (var audioInputStream = AudioInputStream.CreatePushStream())
{
    // Create an AudioConfig object from the AudioInputStream
    var audioConfig = AudioConfig.FromStreamInput(audioInputStream);

    // Read data from your original input stream and write it to the AudioInputStream
    // You can use any buffer size that is appropriate for your application
    byte[] buffer = new byte[1024];
    int bytesRead;

    while ((bytesRead = inputStream.Read(buffer, 0, buffer.Length)) > 0)
    {
        audioInputStream.Write(buffer, 0, bytesRead);
    }

    // Optionally, you can close the AudioInputStream when you're done writing data
    audioInputStream.Close();
    
    // Now you can use the audioConfig with your SpeechRecognizer or any other Speech SDK components
    // For example:
    // var speechRecognizer = new SpeechRecognizer(speechConfig, audioConfig);
    // var result = await speechRecognizer.RecognizeOnceAsync();
}

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
