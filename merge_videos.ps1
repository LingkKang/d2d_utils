<#
Merge multiple videos into one using FFmpeg.

Dependencies:
    ffmpeg

Useage:
    .\merge_videos.ps1 .\test\1.mp4 .\test\2.mp4 .\test\3.mp4
#>

# Function to generate a timestamp
function Get-Timestamp {
    return Get-Date -Format "yyyy-MM-dd-HHmmss"
}

$videoCount = $args.Count
Write-Host $videoCount

# Check if input files are provided
if ($videoCount -eq 0) {
    Write-Host "No input files provided."
    exit
}

# Creating a temporary file to list all input videos
$tempFile = "ffmpeg-temp-file.txt"
Remove-Item -Path $tempFile -ErrorAction Ignore
for ( $i = 0; $i -lt $videoCount; $i++ ) {
    $file = $args[$i]
    if (-Not (Test-Path $file)) {
        Write-Host "The file $file does not exist."
        exit
    }
    Add-Content -Path $tempFile -Value "file '$file'"
}

# Generate the output file name
$outputFile = "$(Get-Timestamp).mp4"

# Execute FFmpeg command to merge videos
ffmpeg -f concat -safe 0 -i $tempFile -c copy $outputFile

# Clean up temporary file
Remove-Item -Path $tempFile

Write-Host "All of $videoCount videos have been merged and saved as $outputFile"
