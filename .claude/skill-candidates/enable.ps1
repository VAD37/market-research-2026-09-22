# Enable exactly one candidate skill for the next fresh session.
# Usage:  .\enable.ps1 strategy-communicator   -> that skill "on", all others "off"
#         .\enable.ps1 pyramid-audit            -> also turns on pyramid-principle-core (dependency)
#         .\enable.ps1 none                     -> everything off
# pyramid-* skills only exist when the plugin is loaded for the session:
#         claude --plugin-dir .claude\skill-candidates\pyramid-principle
param([Parameter(Mandatory)][string]$Name)
$f = Join-Path $PSScriptRoot "..\settings.local.json"
$j = Get-Content $f -Raw | ConvertFrom-Json
$names = $j.skillOverrides.PSObject.Properties.Name
if ($Name -ne "none" -and -not ($names -contains $Name)) { throw "unknown skill: $Name  (known: $($names -join ', '))" }
$deps = @{ "pyramid-audit"="pyramid-principle-core"; "pyramid-long-form"="pyramid-principle-core"; "pyramid-presentation"="pyramid-principle-core"; "pyramid-short-form"="pyramid-principle-core" }
$on = @(); if ($Name -ne "none") { $on = @($Name); if ($deps[$Name]) { $on += $deps[$Name] } }
foreach ($p in $j.skillOverrides.PSObject.Properties) { if ($on -contains $p.Name) { $p.Value = "on" } else { $p.Value = "off" } }
$j | ConvertTo-Json -Depth 5 | Set-Content $f -Encoding utf8
if ($on.Count) { $on | ForEach-Object { "on: $_" } } else { "all off" }
