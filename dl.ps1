
param (
    [Parameter(Mandatory=$true)]
    [string]$Exercise
)

$Track = "python"

Write-Host "Processing request..." -ForegroundColor Cyan
Write-Host "Exercise : $Exercise"
Write-Host "Track    : $Track"
Write-Host "-----------------------------------"

# Verify Exercism CLI is installed
if (-not (Get-Command exercism -ErrorAction SilentlyContinue)) {
    Write-Error "'exercism' CLI is not installed or not in your PATH."
    Write-Error "Please install it first: https://exercism.org"
    exit
}

# Execute the download
Write-Host "Downloading..." -ForegroundColor Yellow
exercism download --track=$Track --exercise=$Exercise

Write-Host "-----------------------------------"
Write-Host "Success! Exercise downloaded." -ForegroundColor Green
