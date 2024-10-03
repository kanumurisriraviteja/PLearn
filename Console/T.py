
using Microsoft.AspNetCore.Http;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

namespace ProxyApi.Middleware
{
    public class ProxyMiddleware
    {
        private readonly RequestDelegate _next;
        private readonly HttpClient _httpClient;

        public ProxyMiddleware(RequestDelegate next, IHttpClientFactory httpClientFactory)
        {
            _next = next;
            _httpClient = httpClientFactory.CreateClient();
        }

        public async Task InvokeAsync(HttpContext context)
        {
            // Check if the route exists within the current project
            var endpoint = context.GetEndpoint();

            // If no matching route is found, act as a proxy
            if (endpoint == null)
            {
                await ForwardRequestToOriginalSource(context);
            }
            else
            {
                // If the route exists, continue with the next middleware
                await _next(context);
            }
        }

        private async Task ForwardRequestToOriginalSource(HttpContext context)
        {
            // Extract the original request path and query string
            var originalRequestPath = context.Request.Path + context.Request.QueryString;
            var destinationUrl = "https://originalsource.com" + originalRequestPath;

            // Create the proxy request
            var requestMessage = new HttpRequestMessage
            {
                RequestUri = new Uri(destinationUrl),
                Method = new HttpMethod(context.Request.Method)
            };

            // Copy the headers from the original request
            foreach (var header in context.Request.Headers)
            {
                if (!requestMessage.Headers.TryAddWithoutValidation(header.Key, (IEnumerable<string>)header.Value))
                {
                    requestMessage.Content?.Headers.TryAddWithoutValidation(header.Key, (IEnumerable<string>)header.Value);
                }
            }

            // Add your custom headers here
            requestMessage.Headers.Add("X-Custom-Header", "CustomHeaderValue");

            // Copy the body content if necessary (POST, PUT, PATCH)
            if (context.Request.ContentLength > 0)
            {
                var streamContent = new StreamContent(context.Request.Body);
                requestMessage.Content = streamContent;
                requestMessage.Content.Headers.ContentType = new MediaTypeHeaderValue(context.Request.ContentType);
            }

            // Send the request to the original source
            var responseMessage = await _httpClient.SendAsync(requestMessage);

            // Copy the response headers back to the context
            foreach (var header in responseMessage.Headers)
            {
                context.Response.Headers[header.Key] = header.Value.ToArray();
            }

            foreach (var header in responseMessage.Content.Headers)
            {
                context.Response.Headers[header.Key] = header.Value.ToArray();
            }

            // Set the response status and content
            context.Response.StatusCode = (int)responseMessage.StatusCode;
            context.Response.ContentType = responseMessage.Content.Headers.ContentType?.ToString();
            var content = await responseMessage.Content.ReadAsStringAsync();

            await context.Response.WriteAsync(content);
        }
    }
}



using Microsoft.AspNetCore.Mvc;
using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using System.Net.Http.Headers;

namespace ProxyApi.Controllers
{
    [Route("{**catchAll}")]
    [ApiController]
    public class ProxyController : ControllerBase
    {
        private readonly HttpClient _httpClient;

        public ProxyController(IHttpClientFactory httpClientFactory)
        {
            _httpClient = httpClientFactory.CreateClient();
        }

        [HttpGet]
        [HttpPost]
        [HttpPut]
        [HttpDelete]
        [HttpPatch]
        public async Task<IActionResult> HandleRequest()
        {
            // Extract the incoming request URL path
            var originalRequestPath = HttpContext.Request.Path + HttpContext.Request.QueryString;
            var destinationUrl = "https://originalsource.com" + originalRequestPath;

            // Create the proxy request
            var requestMessage = new HttpRequestMessage
            {
                RequestUri = new Uri(destinationUrl),
                Method = new HttpMethod(HttpContext.Request.Method)
            };

            // Copy the headers from the incoming request
            foreach (var header in HttpContext.Request.Headers)
            {
                if (!requestMessage.Headers.TryAddWithoutValidation(header.Key, (IEnumerable<string>)header.Value))
                {
                    requestMessage.Content?.Headers.TryAddWithoutValidation(header.Key, (IEnumerable<string>)header.Value);
                }
            }

            // Add your custom headers here
            requestMessage.Headers.Add("X-Custom-Header", "CustomHeaderValue");

            // Copy the body content if it's a POST, PUT, or PATCH request
            if (HttpContext.Request.ContentLength > 0)
            {
                var streamContent = new StreamContent(HttpContext.Request.Body);
                requestMessage.Content = streamContent;
                requestMessage.Content.Headers.ContentType = new MediaTypeHeaderValue(HttpContext.Request.ContentType);
            }

            // Send the request to the original source
            var responseMessage = await _httpClient.SendAsync(requestMessage);

            // Copy the response headers
            foreach (var header in responseMessage.Headers)
            {
                Response.Headers[header.Key] = header.Value.ToArray();
            }

            foreach (var header in responseMessage.Content.Headers)
            {
                Response.Headers[header.Key] = header.Value.ToArray();
            }

            // Return the response from the original source
            return new ContentResult
            {
                Content = await responseMessage.Content.ReadAsStringAsync(),
                StatusCode = (int)responseMessage.StatusCode,
                ContentType = responseMessage.Content.Headers.ContentType?.ToString()
            };
        }
    }
}
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Dictionary<string, string> replacementMap = new Dictionary<string, string>
        {
            { "mo", "tu" },
            { "tu", "we" },
            { "we", "th" },
            { "th", "fr" },
            { "fr", "sa" },
            { "sa", "su" },
            { "su", "mo" }
        };

        string originalString = "mo tu we th fr sa su";
        string[] words = originalString.Split(' ');

        for (int i = 0; i < words.Length; i++)
        {
            if (replacementMap.TryGetValue(words[i], out string replacement))
            {
                words[i] = replacement;
            }
        }

        string replacedString = string.Join(" ", words);
        Console.WriteLine(replacedString);
    }
}

==
using System;

class Program
{
    static void Main()
    {
        // Sample date string in "yyyy-MM-dd HH:mm:ss" format
        string dateString = "2023-12-08 15:30:45";

        // Parse the date string to DateTime
        if (DateTime.TryParseExact(dateString, "yyyy-MM-dd HH:mm:ss", null, System.Globalization.DateTimeStyles.None, out DateTime parsedDate))
        {
            // Decrease the time by 1 hour
            DateTime newDate = parsedDate.AddHours(-1);

            // Print the original and updated date
            Console.WriteLine($"Original Date: {parsedDate:yyyy-MM-dd HH:mm:ss}");
            Console.WriteLine($"Updated Date: {newDate:yyyy-MM-dd HH:mm:ss}");
        }
        else
        {
            Console.WriteLine("Invalid date format.");
        }
    }
}<?xml version="1.0" encoding="utf-8" ?>
<log4net>
  <appender name="FileAppender" type="log4net.Appender.FileAppender">
    <file value="log.txt" />
    <appendToFile value="true" />
    <layout type="log4net.Layout.PatternLayout">
      <conversionPattern value="%date [%thread] %-5level %logger - %message%newline" />
    </layout>
  </appender>
  <root>
    <level value="ALL" />
    <appender-ref ref="FileAppender" />
  </root>
</log4net>

using log4net;
using log4net.Config;

class Program
{
    private static readonly ILog log = LogManager.GetLogger(typeof(Program));

    static void Main()
    {
        // Load log4net configuration
        XmlConfigurator.Configure(new System.IO.FileInfo("log4net.config"));

        // Example usage of logging
        log.Info("This is an informational message.");
        log.Error("This is an error message.");

        // Logs will be written to the specified log file
    }
}


using System;
using System.Text.RegularExpressions;
using System.Linq;

class Program
{
    static void Main()
    {
        string inputString = "week=(2,5,1) day=(mo,we) time=(0:01)";

        // Use regular expressions to extract week, days, and time
        Match weekMatch = Regex.Match(inputString, @"week=\((.*?)\)");
        Match dayMatch = Regex.Match(inputString, @"day=\((.*?)\)");
        Match timeMatch = Regex.Match(inputString, @"time=\((\d+:\d+)\)");

        if (weekMatch.Success && dayMatch.Success && timeMatch.Success)
        {
            // Extract values from matched groups
            string originalWeek = weekMatch.Groups[1].Value;
            string originalDays = dayMatch.Groups[1].Value;
            string originalTime = timeMatch.Groups[1].Value;

            // Update days (mo,we) to (su,tu)
            string updatedDays = originalDays.Replace("mo", "su").Replace("we", "tu");

            // Update time (0:01) to (23:01)
            string updatedTime = "23:01";

            // Construct the updated string
            string updatedString = $"week=({originalWeek}) day=({updatedDays}) time=({updatedTime})";

            Console.WriteLine($"Updated string: {updatedString}");
        }
        else
        {
            Console.WriteLine("Invalid input format. Unable to extract week, days, or time.");
        }
    }
}

=======
class Program
{
    static void Main()
    {
        string inputString = "time=(s=7:00,f=12:00)";

        // Use regular expression to extract start and end times
        Match match = Regex.Match(inputString, @"time=\(s=(\d+:\d+),f=(\d+:\d+)\)");

        if (match.Success)
        {
            // Parse start and end times from the matched groups
            string startTime = match.Groups[1].Value;
            string endTime = match.Groups[2].Value;

            // Parse hours and minutes from the start time
            int startHours = int.Parse(startTime.Split(':')[0]);
            int startMinutes = int.Parse(startTime.Split(':')[1]);

            // Decrease start hours by 1 (or set to 23 if already 0)
            startHours = (startHours > 0) ? startHours - 1 : 23;

            // Construct the updated start time
            string updatedStartTime = $"{startHours:D2}:{startMinutes:D2}";

            // Display the updated time
            string updatedTime = $"time=(s={updatedStartTime},f={endTime})";
            Console.WriteLine($"Updated string: {updatedTime}");
        }
        else
        {
            Console.WriteLine("Invalid input format. Unable to extract time.");
        }
    }
}


=================
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
