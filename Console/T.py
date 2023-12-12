using System;
using System.Data.SqlClient;
using System.Text.RegularExpressions;

class Program
{
    static void Main()
    {
        string connectionString = "your_connection_string_here";
        string tableName = "your_table_name_here";
        string columnName = "your_column_name_here";
        
        // Replace this with your actual SQL query to retrieve the data
        string selectQuery = $"SELECT * FROM {tableName}";

        using (SqlConnection connection = new SqlConnection(connectionString))
        {
            connection.Open();

            using (SqlCommand command = new SqlCommand(selectQuery, connection))
            {
                using (SqlDataReader reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        // Assuming the time column is a string in the format "(h:mm)"
                        string oldTimeString = reader[columnName].ToString();

                        // Use regular expression to extract hours and minutes
                        Match match = Regex.Match(oldTimeString, @"\((\d+):(\d+)\)");

                        if (match.Success)
                        {
                            // Parse hours and minutes from the matched groups
                            int hours = int.Parse(match.Groups[1].Value);
                            int minutes = int.Parse(match.Groups[2].Value);

                            // Adjust hours: if 0, set to 23; otherwise, decrease by 1
                            hours = (hours > 0) ? hours - 1 : 23;

                            // Set minutes to 0
                            minutes = 0;

                            // Construct the updated time string
                            string updatedTimeString = $"({hours:D2}:{minutes:D2})";

                            // Construct conditions for the WHERE clause using your unique columns
                            string whereClause = $"WHERE Column1 = '{reader["Column1"]}' AND Column2 = '{reader["Column2"]}'";

                            // Replace the old time string in the original column value
                            string newColumnValue = Regex.Replace(oldTimeString, @"\(\d+:\d+\)", updatedTimeString);

                            // Update the table with the new value
                            UpdateTable(connection, tableName, columnName, whereClause, newColumnValue);
                        }
                    }
                }
            }
        }
    }

    static void UpdateTable(SqlConnection connection, string tableName, string columnName, string whereClause, string newValue)
    {
        // Replace this with your actual SQL update statement
        string updateQuery = $"UPDATE {tableName} SET {columnName} = @newValue {whereClause}";

        using (SqlCommand updateCommand = new SqlCommand(updateQuery, connection))
        {
            updateCommand.Parameters.AddWithValue("@newValue", newValue);

            int rowsAffected = updateCommand.ExecuteNonQuery();

            Console.WriteLine($"{rowsAffected} row(s) updated.");
        }
    }
}
==============================================================================================
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
