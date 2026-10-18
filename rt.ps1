param (
    [Parameter(Mandatory=$true)]
    [string]$Exercise
)

# Define your main Exercism Python path
$ExercismPath = "$HOME\Exercism\python\$Exercise"

Write-Host "Locating exercise..." -ForegroundColor Cyan
Write-Host "Target Folder: $ExercismPath"
Write-Host "-----------------------------------"

# Check if the folder exists
if (-not (Test-Path -Path $ExercismPath)) {
    Write-Error "Error: The folder for '$Exercise' does not exist at $ExercismPath"
    exit
}

# Change directory into the exercise folder
Set-Location -Path $ExercismPath

# Programmatically find the exact test file name in this folder
$TestFile = Get-ChildItem -Filter "*_test.py" | Select-Object -First 1

if (-not $TestFile) {
    Write-Error "Error: Could not find any test file ending in _test.py in this directory."
    exit
}

Write-Host "Running tests using: .\$($TestFile.Name)" -ForegroundColor Yellow
Write-Host "-----------------------------------"

# Run the exact Exercism Windows test command using the explicitly resolved file name
py -m pytest -o markers=task ".\$($TestFile.Name)"

Write-Host "-----------------------------------"
Write-Host "Testing complete." -ForegroundColor Green
