# trim a video file
param(
    [string]$inputFile
)

# Function to generate a timestamp
function Get-Timestamp {
    return Get-Date -Format "yyyy-MM-dd-HHmmss"
}

# Check if the input file exists
if (-Not (Test-Path $inputFile)) {
    Write-Host "The file $inputFile does not exist."
    exit
}

# Generate the output file name
$outputFile = "$(Get-Timestamp).mp4"

# Execute FFmpeg command
ffmpeg -i $inputFile -ss 2 -t 59 -c copy $outputFile

Write-Host "Video has been cut and saved as $outputFile"
