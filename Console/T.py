using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.CognitiveServices.Speech;

[Route("api/[controller]")]
[ApiController]
public class AudioToTextController : ControllerBase
{
    [HttpPost]
    public async Task<IActionResult> PostAudioFile(IFormFile file)
    {
        if (file == null || file.Length == 0)
        {
            return BadRequest("Audio file is missing or empty.");
        }

        try
        {
            // Replace with your Speech-to-Text service endpoint and API key
            var endpoint = "YOUR_SPEECH_TO_TEXT_ENDPOINT";
            var apiKey = "YOUR_SPEECH_TO_TEXT_API_KEY";

            var config = SpeechConfig.FromEndpoint(new Uri(endpoint), apiKey);
            using (var audioInput = AudioConfig.FromStreamInput(file.OpenReadStream()))
            {
                using (var recognizer = new SpeechRecognizer(config, audioInput))
                {
                    var result = await recognizer.RecognizeOnceAsync();

                    if (result.Reason == ResultReason.RecognizedSpeech)
                    {
                        return Ok(result.Text);
                    }
                    else
                    {
                        return BadRequest("Speech recognition failed.");
                    }
                }
            }
        }
        catch (Exception ex)
        {
            return StatusCode(StatusCodes.Status500InternalServerError, ex.Message);
        }
    }
}
